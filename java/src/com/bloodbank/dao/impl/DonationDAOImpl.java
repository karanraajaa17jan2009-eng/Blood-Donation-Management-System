package com.bloodbank.dao.impl;

import com.bloodbank.dao.DatabaseManager;
import com.bloodbank.dao.DonationDAO;
import com.bloodbank.model.Donation;

import java.sql.*;
import java.time.LocalDate;
import java.util.*;
import java.util.stream.Collectors;

/**
 * Implementation of DonationDAO with JDBC and Synchronized Memory Engine support.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class DonationDAOImpl implements DonationDAO {

    private final DatabaseManager dbManager = DatabaseManager.getInstance();

    @Override
    public boolean recordDonation(Donation donation) {
        if (dbManager.isJdbcActive()) {
            String sql = "INSERT INTO donations (donor_id, blood_group, donation_date, units_donated, hemoglobin_level, phlebotomist_name, remarks) VALUES (?, ?, ?, ?, ?, ?, ?)";
            try (PreparedStatement pstmt = dbManager.getJdbcConnection().prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
                pstmt.setInt(1, donation.getDonorId());
                pstmt.setString(2, donation.getBloodGroup());
                pstmt.setString(3, donation.getDonationDate().toString());
                pstmt.setInt(4, donation.getUnitsDonated());
                pstmt.setDouble(5, donation.getHemoglobinLevel());
                pstmt.setString(6, donation.getPhlebotomistName());
                pstmt.setString(7, donation.getRemarks());
                int rows = pstmt.executeUpdate();
                if (rows > 0) {
                    try (ResultSet rs = pstmt.getGeneratedKeys()) {
                        if (rs.next()) donation.setDonationId(rs.getInt(1));
                    }
                    return true;
                }
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
            }
        }

        // Embedded storage fallback
        int newId = dbManager.getDonationIdGen().getAndIncrement();
        donation.setDonationId(newId);
        dbManager.getDonationList().add(donation);
        return true;
    }

    @Override
    public List<Donation> getAllDonations() {
        if (dbManager.isJdbcActive()) {
            List<Donation> list = new ArrayList<>();
            String sql = "SELECT * FROM donations ORDER BY donation_date DESC, donation_id DESC";
            try (Statement stmt = dbManager.getJdbcConnection().createStatement();
                 ResultSet rs = stmt.executeQuery(sql)) {
                while (rs.next()) {
                    list.add(new Donation(
                            rs.getInt("donation_id"),
                            rs.getInt("donor_id"),
                            rs.getString("blood_group"),
                            LocalDate.parse(rs.getString("donation_date")),
                            rs.getInt("units_donated"),
                            rs.getDouble("hemoglobin_level"),
                            rs.getString("phlebotomist_name"),
                            rs.getString("remarks")
                    ));
                }
                return list;
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
            }
        }

        return new ArrayList<>(dbManager.getDonationList());
    }

    @Override
    public List<Donation> getDonationsByDonorId(int donorId) {
        return getAllDonations().stream()
                .filter(d -> d.getDonorId() == donorId)
                .collect(Collectors.toList());
    }

    @Override
    public List<Donation> getDonationsByBloodGroup(String bloodGroup) {
        return getAllDonations().stream()
                .filter(d -> d.getBloodGroup().equalsIgnoreCase(bloodGroup))
                .collect(Collectors.toList());
    }

    @Override
    public Map<String, Integer> getTotalUnitsByBloodGroup() {
        return getAllDonations().stream()
                .collect(Collectors.groupingBy(
                        Donation::getBloodGroup,
                        Collectors.summingInt(Donation::getUnitsDonated)
                ));
    }

    @Override
    public int getTotalDonationCount() {
        return getAllDonations().size();
    }
}
