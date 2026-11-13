"""
Database Retrieval Module
Scenario 15: Blood Donation Management and Donor Availability Analysis System
Student: Karan Raajaa V | Register No: 732925ITR045 | Class: 25IT3A&B
Institution: Velalar College of Engineering and Technology, Erode - 12
"""

import sqlite3
import os
import csv

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "blood_bank.db")
OUTPUT_CSV_DIR = os.path.join(os.path.dirname(__file__), "..", "database", "extracted_csv")

def get_connection(db_path=DB_PATH):
    """Establishes connection to the SQLite database."""
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database file not found at: {db_path}")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def fetch_table(table_name, conn=None):
    """Fetches all rows and column names from a given table or view."""
    close_after = False
    if conn is None:
        conn = get_connection()
        close_after = True

    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        data = [dict(row) for row in rows]
        return columns, data
    finally:
        if close_after:
            conn.close()

def export_to_csv():
    """Exports all core tables to CSV files for cross-platform data processing."""
    os.makedirs(OUTPUT_CSV_DIR, exist_ok=True)
    conn = get_connection()
    tables = ["blood_stock", "donors", "donations", "hospital_requests", "v_stock_summary", "v_donor_availability"]

    exported = {}
    for table in tables:
        columns, data = fetch_table(table, conn)
        csv_file = os.path.join(OUTPUT_CSV_DIR, f"{table}.csv")
        with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            writer.writerows(data)
        exported[table] = len(data)
        print(f"[ETL Export] Successfully exported {len(data)} records from '{table}' to {csv_file}")

    conn.close()
    return exported

if __name__ == "__main__":
    print("=== Blood Bank Database Retrieval & Extraction ===")
    results = export_to_csv()
    print("ETL Data Extraction Complete:", results)
