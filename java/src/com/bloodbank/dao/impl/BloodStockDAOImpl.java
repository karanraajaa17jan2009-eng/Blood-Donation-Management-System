package com.bloodbank.dao.impl;

import com.bloodbank.dao.BloodStockDAO;
import com.bloodbank.dao.DatabaseManager;
import com.bloodbank.model.BloodStock;

import java.sql.*;
import java.time.LocalDateTime;
import java.util.*;
import java.util.stream.Collectors;

/**
 * Implementation of BloodStockDAO with transactional updates.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class BloodStockDAOImpl implements BloodStockDAO {

    private final DatabaseManager dbManager = DatabaseManager.getInstance();

    @Override
    public List<BloodStock> getAllStock() {
        if (dbManager.isJdbcActive()) {
            List<BloodStock> list = new ArrayList<>();
            String sql = "SELECT * FROM blood_stock ORDER BY blood_group ASC";
            try (Statement stmt = dbManager.getJdbcConnection().createStatement();
                 ResultSet rs = stmt.executeQuery(sql)) {
                while (rs.next()) {
                    list.add(new BloodStock(
                            rs.getString("blood_group"),
                            rs.getInt("available_units"),
                            rs.getInt("minimum_threshold"),
                            LocalDateTime.now()
                    ));
                }
                return list;
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
            }
        }

        return dbManager.getStockMap().values().stream()
                .sorted(Comparator.comparing(BloodStock::getBloodGroup))
                .collect(Collectors.toList());
    }

    @Override
    public Optional<BloodStock> getStockByGroup(String bloodGroup) {
        if (dbManager.isJdbcActive()) {
            String sql = "SELECT * FROM blood_stock WHERE blood_group = ?";
            try (PreparedStatement pstmt = dbManager.getJdbcConnection().prepareStatement(sql)) {
                pstmt.setString(1, bloodGroup);
                try (ResultSet rs = pstmt.executeQuery()) {
                    if (rs.next()) {
                        return Optional.of(new BloodStock(
                                rs.getString("blood_group"),
                                rs.getInt("available_units"),
                                rs.getInt("minimum_threshold"),
                                LocalDateTime.now()
                        ));
                    }
                }
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
            }
        }

        return Optional.ofNullable(dbManager.getStockMap().get(bloodGroup));
    }

    @Override
    public synchronized boolean updateStock(String bloodGroup, int deltaUnits) {
        if (dbManager.isJdbcActive()) {
            String sql = "UPDATE blood_stock SET available_units = available_units + ?, last_updated = CURRENT_TIMESTAMP WHERE blood_group = ? AND (available_units + ?) >= 0";
            try (PreparedStatement pstmt = dbManager.getJdbcConnection().prepareStatement(sql)) {
                pstmt.setInt(1, deltaUnits);
                pstmt.setString(2, bloodGroup);
                pstmt.setInt(3, deltaUnits);
                return pstmt.executeUpdate() > 0;
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
                return false;
            }
        }

        BloodStock stock = dbManager.getStockMap().get(bloodGroup);
        if (stock != null) {
            int newUnits = stock.getAvailableUnits() + deltaUnits;
            if (newUnits >= 0) {
                stock.setAvailableUnits(newUnits);
                stock.setLastUpdated(LocalDateTime.now());
                return true;
            }
        }
        return false;
    }

    @Override
    public synchronized boolean setStock(String bloodGroup, int units) {
        if (units < 0) return false;

        if (dbManager.isJdbcActive()) {
            String sql = "UPDATE blood_stock SET available_units = ?, last_updated = CURRENT_TIMESTAMP WHERE blood_group = ?";
            try (PreparedStatement pstmt = dbManager.getJdbcConnection().prepareStatement(sql)) {
                pstmt.setInt(1, units);
                pstmt.setString(2, bloodGroup);
                return pstmt.executeUpdate() > 0;
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
                return false;
            }
        }

        BloodStock stock = dbManager.getStockMap().get(bloodGroup);
        if (stock != null) {
            stock.setAvailableUnits(units);
            stock.setLastUpdated(LocalDateTime.now());
            return true;
        }
        return false;
    }

    @Override
    public List<BloodStock> getLowStockAlerts() {
        return getAllStock().stream()
                .filter(BloodStock::isDeficit)
                .collect(Collectors.toList());
    }
}

