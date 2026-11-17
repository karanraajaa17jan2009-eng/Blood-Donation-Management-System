# Blood Donation Management and Donor Availability Analysis System
### Academic Activity: Project-Based Assessment — Scenario 15

[![Live Website](https://img.shields.io/badge/🌐%20Live%20Website-24%2F7%20Online-success?style=for-the-badge&logo=googlechrome&logoColor=white)](https://karanraajaa17jan2009-eng.github.io/Blood-Donation-Management-System/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/karanraajaa17jan2009-eng/Blood-Donation-Management-System)
[![Java Version](https://img.shields.io/badge/Java-JDK%2017%20--%2026-orange.svg)](https://www.oracle.com/java/)
[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/DBMS-SQLite%20%7C%20MySQL-green.svg)](https://www.sqlite.org/)
[![Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![License](https://img.shields.io/badge/Academic-Assessment-red.svg)]()

> **🚀 LIVE RUNNING INTERACTIVE WEBSITE (24/7):**  
> Access the live cloud deployment directly at:  
> 👉 **[https://karanraajaa17jan2009-eng.github.io/Blood-Donation-Management-System/](https://karanraajaa17jan2009-eng.github.io/Blood-Donation-Management-System/)**  
> *(Features live blood stock inventory tracking, donor registration form, 90-day cooldown eligibility analyzer, emergency hospital requisitions, and interactive Chart.js visualizations!)*

---

## 📋 Academic Identification

- **Institution:** Velalar College of Engineering and Technology, Erode - 638012
- **Department:** Department of Information Technology
- **Academic Year:** 2026 - 2027 (ODD Semester)
- **Class & Section:** 25IT3A
- **Student Name:** **Karan Raajaa V**
- **Register Number:** **732925ITR045** (Roll No: 45)
- **Assigned Scenario:** **Scenario 15: Blood Donation Management and Donor Availability Analysis System**

### Integrated Course Mapping
1. **25ITT31 - Database Management Systems (DBMS)**: Relational model, ER diagram, SQL DDL/DML, normalization up to BCNF, views, indexing, integrity constraints.
2. **25ITT32 - Java Programming**: OOP abstractions, interfaces, exception handling, collections framework, Java streams & lambdas, console I/O, JDBC persistence.
3. **25ITT33 - Software Engineering**: IEEE 830 SRS, UML Use Case, Class diagrams, Multi-Tier Architecture, Unit/Integration/Black-Box/White-Box testing.
4. **25ITC31 - Foundations of Data Science**: Python ETL, data cleaning, feature engineering, descriptive statistics, exploratory data analysis (EDA), visualizations.

---

## 🎯 Problem Statement & Scenario Description

A blood bank maintains donor information, blood group details, donation records, and blood stock levels. Managing these records manually makes it difficult to identify available donors, monitor blood unit availability, track donation history, and respond promptly to urgent hospital requests.

This project delivers a complete **Blood Donation Management and Donor Availability Analysis System** that:
1. Maintains comprehensive donor demographics and blood group records.
2. Automates donation recording with clinical **90-day cooldown interval verification**.
3. Real-time tracks blood inventory across all 8 ABO/Rh blood groups (`A+`, `A-`, `B+`, `B-`, `AB+`, `AB-`, `O+`, `O-`) with safety threshold deficit alerts.
4. Manages hospital blood requisitions, urgency levels, and automated unit issuance.
5. Performs exploratory data analytics using Python to visualize blood stock distributions, donation trends, and donor availability patterns.

---

## 🏛️ System Architecture

The application adopts a **Multi-Tier Layered Architecture Pattern**:

```
+---------------------------------------------------------------------------------+
|                               Presentation Tier                                 |
|  - Java Interactive Console / CLI Menu Application (ANSI Formatted Tables)      |
|  - Python Interactive Visual Analytics Dashboard (HTML & SVG Charts)            |
+---------------------------------------------------------------------------------+
                                      |
                                      v
+---------------------------------------------------------------------------------+
|                           Application & Business Logic Tier                     |
|  - DonorService: Demographics validation, registration                          |
|  - DonationService: Donation processing & atomic stock synchronization          |
|  - DonorEligibilityService: 90-day medical interval cooldown analyzer          |
|  - InventoryService: Threshold monitoring, buffer alerts                        |
|  - HospitalRequestService: Requisition management & issuance logic              |
|  - ReportService: Java Streams & Collectors tabular reporting                   |
+---------------------------------------------------------------------------------+
                                      |
                                      v
+---------------------------------------------------------------------------------+
|                             Data Access Layer (DAO)                             |
|  - DonorDAO, DonationDAO, BloodStockDAO, HospitalRequestDAO                     |
|  - DatabaseManager: Dual-engine JDBC & Zero-Dependency In-Memory Synchronizer    |
+---------------------------------------------------------------------------------+
                                      |
                                      v
+---------------------------------------------------------------------------------+
|                           Persistence & Database Tier                           |
|  - SQLite 3 (Default zero-config database: database/blood_bank.db)              |
|  - MySQL 8.0+ Compatible (DDL/DML Scripts in database/)                         |
|  - Views: v_stock_summary, v_donor_availability                                 |
+---------------------------------------------------------------------------------+
                                      |
                                      v
+---------------------------------------------------------------------------------+
|                           Python Data Science Pipeline                          |
|  - db_retrieval.py -> data_preprocessing.py -> visualizations.py                |
+---------------------------------------------------------------------------------+
```

---

## 📂 Project Repository Structure

```text
Assingment_1/
├── README.md                                  # Complete Project Documentation
├── database/                                  # Database Layer
│   ├── blood_bank.db                          # Operational SQLite 3 Database
│   ├── schema_sqlite.sql                      # SQLite DDL Schema, Views & Indexes
│   ├── schema_mysql.sql                       # MySQL 8.0+ Compatible DDL Schema
│   ├── sample_data.sql                        # Realistic Seed Dataset (DML)
│   ├── analytical_queries.sql                 # Syllabus-Mapped Complex SQL Queries
│   └── extracted_csv/                         # CSV Exports of Database Tables
├── docs/                                      # Software Engineering Documentation
│   ├── SRS_Document.md                        # IEEE 830 Standard SRS Specification
│   ├── Architecture_and_Design_Diagrams.md    # Architecture, Use Case & Class Diagrams
│   ├── Database_Design_and_Normalization.md   # ER Diagram, Relational Model & Normalization (UNF to BCNF)
│   └── Testing_Document_and_Test_Cases.md     # Testing Methodologies & 12 Test Cases (100% Pass)
├── java/                                      # Java Source Code
│   ├── src/
│   │   └── com/bloodbank/
│   │       ├── Main.java                      # Console Application Entry Point
│   │       ├── model/                         # Domain Entity Models
│   │       │   ├── BloodGroup.java
│   │       │   ├── Donor.java
│   │       │   ├── Donation.java
│   │       │   ├── BloodStock.java
│   │       │   └── HospitalRequest.java
│   │       ├── dao/                           # Data Access Object Interfaces & DB Manager
│   │       │   ├── DatabaseManager.java
│   │       │   ├── DonorDAO.java
│   │       │   ├── DonationDAO.java
│   │       │   ├── BloodStockDAO.java
│   │       │   ├── HospitalRequestDAO.java
│   │       │   └── impl/                      # DAO Implementations
│   │       │       ├── DonorDAOImpl.java
│   │       │       ├── DonationDAOImpl.java
│   │       │       ├── BloodStockDAOImpl.java
│   │       │       └── HospitalRequestDAOImpl.java
│   │       ├── service/                       # Business Services & Eligibility Analyzer
│   │       │   ├── DonorService.java
│   │       │   ├── DonationService.java
│   │       │   ├── DonorEligibilityService.java
│   │       │   ├── InventoryService.java
│   │       │   ├── HospitalRequestService.java
│   │       │   └── ReportService.java
│   │       └── util/                          # Utility Classes
│   │           ├── InputValidator.java
│   │           └── TableFormatter.java
│   ├── bin/                                   # Compiled Java Bytecode (.class)
│   └── lib/                                   # Optional External JDBC Drivers
├── python/                                    # Data Science & Analytics Pipeline
│   ├── db_retrieval.py                        # Database Extraction & CSV Export Module
│   ├── data_preprocessing.py                  # Cleaning, Type Conversion & Feature Engineering
│   ├── visualizations.py                      # Multi-Engine Chart & Dashboard Generator
│   ├── main_analysis.py                       # Automated End-to-End Pipeline Runner
│   ├── analysis_notebook.ipynb                # Interactive Jupyter Notebook (25ITC31)
│   └── requirements.txt                       # Python Dependencies Specification
├── visualizations/                            # Generated Analytical Visuals
│   ├── chart1_blood_stock_availability.svg
│   ├── chart2_donor_blood_group_distribution.svg
│   ├── chart3_monthly_donation_trends.svg
│   ├── chart6_donor_eligibility_breakdown.svg
│   └── dashboard.html                         # Interactive Standalone HTML Dashboard
└── sample_outputs/                            # Execution Logs and Sample Runs
    ├── sample_inputs_and_outputs.md           # Documented Input/Output Walkthroughs
    └── terminal_execution_log.txt             # Captured Real Terminal Execution Log
```

---

## 🚀 Execution Instructions

### Prerequisites
- **Java:** JDK 17 or higher (tested with JDK 26).
- **Python:** Python 3.10 or higher.
- **Git:** Standard git client.

---

### 1. Database Setup
The SQLite database `database/blood_bank.db` is already pre-initialized with all tables, views, and benchmark data.

To re-initialize or regenerate the database from scratch:
```powershell
# From the project root directory
python -c "
import sqlite3
conn = sqlite3.connect('database/blood_bank.db')
with open('database/schema_sqlite.sql') as f: conn.executescript(f.read())
with open('database/sample_data.sql') as f: conn.executescript(f.read())
conn.close()
print('Database successfully re-initialized!')
"
```

*For MySQL users:* Import `database/schema_mysql.sql` followed by `database/sample_data.sql` into your MySQL instance.

---

### 2. Java Console Application

#### A. Compile the Java Source Code:
```powershell
javac -d java/bin -sourcepath java/src (Get-ChildItem -Path java/src -Filter *.java -Recurse | Select-Object -ExpandProperty FullName)
```
*(On Linux/macOS: `javac -d java/bin -sourcepath java/src $(find java/src -name "*.java")`)*

#### B. Run the Interactive Menu Application:
```powershell
java -cp java/bin com.bloodbank.Main
```

#### Menu Options Available:
- `[1]` **Register New Voluntary Donor:** Validates name, age (18-65), phone (10 digits), blood group, and email.
- `[2]` **Record Blood Donation:** Automatically checks the **90-day cooldown period**; if eligible, records donation and increments stock.
- `[3]` **View Blood Stock Inventory:** Displays stock status (`ADEQUATE` vs `DEFICIT`) and triggers low-stock alerts.
- `[4]` **Hospital Blood Requisitions:** Submit requests, check available inventory, and issue blood units.
- `[5]` **Donor Availability Audit:** Filters immediately available donors who meet the 90-day interval for emergency mobilization.
- `[6]` **Analytical Management Reports:** Generates tabular reports using Java Streams.
- `[7]` **Trigger Python Visualizations Pipeline:** Spawns the data science engine directly from Java.
- `[8]` **System Architecture & Metadata:** Displays academic accreditation and schema status.
- `[0]` **Exit.**

---

### 3. Python Data Science & Visualizations Pipeline

#### Run the Automated Data Science Pipeline:
```powershell
python python/main_analysis.py
```

This single command executes:
1. `db_retrieval.py`: Pulls data from `blood_bank.db` and exports CSV copies into `database/extracted_csv/`.
2. `data_preprocessing.py`: Cleans records, handles missing fields, and computes `days_since_last_donation` and `is_eligible`.
3. `visualizations.py`: Generates publication-ready charts in `visualizations/` and creates an interactive `visualizations/dashboard.html`.

#### Interactive Jupyter Notebook:
To launch the Jupyter Notebook for interactive exploration:
```powershell
jupyter notebook python/analysis_notebook.ipynb
```

---

### 4. Interactive 24/7 Live Website

#### Option A: Access Live on the Web (GitHub Pages)
The web application is hosted live 24/7 with zero installation:
👉 **[https://karanraajaa17jan2009-eng.github.io/Blood-Donation-Management-System/](https://karanraajaa17jan2009-eng.github.io/Blood-Donation-Management-System/)**

#### Option B: Run the Website Locally (One-Click)
Double-click **`run_website.bat`** in the project folder, or run:
```powershell
.\.venv\Scripts\python.exe -m http.server 8000
```
Then open `http://localhost:8000` in your browser.
jupyter notebook python/analysis_notebook.ipynb
```

---

## 📊 Visualizations and Analytics Dashboard

The Python visualization module generates the following analytical charts:

| Chart File | Visualization Description | Key Finding |
|---|---|---|
| `chart1_blood_stock_availability.svg` | Bar chart of Available Units vs Safety Threshold across 8 groups | Identified critical deficits in `AB-`, `B-`, and `O-` groups |
| `chart2_donor_blood_group_distribution.svg` | Donut chart of Registered Donors by Blood Group | `O+` (27.8%) and `A+` (22.2%) form the largest donor proportions |
| `chart3_monthly_donation_trends.svg` | Time-series trend of blood donation collections (2026) | Steady upward trend with donation peak during summer drives |
| `chart6_donor_eligibility_breakdown.svg` | Cooldown compliance breakdown (90-day interval) | 50.0% of registered donors are currently eligible to donate |
| `dashboard.html` | Unified responsive HTML analytics dashboard | Integrates all charts into a single viewable dashboard |

> **View the Dashboard:** Open [visualizations/dashboard.html](file:///e:/Assingment_1/visualizations/dashboard.html) in any browser to inspect the complete visual analytics suite.

---

## 🧪 Testing and Verification Summary

- **Total Test Cases Executed:** 12
- **Passed:** 12 (100% Pass Rate)
- **Failed:** 0
- **Techniques Applied:**
  - *Black-Box:* Boundary Value Analysis (BVA on age 18-65 and 90-day cooldown interval) & Equivalence Class Partitioning (ECP).
  - *White-Box:* Cyclomatic Complexity ($V(G) = 3$) and Basis Path Coverage for `DonorEligibilityService`.
  - *Integration:* Multi-table transactions between `donations`, `donors`, and `blood_stock`.

Detailed test specifications and execution logs are available in [Testing_Document_and_Test_Cases.md](file:///e:/Assingment_1/docs/Testing_Document_and_Test_Cases.md).

---

## 📄 Documentation Links

- 📘 [Software Requirements Specification (SRS Document)](file:///e:/Assingment_1/docs/SRS_Document.md)
- 📐 [Architecture, Use Case, and Class Diagrams](file:///e:/Assingment_1/docs/Architecture_and_Design_Diagrams.md)
- 🗄️ [Database Design, Relational Model & Normalization](file:///e:/Assingment_1/docs/Database_Design_and_Normalization.md)
- 🧪 [Testing Techniques and Test Cases Documentation](file:///e:/Assingment_1/docs/Testing_Document_and_Test_Cases.md)
- 💻 [Sample Inputs and Terminal Execution Walkthrough](file:///e:/Assingment_1/sample_outputs/sample_inputs_and_outputs.md)

---

## 👨‍🎓 Author & Submission Note

- **Student:** Karan Raajaa V
- **Register Number:** 732925ITR045
- **Degree / Branch:** B.Tech. Information Technology
- **College:** Velalar College of Engineering and Technology, Erode - 638012
- **Assessment:** Project-Based Assessment (Academic Year 2026-2027 ODD)
- **GitHub Repository Ready:** All required deliverables (SRS, Diagrams, Java source code, SQL scripts, Python analytics, Jupyter notebook, and Sample outputs) are organized and tested.

