package com.bloodbank.service;

import com.bloodbank.dao.BloodStockDAO;
import com.bloodbank.dao.HospitalRequestDAO;
import com.bloodbank.model.BloodStock;
import com.bloodbank.model.HospitalRequest;
import com.bloodbank.util.InputValidator;

import java.util.List;
import java.util.Optional;

/**
 * Service managing Hospital Requisitions and Blood Issuance.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class HospitalRequestService {

    private final HospitalRequestDAO hospitalRequestDAO;
    private final BloodStockDAO bloodStockDAO;

    public HospitalRequestService(HospitalRequestDAO hospitalRequestDAO, BloodStockDAO bloodStockDAO) {
        this.hospitalRequestDAO = hospitalRequestDAO;
        this.bloodStockDAO = bloodStockDAO;
    }

    public boolean submitRequest(HospitalRequest request) {
        if (request.getHospitalName() == null || request.getHospitalName().trim().isEmpty()) {
            throw new IllegalArgumentException("Hospital name cannot be blank.");
        }
        if (!InputValidator.isValidBloodGroup(request.getBloodGroup())) {
            throw new IllegalArgumentException("Invalid blood group requested: " + request.getBloodGroup());
        }
        if (request.getUnitsRequested() <= 0) {
            throw new IllegalArgumentException("Units requested must be greater than zero.");
        }

        return hospitalRequestDAO.addRequest(request);
    }

    public RequestFulfillmentResult fulfillRequest(int requestId, String authorizedBy) {
        Optional<HospitalRequest> reqOpt = hospitalRequestDAO.getRequestById(requestId);
        if (reqOpt.isEmpty()) {
            return new RequestFulfillmentResult(false, "Request ID " + requestId + " not found.");
        }

        HospitalRequest request = reqOpt.get();
        if ("FULFILLED".equalsIgnoreCase(request.getStatus())) {
            return new RequestFulfillmentResult(false, "Request ID " + requestId + " is already fulfilled.");
        }
        if ("REJECTED".equalsIgnoreCase(request.getStatus())) {
            return new RequestFulfillmentResult(false, "Request ID " + requestId + " has been rejected previously.");
        }

        // Check stock availability
        Optional<BloodStock> stockOpt = bloodStockDAO.getStockByGroup(request.getBloodGroup());
        if (stockOpt.isEmpty() || stockOpt.get().getAvailableUnits() < request.getUnitsRequested()) {
            int available = stockOpt.map(BloodStock::getAvailableUnits).orElse(0);
            return new RequestFulfillmentResult(false, String.format(
                    "Insufficient stock for %s! Requested: %d, Available: %d units.",
                    request.getBloodGroup(), request.getUnitsRequested(), available));
        }

        // Deduct stock and update status
        boolean stockDeducted = bloodStockDAO.updateStock(request.getBloodGroup(), -request.getUnitsRequested());
        if (!stockDeducted) {
            return new RequestFulfillmentResult(false, "Database error: Failed to deduct blood units from stock.");
        }

        boolean statusUpdated = hospitalRequestDAO.updateStatus(requestId, "FULFILLED", authorizedBy);
        if (!statusUpdated) {
            // Rollback stock deduction if status update failed
            bloodStockDAO.updateStock(request.getBloodGroup(), request.getUnitsRequested());
            return new RequestFulfillmentResult(false, "Database error: Failed to update request status.");
        }

        return new RequestFulfillmentResult(true, String.format(
                "Request ID %d successfully fulfilled! Issued %d unit(s) of %s to %s.",
                requestId, request.getUnitsRequested(), request.getBloodGroup(), request.getHospitalName()));
    }

    public boolean rejectRequest(int requestId, String reason, String authorizedBy) {
        return hospitalRequestDAO.updateStatus(requestId, "REJECTED", authorizedBy + " (" + reason + ")");
    }

    public List<HospitalRequest> getAllRequests() {
        return hospitalRequestDAO.getAllRequests();
    }

    public List<HospitalRequest> getPendingRequests() {
        return hospitalRequestDAO.getPendingRequests();
    }

    public static class RequestFulfillmentResult {
        private final boolean success;
        private final String message;

        public RequestFulfillmentResult(boolean success, String message) {
            this.success = success;
            this.message = message;
        }

        public boolean isSuccess() { return success; }
        public String getMessage() { return message; }
    }
}

