package com.bloodbank.model;

import java.time.LocalDate;

/**
 * Represents a blood donation event.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class Donation {
    private int donationId;
    private int donorId;
    private String bloodGroup;
    private LocalDate donationDate;
    private int unitsDonated;
    private double hemoglobinLevel;
    private String phlebotomistName;
    private String remarks;

    public Donation() {
        this.donationDate = LocalDate.now();
        this.unitsDonated = 1;
        this.phlebotomistName = "Staff Duty Officer";
        this.remarks = "Fit for donation";
    }

    public Donation(int donationId, int donorId, String bloodGroup, LocalDate donationDate,
                    int unitsDonated, double hemoglobinLevel, String phlebotomistName, String remarks) {
        this.donationId = donationId;
        this.donorId = donorId;
        this.bloodGroup = bloodGroup;
        this.donationDate = (donationDate != null) ? donationDate : LocalDate.now();
        this.unitsDonated = unitsDonated;
        this.hemoglobinLevel = hemoglobinLevel;
        this.phlebotomistName = phlebotomistName;
        this.remarks = remarks;
    }

    // Constructor for registering a new donation
    public Donation(int donorId, String bloodGroup, LocalDate donationDate, 
                    int unitsDonated, double hemoglobinLevel, String remarks) {
        this(0, donorId, bloodGroup, donationDate, unitsDonated, hemoglobinLevel, "Staff Duty Officer", remarks);
    }

    public int getDonationId() {
        return donationId;
    }

    public void setDonationId(int donationId) {
        this.donationId = donationId;
    }

    public int getDonorId() {
        return donorId;
    }

    public void setDonorId(int donorId) {
        this.donorId = donorId;
    }

    public String getBloodGroup() {
        return bloodGroup;
    }

    public void setBloodGroup(String bloodGroup) {
        this.bloodGroup = bloodGroup;
    }

    public LocalDate getDonationDate() {
        return donationDate;
    }

    public void setDonationDate(LocalDate donationDate) {
        this.donationDate = donationDate;
    }

    public int getUnitsDonated() {
        return unitsDonated;
    }

    public void setUnitsDonated(int unitsDonated) {
        this.unitsDonated = unitsDonated;
    }

    public double getHemoglobinLevel() {
        return hemoglobinLevel;
    }

    public void setHemoglobinLevel(double hemoglobinLevel) {
        this.hemoglobinLevel = hemoglobinLevel;
    }

    public String getPhlebotomistName() {
        return phlebotomistName;
    }

    public void setPhlebotomistName(String phlebotomistName) {
        this.phlebotomistName = phlebotomistName;
    }

    public String getRemarks() {
        return remarks;
    }

    public void setRemarks(String remarks) {
        this.remarks = remarks;
    }

    @Override
    public String toString() {
        return String.format("Donation[ID=%d, DonorID=%d, Group='%s', Date=%s, Units=%d, Hb=%.1f]",
                donationId, donorId, bloodGroup, donationDate, unitsDonated, hemoglobinLevel);
    }
}

