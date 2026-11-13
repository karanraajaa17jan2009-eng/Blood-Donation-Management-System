# Software Requirements Specification (SRS)
## Blood Donation Management and Donor Availability Analysis System
**Academic Year:** 2026 - 2027 (ODD)  
**Course Code & Name:** 25ITT33 - Software Engineering / 25ITT31 - DBMS / 25ITT32 - Java Programming / 25ITC31 - Foundations of Data Science  
**Institution:** Velalar College of Engineering and Technology, Erode - 638012  
**Department:** Department of Information Technology  
**Student Name:** Karan Raajaa V  
**Register Number:** 732925ITR045  
**Class / Section:** 25IT3A&B (Roll No. 45)  
**Scenario:** Scenario 15 - Blood Donation Management and Donor Availability Analysis System  

---

## 1. Introduction

### 1.1 Purpose
The purpose of this document is to provide a complete, detailed specification of the requirements for the **Blood Donation Management and Donor Availability Analysis System**. It describes the functional and non-functional requirements, architectural design, database design, user interface workflows, and data visualization capabilities required to manage blood bank operations, track donor records, monitor blood unit stocks, manage hospital emergency blood requests, verify donor medical eligibility intervals, and perform exploratory data analysis using Python.

### 1.2 Document Conventions
This document adheres to the IEEE 830-1998 Standard for Software Requirements Specifications. The following typographical conventions are observed:
- `Courier New` / code blocks: Identifies database attributes, table names, code classes, and SQL statements.
- **Bold**: Emphasizes critical terms, requirements identifiers, and headers.
- *Italics*: Used for secondary definitions and contextual emphasis.
- **FR-[n]**: Designates Functional Requirements.
- **NFR-[n]**: Designates Non-Functional Requirements.

### 1.3 Intended Audience and Reading Suggestions
This document is prepared for:
1. **Academic Evaluators and Faculty Members**: To assess compliance with Software Engineering (25ITT33), DBMS (25ITT31), Java Programming (25ITT32), and Data Science (25ITC31) course criteria.
2. **System Developers and Maintainers**: To understand implementation details, class designs, database schemas, and integration points.
3. **Blood Bank Staff & Healthcare Stakeholders**: To understand operational capabilities, reporting workflows, and safety verification protocols.

### 1.4 Project Scope
The **Blood Donation Management and Donor Availability Analysis System** is an integrated software platform developed using:
- **Core Java (JDK 26)** for business logic, menu-driven command-line interfaces, object-oriented abstractions, transaction services, and JDBC connectivity.
- **Relational DBMS (SQLite & MySQL)** for relational persistence, ACID guarantees, relational integrity, primary/foreign key constraints, and views.
- **Python (3.11 with Pandas, NumPy, Matplotlib, Seaborn)** for ETL database extraction, missing value imputation, statistical preprocessing, and exploratory analytical visualizations.

The system replaces manual paper logs and spreadsheets with an automated, auditable, and data-driven management system that eliminates human error in tracking blood unit expiration, donor eligibility intervals, stock deficits, and hospital emergency requests.

### 1.5 References
- IEEE Std 830-1998: IEEE Recommended Practice for Software Requirements Specifications.
- Pressman, R. S., *Software Engineering: A Practitioner's Approach*, McGraw-Hill.
- Silberschatz, A., Korth, H. F., Sudarshan, S., *Database System Concepts*, McGraw-Hill.
- Schildt, H., *Java: The Complete Reference*, Oracle Press.
- McKinney, W., *Python for Data Analysis*, O'Reilly Media.

---

## 2. Overall Description

### 2.1 Product Perspective
In healthcare ecosystems, blood banks act as critical life-saving intermediaries between voluntary donors and hospital healthcare facilities. Existing manual systems suffer from significant latency:
- Difficulty identifying which past donors are medically eligible for a new donation.
- Inability to quickly compute available units by specific blood group (A+, A-, B+, B-, AB+, AB-, O+, O-).
- Slow response times when hospitals submit urgent blood requisition orders.
- Absence of historical visual trend analysis to forecast blood shortages.

The proposed system addresses these gaps by creating a centralized software solution comprising a Java management engine, an ACID-compliant database, and a Python analytics pipeline.

```
+-----------------------------------------------------------------------+
|                Overall System Architectural Perspective               |
+-----------------------------------------------------------------------+
|  [Blood Bank Staff / Administrator]                                   |
|              |                                                        |
|              v                                                        |
|   +---------------------------------------------------------------+   |
|   |         Java Console / CLI Application (JDK 26)               |   |
|   | - Menu-Driven Interface (Input Validation, Formatting)        |   |
|   | - Service Layer (Donor, Donation, Inventory, Hospital Req)    |   |
|   | - DAO Layer (Data Access Objects & JDBC Connection Manager)   |   |
|   +---------------------------------------------------------------+   |
|                                |                                      |
|                                v                                      |
|   +---------------------------------------------------------------+   |
|   |            Relational Database (SQLite / MySQL)               |   |
|   | - Tables: donors, donations, blood_stock, hospital_requests   |   |
|   | - Triggers, Foreign Keys, Referential Integrity, Views        |   |
|   +---------------------------------------------------------------+   |
|                                |                                      |
|                                v                                      |
|   +---------------------------------------------------------------+   |
|   |             Python Data Science Pipeline (Python 3.11)        |   |
|   | - Database Retrieval (sqlite3 / SQLAlchemy / Pandas)          |   |
|   | - Data Cleaning, Missing Value Imputation, Transformations    |   |
|   | - Visualizations: Stock Levels, Group Distribution, Trends    |   |
|   +---------------------------------------------------------------+   |
+-----------------------------------------------------------------------+
```

### 2.2 Product Functions
The core capabilities of the system are structured into six major modules:
1. **Donor Management Module**: Registers new donors, maintains demographic and contact details, and stores blood groups.
2. **Donation Processing Module**: Records every donation event, unit volume, donation date, and automatically links to the donor profile.
3. **Inventory & Stock Tracking Module**: Maintains real-time unit counts categorized by blood group (A+, A-, B+, B-, AB+, AB-, O+, O-). Updates stock upon collection and deducts stock upon issuance.
4. **Hospital Requisition Module**: Captures blood requests from hospitals (hospital name, blood group, units requested, urgency level), tracks status (`PENDING`, `FULFILLED`, `REJECTED`), and handles unit allocation.
5. **Donor Eligibility Analysis Engine**: Analyzes donor history against clinical safety standards (minimum 90-day cooldown period between donations) to determine immediate donor availability.
6. **Exploratory Data Analytics & Visualization Engine**: Preprocesses historical records and generates comprehensive visual graphs showing donation patterns, inventory distributions, and hospital request fulfillment ratios.

### 2.3 User Classes and Characteristics
- **Blood Bank Administrator / Phlebotomist**: Operates the Java application to record donors, register donations, issue units to hospitals, and generate real-time stock reports. Requires basic computing literacy.
- **Data Analyst / Healthcare Officer**: Executes the Python analytical scripts and inspects generated graphical charts to plan blood drives and forecast shortages.
- **Academic Evaluator**: Reviews code modularity, design pattern usage, schema normalization, test execution logs, and documentation quality.

### 2.4 Operating Environment
- **Operating System:** Windows 10/11, Linux (Ubuntu/Debian), or macOS.
- **Runtime Environment:** Java Development Kit (JDK 17 or JDK 26).
- **Database Engine:** SQLite 3 (built-in zero configuration) and/or MySQL 8.0+.
- **Python Environment:** Python 3.10+ with `pandas`, `numpy`, `matplotlib`, `seaborn`, and `tabulate`.

### 2.5 Design and Implementation Constraints
1. **Clinical Safety Rule:** A donor is strictly ineligible to donate if fewer than 90 days have elapsed since their previous donation date.
2. **Biological Age Constraints:** Donors must be between the ages of 18 and 65 years.
3. **Inventory Conservation Constraint:** Blood stock for any blood group cannot be decremented below zero. If stock is insufficient, the hospital request status must be flagged as `PENDING` or `REJECTED` with an explanatory message.
4. **Persistence Integrity:** All data transactions must be committed to the relational database using foreign key constraints and transactional rollback on failures.

### 2.6 Assumptions and Dependencies
- Donors provide accurate personal and contact information.
- Standard whole-blood donations are measured in units (1 unit ≈ 450 mL).
- The operating environment has read/write permissions for the local database file and chart output directory.

---

## 3. Specific Requirements

### 3.1 External Interface Requirements
#### 3.1.1 User Interfaces
- An ANSI/ASCII formatted terminal interface with interactive numbered menus.
- Clean columnar tabular displays using box-drawing borders for reports and listings.
- Clear error and success prompts with color-coded or tagged status indicators (`[SUCCESS]`, `[ERROR]`, `[WARNING]`, `[INFO]`).

#### 3.1.2 Software Interfaces
- **JDBC Driver:** `org.sqlite.JDBC` / `com.mysql.cj.jdbc.Driver` for Java-to-Database connectivity.
- **Python DB-API 2.0:** `sqlite3` for SQL query retrieval directly into Pandas DataFrames.

---

### 3.2 Functional Requirements

#### FR-1: Donor Registration and Maintenance
- **FR-1.1:** The system shall allow the operator to register a new donor with `donor_id`, `name`, `age`, `gender`, `contact_number`, `email`, `address`, and `blood_group`.
- **FR-1.2:** The system shall validate that `age` is between 18 and 65.
- **FR-1.3:** The system shall validate that `blood_group` belongs to the standard set: `{A+, A-, B+, B-, AB+, AB-, O+, O-}`.
- **FR-1.4:** The system shall validate that `contact_number` consists of a valid 10-digit format.
- **FR-1.5:** The system shall provide search and filter capabilities by donor ID, blood group, and name.

#### FR-2: Blood Donation Processing
- **FR-2.1:** The system shall record a donation with `donation_id`, `donor_id`, `donation_date`, `units_donated`, and `hemoglobin_level`.
- **FR-2.2:** The system shall automatically verify donor eligibility (FR-5) before recording a donation.
- **FR-2.3:** The system shall atomically increment the blood stock level (FR-3) for the donor's blood group upon successful recording of a donation.
- **FR-2.4:** The system shall maintain an immutable donation history log.

#### FR-3: Blood Stock Inventory Management
- **FR-3.1:** The system shall maintain stock records containing `blood_group`, `available_units`, and `last_updated_timestamp`.
- **FR-3.2:** The system shall update stock levels atomically during donations (+units) and issuances (-units).
- **FR-3.3:** The system shall prevent negative stock balances.
- **FR-3.4:** The system shall issue visual warnings when stock for any blood group drops below a predefined safety threshold (e.g., < 5 units).

#### FR-4: Hospital Blood Requisition and Issuance
- **FR-4.1:** The system shall record hospital requests with `request_id`, `hospital_name`, `blood_group_requested`, `units_requested`, `request_date`, `urgency_level` (`NORMAL`, `URGENT`, `CRITICAL`), and `status` (`PENDING`, `FULFILLED`, `REJECTED`).
- **FR-4.2:** When fulfilling a request, the system shall check if available stock is sufficient. If sufficient, decrement the stock, mark status as `FULFILLED`, and record `issuance_date`.
- **FR-4.3:** If stock is insufficient, the system shall allow marking the request as `PENDING` or `REJECTED`, alerting the operator of the shortfall.

#### FR-5: Donor Eligibility Verification & Availability Analysis
- **FR-5.1:** The system shall compute the difference in days between the current date and the donor's last recorded donation date.
- **FR-5.2:** If `days_since_last_donation >= 90` (or if the donor has never donated before), the donor shall be classified as **ELIGIBLE / AVAILABLE**.
- **FR-5.3:** If `days_since_last_donation < 90`, the donor shall be classified as **INELIGIBLE / COOLDOWN**, and the system shall display the remaining cooldown days.
- **FR-5.4:** The system shall generate an **Available Donors Report** filtered by requested blood group to mobilize emergency donors during shortages.

#### FR-6: Reporting and Summaries
- **FR-6.1:** Generate a comprehensive **Stock Availability Report** showing unit counts and status across all 8 blood groups.
- **FR-6.2:** Generate a **Donation History Report** displaying complete chronological donation logs.
- **FR-6.3:** Generate a **Blood Group-Wise Donation Count & Volume Report**.
- **FR-6.4:** Generate a **Hospital Request Summary Report** with breakdown by status and urgency.

#### FR-7: Python ETL, Preprocessing & Visualization
- **FR-7.1:** Retrieve datasets (`donors`, `donations`, `blood_stock`, `hospital_requests`) from the database via Python into Pandas DataFrames.
- **FR-7.2:** Clean and preprocess data: handle missing values, convert date columns to datetime objects, identify outliers, and engineer features (e.g., `days_since_last_donation`, `eligibility_flag`, `turnaround_time`).
- **FR-7.3:** Generate and save informative visualization charts:
  1. *Bar Chart:* Blood Stock Availability vs. Safety Threshold.
  2. *Pie/Donut Chart:* Blood Group Distribution across Registered Donors.
  3. *Line Chart / Trend:* Monthly/Quarterly Donation Volume Trends.
  4. *Histogram with KDE:* Donor Age Demographics & Distribution.
  5. *Stacked / Grouped Bar Chart:* Hospital Request Fulfillment by Urgency Level.
  6. *Heatmap / Correlation Matrix:* Numerical metrics correlation (Age, Units, Hemoglobin).

---

## 4. Non-Functional Requirements

### 4.1 Performance Requirements
- **NFR-1 (Response Time):** Database query operations and menu transitions shall execute within 200 milliseconds under standard load.
- **NFR-2 (Throughput):** Batch report generation shall process over 1,000 records within 1.5 seconds.
- **NFR-3 (Analytical Script Performance):** The Python ETL and visualization pipeline shall generate all charts within 10 seconds.

### 4.2 Safety and Reliability Requirements
- **NFR-4 (Data Integrity):** Foreign key constraints ensure child records in `donations` and `hospital_requests` cannot reference nonexistent `donor_id` or invalid `blood_group`.
- **NFR-5 (Atomic Transactions):** Stock updates and donation logging must be executed within database transactions (`COMMIT`/`ROLLBACK`) to guarantee that partial failures never corrupt inventory levels.
- **NFR-6 (Auditability):** Every donation and issuance must maintain a permanent timestamp.

### 4.3 Security Requirements
- **NFR-7 (Input Sanitization):** SQL injection prevention achieved through Parameterized Queries (`PreparedStatement` in Java, parameterized tuples in Python).
- **NFR-8 (Data Validation):** Robust regex and boundary validations on names, phone numbers, ages, and quantities before reaching the DAO layer.

### 4.4 Software Quality Attributes
- **Maintainability:** Layered architectural pattern (Model-DAO-Service-UI) ensuring loose coupling and high cohesion.
- **Portability:** Pure Java SE code compliant with JDK 17 through JDK 26; standard Python 3 compatible across Windows, Linux, and macOS.
- **Extensibility:** Interface-driven design allowing easy extension to a GUI (JavaFX/Swing) or REST API (Spring Boot) in future iterations.

---

## 5. Requirement Traceability Matrix (RTM)

| Req ID | Requirement Description | Architecture Module | Database Table / Entity | Verification Method |
|---|---|---|---|---|
| **FR-1** | Donor Registration & Demographics | `DonorService`, `DonorDAO` | `donors` | Test Case TC-01, TC-02 |
| **FR-2** | Blood Donation Recording | `DonationService`, `DonationDAO` | `donations`, `blood_stock` | Test Case TC-03, TC-04 |
| **FR-3** | Blood Stock Tracking & Alerts | `InventoryService`, `BloodStockDAO` | `blood_stock` | Test Case TC-05, TC-06 |
| **FR-4** | Hospital Request & Fulfillment | `HospitalRequestService`, `HospitalRequestDAO` | `hospital_requests`, `blood_stock` | Test Case TC-07, TC-08 |
| **FR-5** | Donor Eligibility Analysis (90 Days) | `DonorEligibilityService` | `donors`, `donations` | Test Case TC-09, TC-10 |
| **FR-6** | Management Reports & Aggregation | `ReportService` | All Tables | Test Case TC-11, TC-12 |
| **FR-7** | Python ETL & Visualizations | `python/visualizations.py` | Full Database Schema | Automated Chart Verification |

---
*Prepared and verified for academic submission by Karan Raajaa V (Reg. No: 732925ITR045).*

