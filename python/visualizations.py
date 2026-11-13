"""
Data Visualization Engine
Scenario 15: Blood Donation Management and Donor Availability Analysis System
Student: Karan Raajaa V | Register No: 732925ITR045 | Class: 25IT3A&B
Institution: Velalar College of Engineering and Technology, Erode - 12
"""

import os
import math
from collections import Counter
from db_retrieval import fetch_table, get_connection
from data_preprocessing import (
    preprocess_donors,
    preprocess_donations,
    compute_donor_availability,
    preprocess_hospital_requests
)

VIZ_DIR = os.path.join(os.path.dirname(__file__), "..", "visualizations")

# Check if matplotlib / seaborn is installed
try:
    import matplotlib
    matplotlib.use("Agg") # Non-interactive headless backend
    import matplotlib.pyplot as plt
    import seaborn as sns
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

def ensure_viz_dir():
    os.makedirs(VIZ_DIR, exist_ok=True)

# ==============================================================================
# Matplotlib / Seaborn Visualizations Engine
# ==============================================================================

def generate_matplotlib_charts(stock_data, donors_data, donations_data, requests_data, availability_data):
    """Generates high-resolution PNG charts using Matplotlib and Seaborn."""
    print("[Visualization Engine] Using Matplotlib & Seaborn...")
    sns.set_theme(style="whitegrid", palette="muted")

    # Chart 1: Blood Stock vs Minimum Threshold
    fig, ax = plt.subplots(figsize=(10, 6))
    groups = [s["blood_group"] for s in stock_data]
    units = [int(s["available_units"]) for s in stock_data]
    thresholds = [int(s["minimum_threshold"]) for s in stock_data]
    colors = ["#2ecc71" if u >= t else "#e74c3c" for u, t in zip(units, thresholds)]

    bars = ax.bar(groups, units, color=colors, edgecolor="black", linewidth=1.2, label="Available Units")
    ax.plot(groups, thresholds, color="#d35400", marker="o", linestyle="--", linewidth=2.5, label="Min Safety Threshold")

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.5, str(int(yval)), ha="center", va="bottom", fontweight="bold")

    ax.set_title("Blood Stock Availability vs Safety Threshold by Blood Group", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Blood Group", fontsize=12, labelpad=10)
    ax.set_ylabel("Blood Units", fontsize=12, labelpad=10)
    ax.legend(loc="upper right", frameon=True)
    plt.tight_layout()
    chart1_path = os.path.join(VIZ_DIR, "chart1_blood_stock_availability.png")
    plt.savefig(chart1_path, dpi=300)
    plt.close()
    print("  -> Saved:", chart1_path)

    # Chart 2: Donor Blood Group Distribution (Donut Chart)
    fig, ax = plt.subplots(figsize=(8, 8))
    bg_counts = Counter(d["blood_group"] for d in donors_data)
    labels = list(bg_counts.keys())
    sizes = list(bg_counts.values())
    palette = sns.color_palette("Set2", len(labels))

    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140,
                                      colors=palette, textprops=dict(color="black", fontweight="bold"),
                                      wedgeprops=dict(width=0.45, edgecolor="white", linewidth=2))
    ax.set_title("Registered Donor Distribution by Blood Group", fontsize=14, fontweight="bold", pad=20)
    plt.tight_layout()
    chart2_path = os.path.join(VIZ_DIR, "chart2_donor_blood_group_distribution.png")
    plt.savefig(chart2_path, dpi=300)
    plt.close()
    print("  -> Saved:", chart2_path)

    # Chart 3: Monthly Donation Collection Trends (Line Chart)
    fig, ax = plt.subplots(figsize=(10, 5))
    month_counts = Counter(d["year_month"] for d in donations_data if d["year_month"] != "Unknown")
    sorted_months = sorted(month_counts.keys())
    monthly_units = [month_counts[m] for m in sorted_months]

    ax.plot(sorted_months, monthly_units, marker="s", color="#c0392b", linewidth=2.5, markersize=8, label="Donations Collected")
    ax.fill_between(sorted_months, monthly_units, color="#e74c3c", alpha=0.15)

    for i, txt in enumerate(monthly_units):
        ax.annotate(str(txt), (sorted_months[i], monthly_units[i] + 0.15), ha="center", fontweight="bold")

    ax.set_title("Monthly Blood Donation Collection Trends (2026)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Month (Year-Month)", fontsize=12, labelpad=10)
    ax.set_ylabel("Units Collected", fontsize=12, labelpad=10)
    ax.set_ylim(0, max(monthly_units) + 2)
    ax.legend(loc="upper left")
    plt.tight_layout()
    chart3_path = os.path.join(VIZ_DIR, "chart3_monthly_donation_trends.png")
    plt.savefig(chart3_path, dpi=300)
    plt.close()
    print("  -> Saved:", chart3_path)

    # Chart 4: Donor Age Demographics & Distribution
    fig, ax = plt.subplots(figsize=(9, 5))
    ages = [d["age"] for d in donors_data]
    sns.histplot(ages, bins=8, kde=True, color="#2980b9", edgecolor="black", ax=ax)
    ax.axvline(sum(ages)/len(ages), color="#e74c3c", linestyle="--", linewidth=2, label=f"Mean Age ({sum(ages)/len(ages):.1f} yrs)")
    ax.set_title("Voluntary Donor Age Distribution and Demographics", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Donor Age (Years)", fontsize=12, labelpad=10)
    ax.set_ylabel("Frequency / Count", fontsize=12, labelpad=10)
    ax.legend()
    plt.tight_layout()
    chart4_path = os.path.join(VIZ_DIR, "chart4_donor_age_demographics.png")
    plt.savefig(chart4_path, dpi=300)
    plt.close()
    print("  -> Saved:", chart4_path)

    # Chart 5: Hospital Requisition Status by Urgency
    fig, ax = plt.subplots(figsize=(10, 6))
    urgency_levels = ["NORMAL", "URGENT", "CRITICAL"]
    statuses = ["FULFILLED", "PENDING", "REJECTED"]
    colors = {"FULFILLED": "#27ae60", "PENDING": "#f39c12", "REJECTED": "#c0392b"}

    req_matrix = {u: Counter() for u in urgency_levels}
    for r in requests_data:
        req_matrix[r["urgency_level"]][r["status"]] += 1

    bottoms = [0] * len(urgency_levels)
    for status in statuses:
        counts = [req_matrix[u][status] for u in urgency_levels]
        ax.bar(urgency_levels, counts, bottom=bottoms, label=status, color=colors[status], edgecolor="black", width=0.55)
        bottoms = [b + c for b, c in zip(bottoms, counts)]

    ax.set_title("Hospital Blood Requisitions: Status Breakdown by Urgency Level", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Urgency Level", fontsize=12, labelpad=10)
    ax.set_ylabel("Number of Requests", fontsize=12, labelpad=10)
    ax.legend(title="Request Status")
    plt.tight_layout()
    chart5_path = os.path.join(VIZ_DIR, "chart5_hospital_request_fulfillment.png")
    plt.savefig(chart5_path, dpi=300)
    plt.close()
    print("  -> Saved:", chart5_path)

    # Chart 6: Donor Availability vs Cooldown Breakdown
    fig, ax = plt.subplots(figsize=(10, 6))
    elig_counts = Counter(d["is_eligible"] for d in availability_data)
    labels = ["Eligible to Donate (>= 90 Days)", "Ineligible (Cooldown Active)"]
    vals = [elig_counts[True], elig_counts[False]]
    bar_colors = ["#2ecc71", "#e74c3c"]

    bars = ax.bar(labels, vals, color=bar_colors, edgecolor="black", width=0.5)
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.2, f"{int(yval)} Donors ({yval/len(availability_data)*100:.1f}%)",
                ha="center", va="bottom", fontweight="bold", fontsize=11)

    ax.set_title("Donor Availability Analysis: 90-Day Medical Interval Compliance", fontsize=14, fontweight="bold", pad=15)
    ax.set_ylabel("Number of Registered Donors", fontsize=12, labelpad=10)
    ax.set_ylim(0, max(vals) + 3)
    plt.tight_layout()
    chart6_path = os.path.join(VIZ_DIR, "chart6_donor_eligibility_breakdown.png")
    plt.savefig(chart6_path, dpi=300)
    plt.close()
    print("  -> Saved:", chart6_path)

# ==============================================================================
# Standalone Vector Graphics (SVG & HTML) Engine
# ==============================================================================

def generate_svg_vector_charts(stock_data, donors_data, donations_data, requests_data, availability_data):
    """Generates crisp SVG vector graphics with embedded styles for immediate viewing."""
    print("[Visualization Engine] Generating Standalone Vector Graphics (SVG & HTML)...")

    # Chart 1: Stock Availability SVG
    groups = [s["blood_group"] for s in stock_data]
    units = [int(s["available_units"]) for s in stock_data]
    thresholds = [int(s["minimum_threshold"]) for s in stock_data]
    max_val = max(max(units), max(thresholds)) + 5

    svg1 = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="800" height="480">',
        '<style>',
        '  .title { font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; fill: #2c3e50; }',
        '  .label { font-family: Arial, sans-serif; font-size: 13px; fill: #34495e; text-anchor: middle; }',
        '  .bar-text { font-family: Arial, sans-serif; font-size: 13px; font-weight: bold; fill: #2c3e50; text-anchor: middle; }',
        '  .axis { stroke: #bdc3c7; stroke-width: 1.5; }',
        '  .grid { stroke: #ecf0f1; stroke-width: 1; stroke-dasharray: 4,4; }',
        '</style>',
        '<rect width="100%" height="100%" fill="#ffffff" />',
        '<text x="400" y="40" class="title" text-anchor="middle">Blood Stock Availability vs Safety Threshold</text>',
        '<line x1="80" y1="400" x2="740" y2="400" class="axis" />',
        '<line x1="80" y1="80" x2="80" y2="400" class="axis" />'
    ]

    # Gridlines
    for step in range(0, max_val + 1, 5):
        y_pos = 400 - (step / max_val) * 300
        svg1.append(f'<line x1="80" y1="{y_pos}" x2="740" y2="{y_pos}" class="grid" />')
        svg1.append(f'<text x="70" y="{y_pos+4}" font-family="Arial" font-size="11" fill="#7f8c8d" text-anchor="end">{step}</text>')

    col_width = (740 - 80) / len(groups)
    thresh_points = []
    for i, (g, u, t) in enumerate(zip(groups, units, thresholds)):
        cx = 80 + i * col_width + col_width / 2
        bar_h = (u / max_val) * 300
        bar_y = 400 - bar_h
        color = "#2ecc71" if u >= t else "#e74c3c"
        svg1.append(f'<rect x="{cx-22}" y="{bar_y}" width="44" height="{bar_h}" fill="{color}" rx="3" stroke="#2c3e50" stroke-width="1" />')
        svg1.append(f'<text x="{cx}" y="{bar_y-6}" class="bar-text">{u}</text>')
        svg1.append(f'<text x="{cx}" y="420" class="label">{g}</text>')

        ty = 400 - (t / max_val) * 300
        thresh_points.append(f"{cx},{ty}")
        svg1.append(f'<circle cx="{cx}" cy="{ty}" r="4.5" fill="#d35400" stroke="#ffffff" stroke-width="1.5" />')

    svg1.append(f'<polyline points="{" ".join(thresh_points)}" fill="none" stroke="#d35400" stroke-width="2.5" stroke-dasharray="6,4" />')
    # Legend
    svg1.append('<rect x="520" y="65" width="16" height="16" fill="#2ecc71" rx="2" />')
    svg1.append('<text x="545" y="78" font-family="Arial" font-size="12" fill="#2c3e50">Adequate Stock</text>')
    svg1.append('<rect x="520" y="90" width="16" height="16" fill="#e74c3c" rx="2" />')
    svg1.append('<text x="545" y="103" font-family="Arial" font-size="12" fill="#2c3e50">Critical Deficit</text>')
    svg1.append('<line x1="520" y1="120" x2="536" y2="120" stroke="#d35400" stroke-width="2.5" stroke-dasharray="4,2" />')
    svg1.append('<circle cx="528" cy="120" r="3.5" fill="#d35400" />')
    svg1.append('<text x="545" y="124" font-family="Arial" font-size="12" fill="#2c3e50">Safety Threshold</text>')
    svg1.append('</svg>')

    path1 = os.path.join(VIZ_DIR, "chart1_blood_stock_availability.svg")
    with open(path1, "w", encoding="utf-8") as f:
        f.write("\n".join(svg1))
    print("  -> Saved:", path1)

    # Chart 2: Blood Group Donut SVG
    bg_counts = Counter(d["blood_group"] for d in donors_data)
    total_donors = len(donors_data)
    palette = ["#3498db", "#2ecc71", "#f1c40f", "#e67e22", "#e74c3c", "#9b59b6", "#1abc9c", "#34495e"]

    svg2 = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 500" width="650" height="500">',
        '<style>',
        '  .title { font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; fill: #2c3e50; }',
        '  .legend { font-family: Arial, sans-serif; font-size: 13px; fill: #2c3e50; }',
        '</style>',
        '<rect width="100%" height="100%" fill="#ffffff" />',
        '<text x="325" y="45" class="title" text-anchor="middle">Registered Donors by Blood Group</text>'
    ]

    # Draw Donut Segments
    cx, cy, r_out, r_in = 240, 260, 160, 85
    start_angle = 0.0
    for idx, (grp, count) in enumerate(bg_counts.items()):
        fraction = count / total_donors
        angle = fraction * 2 * math.pi
        end_angle = start_angle + angle

        x1_out = cx + r_out * math.cos(start_angle)
        y1_out = cy + r_out * math.sin(start_angle)
        x2_out = cx + r_out * math.cos(end_angle)
        y2_out = cy + r_out * math.sin(end_angle)

        x1_in = cx + r_in * math.cos(end_angle)
        y1_in = cy + r_in * math.sin(end_angle)
        x2_in = cx + r_in * math.cos(start_angle)
        y2_in = cy + r_in * math.sin(start_angle)

        large_arc = 1 if angle > math.pi else 0
        color = palette[idx % len(palette)]
        d_path = f"M {x1_out} {y1_out} A {r_out} {r_out} 0 {large_arc} 1 {x2_out} {y2_out} L {x1_in} {y1_in} A {r_in} {r_in} 0 {large_arc} 0 {x2_in} {y2_in} Z"
        svg2.append(f'<path d="{d_path}" fill="{color}" stroke="#ffffff" stroke-width="2" />')

        # Legend Entry
        leg_y = 120 + idx * 35
        pct = (count / total_donors) * 100
        svg2.append(f'<rect x="460" y="{leg_y}" width="18" height="18" fill="{color}" rx="3" />')
        svg2.append(f'<text x="490" y="{leg_y+14}" class="legend">{grp}: {count} ({pct:.1f}%)</text>')

        start_angle = end_angle

    svg2.append(f'<text x="{cx}" y="{cy-8}" font-family="Arial" font-size="16" font-weight="bold" fill="#7f8c8d" text-anchor="middle">Total</text>')
    svg2.append(f'<text x="{cx}" y="{cy+18}" font-family="Arial" font-size="22" font-weight="bold" fill="#2c3e50" text-anchor="middle">{total_donors}</text>')
    svg2.append('</svg>')

    path2 = os.path.join(VIZ_DIR, "chart2_donor_blood_group_distribution.svg")
    with open(path2, "w", encoding="utf-8") as f:
        f.write("\n".join(svg2))
    print("  -> Saved:", path2)

    # Chart 3: Monthly Trends SVG
    month_counts = Counter(d["year_month"] for d in donations_data if d["year_month"] != "Unknown")
    sorted_months = sorted(month_counts.keys())
    monthly_units = [month_counts[m] for m in sorted_months]
    max_m = max(monthly_units) + 2

    svg3 = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="800" height="450">',
        '<style>',
        '  .title { font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; fill: #2c3e50; }',
        '  .label { font-family: Arial, sans-serif; font-size: 12px; fill: #34495e; text-anchor: middle; }',
        '  .val-text { font-family: Arial, sans-serif; font-size: 12px; font-weight: bold; fill: #c0392b; text-anchor: middle; }',
        '  .axis { stroke: #bdc3c7; stroke-width: 1.5; }',
        '</style>',
        '<rect width="100%" height="100%" fill="#ffffff" />',
        '<text x="400" y="40" class="title" text-anchor="middle">Monthly Blood Donation Collection Trends (2026)</text>',
        '<line x1="80" y1="380" x2="740" y2="380" class="axis" />',
        '<line x1="80" y1="70" x2="80" y2="380" class="axis" />'
    ]

    m_width = (740 - 80) / len(sorted_months)
    line_pts = []
    area_pts = [f"80,380"]
    for i, m in enumerate(sorted_months):
        u = monthly_units[i]
        cx = 80 + i * m_width + m_width / 2
        cy = 380 - (u / max_m) * 280
        line_pts.append(f"{cx},{cy}")
        area_pts.append(f"{cx},{cy}")

    area_pts.append(f"{740},380")
    svg3.append(f'<polygon points="{" ".join(area_pts)}" fill="#e74c3c" fill-opacity="0.15" />')
    svg3.append(f'<polyline points="{" ".join(line_pts)}" fill="none" stroke="#c0392b" stroke-width="3" />')

    for i, m in enumerate(sorted_months):
        u = monthly_units[i]
        cx = 80 + i * m_width + m_width / 2
        cy = 380 - (u / max_m) * 280
        svg3.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="#c0392b" stroke="#ffffff" stroke-width="2" />')
        svg3.append(f'<text x="{cx}" y="{cy-10}" class="val-text">{u}</text>')
        svg3.append(f'<text x="{cx}" y="405" class="label">{m}</text>')

    svg3.append('</svg>')
    path3 = os.path.join(VIZ_DIR, "chart3_monthly_donation_trends.svg")
    with open(path3, "w", encoding="utf-8") as f:
        f.write("\n".join(svg3))
    print("  -> Saved:", path3)

    # Chart 6: Eligibility Breakdown SVG
    elig_counts = Counter(d["is_eligible"] for d in availability_data)
    n_elig = elig_counts[True]
    n_inelig = elig_counts[False]
    tot = len(availability_data)

    svg6 = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 420" width="700" height="420">',
        '<style>',
        '  .title { font-family: Arial, sans-serif; font-size: 19px; font-weight: bold; fill: #2c3e50; }',
        '  .bar-lbl { font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; fill: #2c3e50; text-anchor: middle; }',
        '  .pct-lbl { font-family: Arial, sans-serif; font-size: 15px; font-weight: bold; fill: #2c3e50; text-anchor: middle; }',
        '</style>',
        '<rect width="100%" height="100%" fill="#ffffff" />',
        '<text x="350" y="45" class="title" text-anchor="middle">Donor Availability Analysis (90-Day Medical Interval)</text>',
        '<line x1="100" y1="340" x2="620" y2="340" stroke="#bdc3c7" stroke-width="1.5" />'
    ]

    h_elig = (n_elig / tot) * 230
    h_inelig = (n_inelig / tot) * 230

    # Eligible Bar
    svg6.append(f'<rect x="180" y="{340 - h_elig}" width="120" height="{h_elig}" fill="#2ecc71" rx="4" stroke="#27ae60" stroke-width="1.5" />')
    svg6.append(f'<text x="240" y="{340 - h_elig - 12}" class="pct-lbl">{n_elig} Donors ({(n_elig/tot)*100:.1f}%)</text>')
    svg6.append(f'<text x="240" y="370" class="bar-lbl">Eligible (Available)</text>')

    # Ineligible Bar
    svg6.append(f'<rect x="400" y="{340 - h_inelig}" width="120" height="{h_inelig}" fill="#e74c3c" rx="4" stroke="#c0392b" stroke-width="1.5" />')
    svg6.append(f'<text x="460" y="{340 - h_inelig - 12}" class="pct-lbl">{n_inelig} Donors ({(n_inelig/tot)*100:.1f}%)</text>')
    svg6.append(f'<text x="460" y="370" class="bar-lbl">Ineligible (Cooldown)</text>')

    svg6.append('</svg>')
    path6 = os.path.join(VIZ_DIR, "chart6_donor_eligibility_breakdown.svg")
    with open(path6, "w", encoding="utf-8") as f:
        f.write("\n".join(svg6))
    print("  -> Saved:", path6)

    # Create an HTML visual dashboard containing all generated visual charts
    dashboard_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Blood Donation Management - Visual Analytics Dashboard</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; margin: 0; padding: 20px; }}
        .header {{ background: linear-gradient(135deg, #c0392b, #8e44ad); color: white; padding: 25px 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 25px; }}
        .header h1 {{ margin: 0; font-size: 26px; }}
        .header p {{ margin: 5px 0 0; opacity: 0.9; font-size: 15px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(480px, 1fr)); gap: 25px; }}
        .card {{ background: white; border-radius: 10px; padding: 20px; box-shadow: 0 3px 10px rgba(0,0,0,0.08); text-align: center; }}
        .card h3 {{ margin-top: 0; color: #2c3e50; font-size: 17px; }}
        .card svg {{ max-width: 100%; height: auto; border: 1px solid #ecf0f1; border-radius: 6px; }}
        .meta {{ background: #ecf0f1; padding: 15px; border-radius: 8px; margin-top: 25px; font-size: 13px; color: #555; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Blood Donation Management & Donor Availability Analytics</h1>
        <p>Scenario 15 | Student: Karan Raajaa V (Reg No: 732925ITR045) | Velalar College of Engineering and Technology</p>
    </div>
    <div class="grid">
        <div class="card">
            <h3>Chart 1: Blood Stock Availability vs Safety Threshold</h3>
            {open(path1, "r", encoding="utf-8").read()}
        </div>
        <div class="card">
            <h3>Chart 2: Registered Donors by Blood Group Distribution</h3>
            {open(path2, "r", encoding="utf-8").read()}
        </div>
        <div class="card">
            <h3>Chart 3: Monthly Blood Donation Trends (2026)</h3>
            {open(path3, "r", encoding="utf-8").read()}
        </div>
        <div class="card">
            <h3>Chart 4: Donor Availability (90-Day Medical Interval)</h3>
            {open(path6, "r", encoding="utf-8").read()}
        </div>
    </div>
    <div class="meta">
        <strong>Academic Evaluation Compliance:</strong> Course 25ITC31 Foundations of Data Science. Charts generated automatically from SQLite database tables via Python ETL pipeline.
    </div>
</body>
</html>
"""
    dash_path = os.path.join(VIZ_DIR, "dashboard.html")
    with open(dash_path, "w", encoding="utf-8") as f:
        f.write(dashboard_html)
    print("  -> Saved Interactive Dashboard:", dash_path)

def generate_all_visualizations():
    """Main driver for generating all visual analytics charts."""
    ensure_viz_dir()
    conn = get_connection()
    _, raw_stock = fetch_table("blood_stock", conn)
    _, raw_donors = fetch_table("donors", conn)
    _, raw_donations = fetch_table("donations", conn)
    _, raw_requests = fetch_table("hospital_requests", conn)
    conn.close()

    donors = preprocess_donors(raw_donors)
    donations = preprocess_donations(raw_donations)
    availability = compute_donor_availability(donors, donations)
    requests = preprocess_hospital_requests(raw_requests)

    # 1. Always generate standalone vector SVG charts and HTML dashboard
    generate_svg_vector_charts(raw_stock, donors, donations, requests, availability)

    # 2. If Matplotlib is available, generate PNG charts
    if HAS_MATPLOTLIB:
        generate_matplotlib_charts(raw_stock, donors, donations, requests, availability)
    else:
        print("[Visualization Engine] Note: matplotlib not installed in local environment; vector SVG visual charts generated with 100% precision.")

if __name__ == "__main__":
    generate_all_visualizations()
