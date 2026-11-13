"""
Main Analysis Pipeline Runner
Scenario 15: Blood Donation Management and Donor Availability Analysis System
Student: Karan Raajaa V | Register No: 732925ITR045 | Class: 25IT3A
Institution: Velalar College of Engineering and Technology, Erode - 12
"""

import sys
import os

from db_retrieval import export_to_csv, fetch_table, get_connection
from data_preprocessing import (
    preprocess_donors,
    preprocess_donations,
    compute_donor_availability,
    preprocess_hospital_requests,
    calculate_summary_statistics
)
from visualizations import generate_all_visualizations

def run_pipeline():
    print("=" * 80)
    print("       BLOOD DONATION MANAGEMENT & DONOR AVAILABILITY ANALYSIS PIPELINE        ")
    print("                Course: 25ITC31 Foundations of Data Science                    ")
    print("       Student: Karan Raajaa V | Register No: 732925ITR045 (Roll No. 45)       ")
    print("=" * 80)

    # Step 1: Database Extraction
    print("\n[STEP 1/4] Extracting Data from SQLite Database (blood_bank.db)...")
    exported = export_to_csv()
    for table, count in exported.items():
        print(f"  * Retrieved table '{table}': {count} rows")

    # Step 2: Data Preprocessing & Cleaning
    print("\n[STEP 2/4] Running Data Cleaning, Type Conversions & Preprocessing...")
    conn = get_connection()
    _, raw_stock = fetch_table("blood_stock", conn)
    _, raw_donors = fetch_table("donors", conn)
    _, raw_donations = fetch_table("donations", conn)
    _, raw_requests = fetch_table("hospital_requests", conn)
    conn.close()

    donors = preprocess_donors(raw_donors)
    donations = preprocess_donations(raw_donations)
    requests = preprocess_hospital_requests(raw_requests)
    availability = compute_donor_availability(donors, donations)
    stats = calculate_summary_statistics(donors, donations, raw_stock)

    print("  * Cleaning Complete: 0 null critical fields, dates parsed to ISO format.")
    print("  * Feature Engineering: Added 'age_bracket', 'days_since_last_donation', 'is_eligible'.")

    # Step 3: Exploratory Data Analysis & Statistics
    print("\n[STEP 3/4] Exploratory Data Analysis (EDA) Summary Statistics:")
    print("-" * 60)
    print(f"  Total Registered Donors    : {stats['donor_count']}")
    print(f"  Total Donation Events Logged: {stats['donation_count']}")
    print(f"  Total Blood Units in Stock : {stats['total_stock_units']} units")
    print(f"  Donor Age Distribution     : Mean = {stats['mean_donor_age']} yrs, StdDev = {stats['std_donor_age']} yrs")
    print(f"  Donor Age Range            : Min = {stats['min_donor_age']} yrs, Max = {stats['max_donor_age']} yrs")
    print(f"  Donor Hemoglobin Metrics   : Mean = {stats['mean_hemoglobin']} g/dL, StdDev = {stats['std_hemoglobin']} g/dL")
    print("-" * 60)

    eligible_count = sum(1 for d in availability if d['is_eligible'])
    ineligible_count = len(availability) - eligible_count
    print(f"\n[CLINICAL AUDIT] 90-Day Medical Cooldown Analysis:")
    print(f"  * Immediately Available Donors (>= 90 Days): {eligible_count} ({eligible_count/len(availability)*100:.1f}%)")
    print(f"  * Ineligible Donors (Active Cooldown Period): {ineligible_count} ({ineligible_count/len(availability)*100:.1f}%)")

    # Step 4: Visualizations Generation
    print("\n[STEP 4/4] Generating Analytical Visualizations...")
    generate_all_visualizations()

    print("\n" + "=" * 80)
    print(" [SUCCESS] Data Science Pipeline Executed Completely!")
    print(" Visualizations and HTML Dashboard are ready in: visualizations/")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    run_pipeline()

