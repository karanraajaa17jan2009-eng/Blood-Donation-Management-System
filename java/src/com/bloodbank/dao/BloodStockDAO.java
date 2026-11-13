package com.bloodbank.dao;

import com.bloodbank.model.BloodStock;
import java.util.List;
import java.util.Optional;

/**
 * Data Access Object interface for Blood Stock Inventory operations.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public interface BloodStockDAO {
    List<BloodStock> getAllStock();
    Optional<BloodStock> getStockByGroup(String bloodGroup);
    boolean updateStock(String bloodGroup, int deltaUnits);
    boolean setStock(String bloodGroup, int units);
    List<BloodStock> getLowStockAlerts();
}

