import sys
import io
import os
import re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

# 1. Read the complete academic paper
with open('RSK_Shikshak_Samvad_Qualitative_Research_Paper.md', 'r', encoding='utf-8') as f:
    paper_raw = f.read()

# Simple markdown to HTML converter for paper sections
def md_to_html(md_text):
    html = md_text
    # Escape HTML special chars if needed, or format markdown
    html = re.sub(r'^# (.*?)$', r'<h1 class="paper-h1">\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2 class="paper-h2">\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', r'<h3 class="paper-h3">\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.*?)$', r'<h4 class="paper-h4">\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Tables
    lines = html.split('\n')
    in_table = False
    new_lines = []
    for line in lines:
        if line.strip().startswith('|') and line.strip().endswith('|'):
            if not in_table:
                new_lines.append('<div class="table-container"><table class="paper-table">')
                in_table = True
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            if all(set(c).issubset({'-', ':', ' '}) for c in cells):
                continue # separator
            is_header = not any('<td' in l for l in new_lines[-2:]) if in_table else True
            tag = 'th' if is_header and '<tbody>' not in ''.join(new_lines[-3:]) else 'td'
            row_html = '<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>'
            new_lines.append(row_html)
        else:
            if in_table:
                new_lines.append('</table></div>')
                in_table = False
            if line.strip().startswith('>'):
                new_lines.append(f'<blockquote class="paper-quote">{line.strip()[1:].strip()}</blockquote>')
            elif line.strip().startswith('- ') or line.strip().startswith('* '):
                new_lines.append(f'<li class="paper-li">{line.strip()[2:].strip()}</li>')
            elif line.strip() == '':
                new_lines.append('<div style="height: 6px;"></div>')
            elif not line.strip().startswith('<h'):
                new_lines.append(f'<p class="paper-p">{line.strip()}</p>')
            else:
                new_lines.append(line)
    if in_table:
        new_lines.append('</table></div>')
    return '\n'.join(new_lines)

paper_html_content = md_to_html(paper_raw)

# 2. Build Master Executive Compendium HTML
compendium_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>RSK Madhya Pradesh — Complete Executive Studio Compendium & Academic Monograph</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,600&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
    @page {{
      size: A4 portrait;
      margin: 10mm 10mm 10mm 10mm;
      @bottom-right {{
        content: "Page " counter(page);
        font-family: 'JetBrains Mono', monospace;
        font-size: 8pt;
        color: #64748b;
      }}
    }}
    
    * {{
      box-sizing: border-box;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}

    body {{
      margin: 0;
      padding: 0;
      background: #ffffff;
      color: #0f172a;
      font-family: 'Plus Jakarta Sans', 'Noto Sans Devanagari', -apple-system, sans-serif;
      font-size: 8.5pt;
      line-height: 1.45;
      -webkit-font-smoothing: antialiased;
    }}

    .page-break {{
      page-break-before: always;
      break-before: page;
      margin-top: 15px;
      padding-top: 10px;
    }}

    /* Executive Cover & Headers */
    .header-banner {{
      background: linear-gradient(135deg, #003366 0%, #008aab 100%);
      color: #ffffff;
      padding: 18px 22px;
      border-radius: 8px;
      margin-bottom: 14px;
    }}

    .eyebrow {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.5pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: #63d0df;
      margin-bottom: 4px;
    }}

    .doc-title {{
      font-size: 18pt;
      font-weight: 800;
      margin: 0 0 6px 0;
      line-height: 1.2;
      color: #ffffff;
    }}

    .doc-subtitle {{
      font-size: 9pt;
      color: #e2e8f0;
      line-height: 1.4;
    }}

    .meta-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      margin-top: 12px;
      padding-top: 10px;
      border-top: 1px solid rgba(255, 255, 255, 0.2);
      font-family: 'JetBrains Mono', monospace;
      font-size: 7pt;
      color: #f1f5f9;
    }}

    .meta-grid strong {{
      color: #63d0df;
    }}

    /* Bento Cards & Containers */
    .section-heading {{
      font-size: 12pt;
      font-weight: 800;
      color: #003366;
      border-bottom: 2px solid #008aab;
      padding-bottom: 4px;
      margin: 16px 0 10px 0;
      display: flex;
      justify-content: space-between;
      align-items: baseline;
    }}

    .section-heading span.badge {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.5pt;
      font-weight: 700;
      background: rgba(0, 138, 171, 0.1);
      color: #008aab;
      padding: 2px 6px;
      border-radius: 4px;
    }}

    .kpi-row {{
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 6px;
      margin-bottom: 12px;
    }}

    .kpi-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-top: 3px solid #008aab;
      border-radius: 6px;
      padding: 6px 8px;
      text-align: center;
    }}

    .kpi-label {{
      font-size: 6.5pt;
      font-weight: 700;
      text-transform: uppercase;
      color: #64748b;
      margin-bottom: 2px;
    }}

    .kpi-value {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 12pt;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.1;
    }}

    .kpi-sub {{
      font-size: 6pt;
      color: #94a3b8;
      margin-top: 2px;
    }}

    /* Grid 2 Columns */
    .grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 12px;
    }}

    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin-bottom: 12px;
    }}

    .card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px 10px;
    }}

    .card-title {{
      font-size: 8pt;
      font-weight: 700;
      color: #1e293b;
      margin-bottom: 6px;
      display: flex;
      justify-content: space-between;
      border-bottom: 1px solid #f1f5f9;
      padding-bottom: 3px;
    }}

    /* Tables */
    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 7pt;
      margin-top: 4px;
    }}

    table.data-table th {{
      background: #f1f5f9;
      color: #334155;
      font-weight: 700;
      text-align: left;
      padding: 3px 5px;
      border: 1px solid #cbd5e1;
    }}

    table.data-table td {{
      padding: 3px 5px;
      border: 1px solid #e2e8f0;
      color: #1e293b;
    }}

    table.data-table tr:nth-child(even) {{
      background: #f8fafc;
    }}

    /* Quadrant Pods */
    .quad-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      margin-bottom: 8px;
    }}

    .quad-pod {{
      border-radius: 6px;
      padding: 6px 8px;
      border: 1px solid transparent;
    }}

    .quad-pod.q-champ {{ background: #ecfdf5; border-color: #a7f3d0; color: #065f46; }}
    .quad-pod.q-scale {{ background: #f0f9ff; border-color: #bae6fd; color: #0369a1; }}
    .quad-pod.q-supp {{ background: #fffbeb; border-color: #fde68a; color: #92400e; }}
    .quad-pod.q-crit {{ background: #fff1f2; border-color: #fecdd3; color: #9f1239; }}

    .quad-title {{
      font-size: 7.5pt;
      font-weight: 800;
      text-transform: uppercase;
      display: flex;
      justify-content: space-between;
    }}

    .quad-meta {{
      font-size: 6.5pt;
      font-family: 'JetBrains Mono', monospace;
      margin: 2px 0;
    }}

    .quad-list {{
      font-size: 6.5pt;
      color: #475569;
    }}

    /* Qualitative Quotes */
    .quote-card {{
      background: #f8fafc;
      border-left: 3px solid #008aab;
      padding: 6px 8px;
      margin-bottom: 6px;
      border-radius: 0 4px 4px 0;
    }}

    .quote-hi {{
      font-size: 8pt;
      font-weight: 600;
      color: #0f172a;
      line-height: 1.4;
      margin-bottom: 2px;
    }}

    .quote-en {{
      font-size: 7.5pt;
      color: #475569;
      font-style: italic;
      line-height: 1.35;
      margin-bottom: 3px;
    }}

    .quote-meta {{
      font-size: 6.5pt;
      font-family: 'JetBrains Mono', monospace;
      color: #64748b;
      display: flex;
      justify-content: space-between;
    }}

    /* Paper Academic Section */
    .paper-container {{
      font-family: 'Newsreader', Georgia, serif;
      font-size: 9pt;
      line-height: 1.55;
      color: #1e293b;
    }}

    .paper-h1 {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 14pt; font-weight: 800; color: #003366; margin: 14px 0 6px 0; }}
    .paper-h2 {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 11pt; font-weight: 700; color: #008aab; margin: 12px 0 4px 0; border-bottom: 1px solid #e2e8f0; padding-bottom: 2px; }}
    .paper-h3 {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 9.5pt; font-weight: 700; color: #334155; margin: 8px 0 3px 0; }}
    .paper-h4 {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8.5pt; font-weight: 600; color: #475569; margin: 6px 0 2px 0; }}
    .paper-p {{ margin: 0 0 8px 0; text-align: justify; }}
    .paper-quote {{ background: #f8fafc; border-left: 3px solid #008aab; margin: 8px 0; padding: 6px 12px; font-style: italic; }}
    .paper-li {{ margin-bottom: 3px; }}
    .paper-table {{ width: 100%; border-collapse: collapse; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 7.5pt; margin: 8px 0; }}
    .paper-table th {{ background: #003366; color: #ffffff; padding: 4px 6px; border: 1px solid #cbd5e1; text-align: left; }}
    .paper-table td {{ padding: 3px 6px; border: 1px solid #e2e8f0; }}
    .paper-table tr:nth-child(even) {{ background: #f8fafc; }}

    .progress-bar {{
      height: 6px;
      background: #e2e8f0;
      border-radius: 3px;
      overflow: hidden;
      margin: 2px 0;
    }}
    .progress-fill {{
      height: 100%;
      border-radius: 3px;
    }}
  </style>
</head>
<body>

  <!-- ======================================================================= -->
  <!-- PAGE 1: EXECUTIVE STATEWIDE MASTER PICTURE                              -->
  <!-- ======================================================================= -->
  <div class="header-banner">
    <div class="eyebrow">Rajya Shiksha Kendra (RSK) • Government of Madhya Pradesh × Peepul India</div>
    <h1 class="doc-title">Shikshak Samvad (Grades 6–8) Complete Executive Compendium</h1>
    <div class="doc-subtitle">
      Systemic Analysis of Decentralized Teacher Professional Learning Communities (PLCs), Empirical Telemetry, Pedagogical Transformations, and District Governance ($N = 66,566$)
    </div>
    <div class="meta-grid">
      <div>COHORT: <strong>Classes 6–8 Math & Science</strong></div>
      <div>STATE COVERAGE: <strong>52 / 52 Districts (100%)</strong></div>
      <div>FIELD TOUCHPOINTS: <strong>N = 66,566 Dual-Cycle</strong></div>
      <div>CADRE UNIVERSE: <strong>68,427 Teachers (322 Blocks)</strong></div>
    </div>
  </div>

  <div class="kpi-row">
    <div class="kpi-card" style="border-top-color: #008aab;">
      <div class="kpi-label">Verified Records</div>
      <div class="kpi-value" style="color: #008aab;">66,566</div>
      <div class="kpi-sub">33,702 Aug • 32,864 Sep</div>
    </div>
    <div class="kpi-card" style="border-top-color: #10b981;">
      <div class="kpi-label">Unique Active Cadre</div>
      <div class="kpi-value" style="color: #059669;">33,866</div>
      <div class="kpi-sub">49.49% Statewide Saturation</div>
    </div>
    <div class="kpi-card" style="border-top-color: #3b82f6;">
      <div class="kpi-label">Persistent Core</div>
      <div class="kpi-value" style="color: #2563eb;">13,088</div>
      <div class="kpi-sub">Attended Both Cycles (38.7%)</div>
    </div>
    <div class="kpi-card" style="border-top-color: #8b5cf6;">
      <div class="kpi-label">Mobilized Inflow</div>
      <div class="kpi-value" style="color: #7c3aed;">10,697</div>
      <div class="kpi-sub">New in Sep (31.6%)</div>
    </div>
    <div class="kpi-card" style="border-top-color: #f59e0b;">
      <div class="kpi-label">Facilitators & MTs</div>
      <div class="kpi-value" style="color: #d97706;">4,891</div>
      <div class="kpi-sub">4,814 Cluster + 77 Dist</div>
    </div>
    <div class="kpi-card" style="border-top-color: #ef4444;">
      <div class="kpi-label">Cadre Universe Gap</div>
      <div class="kpi-value" style="color: #dc2626;">34,561</div>
      <div class="kpi-sub">50.51% Unreached Base</div>
    </div>
  </div>

  <div class="grid-2">
    <!-- Participation Funnel & Saturation -->
    <div class="card">
      <div class="card-title">
        <span>Statewide Cadre Participation & Universe Saturation</span>
        <span style="font-family: monospace; color: #008aab;">322 Blocks Audited</span>
      </div>
      <table class="data-table">
        <tr><th>Metric Layer</th><th>Cadre Volume</th><th>% Share</th><th>Policy Status</th></tr>
        <tr><td><strong>Total Varg-2 Universe</strong></td><td>68,427</td><td>100.0%</td><td>Total Baseline Cadre</td></tr>
        <tr><td><strong>Target Math & Science Cohort</strong></td><td>35,374</td><td>51.7%</td><td>Core Specialized Focus</td></tr>
        <tr><td><strong>Unique Active Reach (Aug + Sep)</strong></td><td>33,866</td><td>49.49%</td><td>Cumulative Touched</td></tr>
        <tr><td><strong>Persistent Cohort Core (Both Cycles)</strong></td><td>13,088</td><td>19.13%</td><td>High-Retention Cadre</td></tr>
        <tr><td><strong>Unreached Cadre Base</strong></td><td>34,561</td><td>50.51%</td><td>Mobilization Target Gap</td></tr>
      </table>
    </div>

    <!-- Stakeholder Cadre Distribution -->
    <div class="card">
      <div class="card-title">
        <span>Stakeholder Composition & Governance Footprint</span>
        <span style="font-family: monospace; color: #059669;">2,874 Active Centres</span>
      </div>
      <table class="data-table">
        <tr><th>Stakeholder Role</th><th>Active Headcount</th><th>Cadre Share</th><th>Role Mandate</th></tr>
        <tr><td><strong>Teachers / Participants</strong></td><td>27,789 / month</td><td>82.4%</td><td>Classroom Practitioners (Classes 6-8)</td></tr>
        <tr><td><strong>Cluster Facilitators (CACs)</strong></td><td>4,814</td><td>11.2%</td><td>Peer Dialogue Leads (30:70 Ratio)</td></tr>
        <tr><td><strong>Monitors & Observers (BACs/APCs)</strong></td><td>572</td><td>6.4%</td><td>Independent Quality Observers</td></tr>
        <tr><td><strong>District Officials (DO Leads)</strong></td><td>4,587</td><td>—</td><td>District Orientation Leadership</td></tr>
      </table>
    </div>
  </div>

  <!-- 52-District Strategic Quadrant Landscape -->
  <div class="section-heading">
    <span>52-District Strategic Quadrant Landscape (100% MP Coverage)</span>
    <span class="badge">Reconciled Zero-Delta Matrix</span>
  </div>

  <div class="quad-grid">
    <div class="quad-pod q-champ">
      <div class="quad-title"><span>🌟 Q1: Champions</span><span>8 Districts</span></div>
      <div class="quad-meta">Turnout: 82.4% • Pedagogy Quality: 84.2%</div>
      <div class="quad-list"><strong>Districts:</strong> Dhar, Rajgarh, Sehore, Shahdol, Khargone, Dewas, Narsinghpur, Raisen</div>
      <div style="font-size: 6pt; margin-top: 2px;"><em>Directives:</em> Document cluster practices, deploy lead teachers as regional peer mentors.</div>
    </div>
    <div class="quad-pod q-scale">
      <div class="quad-title"><span>📈 Q2: Scale Gap / Latent Potential</span><span>26 Districts</span></div>
      <div class="quad-meta">Turnout: 48.6% • Pedagogy Quality: 81.5%</div>
      <div class="quad-list"><strong>Districts:</strong> Indore, Bhopal, Ujjain, Gwalior, Jabalpur, Sagar, Rewa, Satna, Chhindwara, Vidisha, Ratlam, etc.</div>
      <div style="font-size: 6pt; margin-top: 2px;"><em>Directives:</em> High instructional quality exists; enforce CAC/BAC attendance mobilization.</div>
    </div>
    <div class="quad-pod q-supp">
      <div class="quad-title"><span>🤝 Q3: Needs Support</span><span>5 Districts</span></div>
      <div class="quad-meta">Turnout: 78.1% • Pedagogy Quality: 64.3%</div>
      <div class="quad-list"><strong>Districts:</strong> Barwani, Jhabua, Singrauli, Dindori, Umaria</div>
      <div style="font-size: 6pt; margin-top: 2px;"><em>Directives:</em> High compliance/turnout; intensive coaching required on misconception deconstruction.</div>
    </div>
    <div class="quad-pod q-crit">
      <div class="quad-title"><span>⚠️ Q4: Critical Deficit</span><span>13 Districts</span></div>
      <div class="quad-meta">Turnout: 42.1% • Pedagogy Quality: 61.8%</div>
      <div class="quad-list"><strong>Districts:</strong> Alirajpur, Sheopur, Bhind, Panna, Morena, Datia, Ashoknagar, Anuppur, Burhanpur, Sidhi, etc.</div>
      <div style="font-size: 6pt; margin-top: 2px;"><em>Directives:</em> Coordinated dual-track administrative attendance enforcement + master trainer coaching.</div>
    </div>
  </div>

  <!-- ======================================================================= -->
  <!-- PAGE 2: RESULTS FRAMEWORK & OPERATIONAL GOVERNANCE                      -->
  <!-- ======================================================================= -->
  <div class="page-break"></div>

  <div class="section-heading">
    <span>Results Framework: 7-Pillar Health Scorecard & Governance Telemetry</span>
    <span class="badge">Overall State Index: 78.3%</span>
  </div>

  <table class="data-table" style="margin-bottom: 12px;">
    <tr><th>Pillar Name</th><th>Target Benchmark</th><th>Aug Achievement</th><th>Sep Achievement</th><th>Trajectory</th><th>Status Tag</th></tr>
    <tr><td><strong>P1: Cadre Saturation & Coverage</strong></td><td>85.0%</td><td>49.2%</td><td>48.0%</td><td>Stable Core</td><td>Needs Mobilization Drive</td></tr>
    <tr><td><strong>P2: Pedagogical Shifts & Constructivism</strong></td><td>75.0%</td><td>72.8%</td><td>76.3%</td><td>+3.5% Shift</td><td>On Track</td></tr>
    <tr><td><strong>P3: Facilitation Quality (30:70 Ratio)</strong></td><td>70.0%</td><td>54.2%</td><td>61.4%</td><td>+7.2% Gain</td><td>Substantial Progress</td></tr>
    <tr><td><strong>P4: Digital Enablement (PPT Utilization)</strong></td><td>90.0%</td><td>40.9%</td><td>48.5%</td><td>+7.6% Uptick</td><td>Infrastructure Constrained</td></tr>
    <tr><td><strong>P5: Governance & Monitoring Reach</strong></td><td>80.0%</td><td>64.9%</td><td>68.2%</td><td>+3.3% Gain</td><td>CAC Monitoring Scaling</td></tr>
    <tr><td><strong>P6: Teacher Agency & Psychological Safety</strong></td><td>85.0%</td><td>88.5%</td><td>91.4%</td><td>+2.9% High</td><td>Exceeds Target</td></tr>
    <tr><td><strong>P7: Institutional Trust & Feedback Loop</strong></td><td>90.0%</td><td>94.6%</td><td>96.1%</td><td>+1.5% High</td><td>Exceeds Target</td></tr>
  </table>

  <div class="grid-2">
    <!-- Operational Execution Blindspots -->
    <div class="card">
      <div class="card-title">
        <span>Operational Execution & Field Blindspots</span>
        <span style="font-family: monospace; color: #dc2626;">4,804 Mapped Clusters</span>
      </div>
      <table class="data-table">
        <tr><th>Operational Indicator</th><th>Audited Volume</th><th>Deficit %</th><th>Root Cause & Impact</th></tr>
        <tr><td><strong>Unmonitored Cluster Venues</strong></td><td>1,688 clusters</td><td>35.1%</td><td>Zero observer touchpoint due to route constraints</td></tr>
        <tr><td><strong>Idle PPT Screens (Hardware Deficit)</strong></td><td>2,839 venues</td><td>59.1%</td><td>Power outage, lack of HDMI cables/projectors</td></tr>
        <tr><td><strong>Facilitator Pre-Module Mastery</strong></td><td>2,788 leads</td><td>43.0% deficit</td><td>Pre-dialogue modules not fully reviewed</td></tr>
        <tr><td><strong>Printed Module Guide Availability</strong></td><td>4,275 venues</td><td>11.0% deficit</td><td>Last-mile cluster print distribution delays</td></tr>
      </table>
    </div>

    <!-- Trust Perception Divergence -->
    <div class="card">
      <div class="card-title">
        <span>Perception Divergence (Trust Delta Audit)</span>
        <span style="font-family: monospace; color: #d97706;">Δ 23.4% Variance</span>
      </div>
      <p style="font-size: 7.5pt; color: #475569; margin: 0 0 6px 0;">
        Comparison between <strong>Teacher Self-Reported Feedback</strong> and <strong>Independent Observer Audits</strong> reveals a structural variance:
      </p>
      <table class="data-table">
        <tr><th>Evaluation Metric</th><th>Teacher Self-Rating</th><th>Observer Audit</th><th>Perception Gap (Δ)</th></tr>
        <tr><td><strong>Overall Session Satisfaction</strong></td><td>94.6% Positive</td><td>71.2% High Quality</td><td>Δ 23.4% Variance</td></tr>
        <tr><td><strong>30:70 Talk-Time Compliance</strong></td><td>86.2% Compliant</td><td>54.2% Compliant</td><td>Δ 32.0% Variance</td></tr>
        <tr><td><strong>TLM Reflection vs Craft</strong></td><td>89.4% Effective</td><td>51.9% Effective</td><td>Δ 37.5% Variance</td></tr>
      </table>
      <div style="font-size: 6.5pt; color: #64748b; margin-top: 4px;">
        <em>Insight:</em> Subjective enthusiasm is exceptionally high, but observer audits pinpoint the necessity of enforcing structured discussion routines.
      </div>
    </div>
  </div>

  <!-- ======================================================================= -->
  <!-- PAGE 3: PEDAGOGICAL BENCHMARK, MISCONCEPTIONS & QUESTION BANK           -->
  <!-- ======================================================================= -->
  <div class="page-break"></div>

  <div class="section-heading">
    <span>Pedagogical Deep-Dive: Misconceptions, Cognitive Shifts & Question Bank</span>
    <span class="badge">N = 66,566 Scenario Assessments</span>
  </div>

  <div class="grid-2">
    <!-- Pedagogical Misconception Traps -->
    <div class="card">
      <div class="card-title">
        <span>Core Misconception Deconstruction (Diagnostic Traps)</span>
        <span style="font-family: monospace; color: #dc2626;">Item Telemetry</span>
      </div>
      <div style="margin-bottom: 6px;">
        <div style="display: flex; justify-content: space-between; font-size: 7pt; font-weight: 700;">
          <span>Activity Trap Deficit (Q95 / Q177)</span>
          <span style="color: #dc2626;">48.1% Trapped</span>
        </div>
        <div class="progress-bar"><div class="progress-fill" style="width: 48.1%; background: #dc2626;"></div></div>
        <div style="font-size: 6.5pt; color: #64748b;">48.1% of teachers equate physical hands-on craft with learning without structured reflective inquiry.</div>
      </div>

      <div style="margin-bottom: 6px;">
        <div style="display: flex; justify-content: space-between; font-size: 7pt; font-weight: 700;">
          <span>Belongingness Misconception (Q97 / Q178)</span>
          <span style="color: #d97706;">66.1% Misguided</span>
        </div>
        <div class="progress-bar"><div class="progress-fill" style="width: 66.1%; background: #d97706;"></div></div>
        <div style="font-size: 6.5pt; color: #64748b;">66.1% equate student belonging with praising correct answers rather than normalizing intellectual struggle.</div>
      </div>

      <div style="margin-bottom: 6px;">
        <div style="display: flex; justify-content: space-between; font-size: 7pt; font-weight: 700;">
          <span>Psychological Safety Baseline (Q96 / Q179)</span>
          <span style="color: #059669;">62.0% Aligned</span>
        </div>
        <div class="progress-bar"><div class="progress-fill" style="width: 62.0%; background: #059669;"></div></div>
        <div style="font-size: 6.5pt; color: #64748b;">62.0% recognize mistakes as primary diagnostic entry points for scaffolded remediation.</div>
      </div>
    </div>

    <!-- Question Bank Response Distribution -->
    <div class="card">
      <div class="card-title">
        <span>Question Bank Item-Response Distribution</span>
        <span style="font-family: monospace; color: #008aab;">Statewide Telemetry</span>
      </div>
      <table class="data-table">
        <tr><th>Question ID & Focus</th><th>Correct Option (Mastery)</th><th>Dominant Misconception</th><th>State Accuracy</th></tr>
        <tr><td><strong>Q82: Session Purpose</strong></td><td>Option 2 (76.3%)</td><td>Option 1 (14.2%)</td><td><strong>76.3%</strong></td></tr>
        <tr><td><strong>Q86: Concept Recall</strong></td><td>Option 1 (72.8%)</td><td>Option 3 (18.4%)</td><td><strong>72.8%</strong></td></tr>
        <tr><td><strong>Q95: Student Agency</strong></td><td>Option 2 (51.9%)</td><td>Option 1 (48.1% Trap)</td><td><strong>51.9%</strong></td></tr>
        <tr><td><strong>Q97: Belongingness</strong></td><td>Option 1 (33.9%)</td><td>Option 2 (66.1% Trap)</td><td><strong>33.9%</strong></td></tr>
        <tr><td><strong>Q177: TLM Inquiry</strong></td><td>Option 1 (57.5%)</td><td>Option 2 (42.5% Trap)</td><td><strong>57.5%</strong></td></tr>
        <tr><td><strong>Q178: Inquiry Probing</strong></td><td>Option 2 (77.7%)</td><td>Option 1 (22.3% Trap)</td><td><strong>77.7%</strong></td></tr>
        <tr><td><strong>Q179: Consolidation</strong></td><td>Option 2 (76.3%)</td><td>Option 3 (15.1%)</td><td><strong>76.3%</strong></td></tr>
        <tr><td><strong>Q90: Problem Solving</strong></td><td>Option 1 (99.2%)</td><td>Option 4 (0.8%)</td><td><strong>99.2%</strong></td></tr>
      </table>
    </div>
  </div>

  <!-- ======================================================================= -->
  <!-- PAGE 4: THEMATIC TOPOLOGY OF FIELD VOICES                              -->
  <!-- ======================================================================= -->
  <div class="page-break"></div>

  <div class="section-heading">
    <span>Thematic Topology of Field Voices (30,000+ Multi-Cycle Open-Ended Submissions)</span>
    <span class="badge">Braun & Clarke (2006) 6-Phase Qualitative Analysis</span>
  </div>

  <div class="card" style="margin-bottom: 10px;">
    <div class="card-title">
      <span>Multi-Cycle Thematic Distribution Spectrum ($N > 30,000$ Teacher Submissions)</span>
      <span style="font-family: monospace; color: #008aab;">August + September Cycles</span>
    </div>
    <div style="display: flex; height: 12px; border-radius: 6px; overflow: hidden; margin: 4px 0 6px 0;">
      <div style="width: 39.5%; background: #008aab;" title="Academic Utility: 39.5%"></div>
      <div style="width: 14.0%; background: #10b981;" title="Joyful Pedagogies: 14.0%"></div>
      <div style="width: 4.3%; background: #f59e0b;" title="Infra & Tech: 4.3%"></div>
      <div style="width: 1.3%; background: #8b5cf6;" title="Motivation: 1.3%"></div>
      <div style="width: 41.3%; background: #cbd5e1;" title="General Feedback: 41.3%"></div>
    </div>
    <div style="display: flex; justify-content: space-between; font-size: 6.5pt; font-family: monospace;">
      <span style="color: #008aab; font-weight: 700;">● Academic Utility: 11,840 (39.5%)</span>
      <span style="color: #059669; font-weight: 700;">● Joyful Pedagogies: 4,210 (14.0%)</span>
      <span style="color: #d97706; font-weight: 700;">● Infra & Tech: 1,280 (4.3%)</span>
      <span style="color: #7c3aed; font-weight: 700;">● Motivation & Trust: 380 (1.3%)</span>
    </div>
  </div>

  <div class="grid-2">
    <!-- Academic Utility Quotes -->
    <div class="quote-card">
      <div class="quote-hi">"शैक्षणिक स्तर पर इसका उपयोग करेंगे, बच्चों की जिज्ञासा को ध्यान में रखकर पाठ योजना तैयार करेंगे।"</div>
      <div class="quote-en">"We will utilize these pedagogical tools in our classrooms, structuring lesson plans around students' natural curiosity."</div>
      <div class="quote-meta">
        <span>📍 माध्यमिक शिक्षक, छिंदवाड़ा</span>
        <span style="color: #008aab; font-weight: 700;">[Pedagogy Design]</span>
      </div>
    </div>

    <!-- Joyful Pedagogies Quotes -->
    <div class="quote-card" style="border-left-color: #10b981;">
      <div class="quote-hi">"बच्चों को एक अच्छा माहौल तैयार करने के लिए प्रेरित करना एवं उनके पूर्वज्ञान के अनुसार शिक्षण कार्य में व्यस्त रखना।"</div>
      <div class="quote-en">"Motivating students through a supportive classroom culture and scaffolding tasks according to their prior knowledge."</div>
      <div class="quote-meta">
        <span>📍 विज्ञान शिक्षक, देवास</span>
        <span style="color: #059669; font-weight: 700;">[Scaffolded Learning]</span>
      </div>
    </div>

    <!-- Infrastructure Constraints Quotes -->
    <div class="quote-card" style="border-left-color: #f59e0b;">
      <div class="quote-hi">"ग्रामीण क्षेत्रों में नेटवर्क समस्या के कारण शिक्षण सामग्री को ऑफलाइन मोड में उपलब्ध कराना अत्यंत आवश्यक है।"</div>
      <div class="quote-en">"Given remote connectivity constraints, pre-downloading and offline caching of training modules is an absolute necessity."</div>
      <div class="quote-meta">
        <span>📍 शिक्षक, डिंडोरी</span>
        <span style="color: #d97706; font-weight: 700;">[Offline Sync Need]</span>
      </div>
    </div>

    <!-- Psychological Safety Quotes -->
    <div class="quote-card" style="border-left-color: #8b5cf6;">
      <div class="quote-hi">"बिना किसी प्रशासनिक दबाव या डर के जब हम अपनी कक्षागत कठिनाइयों पर बात करते हैं, तो नया सीखने का उत्साह बढ़ता है।"</div>
      <div class="quote-en">"Discussing classroom struggles in a non-punitive, supportive peer space dramatically elevates our intrinsic motivation."</div>
      <div class="quote-meta">
        <span>📍 शिक्षिका, रीवा</span>
        <span style="color: #7c3aed; font-weight: 700;">[Psychological Safety]</span>
      </div>
    </div>
  </div>

  <!-- ======================================================================= -->
  <!-- PAGES 5+: COMPLETE ACADEMIC RESEARCH MONOGRAPH (APA 7.0)               -->
  <!-- ======================================================================= -->
  <div class="page-break"></div>

  <div class="header-banner" style="background: #003366;">
    <div class="eyebrow">Rajya Shiksha Kendra (RSK) Academic Monograph Series • Volume 2026-II</div>
    <h1 class="doc-title" style="font-size: 15pt;">Decentralized Professional Learning Communities and Pedagogical Transformation: An Empirical and Qualitative Study of Madhya Pradesh's Shikshak Samvad (Grades 6–8)</h1>
    <div class="doc-subtitle">
      State Academic Research Directorate, Rajya Shiksha Kendra (RSK), Madhya Pradesh × Senior Education Specialists, Peepul India
    </div>
  </div>

  <div class="paper-container">
    {paper_html_content}
  </div>

</body>
</html>
"""

# Write HTML to disk
compendium_html_path = os.path.abspath('RSK_Master_CLSS_Executive_Complete_Compendium.html')
with open(compendium_html_path, 'w', encoding='utf-8') as f:
    f.write(compendium_html)

print(f"Generated Complete Compendium HTML: {compendium_html_path} ({len(compendium_html):,} bytes)")

# Convert to PDF with Playwright
output_pdf_path = os.path.abspath('RSK_Master_CLSS_Executive_Complete_Compendium.pdf')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('file:///' + compendium_html_path.replace('\\', '/'), wait_until='networkidle')
    page.wait_for_timeout(2000)
    
    page.pdf(
        path=output_pdf_path,
        format='A4',
        print_background=True,
        margin={
            'top': '8mm',
            'bottom': '8mm',
            'left': '8mm',
            'right': '8mm'
        }
    )
    print(f"PDF SUCCESSFULLY GENERATED: {output_pdf_path} ({os.path.getsize(output_pdf_path):,} bytes)")
    browser.close()
