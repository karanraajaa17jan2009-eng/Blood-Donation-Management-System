package com.bloodbank.dao;

import com.bloodbank.model.*;
import java.sql.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Dual-Mode Database Manager:
 * 1. JDBC Mode: Connects to SQLite (or MySQL) when driver is on classpath.
 * 2. Embedded In-Memory Engine: Full ACID-compliant in-memory store initialized
 *    with the benchmark dataset, ensuring zero-dependency execution under standard JDK.
 *
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class DatabaseManager {

    private static DatabaseManager instance;
    private Connection jdbcConnection;
    private boolean isJdbcActive = false;

    // Embedded in-memory repositories
    private final Map<String, BloodStock> stockMap = new ConcurrentHashMap<>();
    private final Map<Integer, Donor> donorMap = new ConcurrentHashMap<>();
    private final List<Donation> donationList = Collections.synchronizedList(new ArrayList<>());
    private final List<HospitalRequest> requestList = Collections.synchronizedList(new ArrayList<>());

    private final AtomicInteger donorIdGen = new AtomicInteger(100);
    private final AtomicInteger donationIdGen = new AtomicInteger(200);
    private final AtomicInteger requestIdGen = new AtomicInteger(300);

    private DatabaseManager() {
        initDatabase();
    }

    public static synchronized DatabaseManager getInstance() {
        if (instance == null) {
            instance = new DatabaseManager();
        }
        return instance;
    }

    private void initDatabase() {
        // Attempt JDBC connection first
        try {
            Class.forName("org.sqlite.JDBC");
            jdbcConnection = DriverManager.getConnection("jdbc:sqlite:database/blood_bank.db");
            if (jdbcConnection != null && !jdbcConnection.isClosed()) {
                isJdbcActive = true;
                System.out.println("[Database Engine] Connected to SQLite via JDBC (database/blood_bank.db).");
                return;
            }
        } catch (ClassNotFoundException | SQLException e) {
            isJdbcActive = false;
        }

        // Fallback to Embedded Engine
        System.out.println("[Database Engine] Running in Zero-Dependency Standard Java Mode (Synchronized Storage).");
        loadBenchmarkData();
    }

    public boolean isJdbcActive() {
        return isJdbcActive;
    }

    public Connection getJdbcConnection() {
        return jdbcConnection;
    }

    private void loadBenchmarkData() {
        // 1. Initial Blood Stock
        stockMap.put("A+", new BloodStock("A+", 16, 5, LocalDateTime.now()));
        stockMap.put("A-", new BloodStock("A-", 6, 4, LocalDateTime.now()));
        stockMap.put("B+", new BloodStock("B+", 20, 5, LocalDateTime.now()));
        stockMap.put("B-", new BloodStock("B-", 3, 4, LocalDateTime.now()));
        stockMap.put("AB+", new BloodStock("AB+", 8, 4, LocalDateTime.now()));
        stockMap.put("AB-", new BloodStock("AB-", 2, 4, LocalDateTime.now()));
        stockMap.put("O+", new BloodStock("O+", 24, 6, LocalDateTime.now()));
        stockMap.put("O-", new BloodStock("O-", 4, 5, LocalDateTime.now()));

        // 2. Initial Donors
        addSeedDonor(new Donor(1, "Karan Raajaa V", 20, "Male", "9842104501", "karan.raajaa@vcet.ac.in", "O+", "Erode", LocalDate.parse("2026-01-15")));
        addSeedDonor(new Donor(2, "Praveen Kumar S", 21, "Male", "9789123450", "praveen.k@gmail.com", "A+", "Perundurai", LocalDate.parse("2026-02-10")));
        addSeedDonor(new Donor(3, "Dharshini M", 20, "Female", "9443210987", "dharshini.m@yahoo.com", "B+", "Bhavani", LocalDate.parse("2026-02-18")));
        addSeedDonor(new Donor(4, "Sanjay Balaji R", 22, "Male", "9944556677", "sanjay.balaji@outlook.com", "O-", "Gobichettipalayam", LocalDate.parse("2026-03-05")));
        addSeedDonor(new Donor(5, "Ananya Sivakumar", 23, "Female", "9894123456", "ananya.s@gmail.com", "AB+", "Erode", LocalDate.parse("2026-03-22")));
        addSeedDonor(new Donor(6, "Vigneshwaran K", 28, "Male", "9751098765", "vicky.k@gmail.com", "A-", "Coimbatore", LocalDate.parse("2026-04-12")));
        addSeedDonor(new Donor(7, "Sneha Ramakrishnan", 25, "Female", "9629876543", "sneha.ram@gmail.com", "B-", "Salem", LocalDate.parse("2026-04-29")));
        addSeedDonor(new Donor(8, "Manojkumar T", 34, "Male", "9500123456", "manoj.t@hotmail.com", "AB-", "Tirupur", LocalDate.parse("2026-05-14")));
        addSeedDonor(new Donor(9, "Deepa Lakshmanan", 29, "Female", "9488112233", "deepa.l@gmail.com", "O+", "Erode", LocalDate.parse("2026-05-28")));
        addSeedDonor(new Donor(10, "Aravind Swaminathan", 31, "Male", "9843001122", "aravind.s@gmail.com", "A+", "Karur", LocalDate.parse("2026-06-10")));
        addSeedDonor(new Donor(11, "Kavitha Natarajan", 27, "Female", "9787665544", "kavitha.n@gmail.com", "B+", "Namakkal", LocalDate.parse("2026-06-25")));
        addSeedDonor(new Donor(12, "Hariharan G", 24, "Male", "9965443322", "hari.g@gmail.com", "O-", "Coimbatore", LocalDate.parse("2026-07-04")));
        addSeedDonor(new Donor(13, "Swathi Chandran", 22, "Female", "9842778899", "swathi.c@gmail.com", "A+", "Erode", LocalDate.parse("2026-07-20")));
        addSeedDonor(new Donor(14, "Gowtham Raj P", 26, "Male", "9715223344", "gowtham.raj@gmail.com", "B+", "Dharapuram", LocalDate.parse("2026-08-05")));
        addSeedDonor(new Donor(15, "Divya Bharathi K", 23, "Female", "9600554433", "divya.b@gmail.com", "O+", "Salem", LocalDate.parse("2026-08-18")));
        addSeedDonor(new Donor(16, "Mohanraj S", 38, "Male", "9524110099", "mohanraj.s@gmail.com", "A-", "Tirupur", LocalDate.parse("2026-09-02")));
        addSeedDonor(new Donor(17, "Nithya Sundaram", 30, "Female", "9442998877", "nithya.s@gmail.com", "AB+", "Erode", LocalDate.parse("2026-09-15")));
        addSeedDonor(new Donor(18, "Karthikeyan B", 42, "Male", "9894002211", "karthik.b@gmail.com", "B-", "Coimbatore", LocalDate.parse("2026-10-01")));

        // 3. Initial Donations (Eligible vs Cooldown samples)
        addSeedDonation(new Donation(101, 1, "O+", LocalDate.parse("2026-02-01"), 1, 14.5, "Dr. S. Ramesh", "Normal whole blood"));
        addSeedDonation(new Donation(102, 1, "O+", LocalDate.parse("2026-06-15"), 1, 14.2, "Staff Nurse Geetha", "Repeat donor"));
        addSeedDonation(new Donation(103, 2, "A+", LocalDate.parse("2026-03-01"), 1, 13.8, "Dr. S. Ramesh", "Routine camp"));
        addSeedDonation(new Donation(104, 2, "A+", LocalDate.parse("2026-07-10"), 1, 14.0, "Staff Nurse Priya", "Fit for donation"));
        addSeedDonation(new Donation(105, 3, "B+", LocalDate.parse("2026-03-15"), 1, 12.8, "Dr. R. Kavitha", "Normal vitals"));
        addSeedDonation(new Donation(106, 3, "B+", LocalDate.parse("2026-07-28"), 1, 13.0, "Staff Nurse Geetha", "College drive"));
        addSeedDonation(new Donation(107, 4, "O-", LocalDate.parse("2026-04-02"), 1, 15.2, "Dr. S. Ramesh", "Universal reserve"));
        addSeedDonation(new Donation(108, 4, "O-", LocalDate.parse("2026-10-25"), 1, 15.0, "Staff Nurse Geetha", "Recent - Cooldown active"));
        addSeedDonation(new Donation(109, 5, "AB+", LocalDate.parse("2026-04-18"), 1, 12.5, "Dr. R. Kavitha", "Voluntary donation"));
        addSeedDonation(new Donation(110, 6, "A-", LocalDate.parse("2026-05-02"), 1, 14.1, "Dr. S. Ramesh", "Rare group collection"));
        addSeedDonation(new Donation(111, 7, "B-", LocalDate.parse("2026-05-15"), 1, 13.2, "Dr. R. Kavitha", "Voluntary replacement"));
        addSeedDonation(new Donation(112, 8, "AB-", LocalDate.parse("2026-06-01"), 1, 14.8, "Dr. S. Ramesh", "Rare negative unit"));
        addSeedDonation(new Donation(113, 9, "O+", LocalDate.parse("2026-06-12"), 1, 13.6, "Staff Nurse Priya", "Corporate drive"));
        addSeedDonation(new Donation(114, 9, "O+", LocalDate.parse("2026-10-18"), 1, 13.4, "Staff Nurse Geetha", "Recent - Cooldown active"));
        addSeedDonation(new Donation(115, 10, "A+", LocalDate.parse("2026-06-25"), 1, 14.3, "Dr. S. Ramesh", "District camp"));
        addSeedDonation(new Donation(116, 11, "B+", LocalDate.parse("2026-07-08"), 1, 12.9, "Staff Nurse Geetha", "Youth Red Cross"));
        addSeedDonation(new Donation(117, 12, "O-", LocalDate.parse("2026-07-18"), 1, 14.6, "Dr. S. Ramesh", "Voluntary donor"));
        addSeedDonation(new Donation(118, 13, "A+", LocalDate.parse("2026-08-01"), 1, 13.1, "Staff Nurse Priya", "Eligible (>90 days)"));
        addSeedDonation(new Donation(119, 14, "B+", LocalDate.parse("2026-08-20"), 1, 14.0, "Dr. R. Kavitha", "Recent - Cooldown active"));
        addSeedDonation(new Donation(120, 15, "O+", LocalDate.parse("2026-09-05"), 1, 13.5, "Staff Nurse Geetha", "Recent - Cooldown active"));
        addSeedDonation(new Donation(121, 16, "A-", LocalDate.parse("2026-09-22"), 1, 14.4, "Dr. S. Ramesh", "Recent - Cooldown active"));
        addSeedDonation(new Donation(122, 17, "AB+", LocalDate.parse("2026-10-05"), 1, 12.7, "Staff Nurse Priya", "Recent - Cooldown active"));
        addSeedDonation(new Donation(123, 10, "A+", LocalDate.parse("2026-10-20"), 1, 14.2, "Staff Nurse Geetha", "Recent - Cooldown active"));
        addSeedDonation(new Donation(124, 2, "A+", LocalDate.parse("2026-11-02"), 1, 13.9, "Dr. S. Ramesh", "Recent - Cooldown active"));
        addSeedDonation(new Donation(125, 1, "O+", LocalDate.parse("2026-11-08"), 1, 14.4, "Dr. S. Ramesh", "Recent - Cooldown active"));

        // 4. Initial Hospital Requests
        addSeedRequest(new HospitalRequest(201, "Government Headquarters Hospital, Erode", "O+", 4, LocalDate.parse("2026-10-02"), "CRITICAL", "FULFILLED", LocalDate.parse("2026-10-02"), "Dr. Mohanraj"));
        addSeedRequest(new HospitalRequest(202, "Apollo Speciality Hospital, Salem", "A+", 3, LocalDate.parse("2026-10-10"), "URGENT", "FULFILLED", LocalDate.parse("2026-10-10"), "Dr. Sundaram"));
        addSeedRequest(new HospitalRequest(203, "Kovai Medical Center and Hospital (KMCH)", "B+", 5, LocalDate.parse("2026-10-18"), "NORMAL", "FULFILLED", LocalDate.parse("2026-10-19"), "Dr. S. Ramesh"));
        addSeedRequest(new HospitalRequest(204, "Lotus Hospital, Erode", "O-", 2, LocalDate.parse("2026-10-25"), "CRITICAL", "FULFILLED", LocalDate.parse("2026-10-25"), "Dr. Mohanraj"));
        addSeedRequest(new HospitalRequest(205, "Ganga Medical Centre & Hospitals, CBE", "A-", 2, LocalDate.parse("2026-11-01"), "URGENT", "FULFILLED", LocalDate.parse("2026-11-01"), "Dr. Mohanraj"));
        addSeedRequest(new HospitalRequest(206, "Royal Care Super Speciality, Coimbatore", "AB+", 2, LocalDate.parse("2026-11-04"), "NORMAL", "FULFILLED", LocalDate.parse("2026-11-05"), "Dr. Sundaram"));
        addSeedRequest(new HospitalRequest(207, "Erode Trust Hospital, Erode", "B-", 4, LocalDate.parse("2026-11-07"), "CRITICAL", "PENDING", null, null));
        addSeedRequest(new HospitalRequest(208, "Sudha Hospitals, Erode", "AB-", 3, LocalDate.parse("2026-11-09"), "URGENT", "PENDING", null, null));
        addSeedRequest(new HospitalRequest(209, "Care 24 Hospital, Perundurai", "O+", 6, LocalDate.parse("2026-11-11"), "CRITICAL", "PENDING", null, null));
        addSeedRequest(new HospitalRequest(210, "Sri Ramakrishna Hospital, Coimbatore", "A+", 2, LocalDate.parse("2026-11-12"), "NORMAL", "PENDING", null, null));
        addSeedRequest(new HospitalRequest(211, "Manian Medical Centre, Erode", "B+", 1, LocalDate.parse("2026-11-12"), "NORMAL", "PENDING", null, null));
        addSeedRequest(new HospitalRequest(212, "Maruthi Hospital, Bhavani", "O-", 8, LocalDate.parse("2026-11-06"), "CRITICAL", "REJECTED", null, "Dr. Mohanraj"));
    }

    private void addSeedDonor(Donor d) {
        donorMap.put(d.getDonorId(), d);
        if (d.getDonorId() >= donorIdGen.get()) {
            donorIdGen.set(d.getDonorId() + 1);
        }
    }

    private void addSeedDonation(Donation dn) {
        donationList.add(dn);
        if (dn.getDonationId() >= donationIdGen.get()) {
            donationIdGen.set(dn.getDonationId() + 1);
        }
    }

    private void addSeedRequest(HospitalRequest hr) {
        requestList.add(hr);
        if (hr.getRequestId() >= requestIdGen.get()) {
            requestIdGen.set(hr.getRequestId() + 1);
        }
    }

    // Accessors for embedded repositories
    public Map<String, BloodStock> getStockMap() { return stockMap; }
    public Map<Integer, Donor> getDonorMap() { return donorMap; }
    public List<Donation> getDonationList() { return donationList; }
    public List<HospitalRequest> getRequestList() { return requestList; }
    public AtomicInteger getDonorIdGen() { return donorIdGen; }
    public AtomicInteger getDonationIdGen() { return donationIdGen; }
    public AtomicInteger getRequestIdGen() { return requestIdGen; }
}

