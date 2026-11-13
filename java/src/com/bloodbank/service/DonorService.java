package com.bloodbank.service;

import com.bloodbank.dao.DonorDAO;
import com.bloodbank.model.Donor;
import com.bloodbank.util.InputValidator;

import java.util.List;
import java.util.Optional;

/**
 * Service orchestrating Donor business operations.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class DonorService {

    private final DonorDAO donorDAO;

    public DonorService(DonorDAO donorDAO) {
        this.donorDAO = donorDAO;
    }

    public boolean registerDonor(Donor donor) throws IllegalArgumentException {
        if (!InputValidator.isValidName(donor.getName())) {
            throw new IllegalArgumentException("Invalid donor name. Must contain 2 to 60 alphabetic characters.");
        }
        if (!InputValidator.isValidAge(donor.getAge())) {
            throw new IllegalArgumentException("Invalid donor age. Must be between 18 and 65 years.");
        }
        if (!InputValidator.isValidPhone(donor.getContactNumber())) {
            throw new IllegalArgumentException("Invalid phone number. Must be a valid 10-digit Indian mobile number.");
        }
        if (!InputValidator.isValidEmail(donor.getEmail())) {
            throw new IllegalArgumentException("Invalid email format.");
        }
        if (!InputValidator.isValidBloodGroup(donor.getBloodGroup())) {
            throw new IllegalArgumentException("Invalid blood group: " + donor.getBloodGroup());
        }

        return donorDAO.addDonor(donor);
    }

    public Optional<Donor> findDonorById(int donorId) {
        return donorDAO.getDonorById(donorId);
    }

    public List<Donor> getAllDonors() {
        return donorDAO.getAllDonors();
    }

    public List<Donor> getDonorsByBloodGroup(String bloodGroup) {
        return donorDAO.getDonorsByBloodGroup(bloodGroup);
    }
}

