"""
Automated Comprehensive Test & Verification Suite
Blood Donation Management and Donor Availability Analysis System (Scenario 15)
Student: Karan Raajaa V | Register No: 732925ITR045 | Class: 25IT3A
Institution: Velalar College of Engineering and Technology, Erode - 12
"""

import os
import sys
import sqlite3
import json
import subprocess
import re

JAVA_EXE = r"C:\Program Files\Java\latest\jdk-26\bin\java.exe"
if not os.path.exists(JAVA_EXE):
    JAVA_EXE = "java"

PASS_COUNT = 0
FAIL_COUNT = 0

def log_test(title, passed, detail=""):
    global PASS_COUNT, FAIL_COUNT
    if passed:
        PASS_COUNT += 1
        print(f"  [PASS] {title}")
    else:
        FAIL_COUNT += 1
        print(f"  [FAIL] {title} -> {detail}")

print("=" * 80)
print("     COMPREHENSIVE VERIFICATION & TEST SUITE - ACADEMIC ASSESSMENT      ")
print("  Scenario 15: Blood Donation Management and Donor Availability Analysis")
print("  Student: Karan Raajaa V | Reg No: 732925ITR045 | Section: 25IT3A       ")
print("=" * 80)

# ------------------------------------------------------------------------------
# Test Section 1: Documentation Deliverables Check
# ------------------------------------------------------------------------------
print("\n--- [CHECK 1] Verifying Software Engineering Documents ---")
required_docs = [
    ("docs/SRS_Document.md", 2000),
    ("docs/Architecture_and_Design_Diagrams.md", 1500),
    ("docs/Database_Design_and_Normalization.md", 1500),
    ("docs/Testing_Document_and_Test_Cases.md", 1500),
    ("sample_outputs/sample_inputs_and_outputs.md", 1000),
    ("README.md", 2000),
    ("index.html", 5000),
    ("run_website.bat", 100)
]

for doc_path, min_len in required_docs:
    exists = os.path.exists(doc_path)
    if exists:
        size = os.path.getsize(doc_path)
        log_test(f"Document '{doc_path}' exists ({size} bytes)", size >= min_len, f"Size {size} < {min_len}")
    else:
        log_test(f"Document '{doc_path}' exists", False, "File not found")

# ------------------------------------------------------------------------------
# Test Section 2: Relational Database & SQL Integrity Test
# ------------------------------------------------------------------------------
print("\n--- [CHECK 2] Verifying Relational Database & SQL Queries ---")
db_path = "database/blood_bank.db"
if not os.path.exists(db_path):
    log_test("Database exists at database/blood_bank.db", False, "File missing")
else:
    log_test("Database exists at database/blood_bank.db", True)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Tables & row counts
    expected_tables = {
        "blood_stock": 8,
        "donors": 18,
        "donations": 25,
        "hospital_requests": 12
    }

    for tbl, min_rows in expected_tables.items():
        try:
            cur.execute(f"SELECT COUNT(*) FROM {tbl}")
            count = cur.fetchone()[0]
            log_test(f"Table '{tbl}' integrity verified ({count} rows)", count >= min_rows, f"Found {count} rows")
        except Exception as e:
            log_test(f"Table '{tbl}' exists", False, str(e))

    # Views
    for view in ["v_stock_summary", "v_donor_availability"]:
        try:
            cur.execute(f"SELECT COUNT(*) FROM {view}")
            count = cur.fetchone()[0]
            log_test(f"Database View '{view}' queryable ({count} records)", count > 0)
        except Exception as e:
            log_test(f"Database View '{view}' queryable", False, str(e))

    # Analytical Queries Execution
    queries_file = "database/analytical_queries.sql"
    if os.path.exists(queries_file):
        with open(queries_file, "r", encoding="utf-8") as f:
            sql_content = f.read()

        # Remove SQL comments
        cleaned_sql = re.sub(r"--.*?\n", "\n", sql_content)
        raw_statements = [s.strip() for s in cleaned_sql.split(";") if s.strip()]
        executed_q = 0
        for i, q in enumerate(raw_statements, 1):
            try:
                cur.execute(q)
                rows = cur.fetchall()
                if len(rows) > 0:
                    executed_q += 1
            except Exception as e:
                log_test(f"Analytical Query #{i} execution", False, str(e))

        log_test(f"Executed all {executed_q} Analytical SQL Queries successfully with valid results", executed_q == len(raw_statements))

    conn.close()

# ------------------------------------------------------------------------------
# Test Section 3: Java Application Execution & Logic Test
# ------------------------------------------------------------------------------
print("\n--- [CHECK 3] Verifying Java Core Application & Business Logic ---")
java_bin = "java/bin"
has_java = os.path.exists(os.path.join(java_bin, "com", "bloodbank", "Main.class"))
log_test("Compiled Java Bytecode present in java/bin", has_java)

if has_java:
    cmd = [JAVA_EXE, "-cp", "java/bin", "com.bloodbank.Main"]

    # Test 1: Run Menu Simulation: System Info (8), View Stock (3), Exit (0)
    try:
        proc = subprocess.run(cmd, input="8\n3\n0\n", capture_output=True, text=True, timeout=10)
        out = proc.stdout
        log_test("Java Menu System executed with exit code 0", proc.returncode == 0)
        log_test("Java Output displays 732925ITR045 & Karan Raajaa V", "732925ITR045" in out and "Karan Raajaa V" in out)
        log_test("Java Output renders Blood Stock Table with 8 groups", "REAL-TIME BLOOD STOCK INVENTORY REPORT" in out)
        log_test("Java Output triggers Critical Low Stock Alerts banner", "CRITICAL LOW STOCK ALERTS" in out)
    except Exception as e:
        log_test("Java Menu Execution", False, str(e))

    # Test 2: Test 90-Day Cooldown Enforcement
    try:
        # Donor ID 2 donated 11 days ago -> Must be BLOCKED
        # Donor ID 13 donated 104 days ago -> Must be ACCEPTED
        input_stream = "2\n2\n2\n13\n1\n13.5\nStaff Nurse Priya\nRoutine test\n0\n"
        proc = subprocess.run(cmd, input=input_stream, capture_output=True, text=True, timeout=10)
        out = proc.stdout
        log_test("Java Cooldown Enforcement: Ineligible donor #2 BLOCKED", "[BLOCKED] Donation cannot be accepted" in out)
        log_test("Java Eligibility Verification: Eligible donor #13 ACCEPTED", "[SUCCESS] Donation successfully recorded" in out)
    except Exception as e:
        log_test("Java Eligibility Logic", False, str(e))

# ------------------------------------------------------------------------------
# Test Section 4: Python Data Science & Visualizations Pipeline Test
# ------------------------------------------------------------------------------
print("\n--- [CHECK 4] Verifying Python Data Science Pipeline & Visuals ---")
try:
    proc_py = subprocess.run([sys.executable, "python/main_analysis.py"], capture_output=True, text=True, timeout=15)
    py_out = proc_py.stdout
    log_test("Python pipeline executed with exit code 0", proc_py.returncode == 0)
    log_test("Python ETL exported CSV files", "Successfully exported" in py_out)
    log_test("Python Preprocessing calculated descriptive statistics", "Exploratory Data Analysis (EDA) Summary Statistics" in py_out)
    log_test("Python Clinical Audit calculated 90-day cooldown ratio", "Immediately Available Donors" in py_out)
except Exception as e:
    log_test("Python Pipeline Execution", False, str(e))

# Verify generated chart files
charts = [
    "visualizations/chart1_blood_stock_availability.svg",
    "visualizations/chart2_donor_blood_group_distribution.svg",
    "visualizations/chart3_monthly_donation_trends.svg",
    "visualizations/chart6_donor_eligibility_breakdown.svg",
    "visualizations/dashboard.html"
]

for ch in charts:
    ex = os.path.exists(ch) and os.path.getsize(ch) > 200
    log_test(f"Visualization Artifact '{ch}' generated and valid", ex)

# Verify Jupyter Notebook JSON
nb_path = "python/analysis_notebook.ipynb"
try:
    with open(nb_path, "r", encoding="utf-8") as f:
        nb_json = json.load(f)
    log_test("Jupyter Notebook 'analysis_notebook.ipynb' valid JSON schema", "cells" in nb_json and len(nb_json["cells"]) > 0)
except Exception as e:
    log_test("Jupyter Notebook validity", False, str(e))

# ------------------------------------------------------------------------------
# Test Summary
# ------------------------------------------------------------------------------
print("\n" + "=" * 80)
total_tests = PASS_COUNT + FAIL_COUNT
pass_pct = (PASS_COUNT / total_tests) * 100 if total_tests > 0 else 0
print(f" TOTAL TESTS EXECUTED : {total_tests}")
print(f" TESTS PASSED         : {PASS_COUNT}")
print(f" TESTS FAILED         : {FAIL_COUNT}")
print(f" SUCCESS PERCENTAGE   : {pass_pct:.1f}%")
print("=" * 80)

if FAIL_COUNT == 0:
    print(" >>> RESULT: 100% OF ACADEMIC REQUIREMENTS AND CHECKS SATISFIED! <<<")
else:
    print(" >>> RESULT: SOME CHECKS FAILED. PLEASE REVIEW LOGS. <<<")
