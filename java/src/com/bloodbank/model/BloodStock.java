package com.bloodbank.model;

import java.time.LocalDateTime;

/**
 * Represents the inventory stock for a particular blood group.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class BloodStock {
    private String bloodGroup;
    private int availableUnits;
    private int minimumThreshold;
    private LocalDateTime lastUpdated;

    public BloodStock() {
        this.minimumThreshold = 5;
        this.lastUpdated = LocalDateTime.now();
    }

    public BloodStock(String bloodGroup, int availableUnits, int minimumThreshold, LocalDateTime lastUpdated) {
        this.bloodGroup = bloodGroup;
        this.availableUnits = availableUnits;
        this.minimumThreshold = minimumThreshold;
        this.lastUpdated = (lastUpdated != null) ? lastUpdated : LocalDateTime.now();
    }

    public BloodStock(String bloodGroup, int availableUnits) {
        this(bloodGroup, availableUnits, 5, LocalDateTime.now());
    }

    public String getBloodGroup() {
        return bloodGroup;
    }

    public void setBloodGroup(String bloodGroup) {
        this.bloodGroup = bloodGroup;
    }

    public int getAvailableUnits() {
        return availableUnits;
    }

    public void setAvailableUnits(int availableUnits) {
        this.availableUnits = availableUnits;
    }

    public int getMinimumThreshold() {
        return minimumThreshold;
    }

    public void setMinimumThreshold(int minimumThreshold) {
        this.minimumThreshold = minimumThreshold;
    }

    public LocalDateTime getLastUpdated() {
        return lastUpdated;
    }

    public void setLastUpdated(LocalDateTime lastUpdated) {
        this.lastUpdated = lastUpdated;
    }

    public boolean isDeficit() {
        return availableUnits < minimumThreshold;
    }

    public boolean isOutOfStock() {
        return availableUnits <= 0;
    }

    public String getStatus() {
        if (availableUnits <= 0) return "OUT OF STOCK";
        if (availableUnits < minimumThreshold) return "CRITICAL DEFICIT";
        if (availableUnits == minimumThreshold) return "LOW BUFFER";
        return "ADEQUATE";
    }

    @Override
    public String toString() {
        return String.format("BloodStock[Group='%s', Units=%d, MinThreshold=%d, Status='%s']",
                bloodGroup, availableUnits, minimumThreshold, getStatus());
    }
}

