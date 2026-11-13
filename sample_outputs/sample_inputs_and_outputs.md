# Sample Inputs and Outputs
## Blood Donation Management and Donor Availability Analysis System
**Academic Year:** 2026 - 2027 (ODD)  
**Course Code & Name:** 25ITT32 - Java Programming / 25ITT31 - DBMS / 25ITC31 - Foundations of Data Science  
**Student Name:** Karan Raajaa V  
**Register Number:** 732925ITR045  
**Class / Section:** 25IT3A&B (Roll No. 45)  
**Scenario:** Scenario 15 - Blood Donation Management and Donor Availability Analysis System  

---

## 1. Overview
This document provides documented sample inputs and actual terminal outputs for all core modules of the **Blood Donation Management System**, demonstrating compliance with academic evaluation criteria.

---

## 2. Sample Execution Scenarios

### Scenario 1: New Voluntary Donor Registration
- **Input Data:**
  - Name: `Ravi Kumar P`
  - Age: `24`
  - Gender: `Male`
  - Contact Number: `9842556677`
  - Email: `ravi.kumar@gmail.com`
  - Blood Group: `O+`
  - City: `Erode`
- **Terminal Interaction & Output:**
  ```text
  --- [1] Register New Voluntary Donor ---
  Enter Donor Full Name: Ravi Kumar P
  Enter Age (18-65): 24
  Enter Gender (Male/Female/Other): Male
  Enter 10-Digit Contact Number: 9842556677
  Enter Email Address: ravi.kumar@gmail.com
  Enter Blood Group (A+, A-, B+, B-, AB+, AB-, O+, O-): O+
  Enter City / Location: Erode

  [SUCCESS] Donor 'Ravi Kumar P' registered successfully with ID #100!
  ```

---

### Scenario 2: Donation Attempt Blocked by 90-Day Medical Cooldown
- **Input Data:**
  - Registered Donor ID: `2` (`Praveen Kumar S`, last donation date was 11 days ago)
- **Terminal Interaction & Output:**
  ```text
  --- [2] Record Blood Donation ---
  Enter Registered Donor ID: 2
   >> Donor Name: Praveen Kumar S | Blood Group: A+ | Status: Ineligible (Cooldown active: 79 days remaining until next donation)

  [BLOCKED] Donation cannot be accepted. Medical cooldown active: 79 days remaining.
  ```

---

### Scenario 3: Successful Donation Recording & Automatic Stock Increment
- **Input Data:**
  - Registered Donor ID: `13` (`Swathi Chandran`, last donation date was 104 days ago $\ge 90$ days)
  - Units Donated: `1`
  - Hemoglobin Level: `13.5` g/dL
  - Phlebotomist: `Staff Nurse Priya`
  - Remarks: `Regular blood donor camp`
- **Terminal Interaction & Output:**
  ```text
  --- [2] Record Blood Donation ---
  Enter Registered Donor ID: 13
   >> Donor Name: Swathi Chandran | Blood Group: A+ | Status: Eligible (Last donated 104 days ago on 2026-08-01)
  Enter Number of Units Donated (Standard: 1): 1
  Enter Donor Hemoglobin Level in g/dL (>= 12.0): 13.5
  Enter Phlebotomist / Attending Nurse Name: Staff Nurse Priya
  Enter Clinical Remarks: Regular blood donor camp

  [SUCCESS] Donation successfully recorded (ID: 200)! Added 1 unit(s) of A+ to stock.
  ```

---

### Scenario 4: Real-Time Blood Stock Inventory and Safety Threshold Alerts
- **Terminal Output:**
  ```text
  =========================================================================================================================
     REAL-TIME BLOOD STOCK INVENTORY REPORT
  =========================================================================================================================
  +-------------+-----------------+---------------+-------------------+------------------+--------------------------------+
  | Blood Group | Available Units | Min Threshold | Surplus / Deficit | Status           | Total Historical Units Donated |
  +=============+=================+===============+===================+==================+================================+
  | A+          | 16              | 5             | +11               | ADEQUATE         | 6                              |
  | A-          | 6               | 4             | +2                | ADEQUATE         | 2                              |
  | AB+         | 8               | 4             | +4                | ADEQUATE         | 2                              |
  | AB-         | 2               | 4             | -2                | CRITICAL DEFICIT | 1                              |
  | B+          | 20              | 5             | +15               | ADEQUATE         | 4                              |
  | B-          | 3               | 4             | -1                | CRITICAL DEFICIT | 1                              |
  | O+          | 24              | 6             | +18               | ADEQUATE         | 6                              |
  | O-          | 4               | 5             | -1                | CRITICAL DEFICIT | 3                              |
  +-------------+-----------------+---------------+-------------------+------------------+--------------------------------+
   Total Count: 8 record(s)

   >> Total Blood Units in Storage: 83 units across 8 blood groups.

  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        CRITICAL LOW STOCK ALERTS                         
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   [ALERT] Blood Group AB- has only 2 unit(s) available (Safety Buffer: 4 units)!
   [ALERT] Blood Group B- has only 3 unit(s) available (Safety Buffer: 4 units)!
   [ALERT] Blood Group O- has only 4 unit(s) available (Safety Buffer: 5 units)!
   >> Recommend organizing targeted donation drives for the above groups.
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  ```

---

### Scenario 5: Hospital Requisition Fulfillment
- **Input Data:**
  - Pending Request ID: `209` (`Care 24 Hospital`, requesting 6 units of `O+`)
  - Authorizing Doctor: `Dr. K. Mohanraj`
- **Terminal Interaction & Output:**
  ```text
  --- [4] Hospital Blood Requisitions & Unit Issuance ---
  Select sub-option (1-5): 4
  Enter Request ID to Fulfill & Issue Units: 209
  Enter Authorizing Officer / Doctor Name: Dr. K. Mohanraj

  [SUCCESS] Request ID 209 successfully fulfilled! Issued 6 unit(s) of O+ to Care 24 Hospital, Perundurai.
  ```

---

### Scenario 6: Hospital Requisition Stock Deficit Prevention
- **Input Data:**
  - Request ID requesting 8 units of `AB-` (Available stock is only 2 units)
- **Terminal Interaction & Output:**
  ```text
  [FAILED] Insufficient stock for AB-! Requested: 8, Available: 2 units.
  ```

---

### Scenario 7: Donor Availability Audit (Filtered for Emergency Mobilization)
- **Input Data:**
  - Blood Group Filter: `O+`
- **Terminal Output:**
  ```text
  =======================================================================================================================
     AVAILABLE DONORS REPORT (90-DAY MEDICAL INTERVAL PASSED) [FILTERED FOR O+]
  =======================================================================================================================
  +----------+--------------------+-------------+-----+------------+-------+--------------+---------------------+
  | Donor ID | Donor Name         | Blood Group | Age | Phone      | City  | Last Donated | Availability Status |
  +==========+====================+=============+=====+============+=======+==============+=====================+
  | 9        | Deepa Lakshmanan   | O+          | 29  | 9488112233 | Erode | 2026-06-12   | AVAILABLE (Eligible)|
  | 15       | Divya Bharathi K   | O+          | 23  | 9600554433 | Salem | Never        | AVAILABLE (Eligible)|
  +----------+--------------------+-------------+-----+------------+-------+--------------+---------------------+
   Total Count: 2 record(s)
  ```

---

### Scenario 8: Python Data Analytics Pipeline Terminal Output
- **Execution Command:** `python python/main_analysis.py`
- **Terminal Output:**
  ```text
  ================================================================================
         BLOOD DONATION MANAGEMENT & DONOR AVAILABILITY ANALYSIS PIPELINE        
                  Course: 25ITC31 Foundations of Data Science                    
         Student: Karan Raajaa V | Register No: 732925ITR045 (Roll No. 45)       
  ================================================================================

  [STEP 1/4] Extracting Data from SQLite Database (blood_bank.db)...
  [ETL Export] Successfully exported 8 records from 'blood_stock'
  [ETL Export] Successfully exported 18 records from 'donors'
  [ETL Export] Successfully exported 25 records from 'donations'
  [ETL Export] Successfully exported 12 records from 'hospital_requests'
  [ETL Export] Successfully exported 8 records from 'v_stock_summary'
  [ETL Export] Successfully exported 18 records from 'v_donor_availability'

  [STEP 2/4] Running Data Cleaning, Type Conversions & Preprocessing...
    * Cleaning Complete: 0 null critical fields, dates parsed to ISO format.
    * Feature Engineering: Added 'age_bracket', 'days_since_last_donation', 'is_eligible'.

  [STEP 3/4] Exploratory Data Analysis (EDA) Summary Statistics:
  ------------------------------------------------------------
    Total Registered Donors    : 18
    Total Donation Events Logged: 25
    Total Blood Units in Stock : 83 units
    Donor Age Distribution     : Mean = 26.94 yrs, StdDev = 6.03 yrs
    Donor Age Range            : Min = 20 yrs, Max = 42 yrs
    Donor Hemoglobin Metrics   : Mean = 13.84 g/dL, StdDev = 0.73 g/dL
  ------------------------------------------------------------

  [CLINICAL AUDIT] 90-Day Medical Cooldown Analysis:
    * Immediately Available Donors (>= 90 Days): 9 (50.0%)
    * Ineligible Donors (Active Cooldown Period): 9 (50.0%)

  [STEP 4/4] Generating Analytical Visualizations...
    -> Saved: visualizations/chart1_blood_stock_availability.svg
    -> Saved: visualizations/chart2_donor_blood_group_distribution.svg
    -> Saved: visualizations/chart3_monthly_donation_trends.svg
    -> Saved: visualizations/chart6_donor_eligibility_breakdown.svg
    -> Saved Interactive Dashboard: visualizations/dashboard.html

  ================================================================================
   [SUCCESS] Data Science Pipeline Executed Completely!
   Visualizations and HTML Dashboard are ready in: visualizations/
  ================================================================================
  ```

---
*Prepared and verified for academic submission by Karan Raajaa V (Reg. No: 732925ITR045).*
