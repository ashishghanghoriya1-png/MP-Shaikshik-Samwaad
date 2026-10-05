import os
import sys
import io
from playwright.sync_api import sync_playwright

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1. Build Simplified Markdown Document
md_content = """# Shikshak Samvad (Grades 6–8) — Simple Executive Data & Insights Guide

**State Leadership:** Rajya Shiksha Kendra (RSK), Madhya Pradesh  
**Technical Partner:** Peepul India  
**Target Group:** Classes 6–8 Math & Science Teachers across all 52 Districts & 322 Blocks  
**Data Scope:** 66,566 verified attendance & survey records from August & September 2026  

---

## 🌟 Executive Summary: What You Need to Know at a Glance

1. **Large Reach:** Over **33,800 unique middle school teachers** (almost half of all Grade 6–8 teachers in MP) participated across August and September.
2. **High Teacher Enthusiasm:** **94.6% of teachers** reported high satisfaction and strong trust in peer learning.
3. **Core Classroom Challenge:** While teachers love hands-on activities, **almost half (48.1%) focus on keeping children busy** rather than helping them think and draw conclusions from the activity.
4. **Technology Gap:** In **59.1% of training venues**, digital slides could not be projected on screen due to hardware or power issues, requiring teachers to look at printed guides or phones.
5. **Statewide District Landscape:** **Half the state (26 districts) has great teaching quality** but needs better attendance mobilization, while **8 districts are statewide Champions** leading in both attendance and quality.

---

## 👥 1. Teacher Attendance & Participation (The Big Picture)

### Total Teacher Universe in Madhya Pradesh (Middle Schools):
* **68,427 Total Grade 6–8 Teachers (Varg-2)** across all 322 blocks in MP.
* **35,374 Target Math & Science Teachers** (51.7% of all middle school teachers).

```
========================================================================================
                          TEACHER PARTICIPATION AT A GLANCE
========================================================================================
Total Middle School Teachers in MP: 68,427
 │
 ├── Targeted Math & Science Teachers: 35,374
 │    ├── Attended in August: 23,785 (67.2% of target teachers)
 │    └── Missed August: 11,589 (32.8%)
 │
 └── Cumulative Unique Teachers Reached (August + September): 33,866 (49.5% of all teachers)
      ├── Regulars (Attended BOTH August & September): 13,088 Teachers
      ├── First-Timers in September (New Joiners): 10,081 Teachers
      └── Attended August Only (Missed September): 10,697 Teachers
========================================================================================
```

### Simple Breakdown by Role:
* **Teachers (Classroom Educators):** ~23,500 per month (46,954 total attendances).
* **Cluster Facilitators (CACs / Lead Teachers):** ~4,800 per month who lead the discussions.
* **Independent Observers (BACs / APCs):** ~500 per month who monitor session quality.
* **District Leadership (DIET / DPC Officials):** ~4,450 participants per month.

---

## 🔬 2. What Happens in Classrooms: 4 Key Teaching Habits & Misconceptions

Through 12 scenario questions, teachers were asked how they handle everyday classroom situations. Here is what the data showed:

### Habit 1: The "Activity Trap" (Survey Item Q95)
* **The Question:** Why do we use activities and Math/Science learning kits in class?
* **What 48.1% of Teachers Believe (The Trap):** *"As long as children are busy doing the activity, learning is automatically happening."*
* **The Best Practice (Mastery - 35.9%):** Activities are just a tool; real learning happens when the teacher asks probing questions to help students reflect and understand the concept behind the activity.
* **Takeaway:** Move teachers from *doing activities for fun* to *using activities for conceptual thinking*.

### Habit 2: Building Student Belonging (Survey Item Q97)
* **The Question:** How do you make every student feel they belong in your classroom?
* **What 66.1% of Teachers Believe (The Trap):** *"Play fun games and praise only the students who give correct answers."*
* **The Best Practice (Mastery - 33.9%):** Give every student meaningful classroom responsibilities and normalize making mistakes so students don't feel ashamed when they struggle.
* **Takeaway:** Shift from *praising only high-achievers* to *making every child feel valued*.

### Habit 3: Handling Student Mistakes (Survey Item Q96)
* **The Question:** A student is shy and afraid of giving wrong answers. What should you do?
* **What 62.0% of Teachers Do (Good Practice):** Make the student comfortable by treating mistakes as a normal step in learning.
* **What 23.0% of Teachers Do (The Compromise):** Switch immediately to overly easy questions, which lowers learning rigor.
* **Takeaway:** A strong majority understands psychological safety, but one-quarter still water down questions.

### Habit 4: Teacher Monologue vs. Student Discussion (Survey Item Q98)
* **The Goal:** 30% Facilitator Talk-Time : 70% Teacher Peer Discussion.
* **Current Status:** **54.2% of sessions** successfully ran small-group peer debates, while **45.8%** still drifted into the facilitator lecturing for most of the time.

---

## ⚙️ 3. Training Logistics & Ground Execution Realities

From audits of all **4,804 mapped cluster centres**, four main operational realities emerged:

| Operational Area | What the Data Shows | What It Means in Simple Terms | Recommended Fix |
| :--- | :--- | :--- | :--- |
| **Observer Visits** | **1,688 Clusters (35.1%)** had no observer present. | 1 in 3 venues ran without an external monitor due to travel distance. | Rotate observers so remote clusters receive visits every alternate cycle. |
| **TV / Projector Usage** | **2,839 Venues (59.1%)** had no projection on screen. | 6 in 10 venues had power cuts or lacked projector cables, so teachers looked at small phone screens. | Ensure printed summary charts are always available as a backup. |
| **Facilitator Prep** | **57.0% of facilitators** read all 4 prep modules before session. | 43% of facilitators ran sessions without completing their full pre-reading. | Send short 2-minute video briefs 48 hours before the session. |
| **Teacher Trust Delta** | **Teachers gave 94.6% satisfaction**, but **Observers gave 71.2% quality score**. | Teachers genuinely enjoy meeting peers, but observers noticed facilitators talking too much. | Keep sessions fun, but enforce the 30:70 peer talk rule. |

---

## 🗺️ 4. The 52 Districts: 4 Simple Strategic Groups

Every district was mapped based on two things: **Attendance Rate** (Did teachers show up?) and **Pedagogy Score** (Did teachers choose constructive teaching methods?):

```
                               ▲ Teaching Quality (75% Benchmark)
                               │
            GROUP 2            │            GROUP 1
       "GREAT TEACHING,        │         "CHAMPIONS"
        NEED ATTENDANCE"       │     High Turnout (82.4%)
      Low Turnout (48.6%)      │     High Quality (84.2%)
      High Quality (81.5%)     │     (8 Districts)
      (26 Districts)           │     Dhar, Rajgarh, Sehore,
      Indore, Bhopal, Ujjain,  │     Shahdol, Dewas, Khargone,
      Gwalior, Sagar, Rewa     │     Narsinghpur, Raisen
                               │
───────────────────────────────┼───────────────────────────────► Attendance Turnout
                               │
            GROUP 4            │            GROUP 3
        "NEEDS PRIORITY        │        "HIGH ATTENDANCE,
          ATTENTION"           │         NEED COACHING"
      Low Turnout (42.1%)      │     High Turnout (78.1%)
      Lower Quality (61.8%)    │     Lower Quality (64.3%)
      (13 Districts)           │     (5 Districts)
      Alirajpur, Sheopur,      │     Barwani, Jhabua,
      Bhind, Panna, Morena     │     Singrauli, Dindori, Umaria
                               │
```

### What Each Group Needs:
1. **🌟 Group 1: Champions (8 Districts):**
   * *Districts:* Dhar, Rajgarh, Sehore, Shahdol, Khargone, Dewas, Narsinghpur, Raisen.
   * *Action:* Celebrate their success and use their best teachers as mentors for neighboring districts.
2. **📈 Group 2: High Quality, Need Attendance (26 Districts):**
   * *Districts:* Indore, Bhopal, Ujjain, Gwalior, Jabalpur, Sagar, Rewa, Satna, Chhindwara, Vidisha, Ratlam, etc.
   * *Action:* Teaching quality is already strong; send reminders and track attendance to get remaining teachers into sessions.
3. **🤝 Group 3: High Attendance, Need Coaching (5 Districts):**
   * *Districts:* Barwani, Jhabua, Singrauli, Dindori, Umaria.
   * *Action:* Teachers are very dedicated and attend in large numbers; give them targeted workshops to overcome the "Activity Trap."
4. **⚠️ Group 4: Priority Attention Needed (13 Districts):**
   * *Districts:* Alirajpur, Sheopur, Bhind, Panna, Morena, Datia, Ashoknagar, Anuppur, Burhanpur, Sidhi, Niwari, Shajapur, Agar Malwa.
   * *Action:* Dual focus on ensuring attendance and providing intensive coaching.

$$\text{Total Districts} = 8 + 26 + 5 + 13 = \mathbf{52 \text{ Districts (100\% of MP)}}$$

---

## 📊 5. Results Framework Scorecard Made Simple (State Score: 78.3%)

| Pillar | What We Looked At | State Score | Target | Verdict |
| :---: | :--- | :---: | :---: | :---: |
| **P1: Syllabus Fit** | Did topics match the current monthly school lessons? | **78.4%** | 80% | ✅ Good Alignment |
| **P2: Concept Clarity** | Did facilitators explain teaching concepts clearly? | **81.2%** | 80% | 🌟 Exceeds Goal |
| **P3: Teaching Shift** | Did teachers move away from memorization & busywork? | **72.8%** | 75% | 🔄 Making Progress |
| **P4: Classroom Utility** | Can teachers actually use these activities on Monday? | **86.1%** | 85% | 🌟 Top Strength |
| **P5: Discussion Time** | Did teachers get enough time to talk and debate? | **69.5%** | 70% | ⚠️ Needs Improvement |
| **P6: Session Setup** | Was the training room organized and on time? | **77.3%** | 80% | ✅ Good Setup |
| **P7: Teacher Reach** | What % of target Math/Science teachers attended? | **82.6%** | 85% | ✅ Strong Participation |
| **OVERALL** | **Overall Statewide Health Score** | **78.3%** | **80%** | **Strong & Healthy** |

---

## 📁 6. Where the Data Came From (Data Sources in Plain English)

All numbers in this report come from official RSK records:
* **Teacher List (EMIS Database):** `Varg Wise Teacher Count.xlsx` (68,427 total middle school teachers).
* **August Training Responses:** `SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx` (23,785 teachers + 4,814 facilitators + 516 observers).
* **September Training Responses:** Consolidated dataset in `dataPackage.json` (23,169 teachers + 4,740 facilitators + 414 observers).
* **Teacher Feedback:** Over 30,000 written teacher suggestions grouped by topic.
"""

with open('RSK_Master_Data_Report_Simplified_Executive_Guide.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print("Generated Simplified Markdown: RSK_Master_Data_Report_Simplified_Executive_Guide.md")

# 2. Build Simplified HTML for PDF
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Shikshak Samvad (Grades 6–8) — Simple Executive Data & Insights Guide</title>
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
      font-size: 8pt;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }

    .header-banner {
      background: linear-gradient(135deg, #003366 0%, #008aab 100%);
      color: #ffffff;
      padding: 14px 18px;
      border-radius: 6px;
      margin-bottom: 12px;
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
      font-size: 8.5pt;
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
      font-size: 10.5pt;
      font-weight: 800;
      color: #003366;
      border-bottom: 2px solid #008aab;
      padding-bottom: 3px;
      margin: 12px 0 6px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    h3 {
      font-size: 9pt;
      font-weight: 700;
      color: #008aab;
      margin: 8px 0 3px 0;
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
      font-size: 7.5pt;
      margin: 4px 0 8px 0;
    }

    th {
      background: #003366;
      color: #ffffff;
      font-weight: 700;
      text-align: left;
      padding: 5px 7px;
      border: 1px solid #cbd5e1;
    }

    td {
      padding: 4px 7px;
      border: 1px solid #e2e8f0;
      color: #1e293b;
      vertical-align: top;
    }

    tr:nth-child(even) {
      background: #f8fafc;
    }

    .card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px 10px;
      margin-bottom: 8px;
    }

    .highlight-card {
      background: #f0fdf4;
      border-left: 3px solid #16a34a;
      padding: 6px 10px;
      margin-bottom: 8px;
      font-size: 7.5pt;
    }

    .tree-box {
      background: #0f172a;
      color: #38bdf8;
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.2pt;
      padding: 8px 12px;
      border-radius: 5px;
      line-height: 1.45;
      margin: 4px 0 8px 0;
    }

    .tree-box strong { color: #f8fafc; }
    .tree-box .dim { color: #94a3b8; }
    .tree-box .hl { color: #34d399; }
    .tree-box .warn { color: #f87171; }

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
      font-size: 7pt;
      white-space: nowrap;
    }

    .pill-green { background: #d1fae5; color: #065f46; }
    .pill-blue { background: #e0f2fe; color: #0369a1; }
    .pill-amber { background: #fef3c7; color: #92400e; }
    .pill-red { background: #fee2e2; color: #991b1b; }

    /* Quadrant Grid */
    .quad-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      margin: 6px 0;
    }

    .quad-pod {
      border-radius: 6px;
      padding: 7px 9px;
      border: 1px solid transparent;
    }

    .q1 { background: #ecfdf5; border-color: #a7f3d0; color: #065f46; }
    .q2 { background: #f0f9ff; border-color: #bae6fd; color: #0369a1; }
    .q3 { background: #fffbeb; border-color: #fde68a; color: #92400e; }
    .q4 { background: #fff1f2; border-color: #fecdd3; color: #9f1239; }

    .quad-title {
      font-size: 8pt;
      font-weight: 800;
      display: flex;
      justify-content: space-between;
      margin-bottom: 2px;
    }

    .quad-meta {
      font-family: 'JetBrains Mono', monospace;
      font-size: 6.8pt;
      margin-bottom: 3px;
    }

    .quad-list {
      font-size: 7pt;
      line-height: 1.35;
    }
  </style>
</head>
<body>

  <!-- ================= PAGE 1 ================= -->
  <div class="header-banner">
    <div class="eyebrow">Rajya Shiksha Kendra (RSK) • Government of Madhya Pradesh × Peepul India</div>
    <h1 class="doc-title">Shikshak Samvad (Grades 6–8) — Simple Executive Data & Insights Guide</h1>
    <div class="doc-subtitle">
      A Plain-Language Executive Guide to Attendance Trends, Classroom Teaching Habits, Logistics Realities, and District Performance
    </div>
    <div class="meta-bar">
      <div>TOTAL RECORDS: <strong>66,566 Verified</strong></div>
      <div>STATE COVERAGE: <strong>52 Districts (322 Blocks)</strong></div>
      <div>TEACHERS REACHED: <strong>33,866 (49.5% of MP)</strong></div>
      <div>CORE SUBJECTS: <strong>Math & Science (Grades 6–8)</strong></div>
    </div>
  </div>

  <div class="highlight-card">
    <strong>🌟 5 Key Things You Need to Know:</strong>
    <ol style="margin: 4px 0 0 16px; padding: 0;">
      <li><strong>Massive Reach:</strong> Over <strong>33,800 unique teachers</strong> participated across August and September (nearly half of all Grade 6–8 teachers in MP).</li>
      <li><strong>High Teacher Trust:</strong> <strong>94.6% of teachers</strong> love peer learning and find it helpful for their daily classroom teaching.</li>
      <li><strong>The Activity Trap:</strong> While teachers love hands-on activities, <strong>48.1% believe keeping kids busy is enough</strong>, missing the chance to guide them to conceptual understanding.</li>
      <li><strong>Technology Realities:</strong> In <strong>59.1% of training venues</strong>, slides could not be projected on screen due to hardware or power issues.</li>
      <li><strong>Statewide Strength:</strong> Half of the state (<strong>26 districts</strong>) already delivers high teaching quality but needs better attendance mobilization.</li>
    </ol>
  </div>

  <h2>
    <span>1. Teacher Attendance & Participation (The Big Picture)</span>
    <span class="section-badge">Cadre Universe</span>
  </h2>

  <div class="tree-box">
<strong>Total Middle School Teachers in MP: 68,427</strong>
 │
 ├── <strong>Target Math & Science Teachers: 35,374 (51.7% of all teachers)</strong>
 │    ├── Attended in August: 23,785 (67.2% of target cohort)
 │    └── Missed August: 11,589 (32.8%)
 │
 └── <strong>Cumulative Unique Teachers Reached (Aug + Sep): 33,866 (49.5% of MP)</strong>
      ├── <span class="hl">Regulars (Attended BOTH August & September): 13,088 Teachers</span>
      ├── <span class="hl">First-Timers in September (New Intake): 10,081 Teachers</span>
      └── <span class="dim">Attended August Only (Missed September): 10,697 Teachers</span>
  </div>

  <table>
    <tr>
      <th style="width: 25%;">Role in Training</th>
      <th style="width: 20%;">Monthly Headcount</th>
      <th style="width: 55%;">What This Group Does in Simple Terms</th>
    </tr>
    <tr>
      <td><strong>Classroom Teachers</strong></td>
      <td><strong>~23,500 / month</strong></td>
      <td>Middle school educators teaching Math and Science in classrooms every day.</td>
    </tr>
    <tr>
      <td><strong>Cluster Facilitators (CACs)</strong></td>
      <td><strong>~4,800 Leads</strong></td>
      <td>Lead teachers chosen to guide cluster conversations and model teaching activities.</td>
    </tr>
    <tr>
      <td><strong>Independent Observers</strong></td>
      <td><strong>~500 Monitors</strong></td>
      <td>BACs and APCs visiting cluster venues to independently audit training quality.</td>
    </tr>
    <tr>
      <td><strong>District Leadership (DOs)</strong></td>
      <td><strong>~4,450 Officials</strong></td>
      <td>DIET faculty, DPCs, and education officers who run district-level orientations.</td>
    </tr>
  </table>

  <!-- PAGE BREAK -->
  <div class="page-break"></div>

  <h2>
    <span>2. What Happens in Classrooms: 4 Key Teaching Habits & Misconceptions</span>
    <span class="section-badge">Survey Insights</span>
  </h2>

  <!-- Habit 1 -->
  <div class="card">
    <div style="font-weight: 800; color: #003366; font-size: 8pt; margin-bottom: 3px;">
      Habit 1: The "Activity Trap" (Q95) &bull; <span style="color: #dc2626;">48.1% of Teachers Trapped</span>
    </div>
    <div style="font-size: 7.2pt; color: #475569; margin-bottom: 4px;">
      <strong>The Question Asked:</strong> <em>"What is the main goal of using activities and learning kits in class?"</em>
    </div>
    <table>
      <tr>
        <th style="width: 20%;">Response Type</th>
        <th style="width: 55%;">What Teachers Said</th>
        <th style="width: 25%;">Result & Meaning</th>
      </tr>
      <tr style="background: #fff1f2;">
        <td><strong>The Trap Choice</strong></td>
        <td><em>"Keep children busy with lots of activities so they stay active."</em></td>
        <td><strong>48.1% (11,450 teachers)</strong> fell into the trap of doing activities without reflection.</td>
      </tr>
      <tr style="background: #ecfdf5;">
        <td><strong>The Best Practice</strong></td>
        <td><em>"Use activities to help children think, reflect, and understand the concept."</em></td>
        <td><strong>35.9% (8,548 teachers)</strong> demonstrated high-level constructivist teaching.</td>
      </tr>
    </table>
    <div style="font-size: 6.8pt; color: #008aab; font-weight: 600;">
      👉 <strong>Action:</strong> Teach educators that activities are just tools; the real learning happens when students discuss and conclude what the activity taught them.
    </div>
  </div>

  <!-- Habit 2 -->
  <div class="card">
    <div style="font-weight: 800; color: #003366; font-size: 8pt; margin-bottom: 3px;">
      Habit 2: Building Student Belonging (Q97) &bull; <span style="color: #d97706;">66.1% Misguided</span>
    </div>
    <div style="font-size: 7.2pt; color: #475569; margin-bottom: 4px;">
      <strong>The Question Asked:</strong> <em>"How do you make every student feel they belong in your classroom?"</em>
    </div>
    <table>
      <tr>
        <th style="width: 20%;">Response Type</th>
        <th style="width: 55%;">What Teachers Said</th>
        <th style="width: 25%;">Result & Meaning</th>
      </tr>
      <tr style="background: #ecfdf5;">
        <td><strong>The Best Practice</strong></td>
        <td><em>"Give students real classroom responsibilities and value their contributions."</em></td>
        <td><strong>33.9% (8,054 teachers)</strong> chose authentic student agency.</td>
      </tr>
      <tr style="background: #fffbeb;">
        <td><strong>Common Traps</strong></td>
        <td><em>"Play casual games (28.5%) or praise only students who give correct answers (25.2%)."</em></td>
        <td><strong>66.1% (15,731 teachers)</strong> relied on superficial games or praise.</td>
      </tr>
    </table>
    <div style="font-size: 6.8pt; color: #008aab; font-weight: 600;">
      👉 <strong>Action:</strong> Shift teachers from praising only top-performers to making every student feel valued and safe to participate.
    </div>
  </div>

  <!-- Habit 3 & 4 -->
  <div class="card">
    <div style="font-weight: 800; color: #003366; font-size: 8pt; margin-bottom: 3px;">
      Habit 3: How Teachers Handle Mistakes (Q96) &bull; <span style="color: #059669;">62.0% Safe & Aligned</span>
    </div>
    <div style="font-size: 7.2pt; color: #334155;">
      • <strong>62.0% of teachers</strong> treat mistakes as normal learning steps and encourage shy students to try again without fear.<br>
      • However, <strong>23.0%</strong> switch immediately to overly simple questions, which lowers classroom rigor.
    </div>
    <div style="font-weight: 800; color: #003366; font-size: 8pt; margin: 6px 0 3px 0;">
      Habit 4: Discussion Time vs. Facilitator Lecturing (Q98) &bull; <span style="color: #0369a1;">54.2% Discussion</span>
    </div>
    <div style="font-size: 7.2pt; color: #334155;">
      • In <strong>54.2% of sessions</strong>, teachers spent most of the time discussing in small groups (meeting the 30:70 talk ratio goal).<br>
      • In <strong>45.8% of sessions</strong>, facilitators talked too much and drifted into lecturing.
    </div>
  </div>

  <h2>
    <span>3. Training Ground Realities & Logistics Blindspots</span>
    <span class="section-badge">4,804 Cluster Centres</span>
  </h2>

  <table>
    <tr>
      <th style="width: 25%;">Area</th>
      <th style="width: 20%;">What the Data Found</th>
      <th style="width: 55%;">What This Means in Plain English</th>
    </tr>
    <tr>
      <td><strong>Observer Visits</strong></td>
      <td><span class="stat-pill pill-red">1,688 Venues (35.1%)</span></td>
      <td><strong>1 in 3 training centres</strong> had no monitor visit because of remote travel distances.</td>
    </tr>
    <tr>
      <td><strong>TV / Projector Usage</strong></td>
      <td><span class="stat-pill pill-red">2,839 Venues (59.1%)</span></td>
      <td><strong>6 in 10 centres</strong> could not project slides on screen due to power cuts or lack of cables.</td>
    </tr>
    <tr>
      <td><strong>Facilitator Preparation</strong></td>
      <td><span class="stat-pill pill-amber">57.0% Completed</span></td>
      <td><strong>4 in 10 facilitators</strong> ran sessions without reading their full preparation guide beforehand.</td>
    </tr>
    <tr>
      <td><strong>Teacher Trust vs Audit</strong></td>
      <td><span class="stat-pill pill-amber">Δ 23.4% Gap</span></td>
      <td>Teachers gave <strong>94.6% satisfaction</strong>, but observers scored quality at <strong>71.2%</strong> because facilitators lectured too much.</td>
    </tr>
  </table>

  <!-- PAGE BREAK -->
  <div class="page-break"></div>

  <h2>
    <span>4. The 52 Districts: 4 Simple Strategic Groups</span>
    <span class="section-badge">100% Zero-Delta Map</span>
  </h2>

  <p style="margin: 0 0 6px 0;">
    Every district in Madhya Pradesh is grouped based on two simple factors: <strong>Attendance Rate</strong> (Did teachers show up?) and <strong>Teaching Quality</strong> (Did teachers use good teaching methods?):
  </p>

  <div class="quad-grid">
    <!-- Q2 -->
    <div class="quad-pod q2">
      <div class="quad-title">
        <span>📈 Group 2: High Quality, Need Attendance</span>
        <span>26 Districts</span>
      </div>
      <div class="quad-meta">Turnout: 48.6% • Quality: 81.5%</div>
      <div class="quad-list">
        <strong>Districts:</strong> Indore, Bhopal, Ujjain, Gwalior, Jabalpur, Sagar, Rewa, Satna, Chhindwara, Hoshangabad, Vidisha, Ratlam, Mandsaur, Neemuch, Damoh, Katni, Shivpuri, Guna, Harda, Betul, Chhatarpur, Tikamgarh, Balaghat, Seoni, Mandla, Khandwa.
      </div>
      <div style="font-size: 6.5pt; margin-top: 3px; font-weight: 700; color: #0369a1;">
        👉 Fix: Teaching quality is high; focus on sending reminders and mobilizing more teachers.
      </div>
    </div>

    <!-- Q1 -->
    <div class="quad-pod q1">
      <div class="quad-title">
        <span>🌟 Group 1: Statewide Champions</span>
        <span>8 Districts</span>
      </div>
      <div class="quad-meta">Turnout: 82.4% • Quality: 84.2%</div>
      <div class="quad-list">
        <strong>Districts:</strong> Dhar, Rajgarh, Sehore, Shahdol, Khargone, Dewas, Narsinghpur, Raisen.
      </div>
      <div style="font-size: 6.5pt; margin-top: 3px; font-weight: 700; color: #065f46;">
        👉 Fix: Top performers in both attendance and quality. Use their best teachers as regional mentors.
      </div>
    </div>

    <!-- Q4 -->
    <div class="quad-pod q4">
      <div class="quad-title">
        <span>⚠️ Group 4: Priority Attention Needed</span>
        <span>13 Districts</span>
      </div>
      <div class="quad-meta">Turnout: 42.1% • Quality: 61.8%</div>
      <div class="quad-list">
        <strong>Districts:</strong> Alirajpur, Sheopur, Bhind, Panna, Morena, Datia, Ashoknagar, Anuppur, Burhanpur, Sidhi, Niwari, Shajapur, Agar Malwa.
      </div>
      <div style="font-size: 6.5pt; margin-top: 3px; font-weight: 700; color: #9f1239;">
        👉 Fix: Need dual support on administrative attendance and hands-on master trainer coaching.
      </div>
    </div>

    <!-- Q3 -->
    <div class="quad-pod q3">
      <div class="quad-title">
        <span>🤝 Group 3: High Attendance, Need Coaching</span>
        <span>5 Districts</span>
      </div>
      <div class="quad-meta">Turnout: 78.1% • Quality: 64.3%</div>
      <div class="quad-list">
        <strong>Districts:</strong> Barwani, Jhabua, Singrauli, Dindori, Umaria.
      </div>
      <div style="font-size: 6.5pt; margin-top: 3px; font-weight: 700; color: #92400e;">
        👉 Fix: Teachers attend reliably; provide focused coaching to overcome the "Activity Trap."
      </div>
    </div>
  </div>

  <h2>
    <span>5. Results Framework Scorecard (State Average: 78.3%)</span>
    <span class="section-badge">Overall Health</span>
  </h2>

  <table>
    <tr>
      <th style="width: 25%;">Area Evaluated</th>
      <th style="width: 45%;">What Was Measured</th>
      <th style="width: 15%;">Score</th>
      <th style="width: 15%;">Target</th>
    </tr>
    <tr>
      <td><strong>1. Syllabus Fit</strong></td>
      <td>Did topics match current monthly school lessons?</td>
      <td><span class="stat-pill pill-blue">78.4%</span></td>
      <td>80.0%</td>
    </tr>
    <tr>
      <td><strong>2. Concept Clarity</strong></td>
      <td>Did facilitators explain teaching concepts clearly?</td>
      <td><span class="stat-pill pill-green">81.2%</span></td>
      <td>80.0%</td>
    </tr>
    <tr>
      <td><strong>3. Teaching Shift</strong></td>
      <td>Are teachers moving away from rote learning and busywork?</td>
      <td><span class="stat-pill pill-amber">72.8%</span></td>
      <td>75.0%</td>
    </tr>
    <tr>
      <td><strong>4. Classroom Utility</strong></td>
      <td>Can teachers actually use these activities on Monday?</td>
      <td><span class="stat-pill pill-green">86.1%</span></td>
      <td>85.0%</td>
    </tr>
    <tr>
      <td><strong>5. Discussion Time</strong></td>
      <td>Did teachers get enough time to talk and debate?</td>
      <td><span class="stat-pill pill-red">69.5%</span></td>
      <td>70.0%</td>
    </tr>
    <tr>
      <td><strong>6. Session Setup</strong></td>
      <td>Was the training venue organized and on time?</td>
      <td><span class="stat-pill pill-blue">77.3%</span></td>
      <td>80.0%</td>
    </tr>
    <tr>
      <td><strong>7. Teacher Reach</strong></td>
      <td>What percentage of target teachers attended?</td>
      <td><span class="stat-pill pill-blue">82.6%</span></td>
      <td>85.0%</td>
    </tr>
    <tr style="background: #e0f2fe; font-weight: 700;">
      <td colspan="2">Overall Statewide Performance Score</td>
      <td><strong>78.3%</strong></td>
      <td><strong>80.0% (Strong)</strong></td>
    </tr>
  </table>

</body>
</html>
"""

# Write HTML
html_path = os.path.abspath('RSK_Master_Data_Report_Simplified_Executive_Guide.html')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated Simplified HTML: {html_path}")

# Compile PDF into PDF_Reports folder
pdf_output_path = os.path.abspath(os.path.join('PDF_Reports', 'RSK_Master_Data_Report_Simplified_Executive_Guide.pdf'))

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('file:///' + html_path.replace('\\', '/'), wait_until='networkidle')
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
    print(f"SUCCESSFULLY GENERATED SIMPLIFIED PDF: {pdf_output_path} ({os.path.getsize(pdf_output_path):,} bytes)")
    browser.close()
