import os
import sys
import io
from playwright.sync_api import sync_playwright

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>RSK Shaikshik Samwaad — Dual-Cycle (August & September) Data Provenance & Lineage Reference</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    @page {
      size: A4 portrait;
      margin: 10mm 10mm 10mm 10mm;
      @bottom-right {
        content: "Page " counter(page);
        font-family: 'JetBrains Mono', monospace;
        font-size: 7.5pt;
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
      font-size: 7.8pt;
      line-height: 1.45;
      -webkit-font-smoothing: antialiased;
    }

    .header-banner {
      background: linear-gradient(135deg, #003366 0%, #008aab 100%);
      color: #ffffff;
      padding: 14px 18px;
      border-radius: 6px;
      margin-bottom: 10px;
    }

    .eyebrow {
      font-family: 'JetBrains Mono', monospace;
      font-size: 7pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: #63d0df;
      margin-bottom: 3px;
    }

    .doc-title {
      font-size: 15pt;
      font-weight: 800;
      margin: 0 0 4px 0;
      line-height: 1.2;
      color: #ffffff;
    }

    .doc-subtitle {
      font-size: 8pt;
      color: #e2e8f0;
      line-height: 1.35;
    }

    .meta-bar {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
      margin-top: 8px;
      padding-top: 6px;
      border-top: 1px solid rgba(255, 255, 255, 0.2);
      font-family: 'JetBrains Mono', monospace;
      font-size: 6.5pt;
      color: #f1f5f9;
    }

    .meta-bar strong {
      color: #63d0df;
    }

    h2 {
      font-size: 9.5pt;
      font-weight: 800;
      color: #003366;
      border-bottom: 1.5px solid #008aab;
      padding-bottom: 3px;
      margin: 10px 0 6px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .section-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 6.5pt;
      font-weight: 700;
      background: rgba(0, 138, 171, 0.1);
      color: #008aab;
      padding: 1px 5px;
      border-radius: 3px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 7.2pt;
      margin: 4px 0 8px 0;
    }

    th {
      background: #003366;
      color: #ffffff;
      font-weight: 700;
      text-align: left;
      padding: 4px 6px;
      border: 1px solid #cbd5e1;
    }

    td {
      padding: 3.5px 6px;
      border: 1px solid #e2e8f0;
      color: #1e293b;
      vertical-align: top;
    }

    tr:nth-child(even) {
      background: #f8fafc;
    }

    .tree-box {
      background: #0f172a;
      color: #38bdf8;
      font-family: 'JetBrains Mono', monospace;
      font-size: 7pt;
      padding: 8px 12px;
      border-radius: 5px;
      line-height: 1.45;
      margin: 4px 0 8px 0;
    }

    .tree-box strong { color: #f8fafc; }
    .tree-box .dim { color: #94a3b8; }
    .tree-box .hl { color: #34d399; }
    .tree-box .warn { color: #f87171; }

    .formula-box {
      background: #f0fdfa;
      border-left: 3px solid #0d9488;
      padding: 6px 10px;
      margin: 4px 0 8px 0;
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.5pt;
      color: #134e4a;
    }

    .page-break {
      page-break-before: always;
      break-before: page;
      margin-top: 10px;
      padding-top: 5px;
    }

    .stat-pill {
      display: inline-block;
      padding: 1px 5px;
      border-radius: 3px;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      font-size: 6.8pt;
      white-space: nowrap;
    }

    .pill-green { background: #d1fae5; color: #065f46; }
    .pill-blue { background: #e0f2fe; color: #0369a1; }
    .pill-amber { background: #fef3c7; color: #92400e; }
    .pill-red { background: #fee2e2; color: #991b1b; }

    code {
      font-family: 'JetBrains Mono', monospace;
      background: #f1f5f9;
      color: #0f172a;
      padding: 1px 3px;
      border-radius: 3px;
      font-size: 6.8pt;
    }
  </style>
</head>
<body>

  <!-- ================= PAGE 1 ================= -->
  <div class="header-banner">
    <div class="eyebrow">Rajya Shiksha Kendra (RSK) • Government of Madhya Pradesh × Peepul India</div>
    <h1 class="doc-title">Dual-Cycle (August & September) Data Provenance & Lineage Reference</h1>
    <div class="doc-subtitle">
      Complete Reconciliation Across August Baseline (N=33,702), September Cycle (N=32,864), and Consolidated Longitudinal Telemetry (N=66,566)
    </div>
    <div class="meta-bar">
      <div>TOTAL TOUCHPOINTS: <strong>N = 66,566</strong></div>
      <div>AUG TOUCHPOINTS: <strong>33,702 Records</strong></div>
      <div>SEP TOUCHPOINTS: <strong>32,864 Records</strong></div>
      <div>UNIQUE TEACHERS: <strong>33,866 (49.49% Reach)</strong></div>
    </div>
  </div>

  <h2>
    <span>1. Dual-Cycle Data Architecture & Ingestion Structure</span>
    <span class="section-badge">Multi-Cycle Master Model</span>
  </h2>
  
  <p style="margin: 0 0 6px 0;">
    The Shikshak Samvad analytics engine aggregates data across two primary cycles: <strong>Cycle 1 (August 2026)</strong> and <strong>Cycle 2 (September 2026)</strong>. While the original physical workbook drops were labeled <code>..._August.xlsx</code>, the system integrates both cycles within <code>dataPackage.json</code> and <code>teacher_cohort_data.json</code> for cross-cycle longitudinal tracking.
  </p>

  <table>
    <tr>
      <th style="width: 20%;">Cadre Role Layer</th>
      <th style="width: 25%;">August 2026 Baseline (Cycle 1)<br><code>SS_ResponseDetail_..._August.xlsx</code></th>
      <th style="width: 25%;">September 2026 Cycle (Cycle 2)<br><code>dataPackage.json [cycles.SEP]</code></th>
      <th style="width: 30%;">Consolidated Multi-Cycle Footprint<br><code>dataPackage.json [CONSOLIDATED]</code></th>
    </tr>
    <tr>
      <td><strong>Cluster Teachers (Participants)</strong></td>
      <td><strong>23,785</strong> Attendees</td>
      <td><strong>23,169</strong> Attendees</td>
      <td><strong>46,954</strong> Total Attendances (<strong>33,866</strong> Unique Teachers)</td>
    </tr>
    <tr>
      <td><strong>District Officials (DO)</strong></td>
      <td><strong>4,454</strong> Participants</td>
      <td><strong>4,434</strong> Participants</td>
      <td><strong>8,888</strong> DO Attendances</td>
    </tr>
    <tr>
      <td><strong>Cluster Facilitators (CACs)</strong></td>
      <td><strong>4,814</strong> Leads</td>
      <td><strong>4,740</strong> Leads</td>
      <td><strong>9,554</strong> Facilitator Attendances</td>
    </tr>
    <tr>
      <td><strong>Cluster Observers (BAC/APC)</strong></td>
      <td><strong>516</strong> Monitors</td>
      <td><strong>414</strong> Monitors</td>
      <td><strong>930</strong> Observer Touchpoints</td>
    </tr>
    <tr>
      <td><strong>District Master Trainers (MT)</strong></td>
      <td><strong>77</strong> Leads</td>
      <td><strong>56</strong> Leads</td>
      <td><strong>133</strong> District MT Attendances</td>
    </tr>
    <tr>
      <td><strong>District Monitors (DPC/DIET)</strong></td>
      <td><strong>56</strong> Monitors</td>
      <td><strong>51</strong> Monitors</td>
      <td><strong>107</strong> District Monitor Touchpoints</td>
    </tr>
    <tr style="background: #e0f2fe; font-weight: 700;">
      <td>Total Reconciled Touchpoints</td>
      <td><strong>33,702 Records</strong></td>
      <td><strong>32,864 Records</strong></td>
      <td><strong>66,566 Total Verified Records</strong></td>
    </tr>
  </table>

  <h2>
    <span>2. Longitudinal Cohort Dynamics (August $\to$ September Tracking)</span>
    <span class="section-badge">N = 33,866 Unique Educators</span>
  </h2>

  <div class="tree-box">
<strong>Total Varg-2 Universe Base (EMIS Master) = 68,427</strong>
 ├── <strong>Unique Middle School Teachers Reached (Aug + Sep) = 33,866 (49.49% Saturation)</strong>
 │    ├── <span class="hl">Persistent Core (Attended BOTH August & September) = 13,088 Teachers (38.65% of active reach)</span>
 │    ├── <span class="dim">Dropped After August (Attended Aug Only) = 10,697 Teachers (31.59%)</span>
 │    └── <span class="hl">Newly Mobilized Inflow (Joined in September Only) = 10,081 Teachers (29.76%)</span>
 └── <span class="warn"><strong>Unreached Cadre Base Gap (Never Attended Either Cycle) = 34,561 Teachers (50.51%)</strong></span>
  </div>

  <table>
    <tr>
      <th style="width: 25%;">Cohort Tracking Metric</th>
      <th style="width: 15%;">Headcount</th>
      <th style="width: 20%;">% Share</th>
      <th style="width: 40%;">Analytical Significance & Source File</th>
    </tr>
    <tr>
      <td><strong>August Active Teachers</strong></td>
      <td><strong>23,785</strong></td>
      <td>34.76% of Universe</td>
      <td><code>SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx</code> &bull; <code>Participants</code></td>
    </tr>
    <tr>
      <td><strong>September Active Teachers</strong></td>
      <td><strong>23,169</strong></td>
      <td>33.86% of Universe</td>
      <td><code>dataPackage.json</code> &bull; <code>cycles.SEP.districtSummary</code></td>
    </tr>
    <tr>
      <td><strong>Persistent Core (Both Cycles)</strong></td>
      <td><span class="stat-pill pill-green">13,088</span></td>
      <td><strong>55.03% Retention</strong></td>
      <td><code>teacher_cohort_data.json</code> &bull; Teachers with verified presence in both cycles.</td>
    </tr>
    <tr>
      <td><strong>New September Intake</strong></td>
      <td><span class="stat-pill pill-blue">10,081</span></td>
      <td><strong>43.51% Fresh Inflow</strong></td>
      <td>First-time participating teachers mobilizing in Cycle 2.</td>
    </tr>
    <tr>
      <td><strong>August-Only Dropout</strong></td>
      <td><span class="stat-pill pill-amber">10,697</span></td>
      <td>44.97% Attrition</td>
      <td>Teachers present in August who were absent in September.</td>
    </tr>
    <tr>
      <td><strong>Cumulative Unique Reach</strong></td>
      <td><span class="stat-pill pill-green">33,866</span></td>
      <td><strong>49.49% Universe Reach</strong></td>
      <td>Combined unique teacher beneficiaries across both cycles ($13,088 + 10,697 + 10,081$).</td>
    </tr>
    <tr>
      <td><strong>Statewide Unreached Base</strong></td>
      <td><span class="stat-pill pill-red">34,561</span></td>
      <td><strong>50.51% Universe Gap</strong></td>
      <td>Teachers in the 68,427 master universe not yet reached in either cycle.</td>
    </tr>
  </table>

  <!-- PAGE BREAK -->
  <div class="page-break"></div>

  <h2>
    <span>3. Source Workbook & Ingestion Registry for Both Cycles</span>
    <span class="section-badge">Exact Data Files & Keys</span>
  </h2>

  <table>
    <tr>
      <th style="width: 10%;">Cycle</th>
      <th style="width: 25%;">Data Asset / Storage Layer</th>
      <th style="width: 30%;">File Name & Structure</th>
      <th style="width: 35%;">Contents & Query Path</th>
    </tr>
    <tr>
      <td><strong>Universe Baseline</strong></td>
      <td>EMIS Cadre Master</td>
      <td><code>Varg Wise Teacher Count.xlsx</code> &bull; <code>Sheet1</code></td>
      <td>322 block rows with counts for Varg-2 Maths (18,214), Biology (17,160), Languages, Social Science (68,427 total).</td>
    </tr>
    <tr>
      <td><strong>Cycle 1 (August)</strong></td>
      <td>Cluster Level Raw Workbook</td>
      <td><code>SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx</code></td>
      <td>Sheets: <code>Participants</code> (23,785), <code>Facilitator</code> (4,814), <code>Monitor</code> (516), <code>Question Master</code>.</td>
    </tr>
    <tr>
      <td><strong>Cycle 1 (August)</strong></td>
      <td>District Level Raw Workbook</td>
      <td><code>SS_ResponseDetail_District Level_Grades 6-8_August.xlsx</code></td>
      <td>Sheets: <code>Participants</code> (4,454 DOs), <code>Facilitator</code> (77 MTs), <code>Monitor</code> (56 DPC/DIET monitors).</td>
    </tr>
    <tr>
      <td><strong>Cycle 2 (September)</strong></td>
      <td>Compiled Cycle Telemetry</td>
      <td><code>dataPackage.json</code> &bull; <code>cycles.SEP</code></td>
      <td>23,169 Cluster Teachers, 4,434 DOs, 4,740 Facilitators, 414 Monitors, 56 District MTs, 51 District Monitors.</td>
    </tr>
    <tr>
      <td><strong>Dual-Cycle Tracking</strong></td>
      <td>Cohort Bridge Database</td>
      <td><code>teacher_cohort_data.json</code></td>
      <td>Cross-cycle employee tracking: Persistent Core (13,088), Dropouts (10,697), Inflow (10,081), Net Unique (33,866).</td>
    </tr>
    <tr>
      <td><strong>Dual-Cycle Scoring</strong></td>
      <td>Results Framework Engine</td>
      <td><code>rfData_inspect.json</code> & <code>dataPackage.json</code></td>
      <td>August Baseline (72.8%) vs September Progress (76.3%) across constructivism, talk-time, and tech.</td>
    </tr>
    <tr>
      <td><strong>Qualitative NLP</strong></td>
      <td>Thematic Voice Engine</td>
      <td><code>dataPackage.json</code> &bull; <code>thematic_topology</code></td>
      <td>30,000+ open-ended submissions across August (18,450) and September (12,000+) coded under Braun & Clarke (2006).</td>
    </tr>
  </table>

  <h2>
    <span>4. Summary of Why Executive Briefing Used the August Baseline Snapshot</span>
    <span class="section-badge">Context & Harmonization</span>
  </h2>

  <table>
    <tr>
      <th style="width: 25%;">Document / View</th>
      <th style="width: 25%;">Primary Scope Shown</th>
      <th style="width: 25%;">Key KPI Values</th>
      <th style="width: 25%;">Context & Harmonization Rationale</th>
    </tr>
    <tr>
      <td><strong>Executive Visual Briefing</strong> (1-Page Briefing)</td>
      <td><strong>August Baseline Snapshot</strong> (Cycle 1 Initial Mobilization)</td>
      <td>• Participants: <strong>28,239</strong><br>• Teachers: <strong>23,785</strong><br>• DOs: <strong>4,454</strong><br>• Centres: <strong>2,874</strong></td>
      <td>Created as the initial policy briefing to establish baseline state performance prior to September comparative cycle rollout.</td>
    </tr>
    <tr>
      <td><strong>Full Master Studio Dashboard</strong> (Interactive & PDF)</td>
      <td><strong>Dual-Cycle Longitudinal</strong> (August + September + Consolidated)</td>
      <td>• Total Verified: <strong>66,566</strong><br>• Unique Reach: <strong>33,866</strong><br>• Persistent Core: <strong>13,088</strong><br>• 52-District Matrix</td>
      <td>Provides multi-cycle filter controls allowing users to switch between August, September, or Consolidated longitudinal view.</td>
    </tr>
    <tr>
      <td><strong>Academic Research Monograph</strong> (APA 7.0 Paper)</td>
      <td><strong>Complete Empirical & Qualitative Dataset</strong></td>
      <td>• $N = 66,566$ records<br>• 55.03% Retention<br>• 43.51% Fresh Inflow<br>• 30,000+ Quotes</td>
      <td>Comprehensive longitudinal empirical analysis evaluating retention, misconception shifts, and institutional governance across cycles.</td>
    </tr>
  </table>

</body>
</html>
"""

# Write HTML to disk
html_file_path = os.path.abspath('RSK_Dual_Cycle_Data_Provenance_and_Lineage_Reference.html')
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated HTML: {html_file_path}")

# Compile PDF using Playwright
pdf_output_path = os.path.abspath('RSK_Dual_Cycle_Data_Provenance_and_Lineage_Reference.pdf')

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
            'top': '8mm',
            'bottom': '8mm',
            'left': '8mm',
            'right': '8mm'
        }
    )
    print(f"SUCCESSFULLY GENERATED PDF: {pdf_output_path} ({os.path.getsize(pdf_output_path):,} bytes)")
    browser.close()
