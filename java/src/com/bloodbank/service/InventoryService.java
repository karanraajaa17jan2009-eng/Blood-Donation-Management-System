package com.bloodbank.service;

import com.bloodbank.dao.BloodStockDAO;
import com.bloodbank.model.BloodStock;

import java.util.List;
import java.util.Optional;

/**
 * Service managing Blood Stock Inventory and safety alerts.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class InventoryService {

    private final BloodStockDAO bloodStockDAO;

    public InventoryService(BloodStockDAO bloodStockDAO) {
        this.bloodStockDAO = bloodStockDAO;
    }

    public List<BloodStock> getAllStock() {
        return bloodStockDAO.getAllStock();
    }

    public Optional<BloodStock> getStock(String bloodGroup) {
        return bloodStockDAO.getStockByGroup(bloodGroup);
    }

    public boolean adjustStock(String bloodGroup, int deltaUnits) {
        return bloodStockDAO.updateStock(bloodGroup, deltaUnits);
    }

    public List<BloodStock> checkLowStockAlerts() {
        return bloodStockDAO.getLowStockAlerts();
    }
}

