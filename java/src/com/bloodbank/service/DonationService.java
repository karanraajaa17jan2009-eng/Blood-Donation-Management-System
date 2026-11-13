package com.bloodbank.service;

import com.bloodbank.dao.BloodStockDAO;
import com.bloodbank.dao.DonationDAO;
import com.bloodbank.dao.DonorDAO;
import com.bloodbank.model.Donation;
import com.bloodbank.model.Donor;
import com.bloodbank.util.InputValidator;

import java.util.List;
import java.util.Optional;

/**
 * Service managing Blood Donations with automatic eligibility verification and inventory synchronization.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class DonationService {

    private final DonationDAO donationDAO;
    private final DonorDAO donorDAO;
    private final BloodStockDAO bloodStockDAO;
    private final DonorEligibilityService eligibilityService;

    public DonationService(DonationDAO donationDAO, DonorDAO donorDAO, 
                           BloodStockDAO bloodStockDAO, DonorEligibilityService eligibilityService) {
        this.donationDAO = donationDAO;
        this.donorDAO = donorDAO;
        this.bloodStockDAO = bloodStockDAO;
        this.eligibilityService = eligibilityService;
    }

    public DonationResult processDonation(Donation donation) {
        // 1. Verify donor existence
        Optional<Donor> donorOpt = donorDAO.getDonorById(donation.getDonorId());
        if (donorOpt.isEmpty()) {
            return new DonationResult(false, "Donor ID " + donation.getDonorId() + " not found in database.");
        }

        Donor donor = donorOpt.get();
        donation.setBloodGroup(donor.getBloodGroup());

        // 2. Clinical Hemoglobin check
        if (!InputValidator.isValidHemoglobin(donation.getHemoglobinLevel())) {
            return new DonationResult(false, String.format(
                    "Hemoglobin level (%.1f g/dL) is outside acceptable clinical range (12.0 - 20.0 g/dL).",
                    donation.getHemoglobinLevel()));
        }

        // 3. Units validation
        if (!InputValidator.isValidUnits(donation.getUnitsDonated())) {
            return new DonationResult(false, "Units donated must be between 1 and 10.");
        }

        // 4. Clinical 90-day Cooldown Eligibility Verification
        DonorEligibilityService.EligibilityReport eligibility = eligibilityService.checkDonorEligibility(donor.getDonorId());
        if (!eligibility.isEligible()) {
            return new DonationResult(false, String.format(
                    "[REJECTED] Donor is currently ineligible. Cooldown period active: %d days remaining.",
                    eligibility.getDaysRemaining()));
        }

        // 5. Atomic persistence: Record donation and increment blood stock
        boolean recorded = donationDAO.recordDonation(donation);
        if (!recorded) {
            return new DonationResult(false, "Failed to persist donation record into database.");
        }

        boolean stockUpdated = bloodStockDAO.updateStock(donor.getBloodGroup(), donation.getUnitsDonated());
        if (!stockUpdated) {
            return new DonationResult(false, "Donation logged, but failed to increment blood stock inventory.");
        }

        return new DonationResult(true, String.format(
                "Donation successfully recorded (ID: %d)! Added %d unit(s) of %s to stock.",
                donation.getDonationId(), donation.getUnitsDonated(), donor.getBloodGroup()));
    }

    public List<Donation> getAllDonations() {
        return donationDAO.getAllDonations();
    }

    public List<Donation> getDonationsByDonorId(int donorId) {
        return donationDAO.getDonationsByDonorId(donorId);
    }

    public static class DonationResult {
        private final boolean success;
        private final String message;

        public DonationResult(boolean success, String message) {
            this.success = success;
            this.message = message;
        }

        public boolean isSuccess() { return success; }
        public String getMessage() { return message; }
    }
}

