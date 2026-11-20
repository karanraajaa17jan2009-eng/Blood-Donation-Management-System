"""
Interactive SQL Query Runner & Table Viewer
Scenario 15: Blood Donation Management and Donor Availability Analysis System
Student: Karan Raajaa V | Register No: 732925ITR045 | Class: 25IT3A
Institution: Velalar College of Engineering and Technology, Erode - 12
"""

import os
import sys
import sqlite3

DB_PATH = os.path.join("database", "blood_bank.db")
SQL_FILE = os.path.join("database", "analytical_queries.sql")

QUERIES = [
    {
        "id": 1,
        "title": "Real-time Blood Stock Inventory Status vs Minimum Threshold",
        "concept": "Categorical CASE expressions, arithmetic surplus/deficit, conditional ordering",
        "sql": """
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
        """.strip()
    },
    {
        "id": 2,
        "title": "Available Donors Meeting 90-Day Medical Eligibility Interval",
        "concept": "LEFT JOIN, MAX(donation_date), Date functions (JULIANDAY), HAVING filter",
        "sql": """
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
        """.strip()
    },
    {
        "id": 3,
        "title": "Blood Group-Wise Total Donations and Volume Aggregation",
        "concept": "LEFT JOIN, Aggregate functions (COUNT, SUM, AVG, ROUND), GROUP BY",
        "sql": """
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
        """.strip()
    },
    {
        "id": 4,
        "title": "Monthly Blood Donation Trends (Temporal Analysis)",
        "concept": "Date string slicing via STRFTIME('%Y-%m'), monthly volume tracking",
        "sql": """
SELECT 
    STRFTIME('%Y-%m', donation_date) AS donation_month,
    COUNT(donation_id) AS total_donations,
    SUM(units_donated) AS total_units_collected,
    COUNT(DISTINCT donor_id) AS unique_active_donors
FROM donations
GROUP BY donation_month
ORDER BY donation_month ASC;
        """.strip()
    },
    {
        "id": 5,
        "title": "Hospital Requisition Fulfillment Analysis by Urgency Level",
        "concept": "Conditional aggregation (SUM with CASE expressions), fulfillment rate percentage",
        "sql": """
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
        """.strip()
    },
    {
        "id": 6,
        "title": "Top Frequent Voluntary Donors (Ranking & Multi-Session Donors)",
        "concept": "INNER JOIN, GROUP BY with HAVING frequency >= 2, multi-column sorting",
        "sql": """
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
        """.strip()
    },
    {
        "id": 7,
        "title": "Registered Donors Who Have Never Donated (Zero Donation Audit)",
        "concept": "Outer Join with IS NULL predicate (Anti-Join Pattern)",
        "sql": """
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
        """.strip()
    },
    {
        "id": 8,
        "title": "Emergency Response Matching: Finding Eligible Donors for Pending Requests",
        "concept": "Multi-table JOIN, correlated subqueries, 90-day cooldown filter",
        "sql": """
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
        """.strip()
    }
]

def print_table(columns, rows):
    """Prints a clean ASCII/Unicode formatted table with borders."""
    if not columns:
        print("  [Empty result set]")
        return

    # Calculate column widths
    widths = [len(str(col)) for col in columns]
    for row in rows:
        for i, val in enumerate(row):
            val_str = str(val) if val is not None else "NULL"
            if len(val_str) > widths[i]:
                widths[i] = len(val_str)

    # Pad widths slightly
    widths = [w + 2 for w in widths]

    # Separator lines
    sep_top = "+" + "+".join("-" * w for w in widths) + "+"
    sep_mid = "+" + "+".join("=" * w for w in widths) + "+"
    sep_bot = "+" + "+".join("-" * w for w in widths) + "+"

    print(sep_top)
    # Header
    header_row = "|" + "|".join(f" {str(col).center(widths[i]-2)} " for i, col in enumerate(columns)) + "|"
    print(header_row)
    print(sep_mid)

    # Data rows
    if not rows:
        no_data = "| " + "No records found".center(sum(widths) + len(widths) - 3) + " |"
        print(no_data)
    else:
        for row in rows:
            row_str = "|"
            for i, val in enumerate(row):
                val_s = str(val) if val is not None else "NULL"
                # Align numbers right, text left
                if isinstance(val, (int, float)):
                    row_str += f" {val_s.rjust(widths[i]-2)} |"
                else:
                    row_str += f" {val_s.ljust(widths[i]-2)} |"
            print(row_str)

    print(sep_bot)
    print(f"  Rows returned: {len(rows)}\n")

def execute_query(conn, query_info):
    """Executes a single query and displays formatted output."""
    cur = conn.cursor()
    print("=" * 95)
    print(f"  [QUERY {query_info['id']}] {query_info['title']}")
    print(f"  Concept: {query_info['concept']}")
    print("=" * 95)
    print("SQL Query:")
    for line in query_info['sql'].split("\n"):
        print(f"  {line}")
    print("-" * 95)

    try:
        cur.execute(query_info['sql'])
        columns = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        print("Query Results Table:")
        print_table(columns, rows)
    except Exception as e:
        print(f"  [ERROR] Execution failed: {e}\n")

def execute_custom_query(conn, sql):
    """Executes an ad-hoc SQL query entered by the user."""
    cur = conn.cursor()
    print("\n" + "=" * 95)
    print(f"  EXECUTING CUSTOM SQL QUERY")
    print("=" * 95)
    try:
        cur.execute(sql)
        if cur.description:
            columns = [desc[0] for desc in cur.description]
            rows = cur.fetchall()
            print("Results Table:")
            print_table(columns, rows)
        else:
            conn.commit()
            print(f"  Statement executed successfully. Rows affected: {cur.rowcount}\n")
    except Exception as e:
        print(f"  [ERROR] Execution failed: {e}\n")

def main():
    if not os.path.exists(DB_PATH):
        print(f"[ERROR] Database file not found at: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)

    # Check CLI arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1].strip()
        if arg.lower() in ("all", "run-all", "a"):
            print("\n" + "#" * 95)
            print("   EXECUTING ALL 8 ANALYTICAL SQL QUERIES (SCENARIO 15: BLOOD BANK SYSTEM)")
            print("   Student: Karan Raajaa V | Reg No: 732925ITR045 | Class: 25IT3A")
            print("#" * 95 + "\n")
            for q in QUERIES:
                execute_query(conn, q)
            conn.close()
            return
        elif arg.isdigit() and 1 <= int(arg) <= 8:
            q_num = int(arg)
            execute_query(conn, QUERIES[q_num - 1])
            conn.close()
            return

    # Interactive Menu
    while True:
        print("\n" + "=" * 80)
        print("    BLOOD DONATION MANAGEMENT SYSTEM - SQL QUERY & TABLE VIEWER     ")
        print("    Scenario 15 | Course: 25ITT31 DBMS | Database: database/blood_bank.db")
        print("    Student: Karan Raajaa V (732925ITR045) | Class: 25IT3A | VCET Erode")
        print("=" * 80)
        for q in QUERIES:
            print(f"  [{q['id']}] {q['title']}")
        print("  ----------------------------------------------------------------------")
        print("  [9] Run ALL 8 Analytical Queries Sequentially")
        print("  [C] Custom SQL Query Runner (Type any SELECT query)")
        print("  [T] View List of Tables and Row Counts in Database")
        print("  [0] Exit")
        print("=" * 80)

        choice = input("Enter choice (0-9, C, T): ").strip()

        if choice == "0":
            print("\nExiting SQL Runner. Thank you!")
            break
        elif choice == "9":
            for q in QUERIES:
                execute_query(conn, q)
        elif choice in ("c", "C"):
            print("\nEnter custom SQL query (terminate with semicolon ';'):")
            custom_sql = input("SQL > ").strip()
            if custom_sql:
                execute_custom_query(conn, custom_sql)
        elif choice in ("t", "T"):
            print("\nDatabase Tables Summary:")
            cur = conn.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type IN ('table', 'view') AND name NOT LIKE 'sqlite_%';")
            items = cur.fetchall()
            summary_cols = ["Type", "Name", "Row Count"]
            summary_rows = []
            for item in items:
                name = item[0]
                cur.execute(f"SELECT COUNT(*) FROM \"{name}\"")
                cnt = cur.fetchone()[0]
                t_type = "VIEW" if name.startswith("v_") else "TABLE"
                summary_rows.append([t_type, name, cnt])
            print_table(summary_cols, summary_rows)
        elif choice.isdigit() and 1 <= int(choice) <= 8:
            execute_query(conn, QUERIES[int(choice) - 1])
        else:
            print("\n[!] Invalid selection. Please enter a number between 0 and 9, C, or T.")

    conn.close()

if __name__ == "__main__":
    main()
