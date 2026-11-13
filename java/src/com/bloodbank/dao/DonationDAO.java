package com.bloodbank.dao;

import com.bloodbank.model.Donation;
import java.util.List;
import java.util.Map;

/**
 * Data Access Object interface for Donation operations.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public interface DonationDAO {
    boolean recordDonation(Donation donation);
    List<Donation> getAllDonations();
    List<Donation> getDonationsByDonorId(int donorId);
    List<Donation> getDonationsByBloodGroup(String bloodGroup);
    Map<String, Integer> getTotalUnitsByBloodGroup();
    int getTotalDonationCount();
}

