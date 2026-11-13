package com.bloodbank.service;

import com.bloodbank.dao.BloodStockDAO;
import com.bloodbank.dao.DonationDAO;
import com.bloodbank.dao.DonorDAO;
import com.bloodbank.dao.HospitalRequestDAO;
import com.bloodbank.model.BloodStock;
import com.bloodbank.model.Donation;
import com.bloodbank.model.Donor;
import com.bloodbank.model.HospitalRequest;
import com.bloodbank.util.TableFormatter;

import java.util.*;
import java.util.stream.Collectors;

/**
 * Service generating analytical management summaries using Java Streams and Lambda expressions.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class ReportService {

    private final BloodStockDAO bloodStockDAO;
    private final DonorDAO donorDAO;
    private final DonationDAO donationDAO;
    private final HospitalRequestDAO hospitalRequestDAO;
    private final DonorEligibilityService eligibilityService;

    public ReportService(BloodStockDAO bloodStockDAO, DonorDAO donorDAO, 
                         DonationDAO donationDAO, HospitalRequestDAO hospitalRequestDAO,
                         DonorEligibilityService eligibilityService) {
        this.bloodStockDAO = bloodStockDAO;
        this.donorDAO = donorDAO;
        this.donationDAO = donationDAO;
        this.hospitalRequestDAO = hospitalRequestDAO;
        this.eligibilityService = eligibilityService;
    }

    public void printStockSummaryReport() {
        List<BloodStock> stocks = bloodStockDAO.getAllStock();
        Map<String, Integer> groupDonations = donationDAO.getTotalUnitsByBloodGroup();

        String[] headers = {"Blood Group", "Available Units", "Min Threshold", "Surplus / Deficit", "Status", "Total Historical Units Donated"};
        List<String[]> rows = new ArrayList<>();

        int totalUnits = 0;
        for (BloodStock s : stocks) {
            int surplus = s.getAvailableUnits() - s.getMinimumThreshold();
            int historical = groupDonations.getOrDefault(s.getBloodGroup(), 0);
            totalUnits += s.getAvailableUnits();

            rows.add(new String[]{
                    s.getBloodGroup(),
                    String.valueOf(s.getAvailableUnits()),
                    String.valueOf(s.getMinimumThreshold()),
                    (surplus >= 0 ? "+" + surplus : String.valueOf(surplus)),
                    s.getStatus(),
                    String.valueOf(historical)
            });
        }

        TableFormatter.printTable("Real-Time Blood Stock Inventory Report", headers, rows);
        System.out.printf(" >> Total Blood Units in Storage: %d units across 8 blood groups.\n\n", totalUnits);
    }

    public void printDonorAvailabilityReport(String bloodGroupFilter) {
        List<DonorEligibilityService.EligibilityReport> reports = eligibilityService.getAvailableDonors(bloodGroupFilter);

        String[] headers = {"Donor ID", "Donor Name", "Blood Group", "Age", "Phone", "City", "Last Donated", "Availability Status"};
        List<String[]> rows = new ArrayList<>();

        for (DonorEligibilityService.EligibilityReport r : reports) {
            Donor d = r.getDonor();
            String lastDateStr = (r.getLastDonationDate() != null) ? r.getLastDonationDate().toString() : "Never Donated";
            rows.add(new String[]{
                    String.valueOf(d.getDonorId()),
                    d.getName(),
                    d.getBloodGroup(),
                    String.valueOf(d.getAge()),
                    d.getContactNumber(),
                    d.getCity(),
                    lastDateStr,
                    "AVAILABLE (Eligible)"
            });
        }

        String filterNote = (bloodGroupFilter != null && !bloodGroupFilter.equalsIgnoreCase("ALL"))
                ? " [Filtered for " + bloodGroupFilter + "]" : " [All Groups]";
        TableFormatter.printTable("Available Donors Report (90-Day Medical Interval Passed)" + filterNote, headers, rows);
    }

    public void printDonationHistoryReport() {
        List<Donation> donations = donationDAO.getAllDonations();
        Map<Integer, Donor> donorMap = donorDAO.getAllDonors().stream()
                .collect(Collectors.toMap(Donor::getDonorId, d -> d, (a, b) -> a));

        String[] headers = {"Donation ID", "Donor Name", "Blood Group", "Date", "Units", "Hb (g/dL)", "Phlebotomist", "Remarks"};
        List<String[]> rows = new ArrayList<>();

        for (Donation dn : donations) {
            Donor d = donorMap.get(dn.getDonorId());
            String donorName = (d != null) ? d.getName() : "Unknown ID #" + dn.getDonorId();

            rows.add(new String[]{
                    String.valueOf(dn.getDonationId()),
                    donorName,
                    dn.getBloodGroup(),
                    dn.getDonationDate().toString(),
                    String.valueOf(dn.getUnitsDonated()),
                    String.format("%.1f", dn.getHemoglobinLevel()),
                    dn.getPhlebotomistName(),
                    dn.getRemarks()
            });
        }

        TableFormatter.printTable("Chronological Blood Donation History Log", headers, rows);
    }

    public void printHospitalRequestsReport() {
        List<HospitalRequest> requests = hospitalRequestDAO.getAllRequests();

        String[] headers = {"Req ID", "Hospital Name", "Blood Group", "Units", "Request Date", "Urgency", "Status", "Fulfillment Date"};
        List<String[]> rows = new ArrayList<>();

        for (HospitalRequest r : requests) {
            rows.add(new String[]{
                    String.valueOf(r.getRequestId()),
                    r.getHospitalName(),
                    r.getBloodGroup(),
                    String.valueOf(r.getUnitsRequested()),
                    r.getRequestDate().toString(),
                    r.getUrgencyLevel(),
                    r.getStatus(),
                    r.getFulfillmentDate() != null ? r.getFulfillmentDate().toString() : "N/A"
            });
        }

        TableFormatter.printTable("Hospital Blood Requisitions and Issuance Report", headers, rows);
    }
}

