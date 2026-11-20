"""
Builds the standalone interactive Class Diagram HTML viewer
Scenario 15: Blood Donation Management and Donor Availability Analysis System
Student: Karan Raajaa V | Register No: 732925ITR045 | Class: 25IT3A
Institution: Velalar College of Engineering and Technology, Erode - 12
"""

import os

def build_class_html():
    with open(os.path.join("diagrams", "class_diagram.svg"), "r", encoding="utf-8") as f:
        svg_content = f.read()

    # Ensure SVG has id="classSvg"
    if 'id="classSvg"' not in svg_content:
        svg_content = svg_content.replace('<svg ', '<svg id="classSvg" ')

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UML Class Diagram - Blood Donation Management System</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #0f172a;
            --teal: #0f766e;
            --teal-light: #ccfbf1;
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
            line-height: 1.5;
        }}

        .container {{
            max-width: 1360px;
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
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.22);
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
            border-color: #0ea5e9;
            color: #0284c7;
            transform: translateY(-1px);
        }}

        .nav-btn.active {{
            background: #0284c7;
            color: white;
            border-color: #0284c7;
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
            color: white;
            border-color: #0284c7;
        }}

        .tool-btn.primary:hover {{
            background: #0369a1;
        }}

        .filter-btn {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            color: #475569;
            cursor: pointer;
            transition: all 0.15s ease;
        }}

        .filter-btn:hover, .filter-btn.active {{
            background: #e0f2fe;
            color: #0369a1;
            border-color: #38bdf8;
        }}

        /* Canvas Container */
        .canvas-container {{
            background: white;
            border: 1px solid var(--border);
            border-top: none;
            border-radius: 0 0 var(--radius) var(--radius);
            box-shadow: var(--shadow);
            overflow: auto;
            max-height: 85vh;
            padding: 20px;
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

        /* Dimming & Highlighting */
        .dimmed {{
            opacity: 0.15 !important;
            transition: opacity 0.3s ease;
        }}

        .highlighted {{
            filter: drop-shadow(0 0 10px rgba(2, 132, 199, 0.8));
            transition: all 0.3s ease;
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
            padding: 20px 24px;
            box-shadow: var(--shadow);
        }}

        .info-card h3 {{
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        /* Footer */
        footer {{
            margin-top: 40px;
            text-align: center;
            color: #64748b;
            font-size: 0.85rem;
            padding-bottom: 20px;
        }}
    </style>
</head>
<body>

<div class="container">
    <!-- Academic Header -->
    <div class="academic-card">
        <div class="academic-title">
            <h1>UML Class Diagram Specification</h1>
            <p>Scenario 15: Blood Donation Management and Donor Availability Analysis System</p>
        </div>
        <div class="student-pill">
            <strong>Student:</strong> Karan Raajaa V (Roll No: 45)<br>
            <strong>Reg No:</strong> 732925ITR045 | <strong>Class:</strong> 25IT3A<br>
            <strong>College:</strong> Velalar College of Engg & Tech, Erode
        </div>
    </div>

    <!-- Navigation Bar -->
    <div class="nav-links">
        <a href="../index.html" class="nav-btn">&larr; Back to Main Website</a>
        <a href="class_diagram.html" class="nav-btn active">📦 UML Class Diagram</a>
        <a href="chen_er_diagram.html" class="nav-btn">🔷 Chen ER Diagram</a>
        <a href="er_diagram.html" class="nav-btn">📊 Crow's Foot Relational ER</a>
        <a href="../docs/Architecture_and_Design_Diagrams.md" class="nav-btn">📖 Architecture & Design Doc</a>
    </div>

    <!-- Toolbar Controls -->
    <div class="toolbar">
        <div class="toolbar-group">
            <span style="font-size: 0.82rem; font-weight: 700; color: #475569; margin-right: 4px;">FOCUS VIEW:</span>
            <button class="filter-btn active" onclick="filterClasses('all', event)">Show All</button>
            <button class="filter-btn" onclick="filterClasses('inheritance', event)">Inheritance Hierarchy (Person & Roles)</button>
            <button class="filter-btn" onclick="filterClasses('entities', event)">Domain Entities (Donation, Stock, Request)</button>
            <button class="filter-btn" onclick="filterClasses('services', event)">Service Layer</button>
        </div>
        <div class="toolbar-group">
            <button class="tool-btn" onclick="zoomIn()">🔍 Zoom +</button>
            <button class="tool-btn" onclick="zoomOut()">🔍 Zoom -</button>
            <button class="tool-btn" onclick="resetZoom()">↺ Reset</button>
            <a href="class_diagram.svg" download="Class_Diagram_Scenario15.svg" class="tool-btn primary">⬇ Download SVG</a>
            <button class="tool-btn" onclick="window.print()">🖨 Print / PDF</button>
        </div>
    </div>

    <!-- Main Canvas with Inline SVG -->
    <div class="canvas-container" id="canvasContainer">
        <div class="svg-wrapper" id="svgWrapper">
            {svg_content}
        </div>
    </div>

    <!-- Detailed Explanation Grid -->
    <div class="info-grid">
        <!-- Card 1: 3-Compartment Class Diagram Structure -->
        <div class="info-card">
            <h3>📦 3-Compartment UML Class Structure</h3>
            <p style="font-size: 0.85rem; color: #475569; margin-bottom: 12px;">
                Following standard UML (ISO/IEC 19505), each class is strictly represented with three stacked compartments:
            </p>
            <ul style="font-size: 0.84rem; color: #334155; line-height: 1.8; padding-left: 20px;">
                <li><strong>Top Compartment (Class Name):</strong> Represents the class identifier (e.g. <code>Person</code>, <code>Donor</code>, <code>BloodStock</code>). Stereotypes like <code>&lt;&lt;Service&gt;&gt;</code> denote architectural layers.</li>
                <li><strong>Middle Compartment (Attributes):</strong> Formatted as <code>visibility name: type [= default]</code>. Example: <code>+age: int</code>, <code>-unitsDonated: int = 1</code>.</li>
                <li><strong>Bottom Compartment (Operations / Methods):</strong> Formatted as <code>visibility name(parameters): returnType</code>. Example: <code>+isAgeEligible(): boolean</code>, <code>+incrementStock(units: int): boolean</code>.</li>
            </ul>
        </div>

        <!-- Card 2: Inheritance & Relationships -->
        <div class="info-card">
            <h3>🔗 Object-Oriented Relationships</h3>
            <ul style="font-size: 0.84rem; color: #334155; line-height: 1.8; padding-left: 20px;">
                <li><strong>Generalization / Inheritance (&Delta; hollow triangle):</strong> <code>Donor</code>, <code>Phlebotomist</code>, and <code>HospitalRepresentative</code> all inherit base demographic attributes (<code>id</code>, <code>name</code>, <code>contactNumber</code>) from the common parent class <code>Person</code>.</li>
                <li><strong>Directed Association (&rarr;):</strong> <code>Donor</code> "1" makes "0..*" <code>Donation</code>; each <code>Donation</code> increments "1" <code>BloodStock</code>; each <code>HospitalRequest</code> requisitions "1" <code>BloodStock</code>.</li>
                <li><strong>Dependency (..&rarr;):</strong> Business services (<code>DonorEligibilityService</code>, <code>InventoryService</code>) depend on domain models to perform clinical checks.</li>
            </ul>
        </div>

        <!-- Card 3: Java Implementation Mapping -->
        <div class="info-card">
            <h3>☕ Java Source Code Mapping</h3>
            <p style="font-size: 0.85rem; color: #475569; margin-bottom: 10px;">
                Every class in this diagram maps directly to compiled Java SE classes in the repository:
            </p>
            <div style="background: #f1f5f9; padding: 12px; border-radius: 8px; font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; line-height: 1.7; color: #0f172a;">
                • com.bloodbank.model.Donor.java<br>
                • com.bloodbank.model.Donation.java<br>
                • com.bloodbank.model.BloodStock.java<br>
                • com.bloodbank.model.HospitalRequest.java<br>
                • com.bloodbank.service.DonorEligibilityService.java<br>
                • com.bloodbank.service.InventoryService.java
            </div>
        </div>
    </div>

    <!-- Academic Footer -->
    <footer>
        <p><strong>Department of Information Technology</strong> • Velalar College of Engineering and Technology, Erode - 638012</p>
        <p style="margin-top: 4px;">Course: 25ITT33 Software Engineering & 25ITT32 Java Programming | Scenario 15</p>
        <p style="margin-top: 4px; color: #0284c7; font-weight: 600;">Student: Karan Raajaa V (732925ITR045) • Class: 25IT3A • Roll No: 45</p>
    </footer>
</div>

<script>
    let currentZoom = 1.0;
    const svgWrapper = document.getElementById('svgWrapper');

    function zoomIn() {{
        if (currentZoom < 2.0) {{
            currentZoom += 0.15;
            applyZoom();
        }}
    }}

    function zoomOut() {{
        if (currentZoom > 0.5) {{
            currentZoom -= 0.15;
            applyZoom();
        }}
    }}

    function resetZoom() {{
        currentZoom = 1.0;
        applyZoom();
    }}

    function applyZoom() {{
        svgWrapper.style.transform = `scale(${{currentZoom}})`;
    }}

    function filterClasses(viewName, evt) {{
        document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
        if (evt && evt.target) {{
            evt.target.classList.add('active');
        }}

        const inheritanceGroup = ['class-person', 'class-donor', 'class-phlebotomist', 'class-hospital-rep', 'inheritance-lines'];
        const entitiesGroup = ['class-donation', 'class-bloodstock', 'class-hospital-request', 'association-lines'];
        const servicesGroup = ['class-eligibility-service', 'class-inventory-service', 'dependency-lines'];

        const allGroups = [...inheritanceGroup, ...entitiesGroup, ...servicesGroup];

        if (viewName === 'all') {{
            allGroups.forEach(id => {{
                const el = document.getElementById(id);
                if (el) {{
                    el.classList.remove('dimmed');
                    el.classList.remove('highlighted');
                }}
            }});
            return;
        }}

        let activeIds = [];
        if (viewName === 'inheritance') activeIds = inheritanceGroup;
        else if (viewName === 'entities') activeIds = entitiesGroup;
        else if (viewName === 'services') activeIds = servicesGroup;

        allGroups.forEach(id => {{
            const el = document.getElementById(id);
            if (el) {{
                if (activeIds.includes(id)) {{
                    el.classList.remove('dimmed');
                    el.classList.add('highlighted');
                }} else {{
                    el.classList.add('dimmed');
                    el.classList.remove('highlighted');
                }}
            }}
        }});
    }}
</script>

</body>
</html>
'''

    out_path = os.path.join("diagrams", "class_diagram.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated {out_path} ({len(html_content)} bytes)")

if __name__ == '__main__':
    build_class_html()
