package com.bloodbank.dao.impl;

import com.bloodbank.dao.DatabaseManager;
import com.bloodbank.dao.HospitalRequestDAO;
import com.bloodbank.model.HospitalRequest;

import java.sql.*;
import java.time.LocalDate;
import java.util.*;
import java.util.stream.Collectors;

/**
 * Implementation of HospitalRequestDAO.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class HospitalRequestDAOImpl implements HospitalRequestDAO {

    private final DatabaseManager dbManager = DatabaseManager.getInstance();

    @Override
    public boolean addRequest(HospitalRequest request) {
        if (dbManager.isJdbcActive()) {
            String sql = "INSERT INTO hospital_requests (hospital_name, blood_group, units_requested, request_date, urgency_level, status) VALUES (?, ?, ?, ?, ?, ?)";
            try (PreparedStatement pstmt = dbManager.getJdbcConnection().prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
                pstmt.setString(1, request.getHospitalName());
                pstmt.setString(2, request.getBloodGroup());
                pstmt.setInt(3, request.getUnitsRequested());
                pstmt.setString(4, request.getRequestDate().toString());
                pstmt.setString(5, request.getUrgencyLevel());
                pstmt.setString(6, request.getStatus());
                int rows = pstmt.executeUpdate();
                if (rows > 0) {
                    try (ResultSet rs = pstmt.getGeneratedKeys()) {
                        if (rs.next()) request.setRequestId(rs.getInt(1));
                    }
                    return true;
                }
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
            }
        }

        int newId = dbManager.getRequestIdGen().getAndIncrement();
        request.setRequestId(newId);
        dbManager.getRequestList().add(request);
        return true;
    }

    @Override
    public Optional<HospitalRequest> getRequestById(int requestId) {
        if (dbManager.isJdbcActive()) {
            String sql = "SELECT * FROM hospital_requests WHERE request_id = ?";
            try (PreparedStatement pstmt = dbManager.getJdbcConnection().prepareStatement(sql)) {
                pstmt.setInt(1, requestId);
                try (ResultSet rs = pstmt.executeQuery()) {
                    if (rs.next()) {
                        return Optional.of(new HospitalRequest(
                                rs.getInt("request_id"),
                                rs.getString("hospital_name"),
                                rs.getString("blood_group"),
                                rs.getInt("units_requested"),
                                LocalDate.parse(rs.getString("request_date")),
                                rs.getString("urgency_level"),
                                rs.getString("status"),
                                rs.getString("fulfillment_date") != null ? LocalDate.parse(rs.getString("fulfillment_date")) : null,
                                rs.getString("authorized_by")
                        ));
                    }
                }
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
            }
        }

        return dbManager.getRequestList().stream()
                .filter(r -> r.getRequestId() == requestId)
                .findFirst();
    }

    @Override
    public List<HospitalRequest> getAllRequests() {
        if (dbManager.isJdbcActive()) {
            List<HospitalRequest> list = new ArrayList<>();
            String sql = "SELECT * FROM hospital_requests ORDER BY request_date DESC, request_id DESC";
            try (Statement stmt = dbManager.getJdbcConnection().createStatement();
                 ResultSet rs = stmt.executeQuery(sql)) {
                while (rs.next()) {
                    list.add(new HospitalRequest(
                            rs.getInt("request_id"),
                            rs.getString("hospital_name"),
                            rs.getString("blood_group"),
                            rs.getInt("units_requested"),
                            LocalDate.parse(rs.getString("request_date")),
                            rs.getString("urgency_level"),
                            rs.getString("status"),
                            rs.getString("fulfillment_date") != null ? LocalDate.parse(rs.getString("fulfillment_date")) : null,
                            rs.getString("authorized_by")
                    ));
                }
                return list;
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
            }
        }

        return new ArrayList<>(dbManager.getRequestList());
    }

    @Override
    public List<HospitalRequest> getPendingRequests() {
        return getAllRequests().stream()
                .filter(r -> "PENDING".equalsIgnoreCase(r.getStatus()))
                .collect(Collectors.toList());
    }

    @Override
    public synchronized boolean updateStatus(int requestId, String status, String authorizedBy) {
        if (dbManager.isJdbcActive()) {
            String sql = "UPDATE hospital_requests SET status = ?, fulfillment_date = CURRENT_DATE, authorized_by = ? WHERE request_id = ?";
            try (PreparedStatement pstmt = dbManager.getJdbcConnection().prepareStatement(sql)) {
                pstmt.setString(1, status);
                pstmt.setString(2, authorizedBy);
                pstmt.setInt(3, requestId);
                return pstmt.executeUpdate() > 0;
            } catch (SQLException e) {
                System.err.println("[JDBC Error] " + e.getMessage());
                return false;
            }
        }

        Optional<HospitalRequest> opt = getRequestById(requestId);
        if (opt.isPresent()) {
            HospitalRequest req = opt.get();
            req.setStatus(status);
            req.setFulfillmentDate(LocalDate.now());
            req.setAuthorizedBy(authorizedBy);
            return true;
        }
        return false;
    }
}
