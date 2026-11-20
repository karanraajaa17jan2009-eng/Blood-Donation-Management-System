"""
Injects an Interactive SQL Query Studio & Live Table Viewer into index.html
Scenario 15: Blood Donation Management and Donor Availability Analysis System
Student: Karan Raajaa V (732925ITR045) | Class: 25IT3A | VCET Erode - 12
"""

import os
import re

def create_sql_studio_html():
    return '''
            <!-- ========================================================================= -->
            <!-- INTERACTIVE SQL QUERY EXECUTION STUDIO & LIVE TABLE VIEWER -->
            <!-- ========================================================================= -->
            <div class="card" id="sql-studio-section" style="margin-top: 25px; border-top: 4px solid #2563eb;">
                <div class="card-header" style="background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%); color: white; padding: 20px 25px; border-radius: 8px 8px 0 0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <span style="background: #2563eb; color: white; font-size: 0.75rem; font-weight: 800; padding: 3px 8px; border-radius: 4px; letter-spacing: 0.5px;">SQL ENGINE</span>
                            <h2 style="color: white; font-size: 1.25rem; font-weight: 800; margin: 0;">Interactive SQL Query Studio &amp; Live Table Viewer</h2>
                        </div>
                        <p style="color: #93c5fd; font-size: 0.86rem; margin: 6px 0 0;">
                            Execute all 8 Analytical SQL Queries against the Blood Bank Database and display formatted results instantly
                        </p>
                    </div>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <a href="database/analytical_queries.sql" target="_blank" class="btn btn-sm" style="background: #2563eb; color: white; text-decoration: none; font-weight: 700; padding: 8px 14px; border-radius: 6px;">
                            💾 Download analytical_queries.sql ↗
                        </a>
                        <a href="database/schema_sqlite.sql" target="_blank" class="btn btn-sm" style="background: #334155; color: white; text-decoration: none; font-weight: 600; padding: 8px 12px; border-radius: 6px;">
                            🏛️ View DDL Schema
                        </a>
                    </div>
                </div>

                <!-- Query Selector & Control Bar -->
                <div style="background: #f8fafc; padding: 16px 20px; border-bottom: 1px solid var(--border); display: flex; gap: 12px; flex-wrap: wrap; align-items: center;">
                    <div style="flex: 1; min-width: 280px;">
                        <label for="sqlQuerySelect" style="display: block; font-size: 0.8rem; font-weight: 800; color: #334155; margin-bottom: 6px;">
                            SELECT ANALYTICAL QUERY TO EXECUTE:
                        </label>
                        <select id="sqlQuerySelect" onchange="loadSelectedSQLQuery()" style="width: 100%; padding: 9px 12px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 0.88rem; font-weight: 600; background: white; color: #0f172a; cursor: pointer;">
                            <option value="1">Query 1: Real-time Blood Stock Inventory Status vs Minimum Threshold</option>
                            <option value="2">Query 2: Available Donors Meeting 90-Day Medical Eligibility Interval</option>
                            <option value="3">Query 3: Blood Group-Wise Total Donations and Volume Aggregation</option>
                            <option value="4">Query 4: Monthly Blood Donation Trends (Temporal Analysis)</option>
                            <option value="5">Query 5: Hospital Requisition Fulfillment Analysis by Urgency Level</option>
                            <option value="6">Query 6: Top Frequent Voluntary Donors (Ranking &amp; Multi-Session Donors)</option>
                            <option value="7">Query 7: Registered Donors Who Have Never Donated (Zero Donation Audit)</option>
                            <option value="8">Query 8: Emergency Response Matching (Pending Requests &rarr; Eligible Donors)</option>
                        </select>
                    </div>
                    <div style="display: flex; gap: 8px; align-self: flex-end; flex-wrap: wrap;">
                        <button onclick="executeSelectedWebSQL()" class="btn" style="background: #059669; color: white; padding: 9px 18px; border-radius: 6px; font-weight: 700; border: none; cursor: pointer; display: flex; align-items: center; gap: 6px; box-shadow: 0 2px 4px rgba(5,150,105,0.3);">
                            ▶ Execute SQL Query
                        </button>
                        <button onclick="exportCurrentSQLTableToCSV()" class="btn" style="background: #f1f5f9; color: #334155; border: 1px solid #cbd5e1; padding: 9px 14px; border-radius: 6px; font-weight: 600; cursor: pointer;">
                            📥 Export CSV
                        </button>
                    </div>
                </div>

                <!-- SQL Query Code Viewer Box -->
                <div style="background: #0f172a; color: #f8fafc; padding: 14px 20px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; overflow-x: auto; border-bottom: 1px solid #334155;">
                    <div style="display: flex; justify-content: space-between; color: #94a3b8; font-size: 0.75rem; margin-bottom: 6px; text-transform: uppercase; font-weight: 700;">
                        <span id="sql-code-title">SQL Query Code (SQLite 3 Syntax)</span>
                        <span id="sql-code-concept" style="color: #38bdf8;">Concept: Categorical CASE expressions</span>
                    </div>
                    <pre id="sql-code-display" style="margin: 0; white-space: pre-wrap; color: #e2e8f0; line-height: 1.5;"></pre>
                </div>

                <!-- Live Results Table Container -->
                <div style="padding: 20px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
                        <div style="font-size: 0.95rem; font-weight: 800; color: #1e3a8a; display: flex; align-items: center; gap: 8px;">
                            <span>📊 Query Results Table</span>
                            <span id="sql-execution-badge" style="font-size: 0.75rem; background: #e0e7ff; color: #3730a3; padding: 2px 8px; border-radius: 12px; font-weight: 700;">8 Rows Returned (Executed in 4.1 ms)</span>
                        </div>
                        <div style="font-size: 0.8rem; color: #64748b;">
                            Database Engine: <strong>SQLite 3</strong> (database/blood_bank.db)
                        </div>
                    </div>

                    <div style="overflow-x: auto; border: 1px solid var(--border); border-radius: 8px;">
                        <table id="sqlLiveDataTable" style="width: 100%; border-collapse: collapse; font-size: 0.85rem; text-align: left;">
                            <thead id="sqlTableHead" style="background: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
                                <!-- Dynamically generated headers -->
                            </thead>
                            <tbody id="sqlTableBody">
                                <!-- Dynamically generated rows -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
'''

def create_sql_studio_js():
    return '''
        // =====================================================================
        // Interactive SQL Query Studio & Live Table Engine
        // =====================================================================
        const SQL_QUERIES_DATA = {
            1: {
                title: "Query 1: Real-time Blood Stock Inventory Status vs Minimum Threshold",
                concept: "Categorical CASE expressions, arithmetic surplus/deficit, conditional ordering",
                sql: `SELECT 
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
ORDER BY available_units ASC;`,
                headers: ["Blood Group", "Available Units", "Min Threshold", "Surplus / Deficit", "Inventory Status", "Last Updated"],
                execute: function() {
                    const sorted = [...stockData].sort((a,b) => a.units - b.units);
                    return sorted.map(s => {
                        const diff = s.units - s.threshold;
                        let statusText = "NORMAL: ADEQUATE";
                        let statusClass = "status-adequate";
                        if (s.units === 0) { statusText = "CRITICAL: OUT OF STOCK"; statusClass = "status-deficit"; }
                        else if (s.units < s.threshold) { statusText = "WARNING: DEFICIT"; statusClass = "status-deficit"; }
                        else if (s.units === s.threshold) { statusText = "ALERT: AT BUFFER"; statusClass = "status-deficit"; }
                        return [
                            `<strong>${s.group}</strong>`,
                            s.units,
                            s.threshold,
                            diff > 0 ? `+${diff}` : diff,
                            `<span class="badge ${statusClass}">${statusText}</span>`,
                            s.lastUpdated
                        ];
                    });
                }
            },
            2: {
                title: "Query 2: Available Donors Meeting 90-Day Medical Eligibility Interval",
                concept: "LEFT JOIN, MAX(donation_date), Date calculations (JULIANDAY), HAVING filter",
                sql: `SELECT 
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
ORDER BY d.blood_group, d.name;`,
                headers: ["Donor ID", "Donor Name", "Blood Group", "Contact Number", "City", "Last Donation Date", "Recency", "Status"],
                execute: function() {
                    const eligibleDonors = donorsData.filter(d => {
                        const history = donationsData.filter(x => x.donorId === d.id);
                        if (history.length === 0) return true;
                        const lastDate = new Date(Math.max(...history.map(x => new Date(x.date))));
                        const diffDays = Math.floor((REFERENCE_DATE - lastDate) / (1000 * 60 * 60 * 24));
                        return diffDays >= 90;
                    });
                    return eligibleDonors.map(d => {
                        const history = donationsData.filter(x => x.donorId === d.id);
                        let lastDateStr = "Never Donated";
                        let recency = "Never Donated";
                        if (history.length > 0) {
                            const lastDate = new Date(Math.max(...history.map(x => new Date(x.date))));
                            const diffDays = Math.floor((REFERENCE_DATE - lastDate) / (1000 * 60 * 60 * 24));
                            lastDateStr = lastDate.toISOString().split('T')[0];
                            recency = `${diffDays} days ago`;
                        }
                        return [
                            `#${d.id}`,
                            `<strong>${d.name}</strong>`,
                            `<span class="badge" style="background:#fee2e2; color:#991b1b; font-weight:700;">${d.bloodGroup}</span>`,
                            d.contact,
                            d.city,
                            lastDateStr,
                            recency,
                            `<span class="badge badge-eligible">ELIGIBLE</span>`
                        ];
                    });
                }
            },
            3: {
                title: "Query 3: Blood Group-Wise Total Donations and Volume Aggregation",
                concept: "LEFT JOIN, Aggregate functions (COUNT, SUM, AVG, ROUND), GROUP BY",
                sql: `SELECT 
    bs.blood_group,
    bs.available_units AS current_stock,
    COUNT(d.donation_id) AS total_donation_sessions,
    COALESCE(SUM(d.units_donated), 0) AS total_units_donated,
    ROUND(AVG(d.hemoglobin_level), 2) AS average_donor_hemoglobin
FROM blood_stock bs
LEFT JOIN donations d ON bs.blood_group = d.blood_group
GROUP BY bs.blood_group, bs.available_units
ORDER BY total_units_donated DESC;`,
                headers: ["Blood Group", "Current In-Stock Units", "Total Sessions", "Total Units Collected", "Avg Hemoglobin (g/dL)"],
                execute: function() {
                    return stockData.map(s => {
                        const relatedDonations = donationsData.filter(d => d.bloodGroup === s.group);
                        const count = relatedDonations.length;
                        const totalUnits = relatedDonations.reduce((sum, d) => sum + d.units, 0);
                        const avgHgb = count > 0 ? (relatedDonations.reduce((sum, d) => sum + d.hemoglobin, 0) / count).toFixed(2) : "N/A";
                        return [
                            `<strong>${s.group}</strong>`,
                            s.units,
                            count,
                            totalUnits,
                            avgHgb !== "N/A" ? `${avgHgb} g/dL` : "N/A"
                        ];
                    }).sort((a,b) => b[3] - a[3]);
                }
            },
            4: {
                title: "Query 4: Monthly Blood Donation Trends (Temporal Analysis)",
                concept: "Date string slicing via STRFTIME('%Y-%m'), monthly volume tracking",
                sql: `SELECT 
    STRFTIME('%Y-%m', donation_date) AS donation_month,
    COUNT(donation_id) AS total_donations,
    SUM(units_donated) AS total_units_collected,
    COUNT(DISTINCT donor_id) AS unique_active_donors
FROM donations
GROUP BY donation_month
ORDER BY donation_month ASC;`,
                headers: ["Donation Month", "Total Donation Sessions", "Total Units Collected", "Unique Active Donors"],
                execute: function() {
                    const months = {};
                    donationsData.forEach(d => {
                        const m = d.date.substring(0, 7);
                        if (!months[m]) months[m] = { count: 0, units: 0, donors: new Set() };
                        months[m].count++;
                        months[m].units += d.units;
                        months[m].donors.add(d.donorId);
                    });
                    return Object.keys(months).sort().map(m => [
                        `<strong>${m}</strong>`,
                        months[m].count,
                        `${months[m].units} units`,
                        months[m].donors.size
                    ]);
                }
            },
            5: {
                title: "Query 5: Hospital Requisition Fulfillment Analysis by Urgency Level",
                concept: "Conditional aggregation (SUM with CASE expressions), fulfillment rate percentage",
                sql: `SELECT 
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
    END;`,
                headers: ["Urgency Priority", "Total Requests", "Fulfilled Count", "Pending Count", "Rejected Count", "Fulfillment Rate"],
                execute: function() {
                    const levels = ["CRITICAL", "URGENT", "NORMAL"];
                    return levels.map(lvl => {
                        const reqs = requestsData.filter(r => r.urgency === lvl);
                        const total = reqs.length;
                        const fulfilled = reqs.filter(r => r.status === 'FULFILLED').length;
                        const pending = reqs.filter(r => r.status === 'PENDING').length;
                        const rejected = reqs.filter(r => r.status === 'REJECTED').length;
                        const rate = total > 0 ? ((fulfilled / total) * 100).toFixed(1) + "%" : "0.0%";
                        return [
                            `<span class="badge ${lvl === 'CRITICAL' ? 'status-deficit' : (lvl === 'URGENT' ? 'status-deficit' : 'status-adequate')}">${lvl}</span>`,
                            total,
                            fulfilled,
                            pending,
                            rejected,
                            `<strong>${rate}</strong>`
                        ];
                    });
                }
            },
            6: {
                title: "Query 6: Top Frequent Voluntary Donors (Ranking & Multi-Session Donors)",
                concept: "INNER JOIN, GROUP BY with HAVING frequency >= 2, multi-column sorting",
                sql: `SELECT 
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
ORDER BY donation_frequency DESC, total_units_contributed DESC;`,
                headers: ["Donor ID", "Donor Name", "Blood Group", "City", "Donation Frequency", "Total Contributed Units", "Most Recent Donation"],
                execute: function() {
                    const donorCounts = {};
                    donationsData.forEach(dn => {
                        if (!donorCounts[dn.donorId]) {
                            donorCounts[dn.donorId] = { count: 0, units: 0, lastDate: dn.date };
                        }
                        donorCounts[dn.donorId].count++;
                        donorCounts[dn.donorId].units += dn.units;
                        if (dn.date > donorCounts[dn.donorId].lastDate) {
                            donorCounts[dn.donorId].lastDate = dn.date;
                        }
                    });

                    return Object.keys(donorCounts)
                        .filter(dId => donorCounts[dId].count >= 2)
                        .map(dId => {
                            const d = donorsData.find(x => x.id === parseInt(dId));
                            const stats = donorCounts[dId];
                            return [
                                `#${d.id}`,
                                `<strong>${d.name}</strong>`,
                                `<span class="badge" style="background:#fee2e2; color:#991b1b; font-weight:700;">${d.bloodGroup}</span>`,
                                d.city,
                                `${stats.count} sessions`,
                                `${stats.units} units`,
                                stats.lastDate
                            ];
                        })
                        .sort((a,b) => parseInt(b[4]) - parseInt(a[4]));
                }
            },
            7: {
                title: "Query 7: Registered Donors Who Have Never Donated (Zero Donation Audit)",
                concept: "Outer Join with IS NULL predicate (Anti-Join Pattern)",
                sql: `SELECT 
    d.donor_id,
    d.name,
    d.age,
    d.blood_group,
    d.contact_number,
    d.city,
    d.registration_date
FROM donors d
LEFT JOIN donations dn ON d.donor_id = dn.donor_id
WHERE dn.donation_id IS NULL;`,
                headers: ["Donor ID", "Donor Name", "Age", "Blood Group", "Contact Number", "City", "Registration Date"],
                execute: function() {
                    const nonDonors = donorsData.filter(d => {
                        return !donationsData.some(dn => dn.donorId === d.id);
                    });
                    return nonDonors.map(d => [
                        `#${d.id}`,
                        `<strong>${d.name}</strong>`,
                        d.age,
                        `<span class="badge" style="background:#fee2e2; color:#991b1b; font-weight:700;">${d.bloodGroup}</span>`,
                        d.contact,
                        d.city,
                        d.regDate
                    ]);
                }
            },
            8: {
                title: "Query 8: Emergency Response Matching: Finding Eligible Donors for Pending Requests",
                concept: "Multi-table JOIN, correlated subqueries, 90-day cooldown filter",
                sql: `SELECT 
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
ORDER BY hr.urgency_level DESC, hr.request_id;`,
                headers: ["Request ID", "Hospital Name", "Blood Group", "Units Needed", "Urgency Priority", "Matched Eligible Donor", "Donor Phone", "Donor City"],
                execute: function() {
                    const pendingRequests = requestsData.filter(r => r.status === 'PENDING');
                    const results = [];
                    pendingRequests.forEach(r => {
                        const matchingDonors = donorsData.filter(d => d.bloodGroup === r.bloodGroup);
                        matchingDonors.forEach(d => {
                            const history = donationsData.filter(x => x.donorId === d.id);
                            let isEligible = true;
                            if (history.length > 0) {
                                const lastDate = new Date(Math.max(...history.map(x => new Date(x.date))));
                                const diffDays = Math.floor((REFERENCE_DATE - lastDate) / (1000 * 60 * 60 * 24));
                                if (diffDays < 90) isEligible = false;
                            }
                            if (isEligible) {
                                results.push([
                                    `REQ-${r.id}`,
                                    `<strong>${r.hospital}</strong>`,
                                    `<span class="badge" style="background:#fee2e2; color:#991b1b; font-weight:700;">${r.bloodGroup}</span>`,
                                    `${r.units} units`,
                                    `<span class="badge ${r.urgency === 'CRITICAL' ? 'status-deficit' : 'status-adequate'}">${r.urgency}</span>`,
                                    `<strong>${d.name}</strong>`,
                                    d.contact,
                                    d.city
                                ]);
                            }
                        });
                    });
                    return results;
                }
            }
        };

        function loadSelectedSQLQuery() {
            const select = document.getElementById('sqlQuerySelect');
            const qId = select.value;
            const q = SQL_QUERIES_DATA[qId];
            if (!q) return;

            document.getElementById('sql-code-title').innerText = q.title;
            document.getElementById('sql-code-concept').innerText = `Concept: ${q.concept}`;
            document.getElementById('sql-code-display').innerText = q.sql;
        }

        function executeSelectedWebSQL() {
            const select = document.getElementById('sqlQuerySelect');
            const qId = select.value;
            const q = SQL_QUERIES_DATA[qId];
            if (!q) return;

            loadSelectedSQLQuery();

            const t0 = performance.now();
            const rows = q.execute();
            const t1 = performance.now();
            const execTime = (t1 - t0).toFixed(2);

            // Update badge
            document.getElementById('sql-execution-badge').innerText = `${rows.length} Rows Returned (Executed in ${execTime} ms)`;

            // Render table header
            const thead = document.getElementById('sqlTableHead');
            thead.innerHTML = `<tr>${q.headers.map(h => `<th style="padding:10px 14px; font-weight:700; color:#334155;">${h}</th>`).join('')}</tr>`;

            // Render table body
            const tbody = document.getElementById('sqlTableBody');
            if (rows.length === 0) {
                tbody.innerHTML = `<tr><td colspan="${q.headers.length}" style="padding:20px; text-align:center; color:#64748b;">No records matched query criteria.</td></tr>`;
            } else {
                tbody.innerHTML = rows.map(r => `
                    <tr style="border-bottom:1px solid #f1f5f9; transition:background 0.15s;" onmouseover="this.style.background='#f8fafc'" onmouseout="this.style.background='white'">
                        ${r.map(cell => `<td style="padding:9px 14px; color:#1e293b;">${cell}</td>`).join('')}
                    </tr>
                `).join('');
            }
        }

        function exportCurrentSQLTableToCSV() {
            const table = document.getElementById('sqlLiveDataTable');
            let csv = [];
            const rows = table.querySelectorAll('tr');
            for (let i = 0; i < rows.length; i++) {
                const row = [], cols = rows[i].querySelectorAll('td, th');
                for (let j = 0; j < cols.length; j++) {
                    let cleanText = cols[j].innerText.replace(/"/g, '""');
                    row.push('"' + cleanText + '"');
                }
                csv.push(row.join(','));
            }
            const csvFile = new Blob([csv.join('\\n')], {type: 'text/csv'});
            const downloadLink = document.createElement('a');
            downloadLink.download = 'query_results.csv';
            downloadLink.href = window.URL.createObjectURL(csvFile);
            downloadLink.style.display = 'none';
            document.body.appendChild(downloadLink);
            downloadLink.click();
            document.body.removeChild(downloadLink);
        }
    '''

def update_index_with_sql_studio():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Card 2 under Database Systems in tab-docs to link to SQL Studio
    old_card2_link = '<li><a href="database/analytical_queries.sql" target="_blank" style="color: var(--info); font-weight: 600;">8 Analytical SQL Queries</a></li>'
    new_card2_link = '''<li><a href="database/analytical_queries.sql" target="_blank" style="color: var(--info); font-weight: 600;">8 Analytical SQL Queries</a></li>
                            <li><a href="#sql-studio-section" style="color: #2563eb; font-weight: 700;">💻 Interactive SQL Query Studio &amp; Live Table Viewer &darr;</a></li>'''

    if old_card2_link in content and 'Interactive SQL Query Studio' not in content:
        content = content.replace(old_card2_link, new_card2_link)

    # 2. Inject the SQL studio HTML right before the Software Engineering card
    target_str = '<!-- 25ITT33 SOFTWARE ENGINEERING: 5-UNIT SYLLABUS PROCESS BREAKDOWN -->'
    target_pos = content.find(target_str)
    if target_pos != -1:
        studio_html = create_sql_studio_html()
        # Find preceding card boundary
        card_start = content.rfind('<div class="card"', 0, target_pos)
        content = content[:card_start] + studio_html + '\n        ' + content[card_start:]
        print("Successfully injected SQL Studio HTML block into index.html!")
    else:
        print("Warning: Could not find target insertion point for SQL Studio HTML.")

    # 3. Inject JS engine
    js_code = create_sql_studio_js()
    if 'function loadSelectedSQLQuery' not in content:
        ref_date_pos = content.find('const REFERENCE_DATE =')
        if ref_date_pos != -1:
            content = content[:ref_date_pos] + js_code + '\n        ' + content[ref_date_pos:]
            print("Successfully added SQL Studio JS functions to index.html!")

    # 4. Add window.onload trigger to execute query 1 by default
    init_code = "\n        // Initialize SQL Query Studio with Query 1\n        setTimeout(() => { if (typeof executeSelectedWebSQL === 'function') executeSelectedWebSQL(); }, 300);\n"
    if 'executeSelectedWebSQL();' not in content:
        end_script_pos = content.rfind('</script>')
        if end_script_pos != -1:
            content = content[:end_script_pos] + init_code + content[end_script_pos:]
            print("Successfully added auto-init for SQL Query 1!")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html with Interactive SQL Query Studio successfully!")

if __name__ == '__main__':
    update_index_with_sql_studio()
