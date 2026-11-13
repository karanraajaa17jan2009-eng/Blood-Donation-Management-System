-- =============================================================================
-- Blood Donation Management and Donor Availability Analysis System
-- Analytical and Reporting SQL Queries
-- Student: Karan Raajaa V | Register No: 732925ITR045 | Class: 25IT3A&B
-- Institution: Velalar College of Engineering and Technology, Erode - 12
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Query 1: Real-time Blood Stock Inventory Status vs Minimum Threshold
-- Demonstrates: Categorical CASE expressions and conditional ordering
-- -----------------------------------------------------------------------------
SELECT 
    blood_group,
    available_units,
    minimum_threshold,
    (available_units - minimum_threshold) AS surplus_or_deficit,
    CASE 
        WHEN available_units = 0 THEN 'CRITICAL: OUT OF STOCK'
        WHEN available_units < minimum_threshold THEN 'WARNING: DEFICIT'
        WHEN available_units = minimum_threshold THEN 'ALERT: AT BUFFER'
        ELSE 'NORMAL: ADEQUATE'
    END AS inventory_status,
    last_updated
FROM blood_stock
ORDER BY available_units ASC;

-- -----------------------------------------------------------------------------
-- Query 2: Identify Available Donors Who Meet the 90-Day Eligibility Interval
-- Demonstrates: LEFT JOIN, Aggregation (MAX), Date functions, HAVING/WHERE filter
-- -----------------------------------------------------------------------------
SELECT 
    d.donor_id,
    d.name AS donor_name,
    d.blood_group,
    d.contact_number,
    d.city,
    COALESCE(MAX(dn.donation_date), 'Never Donated') AS last_donation_date,
    CASE 
        WHEN MAX(dn.donation_date) IS NULL THEN 'Never Donated'
        ELSE CAST(JULIANDAY(CURRENT_DATE) - JULIANDAY(MAX(dn.donation_date)) AS INTEGER) || ' days ago'
    END AS donation_recency,
    'ELIGIBLE' AS status
FROM donors d
LEFT JOIN donations dn ON d.donor_id = dn.donor_id
GROUP BY d.donor_id, d.name, d.blood_group, d.contact_number, d.city
HAVING MAX(dn.donation_date) IS NULL 
    OR CAST(JULIANDAY(CURRENT_DATE) - JULIANDAY(MAX(dn.donation_date)) AS INTEGER) >= 90
ORDER BY d.blood_group, d.name;

-- -----------------------------------------------------------------------------
-- Query 3: Blood Group-Wise Total Donations and Volume Aggregation
-- Demonstrates: INNER JOIN, COUNT, SUM, AVG, GROUP BY, and formatting
-- -----------------------------------------------------------------------------
SELECT 
    bs.blood_group,
    bs.available_units AS current_stock,
    COUNT(d.donation_id) AS total_donation_sessions,
    COALESCE(SUM(d.units_donated), 0) AS total_units_donated,
    ROUND(AVG(d.hemoglobin_level), 2) AS average_donor_hemoglobin
FROM blood_stock bs
LEFT JOIN donations d ON bs.blood_group = d.blood_group
GROUP BY bs.blood_group, bs.available_units
ORDER BY total_units_donated DESC;

-- -----------------------------------------------------------------------------
-- Query 4: Monthly Blood Donation Trends (Temporal Analysis)
-- Demonstrates: String date slicing (STRFTIME), aggregation, and trend analysis
-- -----------------------------------------------------------------------------
SELECT 
    STRFTIME('%Y-%m', donation_date) AS donation_month,
    COUNT(donation_id) AS total_donations,
    SUM(units_donated) AS total_units_collected,
    COUNT(DISTINCT donor_id) AS unique_active_donors
FROM donations
GROUP BY donation_month
ORDER BY donation_month ASC;

-- -----------------------------------------------------------------------------
-- Query 5: Hospital Requisition Fulfillment Analysis by Urgency Level
-- Demonstrates: Pivot/Conditional Aggregation (SUM with CASE)
-- -----------------------------------------------------------------------------
SELECT 
    urgency_level,
    COUNT(request_id) AS total_requests,
    SUM(CASE WHEN status = 'FULFILLED' THEN 1 ELSE 0 END) AS fulfilled_count,
    SUM(CASE WHEN status = 'PENDING' THEN 1 ELSE 0 END) AS pending_count,
    SUM(CASE WHEN status = 'REJECTED' THEN 1 ELSE 0 END) AS rejected_count,
    ROUND((SUM(CASE WHEN status = 'FULFILLED' THEN 1.0 ELSE 0.0 END) / COUNT(request_id)) * 100, 1) || '%' AS fulfillment_rate
FROM hospital_requests
GROUP BY urgency_level
ORDER BY 
    CASE urgency_level
        WHEN 'CRITICAL' THEN 1
        WHEN 'URGENT' THEN 2
        ELSE 3
    END;

-- -----------------------------------------------------------------------------
-- Query 6: Top Frequent Donors (Ranking via Subquery & Aggregation)
-- Demonstrates: Nested Correlated Subquery and HAVING clause
-- -----------------------------------------------------------------------------
SELECT 
    d.donor_id,
    d.name,
    d.blood_group,
    d.city,
    COUNT(dn.donation_id) AS donation_frequency,
    SUM(dn.units_donated) AS total_units_contributed,
    MAX(dn.donation_date) AS most_recent_donation
FROM donors d
JOIN donations dn ON d.donor_id = dn.donor_id
GROUP BY d.donor_id, d.name, d.blood_group, d.city
HAVING COUNT(dn.donation_id) >= 2
ORDER BY donation_frequency DESC, total_units_contributed DESC;

-- -----------------------------------------------------------------------------
-- Query 7: Donors Who Have Never Donated (Zero Donation Audit)
-- Demonstrates: Outer Join with IS NULL predicate (Anti-Join pattern)
-- -----------------------------------------------------------------------------
SELECT 
    d.donor_id,
    d.name,
    d.age,
    d.blood_group,
    d.contact_number,
    d.city,
    d.registration_date
FROM donors d
LEFT JOIN donations dn ON d.donor_id = dn.donor_id
WHERE dn.donation_id IS NULL;

-- -----------------------------------------------------------------------------
-- Query 8: Emergency Response Matching - Finding Eligible Donors for Pending Requests
-- Demonstrates: Multi-table JOIN, correlated conditions, date intervals
-- -----------------------------------------------------------------------------
SELECT 
    hr.request_id,
    hr.hospital_name,
    hr.blood_group,
    hr.units_requested,
    hr.urgency_level,
    d.name AS eligible_donor_name,
    d.contact_number AS donor_phone,
    d.city AS donor_city
FROM hospital_requests hr
JOIN donors d ON hr.blood_group = d.blood_group
LEFT JOIN (
    SELECT donor_id, MAX(donation_date) AS last_date 
    FROM donations 
    GROUP BY donor_id
) last_dn ON d.donor_id = last_dn.donor_id
WHERE hr.status = 'PENDING'
  AND (last_dn.last_date IS NULL OR CAST(JULIANDAY(CURRENT_DATE) - JULIANDAY(last_dn.last_date) AS INTEGER) >= 90)
ORDER BY hr.urgency_level DESC, hr.request_id;

