package com.bloodbank.service;

import com.bloodbank.dao.DonorDAO;
import com.bloodbank.model.Donor;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.*;
import java.util.stream.Collectors;

/**
 * Service to analyze donor eligibility based on clinical 90-day cooldown intervals.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class DonorEligibilityService {

    public static final int MINIMUM_COOLDOWN_DAYS = 90;
    private final DonorDAO donorDAO;

    public DonorEligibilityService(DonorDAO donorDAO) {
        this.donorDAO = donorDAO;
    }

    /**
     * Checks if a donor is eligible based on their last donation date.
     */
    public boolean isEligible(Optional<LocalDate> lastDonationDate) {
        if (lastDonationDate.isEmpty()) {
            return true; // First-time donor is always eligible
        }
        long daysSince = ChronoUnit.DAYS.between(lastDonationDate.get(), LocalDate.now());
        return daysSince >= MINIMUM_COOLDOWN_DAYS;
    }

    /**
     * Returns the days remaining before a donor becomes eligible.
     * Returns 0 if already eligible.
     */
    public long getDaysRemainingInCooldown(Optional<LocalDate> lastDonationDate) {
        if (lastDonationDate.isEmpty()) {
            return 0;
        }
        long daysSince = ChronoUnit.DAYS.between(lastDonationDate.get(), LocalDate.now());
        if (daysSince >= MINIMUM_COOLDOWN_DAYS) {
            return 0;
        }
        return MINIMUM_COOLDOWN_DAYS - daysSince;
    }

    /**
     * Evaluates a donor by ID and returns eligibility details.
     */
    public EligibilityReport checkDonorEligibility(int donorId) {
        Optional<Donor> donorOpt = donorDAO.getDonorById(donorId);
        if (donorOpt.isEmpty()) {
            return new EligibilityReport(null, false, "Donor ID not found", 0, null);
        }

        Donor donor = donorOpt.get();
        Optional<LocalDate> lastDate = donorDAO.getLastDonationDate(donorId);
        boolean eligible = isEligible(lastDate);
        long daysRemaining = getDaysRemainingInCooldown(lastDate);

        String message;
        if (lastDate.isEmpty()) {
            message = "Eligible (First-time voluntary donor)";
        } else if (eligible) {
            long daysSince = ChronoUnit.DAYS.between(lastDate.get(), LocalDate.now());
            message = String.format("Eligible (Last donated %d days ago on %s)", daysSince, lastDate.get());
        } else {
            message = String.format("Ineligible (Cooldown active: %d days remaining until next donation)", daysRemaining);
        }

        return new EligibilityReport(donor, eligible, message, daysRemaining, lastDate.orElse(null));
    }

    /**
     * Retrieves all donors eligible to donate right now, optionally filtered by blood group.
     */
    public List<EligibilityReport> getAvailableDonors(String bloodGroupFilter) {
        List<Donor> donors = (bloodGroupFilter == null || bloodGroupFilter.trim().isEmpty() || bloodGroupFilter.equalsIgnoreCase("ALL"))
                ? donorDAO.getAllDonors()
                : donorDAO.getDonorsByBloodGroup(bloodGroupFilter);

        return donors.stream()
                .map(d -> checkDonorEligibility(d.getDonorId()))
                .filter(EligibilityReport::isEligible)
                .sorted(Comparator.comparing((EligibilityReport r) -> r.getDonor().getBloodGroup())
                        .thenComparing(r -> r.getDonor().getName()))
                .collect(Collectors.toList());
    }

    /**
     * Value record class for eligibility reporting.
     */
    public static class EligibilityReport {
        private final Donor donor;
        private final boolean eligible;
        private final String statusMessage;
        private final long daysRemaining;
        private final LocalDate lastDonationDate;

        public EligibilityReport(Donor donor, boolean eligible, String statusMessage, 
                                 long daysRemaining, LocalDate lastDonationDate) {
            this.donor = donor;
            this.eligible = eligible;
            this.statusMessage = statusMessage;
            this.daysRemaining = daysRemaining;
            this.lastDonationDate = lastDonationDate;
        }

        public Donor getDonor() { return donor; }
        public boolean isEligible() { return eligible; }
        public String getStatusMessage() { return statusMessage; }
        public long getDaysRemaining() { return daysRemaining; }
        public LocalDate getLastDonationDate() { return lastDonationDate; }
    }
}
