package com.bloodbank.dao.impl;

import com.bloodbank.dao.DatabaseManager;
import com.bloodbank.dao.DonorDAO;
import com.bloodbank.model.Donation;
import com.bloodbank.model.Donor;

import java.sql.*;
import java.time.LocalDate;
import java.util.*;
import java.util.stream.Collectors;

/**
 * Implementation of DonorDAO with support for both JDBC and Synchronized Memory Engine.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class DonorDAOImpl implements DonorDAO {

    private final DatabaseManager dbManager = DatabaseManager.getInstance();

    @Override
    public boolean addDonor(Donor donor) {
        if (dbManager.isJdbcActive()) {
            String sql = "INSERT INTO donors (name, age, gender, contact_number, email, blood_group, city, registration_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
            try (PreparedStatement pstmt = dbManager.getJdbcConnection().prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
                pstmt.setString(1, donor.getName());
                pstmt.setInt(2, donor.getAge());
                pstmt.setString(3, donor.getGender());
                pstmt.setString(4, donor.getContactNumber());
                pstmt.setString(5, donor.getEmail());
                pstmt.setString(6, donor.getBloodGroup());
                pstmt.setString(7, donor.getCity());
                pstmt.setString(8, donor.getRegistrationDate().toString());
                int rows = pstmt.executeUpdate();
                if (rows > 0) {
                    try (ResultSet rs = pstmt.getGeneratedKeys()) {
                        if (rs.next()) donor.setDonorId(rs.getInt(1));
                    }
                    return true;
                }
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
            }
        }

        // Embedded storage fallback
        int newId = dbManager.getDonorIdGen().getAndIncrement();
        donor.setDonorId(newId);
        dbManager.getDonorMap().put(newId, donor);
        return true;
    }

    @Override
    public Optional<Donor> getDonorById(int donorId) {
        if (dbManager.isJdbcActive()) {
            String sql = "SELECT * FROM donors WHERE donor_id = ?";
            try (PreparedStatement pstmt = dbManager.getJdbcConnection().prepareStatement(sql)) {
                pstmt.setInt(1, donorId);
                try (ResultSet rs = pstmt.executeQuery()) {
                    if (rs.next()) {
                        return Optional.of(new Donor(
                                rs.getInt("donor_id"),
                                rs.getString("name"),
                                rs.getInt("age"),
                                rs.getString("gender"),
                                rs.getString("contact_number"),
                                rs.getString("email"),
                                rs.getString("blood_group"),
                                rs.getString("city"),
                                LocalDate.parse(rs.getString("registration_date"))
                        ));
                    }
                }
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
            }
        }

        return Optional.ofNullable(dbManager.getDonorMap().get(donorId));
    }

    @Override
    public List<Donor> getAllDonors() {
        if (dbManager.isJdbcActive()) {
            List<Donor> list = new ArrayList<>();
            String sql = "SELECT * FROM donors ORDER BY donor_id ASC";
            try (Statement stmt = dbManager.getJdbcConnection().createStatement();
                 ResultSet rs = stmt.executeQuery(sql)) {
                while (rs.next()) {
                    list.add(new Donor(
                            rs.getInt("donor_id"),
                            rs.getString("name"),
                            rs.getInt("age"),
                            rs.getString("gender"),
                            rs.getString("contact_number"),
                            rs.getString("email"),
                            rs.getString("blood_group"),
                            rs.getString("city"),
                            LocalDate.parse(rs.getString("registration_date"))
                    ));
                }
                return list;
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
            }
        }

        return dbManager.getDonorMap().values().stream()
                .sorted(Comparator.comparingInt(Donor::getDonorId))
                .collect(Collectors.toList());
    }

    @Override
    public List<Donor> getDonorsByBloodGroup(String bloodGroup) {
        return getAllDonors().stream()
                .filter(d -> d.getBloodGroup().equalsIgnoreCase(bloodGroup))
                .collect(Collectors.toList());
    }

    @Override
    public Optional<LocalDate> getLastDonationDate(int donorId) {
        if (dbManager.isJdbcActive()) {
            String sql = "SELECT MAX(donation_date) AS last_date FROM donations WHERE donor_id = ?";
            try (PreparedStatement pstmt = dbManager.getJdbcConnection().prepareStatement(sql)) {
                pstmt.setInt(1, donorId);
                try (ResultSet rs = pstmt.executeQuery()) {
                    if (rs.next() && rs.getString("last_date") != null) {
                        return Optional.of(LocalDate.parse(rs.getString("last_date")));
                    }
                }
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
            }
        }

        return dbManager.getDonationList().stream()
                .filter(dn -> dn.getDonorId() == donorId)
                .map(Donation::getDonationDate)
                .max(LocalDate::compareTo);
    }

    @Override
    public boolean updateDonor(Donor donor) {
        if (dbManager.isJdbcActive()) {
            String sql = "UPDATE donors SET name=?, age=?, gender=?, contact_number=?, email=?, blood_group=?, city=? WHERE donor_id=?";
            try (PreparedStatement pstmt = dbManager.getJdbcConnection().prepareStatement(sql)) {
                pstmt.setString(1, donor.getName());
                pstmt.setInt(2, donor.getAge());
                pstmt.setString(3, donor.getGender());
                pstmt.setString(4, donor.getContactNumber());
                pstmt.setString(5, donor.getEmail());
                pstmt.setString(6, donor.getBloodGroup());
                pstmt.setString(7, donor.getCity());
                pstmt.setInt(8, donor.getDonorId());
                return pstmt.executeUpdate() > 0;
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
            }
        }

        if (dbManager.getDonorMap().containsKey(donor.getDonorId())) {
            dbManager.getDonorMap().put(donor.getDonorId(), donor);
            return true;
        }
        return false;
    }

    @Override
    public boolean deleteDonor(int donorId) {
        if (dbManager.isJdbcActive()) {
            String sql = "DELETE FROM donors WHERE donor_id = ?";
            try (PreparedStatement pstmt = dbManager.getJdbcConnection().prepareStatement(sql)) {
                pstmt.setInt(1, donorId);
                return pstmt.executeUpdate() > 0;
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
            }
        }

        return dbManager.getDonorMap().remove(donorId) != null;
    }
}

