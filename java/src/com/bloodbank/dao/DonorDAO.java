package com.bloodbank.dao;

import com.bloodbank.model.Donor;
import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

/**
 * Data Access Object interface for Donor operations.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public interface DonorDAO {
    boolean addDonor(Donor donor);
    Optional<Donor> getDonorById(int donorId);
    List<Donor> getAllDonors();
    List<Donor> getDonorsByBloodGroup(String bloodGroup);
    Optional<LocalDate> getLastDonationDate(int donorId);
    boolean updateDonor(Donor donor);
    boolean deleteDonor(int donorId);
}

