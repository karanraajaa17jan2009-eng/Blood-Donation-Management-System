-- =============================================================================
-- Blood Donation Management and Donor Availability Analysis System
-- MySQL Database Schema (DDL)
-- Student: Karan Raajaa V | Register No: 732925ITR045 | Class: 25IT3A&B
-- Institution: Velalar College of Engineering and Technology, Erode - 12
-- =============================================================================

CREATE DATABASE IF NOT EXISTS blood_bank_db;
USE blood_bank_db;

-- Drop existing views and tables
DROP VIEW IF EXISTS v_donor_availability;
DROP VIEW IF EXISTS v_stock_summary;
DROP TABLE IF EXISTS hospital_requests;
DROP TABLE IF EXISTS donations;
DROP TABLE IF EXISTS donors;
DROP TABLE IF EXISTS blood_stock;

-- -----------------------------------------------------------------------------
-- Table 1: blood_stock
-- -----------------------------------------------------------------------------
CREATE TABLE blood_stock (
    blood_group VARCHAR(5) PRIMARY KEY,
    available_units INT NOT NULL DEFAULT 0,
    minimum_threshold INT NOT NULL DEFAULT 5,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_units_non_negative CHECK (available_units >= 0),
    CONSTRAINT chk_threshold_non_negative CHECK (minimum_threshold >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------------------------------
-- Table 2: donors
-- -----------------------------------------------------------------------------
CREATE TABLE donors (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE,
    blood_group VARCHAR(5) NOT NULL,
    city VARCHAR(50) NOT NULL,
    registration_date DATE NOT NULL DEFAULT (CURRENT_DATE),
    CONSTRAINT chk_donor_age CHECK (age >= 18 AND age <= 65),
    CONSTRAINT fk_donor_blood_group FOREIGN KEY (blood_group) 
        REFERENCES blood_stock(blood_group) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------------------------------
-- Table 3: donations
-- -----------------------------------------------------------------------------
CREATE TABLE donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_id INT NOT NULL,
    blood_group VARCHAR(5) NOT NULL,
    donation_date DATE NOT NULL,
    units_donated INT NOT NULL DEFAULT 1,
    hemoglobin_level DECIMAL(4, 2) NOT NULL,
    phlebotomist_name VARCHAR(100) DEFAULT 'Staff Duty Officer',
    remarks VARCHAR(255) DEFAULT 'Fit for donation',
    CONSTRAINT chk_units_positive CHECK (units_donated >= 1),
    CONSTRAINT chk_hemoglobin CHECK (hemoglobin_level >= 12.0),
    CONSTRAINT fk_donation_donor FOREIGN KEY (donor_id) 
        REFERENCES donors(donor_id) ON DELETE CASCADE,
    CONSTRAINT fk_donation_blood_group FOREIGN KEY (blood_group) 
        REFERENCES blood_stock(blood_group) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------------------------------
-- Table 4: hospital_requests
-- -----------------------------------------------------------------------------
CREATE TABLE hospital_requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    hospital_name VARCHAR(120) NOT NULL,
    blood_group VARCHAR(5) NOT NULL,
    units_requested INT NOT NULL,
    request_date DATE NOT NULL DEFAULT (CURRENT_DATE),
    urgency_level ENUM('NORMAL', 'URGENT', 'CRITICAL') NOT NULL,
    status ENUM('PENDING', 'FULFILLED', 'REJECTED') NOT NULL DEFAULT 'PENDING',
    fulfillment_date DATE,
    authorized_by VARCHAR(100),
    CONSTRAINT chk_req_units CHECK (units_requested > 0),
    CONSTRAINT fk_request_blood_group FOREIGN KEY (blood_group) 
        REFERENCES blood_stock(blood_group) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------------------------------
-- Indexes
-- -----------------------------------------------------------------------------
CREATE INDEX idx_donations_donor_id ON donations(donor_id);
CREATE INDEX idx_donations_date ON donations(donation_date);
CREATE INDEX idx_donors_blood_group ON donors(blood_group);
CREATE INDEX idx_hospital_requests_status ON hospital_requests(status);

-- -----------------------------------------------------------------------------
-- Views for Reporting
-- -----------------------------------------------------------------------------
CREATE VIEW v_stock_summary AS
SELECT 
    bs.blood_group,
    bs.available_units,
    bs.minimum_threshold,
    CASE 
        WHEN bs.available_units = 0 THEN 'OUT OF STOCK'
        WHEN bs.available_units < bs.minimum_threshold THEN 'CRITICAL DEFICIT'
        WHEN bs.available_units = bs.minimum_threshold THEN 'LOW BUFFER'
        ELSE 'ADEQUATE'
    END AS stock_status,
    COALESCE(SUM(d.units_donated), 0) AS total_historical_donations,
    bs.last_updated
FROM blood_stock bs
LEFT JOIN donations d ON bs.blood_group = d.blood_group
GROUP BY bs.blood_group, bs.available_units, bs.minimum_threshold, bs.last_updated;

CREATE VIEW v_donor_availability AS
SELECT 
    d.donor_id,
    d.name AS donor_name,
    d.age,
    d.gender,
    d.contact_number,
    d.blood_group,
    d.city,
    MAX(dn.donation_date) AS last_donation_date,
    CASE 
        WHEN MAX(dn.donation_date) IS NULL THEN 999
        ELSE DATEDIFF(CURRENT_DATE, MAX(dn.donation_date))
    END AS days_since_last_donation,
    CASE 
        WHEN MAX(dn.donation_date) IS NULL THEN 'ELIGIBLE (First Time)'
        WHEN DATEDIFF(CURRENT_DATE, MAX(dn.donation_date)) >= 90 THEN 'ELIGIBLE'
        ELSE 'INELIGIBLE (Cooldown)'
    END AS eligibility_status,
    CASE 
        WHEN MAX(dn.donation_date) IS NULL THEN 0
        WHEN DATEDIFF(CURRENT_DATE, MAX(dn.donation_date)) >= 90 THEN 0
        ELSE 90 - DATEDIFF(CURRENT_DATE, MAX(dn.donation_date))
    END AS days_remaining_in_cooldown
FROM donors d
LEFT JOIN donations dn ON d.donor_id = dn.donor_id
GROUP BY d.donor_id, d.name, d.age, d.gender, d.contact_number, d.blood_group, d.city;

