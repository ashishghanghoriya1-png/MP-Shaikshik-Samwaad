import os
import sys
import io
from playwright.sync_api import sync_playwright

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>RSK Shaikshik Samwaad — Data Lineage, Mathematical Provenance & 52-District Quadrant Derivation Report</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    @page {
      size: A4 portrait;
      margin: 12mm 12mm 12mm 12mm;
      @bottom-right {
        content: "Page " counter(page);
        font-family: 'JetBrains Mono', monospace;
        font-size: 8pt;
        color: #64748b;
      }
    }
    
    * {
      box-sizing: border-box;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }

    body {
      margin: 0;
      padding: 0;
      background: #ffffff;
      color: #0f172a;
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      font-size: 8.5pt;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }

    .header-banner {
      background: linear-gradient(135deg, #003366 0%, #008aab 100%);
      color: #ffffff;
      padding: 16px 20px;
      border-radius: 8px;
      margin-bottom: 14px;
    }

    .eyebrow {
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.5pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: #63d0df;
      margin-bottom: 4px;
    }

    .doc-title {
      font-size: 16pt;
      font-weight: 800;
      margin: 0 0 6px 0;
      line-height: 1.2;
      color: #ffffff;
    }

    .doc-subtitle {
      font-size: 8.5pt;
      color: #e2e8f0;
      line-height: 1.4;
    }

    .meta-bar {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      margin-top: 10px;
      padding-top: 8px;
      border-top: 1px solid rgba(255, 255, 255, 0.2);
      font-family: 'JetBrains Mono', monospace;
      font-size: 7pt;
      color: #f1f5f9;
    }

    .meta-bar strong {
      color: #63d0df;
    }

    h2 {
      font-size: 11pt;
      font-weight: 800;
      color: #003366;
      border-bottom: 2px solid #008aab;
      padding-bottom: 4px;
      margin: 14px 0 8px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    h3 {
      font-size: 9pt;
      font-weight: 700;
      color: #008aab;
      margin: 10px 0 4px 0;
    }

    .section-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.5pt;
      font-weight: 700;
      background: rgba(0, 138, 171, 0.1);
      color: #008aab;
      padding: 2px 6px;
      border-radius: 4px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 7.5pt;
      margin: 6px 0 10px 0;
    }

    th {
      background: #003366;
      color: #ffffff;
      font-weight: 700;
      text-align: left;
      padding: 5px 8px;
      border: 1px solid #cbd5e1;
    }

    td {
      padding: 4px 8px;
      border: 1px solid #e2e8f0;
      color: #1e293b;
    }

    tr:nth-child(even) {
      background: #f8fafc;
    }

    .card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px 12px;
      margin-bottom: 10px;
    }

    .tree-box {
      background: #0f172a;
      color: #38bdf8;
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.5pt;
      padding: 10px 14px;
      border-radius: 6px;
      line-height: 1.5;
      margin: 6px 0 10px 0;
    }

    .tree-box strong {
      color: #f8fafc;
    }

    .tree-box .dim {
      color: #94a3b8;
    }

    .tree-box .hl {
      color: #34d399;
    }

    .tree-box .warn {
      color: #f87171;
    }

    .formula-box {
      background: #f0fdfa;
      border-left: 3px solid #0d9488;
      padding: 8px 12px;
      margin: 6px 0 10px 0;
      font-family: 'JetBrains Mono', monospace;
      font-size: 8pt;
      color: #134e4a;
    }

    /* Quadrant Diagram Visual */
    .quadrant-matrix {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin: 10px 0;
    }

    .quad-card {
      border-radius: 6px;
      padding: 8px 10px;
      border: 1px solid transparent;
    }

    .q1 { background: #ecfdf5; border-color: #a7f3d0; color: #065f46; }
    .q2 { background: #f0f9ff; border-color: #bae6fd; color: #0369a1; }
    .q3 { background: #fffbeb; border-color: #fde68a; color: #92400e; }
    .q4 { background: #fff1f2; border-color: #fecdd3; color: #9f1239; }

    .quad-header {
      font-size: 8.5pt;
      font-weight: 800;
      display: flex;
      justify-content: space-between;
      margin-bottom: 2px;
    }

    .quad-stats {
      font-family: 'JetBrains Mono', monospace;
      font-size: 7pt;
      margin-bottom: 4px;
      font-weight: 600;
    }

    .quad-body {
      font-size: 7.2pt;
      line-height: 1.35;
    }

    .quad-list {
      font-weight: 600;
      margin-top: 2px;
    }

    .page-break {
      page-break-before: always;
      break-before: page;
      margin-top: 15px;
      padding-top: 5px;
    }

    .stat-pill {
      display: inline-block;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      font-size: 7.5pt;
    }

    .pill-green { background: #d1fae5; color: #065f46; }
    .pill-blue { background: #e0f2fe; color: #0369a1; }
    .pill-amber { background: #fef3c7; color: #92400e; }
    .pill-red { background: #fee2e2; color: #991b1b; }
  </style>
</head>
<body>

  <!-- HEADER -->
  <div class="header-banner">
    <div class="eyebrow">Rajya Shiksha Kendra (RSK) • Government of Madhya Pradesh × Peepul India</div>
    <h1 class="doc-title">Data Lineage, Mathematical Provenance & 52-District Strategic Quadrant Derivation</h1>
    <div class="doc-subtitle">
      Zero-Tolerance Reconciliation Audit, Telemetry Lineage, and Orthogonal Quadrant Mathematics for Shikshak Samvad (Grades 6–8)
    </div>
    <div class="meta-bar">
      <div>STATEWIDE CADRE: <strong>68,427 (Varg-2)</strong></div>
      <div>MATH & SCIENCE: <strong>35,374 Teachers</strong></div>
      <div>VALIDATED TOUCHPOINTS: <strong>N = 66,566</strong></div>
      <div>RECONCILIATION DELTA: <strong>Δ = 0 (100% Exact)</strong></div>
    </div>
  </div>

  <!-- SECTION 1 -->
  <h2>
    <span>1. Primary Raw Data Sources & Scope</span>
    <span class="section-badge">Master Database Architecture</span>
  </h2>
  <p style="margin: 0 0 6px 0;">
    All figures originate from the official <strong>Statewide Teacher CPD Telemetry & Cadre Universe Database</strong> compiled by Rajya Shiksha Kendra (RSK), Madhya Pradesh in technical collaboration with Peepul India.
  </p>

  <table>
    <tr>
      <th style="width: 25%;">Core Data Layer</th>
      <th style="width: 35%;">Raw Source Datasets</th>
      <th style="width: 40%;">Scope & Scale</th>
    </tr>
    <tr>
      <td><strong>Cadre Universe Master</strong></td>
      <td>MP Samagra Shiksha / EMIS Teacher Cadre Database</td>
      <td><strong>68,427 Middle School (Varg-2) Teachers</strong> across 322 Blocks & 52 Districts</td>
    </tr>
    <tr>
      <td><strong>Target Subject Cohort</strong></td>
      <td>Middle School Subject Allocation Roster</td>
      <td><strong>35,374 Math & Science Teachers</strong> (51.7% of total middle school cadre)</td>
    </tr>
    <tr>
      <td><strong>Operational Attendance</strong></td>
      <td>Cluster-Level Physical Attendance Logs & Digital Forms</td>
      <td><strong>N = 66,566 total verified touchpoints</strong> (August: 33,702; September: 32,864)</td>
    </tr>
    <tr>
      <td><strong>Psychometric Telemetry</strong></td>
      <td>Digital Post-Dialogue Scenario Survey System</td>
      <td><strong>12 standardized scenario questions</strong> across conceptual recall, TLM usage, inquiry, and classroom agency</td>
    </tr>
    <tr>
      <td><strong>Qualitative Reflections</strong></td>
      <td>Open-Ended Practitioner Feedback Submissions</td>
      <td><strong>30,000+ qualitative text submissions</strong> coded under Braun & Clarke (2006) 6-phase protocol</td>
    </tr>
  </table>

  <!-- SECTION 2 -->
  <h2>
    <span>2. Lineage of Top-Level KPIs in the Executive Briefing</span>
    <span class="section-badge">Mathematical Reconciliation Tree</span>
  </h2>

  <div class="tree-box">
<strong>Total Cadre Universe (68,427)</strong>
 └── <span class="hl">Target Math & Science Specialists (35,374)</span>
      └── <span class="hl">Actual Teacher Turnout (23,785)</span> + <span class="hl">District Officials (4,454)</span> = <strong>28,239 Total Participants</strong>
           ├── <span class="warn">Unreached Target Gap: 11,589 (32.8%)</span>
           ├── <span class="dim">Other Varg-2 Non-Mobilized Cadre: 33,053</span>
           └── <strong>Total Unreached Cadre Gap: 44,642 (65.2%)</strong>
  </div>

  <table>
    <tr>
      <th>KPI Indicator</th>
      <th>Reconciled Value</th>
      <th>Formula / Mathematical Derivation</th>
      <th>Status & Benchmark</th>
    </tr>
    <tr>
      <td><strong>Participants</strong></td>
      <td><span class="stat-pill pill-blue">28,239 Total</span></td>
      <td>Teachers (<strong>23,785</strong>) + District Officials / DOs (<strong>4,454</strong>) = <strong>28,239</strong></td>
      <td>Verified Active Footprint</td>
    </tr>
    <tr>
      <td><strong>Districts Covered</strong></td>
      <td><span class="stat-pill pill-green">52 / 52 Districts</span></td>
      <td>Complete administrative footprint across all 52 districts in Madhya Pradesh</td>
      <td><strong>100% Saturation</strong></td>
    </tr>
    <tr>
      <td><strong>Training Centres</strong></td>
      <td><span class="stat-pill pill-green">2,874 Active Venues</span></td>
      <td><strong>2,822</strong> Active Cluster Venues + <strong>52</strong> District HQ Centres (out of 4,804 mapped clusters)</td>
      <td>59.8% CRC Saturation</td>
    </tr>
    <tr>
      <td><strong>Observers Deployed</strong></td>
      <td><span class="stat-pill pill-amber">572 Monitors</span></td>
      <td><strong>516</strong> Cluster Observers (CACs/BACs) + <strong>56</strong> District Observers (APCs/DPCs)</td>
      <td>Independent Field Monitoring</td>
    </tr>
    <tr>
      <td><strong>Facilitators & MTs</strong></td>
      <td><span class="stat-pill pill-green">4,891 Leads</span></td>
      <td><strong>4,814</strong> Cluster Lead Teachers/CAC Facilitators + <strong>77</strong> District Master Trainers</td>
      <td>Decentralized Lead Cadre</td>
    </tr>
  </table>

  <!-- PAGE BREAK -->
  <div class="page-break"></div>

  <!-- SECTION 3 -->
  <h2>
    <span>3. How the 52-District Strategic Quadrant Landscape is Derived</span>
    <span class="section-badge">Orthogonal Matrix Formulas</span>
  </h2>
  
  <p style="margin: 0 0 6px 0;">
    The 52-district strategic quadrant matrix is derived using a two-dimensional mathematical coordinate function:
  </p>

  <div class="formula-box">
    <strong>District Position</strong> = <em>f</em>( Operational Turnout % (<strong>X</strong>), Pedagogical Quality Score % (<strong>Y</strong>) )
  </div>

  <div class="card">
    <h3>Axis 1: Operational Turnout (X-Axis)</h3>
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: #003366; margin-bottom: 3px;">
      $$\text{Turnout \%} = \frac{\text{District Actual Attendees}}{\text{District Target Universe}} \times 100$$
    </div>
    <div style="font-size: 7.5pt; color: #475569;">
      <strong>Threshold Cutoff:</strong> $\ge 65\%$ (or $\ge 450$ attendees per district) separates high-mobilization from low-mobilization districts.
    </div>

    <h3 style="margin-top: 8px;">Axis 2: Instructional / Pedagogical Quality (Y-Axis)</h3>
    <div style="font-size: 7.5pt; color: #475569; margin-bottom: 4px;">
      Composite accuracy score across standardized scenario survey questions evaluating whether teachers adopt mastery constructivist pedagogy versus falling into common distractor/activity traps:
    </div>
    <ul style="margin: 0 0 4px 18px; padding: 0; font-size: 7.2pt; color: #334155;">
      <li><strong>Q95 / Q177:</strong> Hands-on TLM purpose (Activity Trap vs. Cognitive Reflection).</li>
      <li><strong>Q97 / Q178:</strong> Classroom Belonging & Inquiry (Surface praise vs. Normalizing intellectual struggle).</li>
      <li><strong>Q96 / Q179:</strong> Psychological safety and mistake diagnostic value.</li>
    </ul>
    <div style="font-size: 7.5pt; color: #475569;">
      <strong>Threshold Cutoff:</strong> $\ge 75\%$ pedagogical accuracy score separates high-quality from support-requiring cohorts.
    </div>
  </div>

  <!-- SECTION 4 -->
  <h2>
    <span>4. Complete Accounting of the 4 Quadrants (8 + 26 + 5 + 13 = 52)</span>
    <span class="section-badge">100% Zero-Delta Accounting</span>
  </h2>

  <!-- Visual 2x2 Grid -->
  <div class="quadrant-matrix">
    <!-- Q2: Top Left -->
    <div class="quad-card q2">
      <div class="quad-header">
        <span>📈 Q2: Scale Gap / Latent Potential</span>
        <span>26 Districts</span>
      </div>
      <div class="quad-stats">Turnout: 48.6% • Quality: 81.5% | Low Turnout &lt;65%, High Quality ≥75%</div>
      <div class="quad-body">
        Strong instructional mastery exists; primary need is CAC/BAC attendance mobilization enforcement.
        <div class="quad-list">Indore, Bhopal, Ujjain, Gwalior, Jabalpur, Sagar, Rewa, Satna, Chhindwara, Hoshangabad, Vidisha, Ratlam, Mandsaur, Neemuch, Damoh, Katni, Shivpuri, Guna, Harda, Betul, Chhatarpur, Tikamgarh, Balaghat, Seoni, Mandla, Khandwa.</div>
      </div>
    </div>

    <!-- Q1: Top Right -->
    <div class="quad-card q1">
      <div class="quad-header">
        <span>🌟 Q1: Champions</span>
        <span>8 Districts</span>
      </div>
      <div class="quad-stats">Turnout: 82.4% • Quality: 84.2% | High Turnout ≥65%, High Quality ≥75%</div>
      <div class="quad-body">
        High compliance and high pedagogical mastery. Serve as statewide lighthouse centres and regional mentors.
        <div class="quad-list">Dhar, Rajgarh, Sehore, Shahdol, Khargone, Dewas, Narsinghpur, Raisen.</div>
      </div>
    </div>

    <!-- Q4: Bottom Left -->
    <div class="quad-card q4">
      <div class="quad-header">
        <span>⚠️ Q4: Critical Deficit</span>
        <span>13 Districts</span>
      </div>
      <div class="quad-stats">Turnout: 42.1% • Quality: 61.8% | Low Turnout &lt;65%, Lower Quality &lt;75%</div>
      <div class="quad-body">
        Dual operational deficit requiring coordinated administrative turnout review + intensive master trainer coaching.
        <div class="quad-list">Alirajpur, Sheopur, Bhind, Panna, Morena, Datia, Ashoknagar, Anuppur, Burhanpur, Sidhi, Niwari, Shajapur, Agar Malwa.</div>
      </div>
    </div>

    <!-- Q3: Bottom Right -->
    <div class="quad-card q3">
      <div class="quad-header">
        <span>🤝 Q3: Needs Support</span>
        <span>5 Districts</span>
      </div>
      <div class="quad-stats">Turnout: 78.1% • Quality: 64.3% | High Turnout ≥65%, Lower Quality &lt;75%</div>
      <div class="quad-body">
        High mobilization and turnout, but persistent misconception traps require focused pedagogical reinforcement.
        <div class="quad-list">Barwani, Jhabua, Singrauli, Dindori, Umaria.</div>
      </div>
    </div>
  </div>

  <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 4px; padding: 6px 10px; font-size: 7.5pt; font-family: 'JetBrains Mono', monospace; text-align: center; margin-bottom: 12px;">
    <strong>Total Districts Reconciled:</strong> 8 (Q1) + 26 (Q2) + 5 (Q3) + 13 (Q4) = <strong>52 Districts (100% Zero-Delta Verification)</strong>
  </div>

  <!-- SECTION 5 -->
  <h2>
    <span>5. Provenance of Pedagogical Traps & Operations Gaps</span>
    <span class="section-badge">Empirical Survey Telemetry</span>
  </h2>

  <table>
    <tr>
      <th style="width: 30%;">Indicator & Item ID</th>
      <th style="width: 20%;">Empirical Value</th>
      <th style="width: 50%;">Underlying Data Source & Pedagogical Meaning</th>
    </tr>
    <tr>
      <td><strong>Activity Trap Deficit</strong><br><span style="font-family: monospace; color: #64748b;">(Q95 / Q177)</span></td>
      <td><span class="stat-pill pill-red">48.1% Trapped</span></td>
      <td>Derived from survey telemetry where <strong>48.1%</strong> of responding teachers selected the option equating "keeping children busy in physical activities" with learning, rather than scaffolding structured cognitive reflection.</td>
    </tr>
    <tr>
      <td><strong>Belonging Misconception</strong><br><span style="font-family: monospace; color: #64748b;">(Q97 / Q178)</span></td>
      <td><span class="stat-pill pill-amber">66.1% Misguided</span></td>
      <td><strong>66.1%</strong> of respondents equated student belonging with praising correct answers, rather than normalizing mistakes and intellectual struggle as essential learning steps.</td>
    </tr>
    <tr>
      <td><strong>Observer Unmonitored Gap</strong><br><span style="font-family: monospace; color: #64748b;">(CRC Coverage)</span></td>
      <td><span class="stat-pill pill-red">1,688 Clusters (35.1%)</span></td>
      <td>Calculated by cross-referencing total mapped clusters (<strong>4,804</strong>) against observer digital check-in timestamps, identifying clusters with zero observer touchpoints.</td>
    </tr>
    <tr>
      <td><strong>Trust Perception Delta</strong><br><span style="font-family: monospace; color: #64748b;">(Divergence Audit)</span></td>
      <td><span class="stat-pill pill-amber">Δ 23.4% Variance</span></td>
      <td>Difference between Teacher Self-Reported Satisfaction (<strong>94.6%</strong>) and Independent Observer Audit Assessment (<strong>71.2%</strong>).</td>
    </tr>
  </table>

</body>
</html>
"""

# Write HTML to disk
html_file_path = os.path.abspath('RSK_Data_Lineage_and_Quadrant_Provenance_Report.html')
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated HTML: {html_file_path}")

# Compile to PDF with Playwright
pdf_output_path = os.path.abspath('RSK_Data_Lineage_and_Quadrant_Provenance_Report.pdf')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('file:///' + html_file_path.replace('\\', '/'), wait_until='networkidle')
    page.wait_for_timeout(1500)
    
    page.pdf(
        path=pdf_output_path,
        format='A4',
        print_background=True,
        margin={
            'top': '10mm',
            'bottom': '10mm',
            'left': '10mm',
            'right': '10mm'
        }
    )
    print(f"SUCCESSFULLY GENERATED PDF: {pdf_output_path} ({os.path.getsize(pdf_output_path):,} bytes)")
    browser.close()
