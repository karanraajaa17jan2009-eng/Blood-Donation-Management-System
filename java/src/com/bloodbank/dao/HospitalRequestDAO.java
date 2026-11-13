package com.bloodbank.dao;

import com.bloodbank.model.HospitalRequest;
import java.util.List;
import java.util.Optional;

/**
 * Data Access Object interface for Hospital Blood Requisitions.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public interface HospitalRequestDAO {
    boolean addRequest(HospitalRequest request);
    Optional<HospitalRequest> getRequestById(int requestId);
    List<HospitalRequest> getAllRequests();
    List<HospitalRequest> getPendingRequests();
    boolean updateStatus(int requestId, String status, String authorizedBy);
}
