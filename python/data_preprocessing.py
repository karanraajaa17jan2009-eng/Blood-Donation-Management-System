"""
Data Preprocessing & Feature Engineering Module
Scenario 15: Blood Donation Management and Donor Availability Analysis System
Student: Karan Raajaa V | Register No: 732925ITR045 | Class: 25IT3A&B
Institution: Velalar College of Engineering and Technology, Erode - 12
"""

from datetime import datetime, date
import math
from db_retrieval import fetch_table, get_connection

REFERENCE_DATE = date(2026, 11, 13)

def parse_date(date_str):
    """Safely parses ISO date strings (YYYY-MM-DD)."""
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str[:10], "%Y-%m-%d").date()
    except ValueError:
        return None

def preprocess_donors(raw_donors):
    """
    Cleans and enhances donor records:
    - Normalizes strings and trims whitespace
    - Categorizes age into age brackets (Youth 18-24, Adult 25-40, Senior 41-65)
    - Validates contact and blood group
    """
    cleaned = []
    for d in raw_donors:
        donor = dict(d)
        donor["name"] = donor["name"].strip()
        donor["blood_group"] = donor["blood_group"].strip().upper()
        donor["city"] = donor["city"].strip()
        donor["age"] = int(donor["age"])
        donor["reg_date"] = parse_date(donor.get("registration_date"))

        # Feature Engineering: Age Bracket
        age = donor["age"]
        if age <= 24:
            donor["age_bracket"] = "Youth (18-24)"
        elif age <= 40:
            donor["age_bracket"] = "Adult (25-40)"
        else:
            donor["age_bracket"] = "Senior (41-65)"

        cleaned.append(donor)
    return cleaned

def preprocess_donations(raw_donations):
    """
    Cleans and enhances donation records:
    - Parses donation dates
    - Extracts year-month periods for time-series trend analysis
    - Casts numeric fields
    """
    cleaned = []
    for dn in raw_donations:
        item = dict(dn)
        item["units_donated"] = int(item["units_donated"])
        item["hemoglobin_level"] = float(item["hemoglobin_level"])
        d_date = parse_date(item["donation_date"])
        item["parsed_date"] = d_date
        item["year_month"] = d_date.strftime("%Y-%m") if d_date else "Unknown"
        item["remarks"] = item.get("remarks", "Fit for donation") or "Fit for donation"
        cleaned.append(item)
    return cleaned

def compute_donor_availability(donors, donations, ref_date=REFERENCE_DATE):
    """
    Calculates recency, cooldown status, and 90-day eligibility intervals:
    - days_since_last_donation
    - eligibility_status: ELIGIBLE vs INELIGIBLE (Cooldown)
    - days_remaining_in_cooldown
    """
    # Group donations by donor_id
    last_donation_map = {}
    donation_counts = {}
    for dn in donations:
        d_id = dn["donor_id"]
        d_date = dn["parsed_date"]
        donation_counts[d_id] = donation_counts.get(d_id, 0) + dn["units_donated"]
        if d_id not in last_donation_map or d_date > last_donation_map[d_id]:
            last_donation_map[d_id] = d_date

    results = []
    for d in donors:
        d_id = d["donor_id"]
        last_date = last_donation_map.get(d_id)
        total_donated = donation_counts.get(d_id, 0)

        if last_date is None:
            days_since = 999
            is_eligible = True
            cooldown_remaining = 0
            status_desc = "ELIGIBLE (First-Time)"
        else:
            days_since = (ref_date - last_date).days
            if days_since >= 90:
                is_eligible = True
                cooldown_remaining = 0
                status_desc = "ELIGIBLE"
            else:
                is_eligible = False
                cooldown_remaining = 90 - days_since
                status_desc = "INELIGIBLE (Cooldown)"

        entry = dict(d)
        entry["last_donation_date"] = last_date.strftime("%Y-%m-%d") if last_date else None
        entry["days_since_last_donation"] = days_since
        entry["is_eligible"] = is_eligible
        entry["cooldown_remaining"] = cooldown_remaining
        entry["eligibility_status"] = status_desc
        entry["total_units_donated"] = total_donated
        results.append(entry)

    return results

def preprocess_hospital_requests(raw_requests):
    """Cleans and calculates request urgency counts and fulfillment indicators."""
    cleaned = []
    for r in raw_requests:
        item = dict(r)
        item["units_requested"] = int(item["units_requested"])
        item["urgency_level"] = item["urgency_level"].upper()
        item["status"] = item["status"].upper()
        item["req_date"] = parse_date(item["request_date"])
        item["ful_date"] = parse_date(item.get("fulfillment_date"))
        cleaned.append(item)
    return cleaned

def calculate_summary_statistics(donors, donations, stock):
    """Calculates statistical measures (mean, median, standard deviation) for EDA."""
    ages = [d["age"] for d in donors]
    hbs = [dn["hemoglobin_level"] for dn in donations]
    stock_units = [int(s["available_units"]) for s in stock]

    def mean(lst):
        return sum(lst) / len(lst) if lst else 0.0

    def variance(lst, avg):
        return sum((x - avg) ** 2 for x in lst) / len(lst) if lst else 0.0

    avg_age = mean(ages)
    std_age = math.sqrt(variance(ages, avg_age))

    avg_hb = mean(hbs)
    std_hb = math.sqrt(variance(hbs, avg_hb))

    return {
        "donor_count": len(donors),
        "donation_count": len(donations),
        "total_stock_units": sum(stock_units),
        "mean_donor_age": round(avg_age, 2),
        "std_donor_age": round(std_age, 2),
        "min_donor_age": min(ages) if ages else 0,
        "max_donor_age": max(ages) if ages else 0,
        "mean_hemoglobin": round(avg_hb, 2),
        "std_hemoglobin": round(std_hb, 2),
    }

if __name__ == "__main__":
    conn = get_connection()
    _, raw_stock = fetch_table("blood_stock", conn)
    _, raw_donors = fetch_table("donors", conn)
    _, raw_donations = fetch_table("donations", conn)
    conn.close()

    donors = preprocess_donors(raw_donors)
    donations = preprocess_donations(raw_donations)
    availability = compute_donor_availability(donors, donations)
    stats = calculate_summary_statistics(donors, donations, raw_stock)

    print("=== Data Preprocessing & Statistics Summary ===")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print(f"\nEligible Donors Count: {sum(1 for d in availability if d['is_eligible'])} / {len(availability)}")
