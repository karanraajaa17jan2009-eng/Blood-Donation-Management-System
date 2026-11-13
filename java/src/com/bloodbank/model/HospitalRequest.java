package com.bloodbank.model;

import java.time.LocalDate;

/**
 * Represents a blood requisition request from a healthcare facility.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class HospitalRequest {
    private int requestId;
    private String hospitalName;
    private String bloodGroup;
    private int unitsRequested;
    private LocalDate requestDate;
    private String urgencyLevel; // NORMAL, URGENT, CRITICAL
    private String status;       // PENDING, FULFILLED, REJECTED
    private LocalDate fulfillmentDate;
    private String authorizedBy;

    public HospitalRequest() {
        this.requestDate = LocalDate.now();
        this.urgencyLevel = "NORMAL";
        this.status = "PENDING";
    }

    public HospitalRequest(int requestId, String hospitalName, String bloodGroup, int unitsRequested,
                           LocalDate requestDate, String urgencyLevel, String status,
                           LocalDate fulfillmentDate, String authorizedBy) {
        this.requestId = requestId;
        this.hospitalName = hospitalName;
        this.bloodGroup = bloodGroup;
        this.unitsRequested = unitsRequested;
        this.requestDate = (requestDate != null) ? requestDate : LocalDate.now();
        this.urgencyLevel = urgencyLevel;
        this.status = (status != null) ? status : "PENDING";
        this.fulfillmentDate = fulfillmentDate;
        this.authorizedBy = authorizedBy;
    }

    // Constructor for registering a new requisition
    public HospitalRequest(String hospitalName, String bloodGroup, int unitsRequested, String urgencyLevel) {
        this(0, hospitalName, bloodGroup, unitsRequested, LocalDate.now(), urgencyLevel, "PENDING", null, null);
    }

    public int getRequestId() {
        return requestId;
    }

    public void setRequestId(int requestId) {
        this.requestId = requestId;
    }

    public String getHospitalName() {
        return hospitalName;
    }

    public void setHospitalName(String hospitalName) {
        this.hospitalName = hospitalName;
    }

    public String getBloodGroup() {
        return bloodGroup;
    }

    public void setBloodGroup(String bloodGroup) {
        this.bloodGroup = bloodGroup;
    }

    public int getUnitsRequested() {
        return unitsRequested;
    }

    public void setUnitsRequested(int unitsRequested) {
        this.unitsRequested = unitsRequested;
    }

    public LocalDate getRequestDate() {
        return requestDate;
    }

    public void setRequestDate(LocalDate requestDate) {
        this.requestDate = requestDate;
    }

    public String getUrgencyLevel() {
        return urgencyLevel;
    }

    public void setUrgencyLevel(String urgencyLevel) {
        this.urgencyLevel = urgencyLevel;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public LocalDate getFulfillmentDate() {
        return fulfillmentDate;
    }

    public void setFulfillmentDate(LocalDate fulfillmentDate) {
        this.fulfillmentDate = fulfillmentDate;
    }

    public String getAuthorizedBy() {
        return authorizedBy;
    }

    public void setAuthorizedBy(String authorizedBy) {
        this.authorizedBy = authorizedBy;
    }

    @Override
    public String toString() {
        return String.format("HospitalRequest[ID=%d, Hospital='%s', Group='%s', Units=%d, Urgency='%s', Status='%s']",
                requestId, hospitalName, bloodGroup, unitsRequested, urgencyLevel, status);
    }
}

