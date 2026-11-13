# Testing Techniques and Test Cases Documentation
## Blood Donation Management and Donor Availability Analysis System
**Academic Year:** 2026 - 2027 (ODD)  
**Course Code & Name:** 25ITT33 - Software Engineering  
**Student Name:** Karan Raajaa V  
**Register Number:** 732925ITR045  
**Class / Section:** 25IT3A (Roll No. 45)  
**Scenario:** Scenario 15 - Blood Donation Management and Donor Availability Analysis System  

---

## 1. Testing Strategy and Methodologies

Comprehensive testing was planned and executed across multiple stages of software development to guarantee functional accuracy, robust error handling, boundary validation, and referential database integrity.

```
+-------------------------------------------------------------------------+
|                         V-Model Testing Strategy                        |
+-------------------------------------------------------------------------+
|  Requirements Specification   <-------->  System & Acceptance Testing   |
|         \                                          /                    |
|      Architectural Design     <-------->   Integration Testing          |
|            \                                    /                       |
|          Detailed Design      <-------->   Unit & Component Testing     |
|               \                              /                          |
|                +------> Code Construction --+                           |
+-------------------------------------------------------------------------+
```

### 1.1 Testing Levels
1. **Unit Testing:** Focuses on individual Java methods and service classes (e.g., date interval calculation, input validation regex, stock arithmetic).
2. **Integration Testing:** Verifies end-to-end data flow between UI handlers, Services, Data Access Objects (DAOs), and the relational database transactions.
3. **System Testing:** Validates that all integrated modules (Java console, SQLite database, and Python visualization script) execute seamlessly as a unified system according to the SRS.

### 1.2 Testing Techniques Applied

#### A. Black-Box Testing Techniques
1. **Equivalence Class Partitioning (ECP):**
   - **Donor Age:**
     - Invalid Class 1: $\text{Age} < 18$ (Underage) $\to$ Rejected
     - Valid Class: $18 \le \text{Age} \le 65$ $\to$ Accepted
     - Invalid Class 2: $\text{Age} > 65$ (Overage) $\to$ Rejected
   - **Eligibility Cooldown Interval:**
     - Invalid Class (Ineligible): $\text{Days Since Last Donation} < 90$ $\to$ Blocked from donating
     - Valid Class (Eligible): $\text{Days Since Last Donation} \ge 90$ or Never Donated $\to$ Permitted to donate
   - **Blood Group Domains:**
     - Valid: `A+`, `A-`, `B+`, `B-`, `AB+`, `AB-`, `O+`, `O-`
     - Invalid: Any other string (`C+`, `XYZ`, `123`, blank)

2. **Boundary Value Analysis (BVA):**
   - **Donor Age Boundaries:** Tested values: 17 (Invalid), 18 (Boundary Valid), 19 (Nominal), 64 (Nominal), 65 (Boundary Valid), 66 (Invalid).
   - **Donation Cooldown Boundaries:** Tested values: 89 days (Boundary Ineligible - Blocked), 90 days (Boundary Eligible - Allowed), 91 days (Eligible - Allowed).
   - **Stock Quantity Boundaries:** Tested inventory decrements at 0 units (prevent negative stock), 1 unit, and threshold values (5 units).

#### B. White-Box Testing Techniques
1. **Basis Path Testing & Cyclomatic Complexity:**
   - Evaluated the control flow of `DonorEligibilityService.isEligible(lastDonationDate)`:
     - Predicate node 1: `if (lastDonationDate == null) return true;`
     - Predicate node 2: `long days = ChronoUnit.DAYS.between(lastDonationDate, today);`
     - Predicate node 3: `if (days >= 90) return true; else return false;`
   - **Cyclomatic Complexity:** $V(G) = P + 1 = 2 + 1 = 3$.
   - Three independent basis paths identified and executed to guarantee 100% statement and branch coverage.

---

## 2. Comprehensive Test Cases and Results

| Test Case ID | Test Scenario / Objective | Input Data / Preconditions | Execution Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|---|
| **TC-01** | Register Donor - Valid Demographic Input | Name: "Ravi Kumar", Age: 28, Blood Group: "O+", Phone: "9876543210" | 1. Choose Option 1 (Register Donor)<br>2. Enter valid demographic data | System saves record, assigns new `donor_id`, prints success message | Record inserted in `donors` table; success confirmation displayed | **PASS** |
| **TC-02** | Register Donor - Underage Boundary (Age = 17) | Age: 17, Name: "Minor Donor", Blood Group: "A+" | 1. Choose Option 1<br>2. Enter Age: 17 | Validation error: Age must be between 18 and 65; insertion aborted | "Error: Donor must be at least 18 years of age." prompted | **PASS** |
| **TC-03** | Register Donor - Invalid Blood Group String | Blood Group: "X+" | 1. Choose Option 1<br>2. Enter Blood Group: "X+" | Validation error: Invalid blood group; prompts re-entry | "Error: Invalid blood group. Must be A+, A-, B+, etc." | **PASS** |
| **TC-04** | Record Donation - First-time Donor (No Past History) | Donor ID: 101, Units: 1, Hemoglobin: 13.5 | 1. Choose Option 2 (Record Donation)<br>2. Select Donor ID: 101 | System identifies zero prior donations $\to$ Eligible. Records donation and increments stock | Donation logged; blood stock for donor group incremented by 1 | **PASS** |
| **TC-05** | Record Donation - Cooldown Period Ineligible (< 90 Days) | Donor ID: 102 (Last donated 42 days ago) | 1. Choose Option 2<br>2. Enter Donor ID: 102 | System detects 42 < 90 days. Displays cooldown alert with remaining 48 days; rejects donation | "[REJECTED] Ineligible to donate. 48 days remaining in cooldown." | **PASS** |
| **TC-06** | Record Donation - Cooldown Period Eligible (>= 90 Days) | Donor ID: 103 (Last donated 110 days ago) | 1. Choose Option 2<br>2. Enter Donor ID: 103 | System detects 110 >= 90 days $\to$ Eligible. Records donation and updates stock | Donation logged; stock incremented; success message printed | **PASS** |
| **TC-07** | Inventory Stock Update - Atomic Increment | Blood Group: "B+", Units: 2 | 1. Record 2 units donation for B+ donor | Available units for B+ increases by 2; timestamp updated | B+ stock incremented from 12 to 14 units | **PASS** |
| **TC-08** | Hospital Request - Fulfill with Sufficient Stock | Hospital: "Apollo Hospital", Blood Group: "A+", Units: 3 (Stock: 15) | 1. Choose Option 4 (Fulfill Request)<br>2. Select Pending Request | Stock decremented by 3 (15 -> 12); status updated to `FULFILLED` | Units decremented; status set to `FULFILLED` | **PASS** |
| **TC-09** | Hospital Request - Stock Deficit (Insufficient Units) | Hospital: "KMCH", Blood Group: "AB-", Units: 8 (Stock: 2) | 1. Attempt to fulfill request of 8 units | Insufficient stock error displayed; stock untouched; status remains `PENDING` | "Error: Insufficient stock (Available: 2, Requested: 8)." | **PASS** |
| **TC-10** | Donor Availability Audit by Blood Group | Query: "O+" | 1. Choose Option 5 (Donor Availability Analysis)<br>2. Filter by "O+" | Returns list of O+ donors whose last donation date is >= 90 days ago or null | Formatted table of available O+ donors with contact details | **PASS** |
| **TC-11** | Management Report - Stock Status & Low Stock Alert | Stock levels across all 8 groups | 1. Choose Option 6 (Stock Summary Report) | Displays table of all blood groups, units available, status (`ADEQUATE` / `LOW STOCK`) | Formatted table with warning tags for stock < 5 units | **PASS** |
| **TC-12** | Python Data Science Pipeline Execution | Database: `blood_bank.db` | 1. Execute `python python/main_analysis.py` | Extracts tables, cleans data, computes metrics, and generates 5+ PNG charts in `visualizations/` | 5 PNG charts saved; terminal summary logs generated | **PASS** |

---

## 3. Test Execution Summary

- **Total Test Cases Executed:** 12
- **Passed:** 12
- **Failed:** 0
- **Pass Percentage:** 100.0%
- **Defects Identified and Resolved:**
  1. *Defect:* Leap year date calculation error when calculating days between dates manually.  
     *Resolution:* Adopted `java.time.LocalDate` and `java.time.temporal.ChronoUnit.DAYS` for accurate calendar arithmetic.
  2. *Defect:* Stock level decrementing into negative numbers during concurrent hospital request issuances.  
     *Resolution:* Added SQL check constraint `CHECK (available_units >= 0)` and synchronized transactional verification in `InventoryService`.

---
*Prepared and verified for academic submission by Karan Raajaa V (Reg. No: 732925ITR045).*

