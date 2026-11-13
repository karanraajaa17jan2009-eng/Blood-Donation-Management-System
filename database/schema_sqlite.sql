-- =============================================================================
-- Blood Donation Management and Donor Availability Analysis System
-- SQLite Database Schema (DDL)
-- Student: Karan Raajaa V | Register No: 732925ITR045 | Class: 25IT3A
-- Institution: Velalar College of Engineering and Technology, Erode - 12
-- =============================================================================

PRAGMA foreign_keys = ON;

-- Drop existing views and tables if they exist
DROP VIEW IF EXISTS v_donor_availability;
DROP VIEW IF EXISTS v_stock_summary;
DROP TABLE IF EXISTS hospital_requests;
DROP TABLE IF EXISTS donations;
DROP TABLE IF EXISTS donors;
DROP TABLE IF EXISTS blood_stock;

-- -----------------------------------------------------------------------------
-- Table 1: blood_stock
-- Maintains inventory of blood units categorized by blood group
-- -----------------------------------------------------------------------------
CREATE TABLE blood_stock (
    blood_group VARCHAR(5) PRIMARY KEY,
    available_units INTEGER NOT NULL DEFAULT 0 CHECK (available_units >= 0),
    minimum_threshold INTEGER NOT NULL DEFAULT 5 CHECK (minimum_threshold >= 0),
    last_updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- Table 2: donors
-- Stores personal, contact, and blood group details of voluntary donors
-- -----------------------------------------------------------------------------
CREATE TABLE donors (
    donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    age INTEGER NOT NULL CHECK (age >= 18 AND age <= 65),
    gender VARCHAR(10) NOT NULL CHECK (gender IN ('Male', 'Female', 'Other')),
    contact_number VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE,
    blood_group VARCHAR(5) NOT NULL,
    city VARCHAR(50) NOT NULL,
    registration_date DATE NOT NULL DEFAULT (CURRENT_DATE),
    FOREIGN KEY (blood_group) REFERENCES blood_stock(blood_group) ON UPDATE CASCADE
);

-- -----------------------------------------------------------------------------
-- Table 3: donations
-- Records individual donation events and tracks blood units collected
-- -----------------------------------------------------------------------------
CREATE TABLE donations (
    donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    donor_id INTEGER NOT NULL,
    blood_group VARCHAR(5) NOT NULL,
    donation_date DATE NOT NULL,
    units_donated INTEGER NOT NULL DEFAULT 1 CHECK (units_donated >= 1),
    hemoglobin_level DECIMAL(4, 2) NOT NULL CHECK (hemoglobin_level >= 12.0),
    phlebotomist_name VARCHAR(100) DEFAULT 'Staff Duty Officer',
    remarks VARCHAR(255) DEFAULT 'Fit for donation',
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id) ON DELETE CASCADE,
    FOREIGN KEY (blood_group) REFERENCES blood_stock(blood_group) ON UPDATE CASCADE
);

-- -----------------------------------------------------------------------------
-- Table 4: hospital_requests
-- Tracks blood unit requisitions from medical facilities and fulfillment status
-- -----------------------------------------------------------------------------
CREATE TABLE hospital_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hospital_name VARCHAR(120) NOT NULL,
    blood_group VARCHAR(5) NOT NULL,
    units_requested INTEGER NOT NULL CHECK (units_requested > 0),
    request_date DATE NOT NULL DEFAULT (CURRENT_DATE),
    urgency_level VARCHAR(10) NOT NULL CHECK (urgency_level IN ('NORMAL', 'URGENT', 'CRITICAL')),
    status VARCHAR(15) NOT NULL DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'FULFILLED', 'REJECTED')),
    fulfillment_date DATE,
    authorized_by VARCHAR(100),
    FOREIGN KEY (blood_group) REFERENCES blood_stock(blood_group) ON UPDATE CASCADE
);

-- -----------------------------------------------------------------------------
-- Indexes for High Performance Querying
-- -----------------------------------------------------------------------------
CREATE INDEX idx_donations_donor_id ON donations(donor_id);
CREATE INDEX idx_donations_date ON donations(donation_date);
CREATE INDEX idx_donors_blood_group ON donors(blood_group);
CREATE INDEX idx_hospital_requests_status ON hospital_requests(status);

-- -----------------------------------------------------------------------------
-- Database Views for Reporting and Analytics
-- -----------------------------------------------------------------------------

-- View 1: Current Stock Summary with Status Indicator
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

-- View 2: Donor Availability and 90-Day Eligibility Analysis
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
        ELSE CAST(JULIANDAY(CURRENT_DATE) - JULIANDAY(MAX(dn.donation_date)) AS INTEGER)
    END AS days_since_last_donation,
    CASE 
        WHEN MAX(dn.donation_date) IS NULL THEN 'ELIGIBLE (First Time)'
        WHEN CAST(JULIANDAY(CURRENT_DATE) - JULIANDAY(MAX(dn.donation_date)) AS INTEGER) >= 90 THEN 'ELIGIBLE'
        ELSE 'INELIGIBLE (Cooldown)'
    END AS eligibility_status,
    CASE 
        WHEN MAX(dn.donation_date) IS NULL THEN 0
        WHEN CAST(JULIANDAY(CURRENT_DATE) - JULIANDAY(MAX(dn.donation_date)) AS INTEGER) >= 90 THEN 0
        ELSE 90 - CAST(JULIANDAY(CURRENT_DATE) - JULIANDAY(MAX(dn.donation_date)) AS INTEGER)
    END AS days_remaining_in_cooldown
FROM donors d
LEFT JOIN donations dn ON d.donor_id = dn.donor_id
GROUP BY d.donor_id, d.name, d.age, d.gender, d.contact_number, d.blood_group, d.city;

