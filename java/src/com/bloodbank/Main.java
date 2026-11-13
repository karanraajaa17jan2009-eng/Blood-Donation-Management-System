package com.bloodbank;

import com.bloodbank.dao.*;
import com.bloodbank.dao.impl.*;
import com.bloodbank.model.*;
import com.bloodbank.service.*;
import com.bloodbank.util.InputValidator;
import com.bloodbank.util.TableFormatter;

import java.time.LocalDate;
import java.util.*;

/**
 * Interactive Console Application Entry Point.
 * Academic Activity - Project-Based Assessment
 * Scenario 15: Blood Donation Management and Donor Availability Analysis System
 *
 * Student Name: Karan Raajaa V
 * Register Number: 732925ITR045
 * Class / Section: 25IT3A&B (Roll No. 45)
 * Institution: Velalar College of Engineering and Technology, Erode - 638012
 */
public class Main {

    private final Scanner scanner = new Scanner(System.in);

    // DAOs
    private final DonorDAO donorDAO = new DonorDAOImpl();
    private final DonationDAO donationDAO = new DonationDAOImpl();
    private final BloodStockDAO bloodStockDAO = new BloodStockDAOImpl();
    private final HospitalRequestDAO hospitalRequestDAO = new HospitalRequestDAOImpl();

    // Services
    private final DonorEligibilityService eligibilityService = new DonorEligibilityService(donorDAO);
    private final DonorService donorService = new DonorService(donorDAO);
    private final DonationService donationService = new DonationService(donationDAO, donorDAO, bloodStockDAO, eligibilityService);
    private final InventoryService inventoryService = new InventoryService(bloodStockDAO);
    private final HospitalRequestService hospitalRequestService = new HospitalRequestService(hospitalRequestDAO, bloodStockDAO);
    private final ReportService reportService = new ReportService(bloodStockDAO, donorDAO, donationDAO, hospitalRequestDAO, eligibilityService);

    public static void main(String[] args) {
        Main app = new Main();
        app.run();
    }

    public void run() {
        printBanner();
        boolean running = true;

        while (running) {
            printMainMenu();
            System.out.print("Enter your choice (0-8): ");
            String input = scanner.nextLine().trim();

            switch (input) {
                case "1":
                    handleRegisterDonor();
                    break;
                case "2":
                    handleRecordDonation();
                    break;
                case "3":
                    handleViewStock();
                    break;
                case "4":
                    handleHospitalRequests();
                    break;
                case "5":
                    handleDonorAvailabilityAudit();
                    break;
                case "6":
                    handleReportsSubmenu();
                    break;
                case "7":
                    handleRunPythonAnalytics();
                    break;
                case "8":
                    handleSystemInfo();
                    break;
                case "0":
                    System.out.println("\nThank you for using the Blood Donation Management System. Goodbye!");
                    running = false;
                    break;
                default:
                    System.out.println("\n[ERROR] Invalid menu choice. Please select a number between 0 and 8.\n");
            }
        }
    }

    private void printBanner() {
        System.out.println("================================================================================");
        System.out.println("          VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY, ERODE - 12            ");
        System.out.println("                   DEPARTMENT OF INFORMATION TECHNOLOGY                         ");
        System.out.println("              ACADEMIC YEAR: 2026 - 2027 (ODD) | CLASS: 25IT3A&B                ");
        System.out.println("--------------------------------------------------------------------------------");
        System.out.println("   Scenario 15: Blood Donation Management and Donor Availability Analysis System");
        System.out.println("   Developed by: Karan Raajaa V  |  Register No: 732925ITR045 (Roll No. 45)      ");
        System.out.println("================================================================================");
    }

    private void printMainMenu() {
        System.out.println("\n+------------------------------------------------------------------------------+");
        System.out.println("|                            MAIN OPERATION MENU                               |");
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("|  [1] Register New Voluntary Donor                                            |");
        System.out.println("|  [2] Record Blood Donation (with 90-Day Clinical Eligibility Verification)   |");
        System.out.println("|  [3] View Blood Stock Inventory & Safety Threshold Alerts                    |");
        System.out.println("|  [4] Hospital Blood Requisitions & Unit Issuance                             |");
        System.out.println("|  [5] Donor Availability & 90-Day Eligibility Audit (Filter by Group)         |");
        System.out.println("|  [6] View Analytical Management Reports                                      |");
        System.out.println("|  [7] Trigger Python Data Science & Visualizations Pipeline                   |");
        System.out.println("|  [8] System Architecture & Database Metadata                                 |");
        System.out.println("|  [0] Exit System                                                             |");
        System.out.println("+------------------------------------------------------------------------------+");
    }

    // -------------------------------------------------------------------------
    // Module 1: Register New Donor
    // -------------------------------------------------------------------------
    private void handleRegisterDonor() {
        System.out.println("\n--- [1] Register New Voluntary Donor ---");
        try {
            System.out.print("Enter Donor Full Name: ");
            String name = scanner.nextLine().trim();

            System.out.print("Enter Age (18-65): ");
            int age = Integer.parseInt(scanner.nextLine().trim());

            System.out.print("Enter Gender (Male/Female/Other): ");
            String gender = scanner.nextLine().trim();

            System.out.print("Enter 10-Digit Contact Number: ");
            String phone = scanner.nextLine().trim();

            System.out.print("Enter Email Address: ");
            String email = scanner.nextLine().trim();

            System.out.print("Enter Blood Group (A+, A-, B+, B-, AB+, AB-, O+, O-): ");
            String bloodGroup = scanner.nextLine().trim().toUpperCase();

            System.out.print("Enter City / Location: ");
            String city = scanner.nextLine().trim();

            Donor donor = new Donor(name, age, gender, phone, email, bloodGroup, city);
            boolean success = donorService.registerDonor(donor);

            if (success) {
                System.out.printf("\n[SUCCESS] Donor '%s' registered successfully with ID #%d!\n",
                        donor.getName(), donor.getDonorId());
            } else {
                System.out.println("\n[ERROR] Failed to save donor to database.\n");
            }
        } catch (NumberFormatException e) {
            System.out.println("\n[ERROR] Invalid number format entered for age.");
        } catch (IllegalArgumentException e) {
            System.out.println("\n[VALIDATION FAILED] " + e.getMessage());
        }
    }

    // -------------------------------------------------------------------------
    // Module 2: Record Blood Donation
    // -------------------------------------------------------------------------
    private void handleRecordDonation() {
        System.out.println("\n--- [2] Record Blood Donation ---");
        try {
            System.out.print("Enter Registered Donor ID: ");
            int donorId = Integer.parseInt(scanner.nextLine().trim());

            // Check eligibility upfront to provide immediate feedback
            DonorEligibilityService.EligibilityReport report = eligibilityService.checkDonorEligibility(donorId);
            if (report.getDonor() == null) {
                System.out.printf("\n[ERROR] Donor ID #%d not found in records.\n", donorId);
                return;
            }

            System.out.printf(" >> Donor Name: %s | Blood Group: %s | Status: %s\n",
                    report.getDonor().getName(), report.getDonor().getBloodGroup(), report.getStatusMessage());

            if (!report.isEligible()) {
                System.out.printf("\n[BLOCKED] Donation cannot be accepted. Medical cooldown active: %d days remaining.\n",
                        report.getDaysRemaining());
                return;
            }

            System.out.print("Enter Number of Units Donated (Standard: 1): ");
            int units = Integer.parseInt(scanner.nextLine().trim());

            System.out.print("Enter Donor Hemoglobin Level in g/dL (>= 12.0): ");
            double hb = Double.parseDouble(scanner.nextLine().trim());

            System.out.print("Enter Phlebotomist / Attending Nurse Name: ");
            String staff = scanner.nextLine().trim();
            if (staff.isEmpty()) staff = "Staff Duty Officer";

            System.out.print("Enter Clinical Remarks: ");
            String remarks = scanner.nextLine().trim();
            if (remarks.isEmpty()) remarks = "Fit for donation";

            Donation donation = new Donation(0, donorId, report.getDonor().getBloodGroup(),
                    LocalDate.now(), units, hb, staff, remarks);

            DonationService.DonationResult result = donationService.processDonation(donation);
            if (result.isSuccess()) {
                System.out.println("\n[SUCCESS] " + result.getMessage());
            } else {
                System.out.println("\n[REJECTED] " + result.getMessage());
            }

        } catch (NumberFormatException e) {
            System.out.println("\n[ERROR] Invalid numeric input for ID, units, or hemoglobin.");
        }
    }

    // -------------------------------------------------------------------------
    // Module 3: View Blood Stock
    // -------------------------------------------------------------------------
    private void handleViewStock() {
        reportService.printStockSummaryReport();

        List<BloodStock> lowStocks = inventoryService.checkLowStockAlerts();
        if (!lowStocks.isEmpty()) {
            System.out.println("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
            System.out.println("                      CRITICAL LOW STOCK ALERTS                         ");
            System.out.println("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
            for (BloodStock bs : lowStocks) {
                System.out.printf(" [ALERT] Blood Group %s has only %d unit(s) available (Safety Buffer: %d units)!\n",
                        bs.getBloodGroup(), bs.getAvailableUnits(), bs.getMinimumThreshold());
            }
            System.out.println(" >> Recommend organizing targeted donation drives for the above groups.");
            System.out.println("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
        }
    }

    // -------------------------------------------------------------------------
    // Module 4: Hospital Blood Requisitions
    // -------------------------------------------------------------------------
    private void handleHospitalRequests() {
        System.out.println("\n--- [4] Hospital Blood Requisitions & Unit Issuance ---");
        System.out.println(" 1. View All Hospital Requests");
        System.out.println(" 2. View Pending Requests Only");
        System.out.println(" 3. Submit New Hospital Requisition");
        System.out.println(" 4. Fulfill & Issue Blood Units to Hospital");
        System.out.println(" 5. Return to Main Menu");
        System.out.print("Select sub-option (1-5): ");
        String sub = scanner.nextLine().trim();

        switch (sub) {
            case "1":
                reportService.printHospitalRequestsReport();
                break;
            case "2":
                printPendingHospitalRequests();
                break;
            case "3":
                submitHospitalRequest();
                break;
            case "4":
                fulfillHospitalRequest();
                break;
            case "5":
                break;
            default:
                System.out.println("[ERROR] Invalid sub-option.");
        }
    }

    private void printPendingHospitalRequests() {
        List<HospitalRequest> pending = hospitalRequestService.getPendingRequests();
        String[] headers = {"Req ID", "Hospital Name", "Blood Group", "Units Needed", "Request Date", "Urgency"};
        List<String[]> rows = new ArrayList<>();
        for (HospitalRequest r : pending) {
            rows.add(new String[]{
                    String.valueOf(r.getRequestId()),
                    r.getHospitalName(),
                    r.getBloodGroup(),
                    String.valueOf(r.getUnitsRequested()),
                    r.getRequestDate().toString(),
                    r.getUrgencyLevel()
            });
        }
        TableFormatter.printTable("Active Pending Hospital Requisitions", headers, rows);
    }

    private void submitHospitalRequest() {
        try {
            System.out.print("Enter Hospital / Medical Facility Name: ");
            String hospital = scanner.nextLine().trim();

            System.out.print("Enter Blood Group Needed (A+, A-, etc.): ");
            String bg = scanner.nextLine().trim().toUpperCase();

            System.out.print("Enter Number of Units Requested: ");
            int units = Integer.parseInt(scanner.nextLine().trim());

            System.out.print("Enter Urgency Level (NORMAL / URGENT / CRITICAL): ");
            String urgency = scanner.nextLine().trim().toUpperCase();

            HospitalRequest req = new HospitalRequest(hospital, bg, units, urgency);
            boolean ok = hospitalRequestService.submitRequest(req);
            if (ok) {
                System.out.printf("\n[SUCCESS] Requisition logged with Request ID #%d!\n", req.getRequestId());
            } else {
                System.out.println("\n[ERROR] Failed to save request.");
            }
        } catch (Exception e) {
            System.out.println("\n[ERROR] " + e.getMessage());
        }
    }

    private void fulfillHospitalRequest() {
        try {
            System.out.print("Enter Request ID to Fulfill & Issue Units: ");
            int reqId = Integer.parseInt(scanner.nextLine().trim());

            System.out.print("Enter Authorizing Officer / Doctor Name: ");
            String authBy = scanner.nextLine().trim();
            if (authBy.isEmpty()) authBy = "Duty Medical Officer";

            HospitalRequestService.RequestFulfillmentResult res =
                    hospitalRequestService.fulfillRequest(reqId, authBy);

            if (res.isSuccess()) {
                System.out.println("\n[SUCCESS] " + res.getMessage());
            } else {
                System.out.println("\n[FAILED] " + res.getMessage());
            }
        } catch (NumberFormatException e) {
            System.out.println("\n[ERROR] Invalid Request ID format.");
        }
    }

    // -------------------------------------------------------------------------
    // Module 5: Donor Availability Audit
    // -------------------------------------------------------------------------
    private void handleDonorAvailabilityAudit() {
        System.out.println("\n--- [5] Donor Availability & 90-Day Eligibility Audit ---");
        System.out.print("Enter Blood Group filter (or press Enter / type ALL for all groups): ");
        String filter = scanner.nextLine().trim().toUpperCase();
        if (filter.isEmpty()) filter = "ALL";

        reportService.printDonorAvailabilityReport(filter);
    }

    // -------------------------------------------------------------------------
    // Module 6: Analytical Management Reports
    // -------------------------------------------------------------------------
    private void handleReportsSubmenu() {
        System.out.println("\n--- [6] Analytical Management Reports ---");
        System.out.println(" 1. Comprehensive Blood Stock Inventory Status");
        System.out.println(" 2. Complete Chronological Donation History Log");
        System.out.println(" 3. Hospital Requisition Status Summary");
        System.out.println(" 4. All Registered Donors Directory");
        System.out.println(" 5. Return to Main Menu");
        System.out.print("Select report (1-5): ");
        String choice = scanner.nextLine().trim();

        switch (choice) {
            case "1":
                reportService.printStockSummaryReport();
                break;
            case "2":
                reportService.printDonationHistoryReport();
                break;
            case "3":
                reportService.printHospitalRequestsReport();
                break;
            case "4":
                printAllDonorsDirectory();
                break;
            case "5":
                break;
            default:
                System.out.println("[ERROR] Invalid choice.");
        }
    }

    private void printAllDonorsDirectory() {
        List<Donor> donors = donorService.getAllDonors();
        String[] headers = {"ID", "Name", "Age", "Gender", "Blood Group", "Contact Number", "Email", "City", "Registered Date"};
        List<String[]> rows = new ArrayList<>();
        for (Donor d : donors) {
            rows.add(new String[]{
                    String.valueOf(d.getDonorId()),
                    d.getName(),
                    String.valueOf(d.getAge()),
                    d.getGender(),
                    d.getBloodGroup(),
                    d.getContactNumber(),
                    d.getEmail(),
                    d.getCity(),
                    d.getRegistrationDate().toString()
            });
        }
        TableFormatter.printTable("Registered Voluntary Donors Directory", headers, rows);
    }

    // -------------------------------------------------------------------------
    // Module 7: Python Analytics Trigger
    // -------------------------------------------------------------------------
    private void handleRunPythonAnalytics() {
        System.out.println("\n--- [7] Trigger Python Data Science & Visualization Pipeline ---");
        System.out.println("Executing: python python/main_analysis.py");
        try {
            ProcessBuilder pb = new ProcessBuilder("python", "python/main_analysis.py");
            pb.inheritIO();
            Process process = pb.start();
            int exitCode = process.waitFor();
            if (exitCode == 0) {
                System.out.println("\n[SUCCESS] Python analysis pipeline executed successfully!");
                System.out.println(" >> Charts generated in folder: visualizations/\n");
            } else {
                System.out.printf("\n[WARNING] Python process returned exit code %d.\n", exitCode);
            }
        } catch (Exception e) {
            System.out.println("[INFO] To run the Python visualization pipeline manually from terminal:");
            System.out.println("       python python/main_analysis.py");
            System.out.println("       (Make sure python is installed and in your system PATH)");
        }
    }

    // -------------------------------------------------------------------------
    // Module 8: System Architecture & Metadata
    // -------------------------------------------------------------------------
    private void handleSystemInfo() {
        System.out.println("\n================================================================================");
        System.out.println("                          SYSTEM INFORMATION & METADATA                         ");
        System.out.println("================================================================================");
        System.out.println(" Project Title   : Blood Donation Management and Donor Availability Analysis");
        System.out.println(" Scenario Number : Scenario 15");
        System.out.println(" Student Name    : Karan Raajaa V");
        System.out.println(" Register Number : 732925ITR045 (Roll No: 45)");
        System.out.println(" Department      : Department of Information Technology");
        System.out.println(" Institution     : Velalar College of Engineering and Technology, Erode - 12");
        System.out.println(" Academic Year   : 2026 - 2027 (ODD)");
        System.out.println(" Courses Mapped  : 25ITT31 (DBMS), 25ITT32 (Java), 25ITT33 (SE), 25ITC31 (Data Science)");
        System.out.println(" Architecture    : Multi-Tier Layered Architecture (Model - DAO - Service - UI)");
        System.out.println(" Database Engine : SQLite 3 (Default) / MySQL 8.0+ Compatible");
        System.out.println(" Database Status : " + (DatabaseManager.getInstance().isJdbcActive() ? "Connected via JDBC" : "Synchronized Memory Engine Active"));
        System.out.println(" Registered Donors: " + donorDAO.getAllDonors().size());
        System.out.println(" Total Donations  : " + donationDAO.getTotalDonationCount());
        System.out.println(" Hospital Requests: " + hospitalRequestDAO.getAllRequests().size());
        System.out.println("================================================================================\n");
    }
}
