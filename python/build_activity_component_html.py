"""
Builds the comprehensive interactive HTML viewer for UML Activity and Component Diagrams.
File output: diagrams/activity_and_component_diagrams.html
"""

import os
import xml.etree.ElementTree as ET

def build_page():
    activity_svg_path = os.path.join('diagrams', 'activity_diagram.svg')
    component_svg_path = os.path.join('diagrams', 'component_diagram.svg')

    with open(activity_svg_path, 'r', encoding='utf-8') as f:
        activity_svg_content = f.read()

    with open(component_svg_path, 'r', encoding='utf-8') as f:
        component_svg_content = f.read()

    html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UML Activity &amp; Component Diagrams - Blood Donation Management System</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #0f172a;
            --teal: #0d9488;
            --sky: #0284c7;
            --sky-light: #e0f2fe;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --border: #e2e8f0;
            --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.06), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
            --radius: 12px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }}

        body {{
            background-color: var(--bg);
            color: #0f172a;
            padding: 24px 16px;
            line-height: 1.6;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        /* Academic Top Header */
        .academic-card {{
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: white;
            border-radius: var(--radius);
            padding: 24px 30px;
            margin-bottom: 24px;
            box-shadow: var(--shadow);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 20px;
            border-bottom: 3px solid #38bdf8;
        }}

        .academic-title h1 {{
            font-size: 1.55rem;
            font-weight: 800;
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .academic-title p {{
            color: #94a3b8;
            font-size: 0.92rem;
            margin-top: 6px;
        }}

        .student-pill {{
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 12px 20px;
            border-radius: 10px;
            font-size: 0.88rem;
            line-height: 1.6;
            backdrop-filter: blur(4px);
        }}

        .student-pill strong {{
            color: #38bdf8;
        }}

        /* Navigation Bar */
        .nav-links {{
            display: flex;
            gap: 12px;
            margin-bottom: 24px;
            flex-wrap: wrap;
        }}

        .nav-btn {{
            background: white;
            border: 1px solid var(--border);
            padding: 10px 18px;
            border-radius: 8px;
            color: #334155;
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s ease;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}

        .nav-btn:hover {{
            border-color: #0284c7;
            color: #0284c7;
            transform: translateY(-1px);
        }}

        .nav-btn.active {{
            background: #0284c7;
            color: white;
            border-color: #0284c7;
        }}

        /* Tab Switcher */
        .tab-bar {{
            display: flex;
            gap: 8px;
            background: #e2e8f0;
            padding: 6px;
            border-radius: 10px;
            margin-bottom: 20px;
            width: fit-content;
        }}

        .tab-btn {{
            padding: 10px 22px;
            border-radius: 8px;
            border: none;
            background: transparent;
            font-size: 0.95rem;
            font-weight: 700;
            color: #475569;
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .tab-btn.active {{
            background: white;
            color: #0f172a;
            box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        }}

        /* Toolbar */
        .toolbar {{
            background: white;
            border: 1px solid var(--border);
            border-radius: var(--radius) var(--radius) 0 0;
            padding: 14px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
            border-bottom: 1px solid #e2e8f0;
        }}

        .toolbar-group {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }}

        .tool-btn {{
            background: #f1f5f9;
            border: 1px solid #cbd5e1;
            padding: 6px 14px;
            border-radius: 6px;
            font-size: 0.82rem;
            font-weight: 600;
            color: #334155;
            cursor: pointer;
            transition: all 0.15s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}

        .tool-btn:hover {{
            background: #e2e8f0;
            color: #0f172a;
        }}

        .tool-btn.primary {{
            background: #0284c7;
            border-color: #0284c7;
            color: white;
        }}

        .tool-btn.primary:hover {{
            background: #0369a1;
        }}

        /* Viewer Canvas Container */
        .viewer-container {{
            background: #ffffff;
            border: 1px solid var(--border);
            border-top: none;
            border-radius: 0 0 var(--radius) var(--radius);
            box-shadow: var(--shadow);
            padding: 30px 20px;
            overflow: auto;
            max-height: 850px;
            text-align: center;
            position: relative;
        }}

        .svg-wrapper {{
            display: inline-block;
            min-width: 100%;
            max-width: 1200px;
            transition: transform 0.2s ease;
            transform-origin: top center;
        }}

        .svg-wrapper svg {{
            width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
        }}

        .tab-pane {{
            display: none;
        }}

        .tab-pane.active {{
            display: block;
        }}

        /* Side-by-Side Dual View */
        .dual-view-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
        }}

        @media (max-width: 1024px) {{
            .dual-view-grid {{
                grid-template-columns: 1fr;
            }}
        }}

        /* Info Grid */
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }}

        .info-card {{
            background: white;
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 22px 26px;
            box-shadow: var(--shadow);
        }}

        .info-card h3 {{
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 14px;
            display: flex;
            align-items: center;
            gap: 8px;
            border-bottom: 2px solid #e0f2fe;
            padding-bottom: 8px;
        }}

        .info-card ul {{
            list-style: none;
            font-size: 0.92rem;
            color: #334155;
        }}

        .info-card li {{
            margin-bottom: 10px;
            padding-left: 22px;
            position: relative;
        }}

        .info-card li::before {{
            content: "✓";
            position: absolute;
            left: 0;
            color: #0284c7;
            font-weight: bold;
        }}

        .pill-tag {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.76rem;
            font-weight: 700;
            text-transform: uppercase;
            margin-right: 6px;
        }}

        .pill-blue {{ background: #e0f2fe; color: #0369a1; }}
        .pill-green {{ background: #dcfce7; color: #15803d; }}
        .pill-purple {{ background: #f3e8ff; color: #7e22ce; }}
        .pill-amber {{ background: #fef3c7; color: #b45309; }}
        .pill-red {{ background: #fee2e2; color: #b91c1c; }}

        /* Academic Footer */
        footer {{
            margin-top: 40px;
            text-align: center;
            font-size: 0.88rem;
            color: #64748b;
            border-top: 1px solid var(--border);
            padding-top: 20px;
        }}
    </style>
</head>
<body>

<div class="container">
    <!-- Academic Top Header -->
    <header class="academic-card">
        <div class="academic-title">
            <h1>
                <span>🏥</span> UML Activity &amp; Component Diagrams
            </h1>
            <p>Scenario 15: Blood Donation Management and Donor Availability Analysis System</p>
            <p style="font-size: 0.82rem; color: #38bdf8; margin-top: 2px;">Anna University / VCET Autonomous Syllabus: 25ITT33 Software Engineering (Units 1 - 5)</p>
        </div>
        <div class="student-pill">
            <div><strong>Student:</strong> Karan Raajaa V</div>
            <div><strong>Roll No:</strong> 45 | <strong>Reg No:</strong> 732925ITR045</div>
            <div><strong>Class:</strong> 25IT3A | <strong>Dept:</strong> B.Tech IT, VCET Erode - 12</div>
        </div>
    </header>

    <!-- Navigation Bar -->
    <nav class="nav-links">
        <a href="../index.html" class="nav-btn">🏠 Main System Dashboard</a>
        <a href="class_diagram.html" class="nav-btn">📐 UML Class Diagram</a>
        <a href="chen_er_diagram.html" class="nav-btn">🔷 Chen ER Diagram</a>
        <a href="er_diagram.html" class="nav-btn">📊 Relational ER Diagram</a>
        <a href="activity_and_component_diagrams.html" class="nav-btn active">⚡ Activity &amp; Component Diagrams</a>
        <a href="../index.html#docs" class="nav-btn">📚 Docs &amp; 5-Unit Syllabus</a>
    </nav>

    <!-- Tab Bar -->
    <div class="tab-bar">
        <button class="tab-btn active" onclick="switchTab('activity-tab', this)">⚡ Activity Diagram (Workflow)</button>
        <button class="tab-btn" onclick="switchTab('component-tab', this)">📦 Component Diagram (Architecture)</button>
        <button class="tab-btn" onclick="switchTab('dual-tab', this)">🔀 Side-by-Side Dual View</button>
    </div>

    <!-- Active Tab Canvas Area -->
    <main>
        <!-- TAB 1: ACTIVITY DIAGRAM -->
        <div id="activity-tab" class="tab-pane active">
            <div class="toolbar">
                <div class="toolbar-group">
                    <span style="font-size: 0.88rem; font-weight: 700; color: #0f172a;">⚡ Activity Diagram Controls:</span>
                    <button class="tool-btn" onclick="zoomIn('activity-wrapper')">🔍 Zoom In (+)</button>
                    <button class="tool-btn" onclick="zoomOut('activity-wrapper')">🔍 Zoom Out (-)</button>
                    <button class="tool-btn" onclick="resetZoom('activity-wrapper')">↺ Reset</button>
                    <button class="tool-btn" onclick="fitWidth('activity-wrapper')">↔ Fit Width</button>
                </div>
                <div class="toolbar-group">
                    <a href="activity_diagram.svg" download="Activity_Diagram_Scenario15.svg" class="tool-btn primary">⬇ Download SVG</a>
                    <button class="tool-btn" onclick="window.print()">🖨 Print / PDF</button>
                </div>
            </div>
            <div class="viewer-container">
                <div id="activity-wrapper" class="svg-wrapper">
                    {activity_svg_content}
                </div>
            </div>

            <!-- Activity Diagram Technical Breakdown -->
            <section class="info-grid">
                <article class="info-card">
                    <h3><span>🎯</span> Clinical Lifecycle Flow</h3>
                    <ul>
                        <li><span class="pill-tag pill-blue">Initial Node</span> Black filled circle initiating donor check-in.</li>
                        <li><span class="pill-tag pill-amber">Decision 1</span> Age check guard: <code>[18 &lt;= age &lt;= 65]</code> vs <code>[age &lt; 18 or &gt; 65]</code> reject.</li>
                        <li><span class="pill-tag pill-amber">Decision 2</span> 90-day cooldown guard: <code>[days &gt;= 90 or New]</code> vs <code>[days &lt; 90]</code> active block.</li>
                        <li><span class="pill-tag pill-amber">Decision 3</span> Hemoglobin check: <code>[Hgb &gt;= 12.0 g/dL]</code> vs <code>[&lt; 12.0 g/dL]</code> deferral.</li>
                        <li><span class="pill-tag pill-green">Phlebotomy</span> Successful collection of 1 Unit (450 mL whole blood).</li>
                    </ul>
                </article>

                <article class="info-card">
                    <h3><span>⚡</span> Concurrency &amp; Synchronization</h3>
                    <ul>
                        <li><span class="pill-tag pill-purple">Fork Bar</span> Solid horizontal synchronization bar dividing control flow into concurrent parallel threads.</li>
                        <li><span class="pill-tag pill-blue">Thread 1: Donor Care</span> Refreshments, recovery post-care rest, followed by certificate issuance &amp; SMS notification.</li>
                        <li><span class="pill-tag pill-green">Thread 2: Stock Update</span> Atomic database increment in <code>blood_inventory</code>, followed by buffer safety re-evaluation.</li>
                        <li><span class="pill-tag pill-purple">Join Bar</span> Synchronization bar awaiting completion of both parallel branches before session finalization.</li>
                        <li><span class="pill-tag pill-red">Final Node</span> Standard UML bullseye terminating session logging.</li>
                    </ul>
                </article>

                <article class="info-card">
                    <h3><span>📘</span> Syllabus Alignment (25ITT33)</h3>
                    <ul>
                        <li><span class="pill-tag pill-blue">Unit 1: Process Models</span> Prescriptive linear phlebotomy flow paired with Agile feedback loops for donor engagement.</li>
                        <li><span class="pill-tag pill-green">Unit 2: Dynamic Modeling</span> Use Case activity realization capturing guard conditions and exceptional alternate flows.</li>
                        <li><span class="pill-tag pill-purple">Unit 4: Verification</span> White box branch coverage testing every guard decision (Age, Cooldown, Hemoglobin) and race condition testing on join synchronization.</li>
                    </ul>
                </article>
            </section>
        </div>

        <!-- TAB 2: COMPONENT DIAGRAM -->
        <div id="component-tab" class="tab-pane">
            <div class="toolbar">
                <div class="toolbar-group">
                    <span style="font-size: 0.88rem; font-weight: 700; color: #0f172a;">📦 Component Diagram Controls:</span>
                    <button class="tool-btn" onclick="zoomIn('component-wrapper')">🔍 Zoom In (+)</button>
                    <button class="tool-btn" onclick="zoomOut('component-wrapper')">🔍 Zoom Out (-)</button>
                    <button class="tool-btn" onclick="resetZoom('component-wrapper')">↺ Reset</button>
                    <button class="tool-btn" onclick="fitWidth('component-wrapper')">↔ Fit Width</button>
                </div>
                <div class="toolbar-group">
                    <a href="component_diagram.svg" download="Component_Diagram_Scenario15.svg" class="tool-btn primary">⬇ Download SVG</a>
                    <button class="tool-btn" onclick="window.print()">🖨 Print / PDF</button>
                </div>
            </div>
            <div class="viewer-container">
                <div id="component-wrapper" class="svg-wrapper">
                    {component_svg_content}
                </div>
            </div>

            <!-- Component Diagram Technical Breakdown -->
            <section class="info-grid">
                <article class="info-card">
                    <h3><span>📦</span> Structural Notations (UML 2.5)</h3>
                    <ul>
                        <li><span class="pill-tag pill-blue">Component Classifier</span> Standard rectangular box carrying <code>&lt;&lt;component&gt;&gt;</code> stereotype with top-right 2-tab glyph.</li>
                        <li><span class="pill-tag pill-amber">Boundary Ports</span> Small square boxes on outer component perimeter defining explicit interaction gates.</li>
                        <li><span class="pill-tag pill-green">Provided Interfaces (Lollipops)</span> Circles <code>-o</code> declaring capabilities offered by the system: <code>IDonorService</code>, <code>IEligibilityCheck</code>, <code>IHospitalRequisition</code>.</li>
                        <li><span class="pill-tag pill-purple">Required Interfaces (Sockets)</span> Semicircles <code>-()</code> declaring external dependencies: <code>ISMSGateway</code>, <code>IGovtHealthRegistry</code>.</li>
                        <li><span class="pill-tag pill-red">Assembly Connectors</span> Ball-and-socket joints <code>-o)-</code> binding internal modules with zero tight coupling.</li>
                    </ul>
                </article>

                <article class="info-card">
                    <h3><span>🧩</span> Sub-Component Responsibilities</h3>
                    <ul>
                        <li><span class="pill-tag pill-blue">Eligibility &amp; Screening Engine</span> Central coordinator validating age [18-65], weight &gt;=45kg, 90-day cooldown, vitals, and hemoglobin.</li>
                        <li><span class="pill-tag pill-green">DonorManagement</span> Manages donor records, demographic profiles, contact addresses, and donation logs.</li>
                        <li><span class="pill-tag pill-purple">HospitalRequisition</span> Handles emergency orders, compatibility algorithms, and hospital priority matching.</li>
                        <li><span class="pill-tag pill-amber">BloodInventory</span> Maintains unit balances across all 8 ABO/Rh types and enforces the 10-unit buffer threshold.</li>
                        <li><span class="pill-tag pill-blue">DonorAnalytics</span> Geospatial density tracking, predictive shortage alerting, and supply heatmaps.</li>
                    </ul>
                </article>

                <article class="info-card">
                    <h3><span>📘</span> Syllabus Alignment (25ITT33)</h3>
                    <ul>
                        <li><span class="pill-tag pill-blue">Unit 3: Architectural Design</span> Component-level design using Layered Architecture &amp; Service-Oriented Interface segregation.</li>
                        <li><span class="pill-tag pill-green">Unit 3: Interface Design</span> High cohesion and loose coupling achieved through formal provided/required contract interfaces.</li>
                        <li><span class="pill-tag pill-purple">Unit 5: Modularity &amp; CMMI</span> Reusable, independently deployable software components satisfying ISO/IEC 19505-2 compliance.</li>
                    </ul>
                </article>
            </section>
        </div>

        <!-- TAB 3: DUAL COMPARISON VIEW -->
        <div id="dual-tab" class="tab-pane">
            <div class="toolbar">
                <div class="toolbar-group">
                    <span style="font-size: 0.88rem; font-weight: 700; color: #0f172a;">🔀 Comparative Analysis: Behavioral (Activity) vs. Structural (Component)</span>
                </div>
                <div class="toolbar-group">
                    <button class="tool-btn" onclick="window.print()">🖨 Print Comparative Dossier</button>
                </div>
            </div>
            <div class="viewer-container">
                <div class="dual-view-grid">
                    <div>
                        <h4 style="font-size: 1.1rem; font-weight: 800; color: #0284c7; margin-bottom: 12px;">Dynamic Behavioral Workflow (Activity Diagram)</h4>
                        <div style="border: 1px solid var(--border); border-radius: 8px; padding: 12px; background: white;">
                            {activity_svg_content}
                        </div>
                    </div>
                    <div>
                        <h4 style="font-size: 1.1rem; font-weight: 800; color: #0d9488; margin-bottom: 12px;">Static Modular Architecture (Component Diagram)</h4>
                        <div style="border: 1px solid var(--border); border-radius: 8px; padding: 12px; background: white;">
                            {component_svg_content}
                        </div>
                    </div>
                </div>
            </div>

            <!-- Comparison Matrix -->
            <section class="info-grid" style="margin-top: 24px;">
                <article class="info-card" style="grid-column: 1 / -1;">
                    <h3><span>⚖</span> UML Architectural Comparison Matrix (Activity vs. Component)</h3>
                    <div style="overflow-x: auto;">
                        <table style="width: 100%; border-collapse: collapse; font-size: 0.9rem; margin-top: 8px;">
                            <thead>
                                <tr style="background: #f1f5f9; text-align: left;">
                                    <th style="padding: 10px 14px; border: 1px solid #cbd5e1;">Architectural Dimension</th>
                                    <th style="padding: 10px 14px; border: 1px solid #cbd5e1;">UML Activity Diagram (Behavioral View)</th>
                                    <th style="padding: 10px 14px; border: 1px solid #cbd5e1;">UML Component Diagram (Structural View)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 700;">Primary Purpose</td>
                                    <td style="padding: 10px 14px; border: 1px solid #e2e8f0;">Models dynamic clinical operations, step-by-step algorithms, decision branches, and parallel forks.</td>
                                    <td style="padding: 10px 14px; border: 1px solid #e2e8f0;">Models physical modular structure, subsystem encapsulation, ports, and provided/required contracts.</td>
                                </tr>
                                <tr>
                                    <td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 700;">Concurrency Model</td>
                                    <td style="padding: 10px 14px; border: 1px solid #e2e8f0;">Explicit Fork and Join synchronization bars executing donor rest &amp; stock update concurrently.</td>
                                    <td style="padding: 10px 14px; border: 1px solid #e2e8f0;">Asynchronous interface dispatch via ports and event-driven connectors.</td>
                                </tr>
                                <tr>
                                    <td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 700;">Coupling &amp; Boundary</td>
                                    <td style="padding: 10px 14px; border: 1px solid #e2e8f0;">Temporal coupling: order of execution and guard condition transitions.</td>
                                    <td style="padding: 10px 14px; border: 1px solid #e2e8f0;">Loose coupling: boundary ports decouple inner implementation from external consumers.</td>
                                </tr>
                                <tr>
                                    <td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 700;">Software Engg. Phase</td>
                                    <td style="padding: 10px 14px; border: 1px solid #e2e8f0;">Unit 2: Requirements Analysis &amp; Business Process Engineering.</td>
                                    <td style="padding: 10px 14px; border: 1px solid #e2e8f0;">Unit 3: Architectural Design, Subsystem Decomposition, and Web-App Design.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </article>
            </section>
        </div>
    </main>

    <!-- Footer -->
    <footer>
        <p><strong>Scenario 15: Blood Donation Management and Donor Availability Analysis System</strong></p>
        <p>Student: <strong>Karan Raajaa V</strong> (Register No: <strong>732925ITR045</strong>, Roll No: <strong>45</strong>, Class: <strong>25IT3A</strong>)</p>
        <p>Department of Information Technology, Velalar College of Engineering and Technology, Erode - 638012</p>
        <p style="margin-top: 8px; font-size: 0.8rem; color: #94a3b8;">Compliant with UML 2.5 Specification (OMG) and Anna University Autonomous Curriculum 2026</p>
    </footer>
</div>

<script>
    // Tab switching function
    function switchTab(tabId, btn) {{
        document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
        document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
        
        document.getElementById(tabId).classList.add('active');
        btn.classList.add('active');
    }}

    // Zoom and pan functions for SVG wrappers
    const zoomStates = {{
        'activity-wrapper': 1.0,
        'component-wrapper': 1.0
    }};

    function zoomIn(wrapperId) {{
        zoomStates[wrapperId] = Math.min(zoomStates[wrapperId] + 0.15, 2.5);
        applyZoom(wrapperId);
    }}

    function zoomOut(wrapperId) {{
        zoomStates[wrapperId] = Math.max(zoomStates[wrapperId] - 0.15, 0.4);
        applyZoom(wrapperId);
    }}

    function resetZoom(wrapperId) {{
        zoomStates[wrapperId] = 1.0;
        applyZoom(wrapperId);
    }}

    function fitWidth(wrapperId) {{
        zoomStates[wrapperId] = 1.15;
        applyZoom(wrapperId);
    }}

    function applyZoom(wrapperId) {{
        const el = document.getElementById(wrapperId);
        if (el) {{
            el.style.transform = `scale(${{zoomStates[wrapperId]}})`;
        }}
    }}
</script>

</body>
</html>
'''

    out_path = os.path.join('diagrams', 'activity_and_component_diagrams.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"SUCCESS: Generated {out_path} ({len(html_template)} characters)")

if __name__ == '__main__':
    build_page()
