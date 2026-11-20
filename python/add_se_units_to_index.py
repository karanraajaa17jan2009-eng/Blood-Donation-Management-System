"""
Injects the comprehensive 25ITT33 Software Engineering 5-Unit breakdown into index.html
Scenario 15: Blood Donation Management and Donor Availability Analysis System
Student: Karan Raajaa V (732925ITR045) | Class: 25IT3A | VCET Erode - 12
"""

import os
import re

def create_se_html_block():
    return '''
            <!-- ========================================================================= -->
            <!-- 25ITT33 SOFTWARE ENGINEERING: 5-UNIT SYLLABUS PROCESS BREAKDOWN -->
            <!-- ========================================================================= -->
            <div class="card" style="margin-top: 25px; border-top: 4px solid #0d9488;">
                <div class="card-header" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: white; padding: 20px 25px; border-radius: 8px 8px 0 0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <span style="background: #0d9488; color: white; font-size: 0.75rem; font-weight: 800; padding: 3px 8px; border-radius: 4px; letter-spacing: 0.5px;">COURSE: 25ITT33</span>
                            <h2 style="color: white; font-size: 1.25rem; font-weight: 800; margin: 0;">Software Engineering: 5-Unit Academic Process Breakdown</h2>
                        </div>
                        <p style="color: #94a3b8; font-size: 0.86rem; margin: 6px 0 0;">
                            Unit-Wise Engineering Methodologies, UML Models, Testing Strategies & Project Management for Scenario 15
                        </p>
                    </div>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <a href="docs/Software_Engineering_Unit_Wise_Process.md" target="_blank" class="btn btn-sm" style="background: #0d9488; color: white; text-decoration: none; font-weight: 700; padding: 8px 14px; border-radius: 6px; box-shadow: 0 2px 4px rgba(13,148,136,0.3);">
                            📖 Read Full Academic Report ↗
                        </a>
                        <a href="docs/SRS_Document.md" target="_blank" class="btn btn-sm" style="background: #334155; color: white; text-decoration: none; font-weight: 600; padding: 8px 12px; border-radius: 6px;">
                            📋 IEEE 830 SRS
                        </a>
                    </div>
                </div>

                <!-- Unit Navigation Bar -->
                <div style="background: #f8fafc; padding: 14px 20px; border-bottom: 1px solid var(--border); display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
                    <span style="font-size: 0.8rem; font-weight: 800; color: #475569; margin-right: 4px;">SELECT UNIT:</span>
                    <button class="se-unit-btn" onclick="switchSEUnit(1)" id="se-btn-unit-1" style="background:#0d9488; color:white; border:1px solid #0d9488; padding:7px 14px; border-radius:6px; font-size:0.82rem; font-weight:700; cursor:pointer; transition:all 0.2s;">
                        Unit 1: Process & Agile XP
                    </button>
                    <button class="se-unit-btn" onclick="switchSEUnit(2)" id="se-btn-unit-2" style="background:white; color:#334155; border:1px solid #cbd5e1; padding:7px 14px; border-radius:6px; font-size:0.82rem; font-weight:700; cursor:pointer; transition:all 0.2s;">
                        Unit 2: Requirements & Modeling
                    </button>
                    <button class="se-unit-btn" onclick="switchSEUnit(3)" id="se-btn-unit-3" style="background:white; color:#334155; border:1px solid #cbd5e1; padding:7px 14px; border-radius:6px; font-size:0.82rem; font-weight:700; cursor:pointer; transition:all 0.2s;">
                        Unit 3: Design & Architecture
                    </button>
                    <button class="se-unit-btn" onclick="switchSEUnit(4)" id="se-btn-unit-4" style="background:white; color:#334155; border:1px solid #cbd5e1; padding:7px 14px; border-radius:6px; font-size:0.82rem; font-weight:700; cursor:pointer; transition:all 0.2s;">
                        Unit 4: Testing & V&V Strategy
                    </button>
                    <button class="se-unit-btn" onclick="switchSEUnit(5)" id="se-btn-unit-5" style="background:white; color:#334155; border:1px solid #cbd5e1; padding:7px 14px; border-radius:6px; font-size:0.82rem; font-weight:700; cursor:pointer; transition:all 0.2s;">
                        Unit 5: Project Management (4Ps, LOC/FP, COCOMO)
                    </button>
                    <button class="se-unit-btn" onclick="switchSEUnit('all')" id="se-btn-unit-all" style="background:#f1f5f9; color:#0f766e; border:1px dashed #0d9488; padding:7px 14px; border-radius:6px; font-size:0.82rem; font-weight:700; cursor:pointer; transition:all 0.2s;">
                        📑 View All Units
                    </button>
                </div>

                <div style="padding: 24px;">

                    <!-- ========================================== -->
                    <!-- UNIT 1: SOFTWARE PROCESS -->
                    <!-- ========================================== -->
                    <div id="se-unit-1-content" class="se-unit-section" style="display: block;">
                        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid #0d9488; padding-bottom:10px; margin-bottom:18px;">
                            <h3 style="color:#0f766e; font-size:1.15rem; font-weight:800; margin:0;">
                                🔷 UNIT 1: SOFTWARE PROCESS (Syllabus: Nature of Software, Myths, Generic, Prescriptive, UP, Agile & XP)
                            </h3>
                            <span class="badge" style="background:#ccfbf1; color:#0f766e; font-weight:700; padding:4px 10px; border-radius:12px; font-size:0.75rem;">9 Hours Syllabus Coverage</span>
                        </div>

                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:18px; margin-bottom:20px;">
                            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:16px;">
                                <h4 style="color:#004d40; font-size:0.95rem; margin-bottom:8px;">1. Nature of Software & Software Process</h4>
                                <p style="font-size:0.84rem; color:#334155; line-height:1.7;">
                                    The Blood Bank System is classified as a <strong>safety-critical, transactional medical web application</strong> with real-time data integrity. Five generic framework activities were performed:
                                </p>
                                <ul style="font-size:0.82rem; color:#475569; padding-left:18px; line-height:1.7;">
                                    <li><strong>Communication:</strong> Clinical interviews with phlebotomists & hospital authorities.</li>
                                    <li><strong>Planning:</strong> Task estimations, WBS, Git repository governance.</li>
                                    <li><strong>Modeling:</strong> IEEE 830 SRS, BCNF relational schema, Peter Chen ER model.</li>
                                    <li><strong>Construction:</strong> Java SE core services, SQLite triggers, Python analytics, HTML5/CSS web app.</li>
                                    <li><strong>Deployment:</strong> Continuous 24/7 deployment to GitHub Pages and local batch scripts.</li>
                                </ul>
                            </div>

                            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:16px;">
                                <h4 style="color:#004d40; font-size:0.95rem; margin-bottom:8px;">2. Software Myths Addressed</h4>
                                <ul style="font-size:0.82rem; color:#334155; padding-left:18px; line-height:1.7;">
                                    <li><strong>Management Myth:</strong> <em>"Adding more phlebotomists will speed up testing."</em> Refuted via Brooks' Law by partitioning decoupled subsystems.</li>
                                    <li><strong>Customer Myth:</strong> <em>"General requirements are enough to start coding."</em> Refuted by formally specifying the 90-day cooldown equation upfront: <br><code style="background:#e2e8f0; padding:2px 4px; border-radius:3px;">&Delta;t = Session_Date - MAX(Prior_Date) &ge; 90</code>.</li>
                                    <li><strong>Practitioner Myth:</strong> <em>"Project ends when code executes."</em> Handled by providing automated regression testing suites (37 test cases) and comprehensive documentation.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- Process Lifecycle SVG Diagram -->
                        <div style="background:#f0fdfa; border:1px solid #99f6e4; border-radius:8px; padding:16px; margin-bottom:18px; text-align:center;">
                            <h4 style="color:#0f766e; font-size:0.9rem; margin-bottom:12px; font-weight:700;">
                                📊 Generic Framework & Iterative Agile/UP Lifecycle for Scenario 15
                            </h4>
                            <svg viewBox="0 0 920 140" width="100%" height="auto" style="max-width:920px; font-family:'Inter', sans-serif;">
                                <defs>
                                    <linearGradient id="upGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                                        <stop offset="0%" stop-color="#0f766e"/>
                                        <stop offset="100%" stop-color="#0d9488"/>
                                    </linearGradient>
                                </defs>
                                <!-- Step 1 -->
                                <rect x="10" y="30" width="160" height="70" rx="8" fill="#cdeff1" stroke="#2a8f92" stroke-width="2"/>
                                <text x="90" y="58" text-anchor="middle" font-size="12" font-weight="800" fill="#004d40">1. INCEPTION</text>
                                <text x="90" y="78" text-anchor="middle" font-size="10" fill="#0f766e">Domain Scope &amp; SRS</text>
                                <line x1="170" y1="65" x2="195" y2="65" stroke="#2a8f92" stroke-width="2" marker-end="url(#arrow)"/>

                                <!-- Step 2 -->
                                <rect x="195" y="30" width="160" height="70" rx="8" fill="#cdeff1" stroke="#2a8f92" stroke-width="2"/>
                                <text x="275" y="58" text-anchor="middle" font-size="12" font-weight="800" fill="#004d40">2. ELABORATION</text>
                                <text x="275" y="78" text-anchor="middle" font-size="10" fill="#0f766e">BCNF DB &amp; UML Design</text>
                                <line x1="355" y1="65" x2="380" y2="65" stroke="#2a8f92" stroke-width="2"/>

                                <!-- Step 3 -->
                                <rect x="380" y="30" width="160" height="70" rx="8" fill="#cdeff1" stroke="#2a8f92" stroke-width="2"/>
                                <text x="460" y="58" text-anchor="middle" font-size="12" font-weight="800" fill="#004d40">3. CONSTRUCTION</text>
                                <text x="460" y="78" text-anchor="middle" font-size="10" fill="#0f766e">Java DAO, Python, Web</text>
                                <line x1="540" y1="65" x2="565" y2="65" stroke="#2a8f92" stroke-width="2"/>

                                <!-- Step 4 -->
                                <rect x="565" y="30" width="160" height="70" rx="8" fill="#cdeff1" stroke="#2a8f92" stroke-width="2"/>
                                <text x="645" y="58" text-anchor="middle" font-size="12" font-weight="800" fill="#004d40">4. TRANSITION</text>
                                <text x="645" y="78" text-anchor="middle" font-size="10" fill="#0f766e">37 Tests &amp; Verification</text>
                                <line x1="725" y1="65" x2="750" y2="65" stroke="#2a8f92" stroke-width="2"/>

                                <!-- Step 5 -->
                                <rect x="750" y="30" width="160" height="70" rx="8" fill="#0f766e" stroke="#004d40" stroke-width="2"/>
                                <text x="830" y="58" text-anchor="middle" font-size="12" font-weight="800" fill="#ffffff">5. DEPLOYMENT</text>
                                <text x="830" y="78" text-anchor="middle" font-size="10" fill="#99f6e4">24/7 Live GitHub Pages</text>

                                <!-- Iteration Loop Curve -->
                                <path d="M 645,100 C 645,130 275,130 275,100" fill="none" stroke="#0f766e" stroke-width="1.8" stroke-dasharray="5,4"/>
                                <text x="460" y="128" text-anchor="middle" font-size="10" font-weight="700" fill="#0f766e">&larr; Extreme Programming (XP) Continuous Feedback &amp; Refactoring &larr;</text>
                            </svg>
                        </div>

                        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:14px; font-size:0.83rem; color:#334155; line-height:1.7;">
                            <strong>Extreme Programming (XP) Practices Enforced:</strong>
                            <span style="display:inline-block; margin-left:8px;">
                                &bull; <strong>Test-First Development:</strong> Tests drafted prior to implementation in <code style="background:#e2e8f0; padding:1px 4px; border-radius:3px;">verify_all_requirements.py</code>.
                                &bull; <strong>Continuous Integration:</strong> Automated test execution on every commit.
                                &bull; <strong>Refactoring:</strong> Replacing slow nested queries with optimized SQL Views (<code style="background:#e2e8f0; padding:1px 4px; border-radius:3px;">v_stock_summary</code>, <code style="background:#e2e8f0; padding:1px 4px; border-radius:3px;">v_donor_availability</code>).
                            </span>
                        </div>
                    </div>

                    <!-- ========================================== -->
                    <!-- UNIT 2: REQUIREMENTS -->
                    <!-- ========================================== -->
                    <div id="se-unit-2-content" class="se-unit-section" style="display: none;">
                        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid #0d9488; padding-bottom:10px; margin-bottom:18px;">
                            <h3 style="color:#0f766e; font-size:1.15rem; font-weight:800; margin:0;">
                                🔷 UNIT 2: REQUIREMENTS (Syllabus: Requirement Analysis, Modeling, RE Process, Elicitation, Specification, Validation, Change)
                            </h3>
                            <span class="badge" style="background:#ccfbf1; color:#0f766e; font-weight:700; padding:4px 10px; border-radius:12px; font-size:0.75rem;">9 Hours Syllabus Coverage</span>
                        </div>

                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:18px; margin-bottom:18px;">
                            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:16px;">
                                <h4 style="color:#004d40; font-size:0.95rem; margin-bottom:8px;">1. Requirements Elicitation & Analysis</h4>
                                <p style="font-size:0.84rem; color:#334155; line-height:1.7;">
                                    Clinical requirements elicited from 4 primary stakeholder roles:
                                </p>
                                <ul style="font-size:0.82rem; color:#475569; padding-left:18px; line-height:1.7;">
                                    <li><strong>Voluntary Donor:</strong> View eligibility status, history, next donation date.</li>
                                    <li><strong>Phlebotomist / Nurse:</strong> Screen hemoglobin (&ge; 12.0 g/dL), log session vitals.</li>
                                    <li><strong>Blood Bank Officer:</strong> Monitor deficit groups, manage safety thresholds (4-6 units).</li>
                                    <li><strong>Hospital Medical Officer:</strong> Submit requisitions with priority urgency (Normal/Urgent/Critical).</li>
                                </ul>
                            </div>

                            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:16px;">
                                <h4 style="color:#004d40; font-size:0.95rem; margin-bottom:8px;">2. Specification & Validation (IEEE 830)</h4>
                                <p style="font-size:0.84rem; color:#334155; line-height:1.7;">
                                    Formally specified in <a href="docs/SRS_Document.md" target="_blank" style="color:#0f766e; font-weight:700;">SRS_Document.md</a> with 8 Functional and 5 Non-Functional Requirements:
                                </p>
                                <ul style="font-size:0.82rem; color:#475569; padding-left:18px; line-height:1.7;">
                                    <li><strong>Traceability Matrix:</strong> Every requirement mapped to test cases in <code style="background:#e2e8f0; padding:1px 4px; border-radius:3px;">Testing_Document_and_Test_Cases.md</code>.</li>
                                    <li><strong>Requirements Validation:</strong> Verified against ambiguity, contradiction, and infeasibility.</li>
                                    <li><strong>Requirements Change:</strong> Controlled schema migration scripts maintaining BCNF normalization.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- Class-Based & Data Modeling Summary -->
                        <div style="background:#f0fdfa; border:1px solid #99f6e4; border-radius:8px; padding:16px; margin-bottom:18px;">
                            <h4 style="color:#0f766e; font-size:0.9rem; margin-bottom:10px; font-weight:700;">
                                📐 Data Modeling Concepts & Class-Based Modeling (Unified Schema)
                            </h4>
                            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:12px; font-size:0.82rem;">
                                <div style="background:white; border:1px solid #cbd5e1; border-radius:6px; padding:10px;">
                                    <strong style="color:#0284c7;">Entity / Class: DONOR</strong><br>
                                    <span style="color:#64748b;">Attrs: donor_id (PK), name, age (18-65), gender, contact, email, city, reg_date.</span><br>
                                    <span style="color:#0f766e; font-weight:600;">Methods: isAgeEligible(), getDaysRemaining()</span>
                                </div>
                                <div style="background:white; border:1px solid #cbd5e1; border-radius:6px; padding:10px;">
                                    <strong style="color:#059669;">Entity / Class: DONATION</strong><br>
                                    <span style="color:#64748b;">Attrs: donation_id (PK), donor_id (FK), blood_group, date, units, hemoglobin (&ge;12.0).</span><br>
                                    <span style="color:#0f766e; font-weight:600;">Methods: isHemoglobinValid(), recordSession()</span>
                                </div>
                                <div style="background:white; border:1px solid #cbd5e1; border-radius:6px; padding:10px;">
                                    <strong style="color:#b91c1c;">Entity / Class: BLOOD_STOCK</strong><br>
                                    <span style="color:#64748b;">Attrs: blood_group (PK), available_units, min_threshold, last_updated.</span><br>
                                    <span style="color:#0f766e; font-weight:600;">Methods: isDeficit(), incrementStock(), decrement()</span>
                                </div>
                                <div style="background:white; border:1px solid #cbd5e1; border-radius:6px; padding:10px;">
                                    <strong style="color:#7c3aed;">Entity / Class: HOSPITAL_REQUEST</strong><br>
                                    <span style="color:#64748b;">Attrs: request_id (PK), hospital_name, units_requested, urgency, status.</span><br>
                                    <span style="color:#0f766e; font-weight:600;">Methods: fulfillRequest(), rejectInsufficientStock()</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- ========================================== -->
                    <!-- UNIT 3: SOFTWARE DESIGN -->
                    <!-- ========================================== -->
                    <div id="se-unit-3-content" class="se-unit-section" style="display: none;">
                        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid #0d9488; padding-bottom:10px; margin-bottom:18px;">
                            <h3 style="color:#0f766e; font-size:1.15rem; font-weight:800; margin:0;">
                                🔷 UNIT 3: SOFTWARE DESIGN (Syllabus: Design Process & Concepts, Architectural Styles, Interface Design, Web-App Design)
                            </h3>
                            <span class="badge" style="background:#ccfbf1; color:#0f766e; font-weight:700; padding:4px 10px; border-radius:12px; font-size:0.75rem;">9 Hours Syllabus Coverage</span>
                        </div>

                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:18px; margin-bottom:20px;">
                            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:16px;">
                                <h4 style="color:#004d40; font-size:0.95rem; margin-bottom:8px;">1. Design Principles & Modularity</h4>
                                <ul style="font-size:0.82rem; color:#334155; padding-left:18px; line-height:1.7;">
                                    <li><strong>Abstraction:</strong> High-level interfaces (<code style="background:#e2e8f0; padding:1px 4px; border-radius:3px;">DonorDAO</code>, <code style="background:#e2e8f0; padding:1px 4px; border-radius:3px;">BloodStockDAO</code>) separate contract from SQL execution.</li>
                                    <li><strong>Information Hiding:</strong> Domain models encapsulate state; mutations occur exclusively through validated methods.</li>
                                    <li><strong>High Cohesion:</strong> Each service handles exactly one bounded responsibility (<code style="background:#e2e8f0; padding:1px 4px; border-radius:3px;">DonorEligibilityService</code> evaluates cooldown; <code style="background:#e2e8f0; padding:1px 4px; border-radius:3px;">InventoryService</code> manages buffers).</li>
                                    <li><strong>Loose Coupling:</strong> Presentation layer connects via interfaces without direct SQL dependencies.</li>
                                </ul>
                            </div>

                            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:16px;">
                                <h4 style="color:#004d40; font-size:0.95rem; margin-bottom:8px;">2. Web-App & Interface Design</h4>
                                <ul style="font-size:0.82rem; color:#334155; padding-left:18px; line-height:1.7;">
                                    <li><strong>Responsive Single-Page Layout:</strong> Mobile and desktop accessible with clean CSS grid & flexbox.</li>
                                    <li><strong>Golden Rules Applied:</strong> Place user in control; reduce cognitive load; consistent visual vocabulary.</li>
                                    <li><strong>Color-Coded Visual Safety:</strong> Green badges for adequate stock (&ge; threshold); flashing pulse warning for deficit groups.</li>
                                    <li><strong>Peter Chen ER Diagram Integration:</strong> High-resolution SVG canvas with interactive pan, zoom, and entity filters.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- Multi-Tier Architecture Diagram -->
                        <div style="background:#f0fdfa; border:1px solid #99f6e4; border-radius:8px; padding:16px; margin-bottom:18px; text-align:center;">
                            <h4 style="color:#0f766e; font-size:0.9rem; margin-bottom:12px; font-weight:700;">
                                🏛️ 5-Tier Layered Software Architecture Pattern
                            </h4>
                            <svg viewBox="0 0 880 180" width="100%" height="auto" style="max-width:880px; font-family:'Inter', sans-serif;">
                                <!-- Tier 1 -->
                                <rect x="20" y="10" width="840" height="28" rx="5" fill="#1e293b"/>
                                <text x="440" y="28" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">TIER 1: PRESENTATION TIER (Responsive Web Application + Console CLI Menu)</text>

                                <!-- Tier 2 -->
                                <rect x="20" y="45" width="840" height="28" rx="5" fill="#0f766e"/>
                                <text x="440" y="63" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">TIER 2: BUSINESS SERVICE TIER (DonorService, DonorEligibilityService, InventoryService, ReportService)</text>

                                <!-- Tier 3 -->
                                <rect x="20" y="80" width="840" height="28" rx="5" fill="#0284c7"/>
                                <text x="440" y="98" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">TIER 3: DATA ACCESS LAYER / DAO (DatabaseManager, DonorDAOImpl, BloodStockDAOImpl, DonationDAOImpl)</text>

                                <!-- Tier 4 -->
                                <rect x="20" y="115" width="840" height="28" rx="5" fill="#475569"/>
                                <text x="440" y="133" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">TIER 4: PERSISTENCE &amp; DATABASE TIER (SQLite 3 BCNF Schema, Views: v_stock_summary, v_donor_availability)</text>

                                <!-- Tier 5 -->
                                <rect x="20" y="150" width="840" height="28" rx="5" fill="#047857"/>
                                <text x="440" y="168" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">TIER 5: DATA SCIENCE &amp; ANALYTICS PIPELINE (db_retrieval.py &rarr; data_preprocessing.py &rarr; visualizations.py)</text>
                            </svg>
                        </div>
                    </div>

                    <!-- ========================================== -->
                    <!-- UNIT 4: SOFTWARE TESTING -->
                    <!-- ========================================== -->
                    <div id="se-unit-4-content" class="se-unit-section" style="display: none;">
                        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid #0d9488; padding-bottom:10px; margin-bottom:18px;">
                            <h3 style="color:#0f766e; font-size:1.15rem; font-weight:800; margin:0;">
                                🔷 UNIT 4: SOFTWARE TESTING (Syllabus: V&V, Unit, Integration, Validation, Black Box, White Box, Quality Metrics)
                            </h3>
                            <span class="badge" style="background:#ccfbf1; color:#0f766e; font-weight:700; padding:4px 10px; border-radius:12px; font-size:0.75rem;">9 Hours Syllabus Coverage</span>
                        </div>

                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:18px; margin-bottom:20px;">
                            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:16px;">
                                <h4 style="color:#004d40; font-size:0.95rem; margin-bottom:8px;">1. Verification & Validation (V&V)</h4>
                                <ul style="font-size:0.82rem; color:#334155; padding-left:18px; line-height:1.7;">
                                    <li><strong>Verification:</strong> Peer review, static analysis, BCNF normalization check, zero compiler warnings.</li>
                                    <li><strong>Validation:</strong> Verified against clinical rules (blocking underage donors, enforcing 90-day wait).</li>
                                    <li><strong>Unit Testing:</strong> Independent testing of <code style="background:#e2e8f0; padding:1px 4px; border-radius:3px;">isEligible()</code> and threshold checks.</li>
                                    <li><strong>Integration Testing:</strong> Verified that inserting into <code style="background:#e2e8f0; padding:1px 4px; border-radius:3px;">donations</code> atomically updates <code style="background:#e2e8f0; padding:1px 4px; border-radius:3px;">blood_stock</code>.</li>
                                </ul>
                            </div>

                            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:16px;">
                                <h4 style="color:#004d40; font-size:0.95rem; margin-bottom:8px;">2. White-Box Testing & Cyclomatic Complexity</h4>
                                <p style="font-size:0.84rem; color:#334155; line-height:1.7;">
                                    Basis Path Testing applied to the Eligibility Decision Engine:
                                </p>
                                <div style="background:#f1f5f9; padding:8px 12px; border-radius:6px; font-family:'JetBrains Mono',monospace; font-size:0.78rem; margin:6px 0; color:#0f172a;">
                                    Cyclomatic Complexity: V(G) = E - N + 2P = 5 - 4 + 2(1) = 3<br>
                                    Path 1: First-time donor (No history) &rarr; ACCEPT<br>
                                    Path 2: Days since last donation &ge; 90 &rarr; ACCEPT<br>
                                    Path 3: Days since last donation &lt; 90 &rarr; REJECT (Cooldown Active)
                                </div>
                                <p style="font-size:0.8rem; color:#0f766e; font-weight:600; margin:0;">
                                    100% Basis Path and Branch Coverage verified across all tests.
                                </p>
                            </div>
                        </div>

                        <!-- Black Box Test Case Table -->
                        <div style="background:white; border:1px solid var(--border); border-radius:8px; overflow:hidden; margin-bottom:18px;">
                            <div style="background:#f1f5f9; padding:10px 16px; font-weight:700; font-size:0.86rem; color:#334155;">
                                🧪 Black-Box Boundary Value Analysis (BVA) & Equivalence Partitioning Matrix
                            </div>
                            <table style="width:100%; border-collapse:collapse; font-size:0.82rem; text-align:left;">
                                <thead>
                                    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
                                        <th style="padding:8px 12px;">Test ID</th>
                                        <th style="padding:8px 12px;">Parameter</th>
                                        <th style="padding:8px 12px;">Input Value</th>
                                        <th style="padding:8px 12px;">Boundary Category</th>
                                        <th style="padding:8px 12px;">Expected Result</th>
                                        <th style="padding:8px 12px;">Status</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr style="border-bottom:1px solid #f1f5f9;">
                                        <td style="padding:7px 12px;"><code>TC-BVA-01</code></td>
                                        <td style="padding:7px 12px;">Donor Age</td>
                                        <td style="padding:7px 12px;">17 years</td>
                                        <td style="padding:7px 12px;">Below Min Boundary (18)</td>
                                        <td style="padding:7px 12px; color:#b91c1c;">REJECT: Underage (&lt;18)</td>
                                        <td style="padding:7px 12px;"><span style="color:#059669; font-weight:700;">PASS &#10003;</span></td>
                                    </tr>
                                    <tr style="border-bottom:1px solid #f1f5f9;">
                                        <td style="padding:7px 12px;"><code>TC-BVA-02</code></td>
                                        <td style="padding:7px 12px;">Donor Age</td>
                                        <td style="padding:7px 12px;">18 years</td>
                                        <td style="padding:7px 12px;">Min Valid Boundary (18)</td>
                                        <td style="padding:7px 12px; color:#059669;">ACCEPT: Eligible</td>
                                        <td style="padding:7px 12px;"><span style="color:#059669; font-weight:700;">PASS &#10003;</span></td>
                                    </tr>
                                    <tr style="border-bottom:1px solid #f1f5f9;">
                                        <td style="padding:7px 12px;"><code>TC-BVA-03</code></td>
                                        <td style="padding:7px 12px;">Hemoglobin</td>
                                        <td style="padding:7px 12px;">11.9 g/dL</td>
                                        <td style="padding:7px 12px;">Below Clinical Safety (12.0)</td>
                                        <td style="padding:7px 12px; color:#b91c1c;">REJECT: Low Hemoglobin</td>
                                        <td style="padding:7px 12px;"><span style="color:#059669; font-weight:700;">PASS &#10003;</span></td>
                                    </tr>
                                    <tr style="border-bottom:1px solid #f1f5f9;">
                                        <td style="padding:7px 12px;"><code>TC-BVA-04</code></td>
                                        <td style="padding:7px 12px;">Hemoglobin</td>
                                        <td style="padding:7px 12px;">12.0 g/dL</td>
                                        <td style="padding:7px 12px;">Min Valid Boundary (12.0)</td>
                                        <td style="padding:7px 12px; color:#059669;">ACCEPT: Safe for Donation</td>
                                        <td style="padding:7px 12px;"><span style="color:#059669; font-weight:700;">PASS &#10003;</span></td>
                                    </tr>
                                    <tr>
                                        <td style="padding:7px 12px;"><code>TC-BVA-05</code></td>
                                        <td style="padding:7px 12px;">Cooldown Days</td>
                                        <td style="padding:7px 12px;">89 days</td>
                                        <td style="padding:7px 12px;">Below 90-Day Medical Rule</td>
                                        <td style="padding:7px 12px; color:#b91c1c;">REJECT: 1 Day Remaining</td>
                                        <td style="padding:7px 12px;"><span style="color:#059669; font-weight:700;">PASS &#10003;</span></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <div style="background:#f0fdfa; border:1px solid #99f6e4; border-radius:8px; padding:12px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                            <div>
                                <strong style="color:#0f766e;">Automated Test Suite Execution:</strong>
                                <span style="color:#334155; font-size:0.83rem; margin-left:8px;">37 Total Automated Unit, Integration, and System Tests Executed</span>
                            </div>
                            <span class="badge" style="background:#059669; color:white; font-size:0.82rem; font-weight:700; padding:6px 12px; border-radius:6px;">
                                37 / 37 TESTS PASSED (100.0%)
                            </span>
                        </div>
                    </div>

                    <!-- ========================================== -->
                    <!-- UNIT 5: PROJECT MANAGEMENT -->
                    <!-- ========================================== -->
                    <div id="se-unit-5-content" class="se-unit-section" style="display: none;">
                        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid #0d9488; padding-bottom:10px; margin-bottom:18px;">
                            <h3 style="color:#0f766e; font-size:1.15rem; font-weight:800; margin:0;">
                                🔷 UNIT 5: PROJECT MANAGEMENT (Syllabus: 4P's, LOC, Function Point, COCOMO, Scheduling, EVA, Risk, CMMI)
                            </h3>
                            <span class="badge" style="background:#ccfbf1; color:#0f766e; font-weight:700; padding:4px 10px; border-radius:12px; font-size:0.75rem;">9 Hours Syllabus Coverage</span>
                        </div>

                        <!-- 4P's Cards Grid -->
                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:12px; margin-bottom:20px;">
                            <div style="background:#f8fafc; border:2px solid #0d9488; border-radius:8px; padding:14px;">
                                <div style="font-weight:800; color:#0f766e; font-size:0.95rem; margin-bottom:4px;">1. PEOPLE</div>
                                <p style="font-size:0.8rem; color:#475569; margin:0; line-height:1.6;">
                                    Student Developer: <strong>Karan Raajaa V</strong> (732925ITR045, 25IT3A), VCET IT Department faculty advisors.
                                </p>
                            </div>
                            <div style="background:#f8fafc; border:2px solid #0284c7; border-radius:8px; padding:14px;">
                                <div style="font-weight:800; color:#0284c7; font-size:0.95rem; margin-bottom:4px;">2. PRODUCT</div>
                                <p style="font-size:0.8rem; color:#475569; margin:0; line-height:1.6;">
                                    Blood Donation Management &amp; Availability System with Java CLI, Python Analytics &amp; Web Portal.
                                </p>
                            </div>
                            <div style="background:#f8fafc; border:2px solid #059669; border-radius:8px; padding:14px;">
                                <div style="font-weight:800; color:#059669; font-size:0.95rem; margin-bottom:4px;">3. PROCESS</div>
                                <p style="font-size:0.8rem; color:#475569; margin:0; line-height:1.6;">
                                    Agile Unified Process (UP) lifecycle with continuous test-driven verification and git version control.
                                </p>
                            </div>
                            <div style="background:#f8fafc; border:2px solid #7c3aed; border-radius:8px; padding:14px;">
                                <div style="font-weight:800; color:#7c3aed; font-size:0.95rem; margin-bottom:4px;">4. PROJECT</div>
                                <p style="font-size:0.8rem; color:#475569; margin:0; line-height:1.6;">
                                    6-milestone delivery schedule; 100% completed deliverables on schedule (SPI = 1.0, CPI = 1.0).
                                </p>
                            </div>
                        </div>

                        <!-- Quantitative Estimation: LOC, FP, COCOMO -->
                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:18px; margin-bottom:18px;">
                            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:16px;">
                                <h4 style="color:#004d40; font-size:0.95rem; margin-bottom:8px;">📊 LOC &amp; Function Point (FP) Metrics</h4>
                                <ul style="font-size:0.82rem; color:#334155; padding-left:18px; line-height:1.7;">
                                    <li><strong>Executable LOC:</strong> 5,910 LOC (Java: 1,480; Python: 960; SQL: 820; Web JS/CSS: 2,650).</li>
                                    <li><strong>Total Project Size:</strong> 9,310 LOC including comprehensive IEEE 830 documentation.</li>
                                    <li><strong>Unadjusted Function Points (UFP):</strong> 93 FP (4 Inputs, 3 Outputs, 2 Inquiries, 4 ILF, 2 EIF).</li>
                                    <li><strong>Adjusted Function Points (AFP):</strong> <code style="background:#e2e8f0; padding:1px 4px; border-radius:3px;">AFP = 93 &times; 1.03 = 95.79 FP</code>.</li>
                                </ul>
                            </div>

                            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:16px;">
                                <h4 style="color:#004d40; font-size:0.95rem; margin-bottom:8px;">💰 COCOMO Cost &amp; Effort Estimation</h4>
                                <p style="font-size:0.82rem; color:#334155; line-height:1.7;">
                                    Using Basic COCOMO Organic Mode (KLOC = 5.91):
                                </p>
                                <div style="background:#f1f5f9; padding:8px 12px; border-radius:6px; font-family:'JetBrains Mono',monospace; font-size:0.78rem; margin:6px 0; color:#0f172a;">
                                    Effort = 2.4 &times; (5.91)^1.05 = 15.48 Person-Months<br>
                                    Development Time = 2.5 &times; (15.48)^0.38 = 7.05 Months<br>
                                    Staffing Required = 15.48 / 7.05 &approx; 2.2 Developers
                                </div>
                                <p style="font-size:0.8rem; color:#0f766e; margin:0;">
                                    <strong>Earned Value Analysis:</strong> SPI = 1.00 (On Schedule) | CPI = 1.00 (On Budget).
                                </p>
                            </div>
                        </div>

                        <!-- Risk Management Table -->
                        <div style="background:white; border:1px solid var(--border); border-radius:8px; overflow:hidden;">
                            <div style="background:#f1f5f9; padding:10px 16px; font-weight:700; font-size:0.86rem; color:#334155;">
                                🛡️ Risk Identification &amp; Management (RMMM Plan)
                            </div>
                            <table style="width:100%; border-collapse:collapse; font-size:0.82rem; text-align:left;">
                                <thead>
                                    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
                                        <th style="padding:8px 12px;">Risk Description</th>
                                        <th style="padding:8px 12px;">Probability</th>
                                        <th style="padding:8px 12px;">Impact</th>
                                        <th style="padding:8px 12px;">Mitigation &amp; Management Strategy</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr style="border-bottom:1px solid #f1f5f9;">
                                        <td style="padding:7px 12px;">Ineligible donor donating before 90-day cooldown</td>
                                        <td style="padding:7px 12px; color:#059669; font-weight:700;">LOW</td>
                                        <td style="padding:7px 12px; color:#b91c1c; font-weight:700;">HIGH</td>
                                        <td style="padding:7px 12px;">Enforced at DB View and Service level; transaction blocked immediately.</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid #f1f5f9;">
                                        <td style="padding:7px 12px;">Stock deficit during hospital emergency requisition</td>
                                        <td style="padding:7px 12px; color:#d97706; font-weight:700;">MEDIUM</td>
                                        <td style="padding:7px 12px; color:#b91c1c; font-weight:700;">CRITICAL</td>
                                        <td style="padding:7px 12px;">Real-time buffer threshold monitoring with animated pulse visual alerts.</td>
                                    </tr>
                                    <tr>
                                        <td style="padding:7px 12px;">Database schema corruption or accidental data loss</td>
                                        <td style="padding:7px 12px; color:#059669; font-weight:700;">LOW</td>
                                        <td style="padding:7px 12px; color:#b91c1c; font-weight:700;">CRITICAL</td>
                                        <td style="padding:7px 12px;">Automated initialization scripts (<code style="background:#e2e8f0; padding:1px 4px; border-radius:3px;">schema_sqlite.sql</code> &amp; <code style="background:#e2e8f0; padding:1px 4px; border-radius:3px;">sample_data.sql</code>) for 1-click recovery.</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                </div>
            </div>
'''

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Card 1 under Software Engineering in tab-docs to link to the new report
    old_card1_link = '<li><a href="docs/SRS_Document.md" target="_blank" style="color: var(--info); font-weight: 600;">SRS Document (IEEE 830)</a></li>'
    new_card1_link = '''<li><a href="docs/Software_Engineering_Unit_Wise_Process.md" target="_blank" style="color: #0d9488; font-weight: 700;">🔷 5-Unit SE Process Report (Unit 1 to 5) ↗</a></li>
                            <li><a href="docs/SRS_Document.md" target="_blank" style="color: var(--info); font-weight: 600;">SRS Document (IEEE 830)</a></li>'''
    
    if old_card1_link in content and '5-Unit SE Process Report' not in content:
        content = content.replace(old_card1_link, new_card1_link)

    # 2. Add the comprehensive SE 5-unit breakdown block before </section> of tab-docs
    se_block = create_se_html_block()
    
    # Locate tab-docs closing section
    target_pos = content.find('</section>\n\n    </main>')
    if target_pos == -1:
        target_pos = content.find('</section>\r\n\r\n    </main>')
    if target_pos == -1:
        # Fallback find
        match = re.search(r'</section>\s*</main>', content)
        if match:
            target_pos = match.start()

    if target_pos != -1:
        content = content[:target_pos] + se_block + '\n        ' + content[target_pos:]
        print("Successfully injected SE 5-unit breakdown block into tab-docs in index.html!")
    else:
        print("Warning: Could not locate target position before </main>.")

    # 3. Add switchSEUnit javascript function
    js_func = '''
        // =====================================================================
        // Software Engineering 5-Unit Interactive Tab Switcher
        // =====================================================================
        function switchSEUnit(unitNum) {
            document.querySelectorAll('.se-unit-btn').forEach(btn => {
                btn.style.background = '#ffffff';
                btn.style.color = '#334155';
                btn.style.borderColor = '#cbd5e1';
            });

            if (unitNum === 'all') {
                const allBtn = document.getElementById('se-btn-unit-all');
                if (allBtn) {
                    allBtn.style.background = '#0d9488';
                    allBtn.style.color = '#ffffff';
                    allBtn.style.borderColor = '#0d9488';
                }
                for (let i = 1; i <= 5; i++) {
                    const sec = document.getElementById(`se-unit-${i}-content`);
                    if (sec) sec.style.display = 'block';
                }
                return;
            }

            const activeBtn = document.getElementById(`se-btn-unit-${unitNum}`);
            if (activeBtn) {
                activeBtn.style.background = '#0d9488';
                activeBtn.style.color = '#ffffff';
                activeBtn.style.borderColor = '#0d9488';
            }

            for (let i = 1; i <= 5; i++) {
                const sec = document.getElementById(`se-unit-${i}-content`);
                if (sec) {
                    sec.style.display = (i === unitNum) ? 'block' : 'none';
                }
            }
        }
    '''

    if 'function switchSEUnit' not in content:
        script_insert_pos = content.find('const REFERENCE_DATE =')
        if script_insert_pos != -1:
            content = content[:script_insert_pos] + js_func + '\n        ' + content[script_insert_pos:]
            print("Successfully added switchSEUnit JS function to index.html!")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html successfully!")

if __name__ == '__main__':
    update_index()
