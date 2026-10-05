# RSK Shaikshik Samwaad: Executive Data Origin, Methodology & Reference Guide

**Document Purpose:** Comprehensive provenance, mathematical reconciliation, and data origin manual for the *RSK Shaikshik Samwaad Two-Cycle Comparative Briefing*.  
**Apex State Body:** Rajya Shiksha Kendra (RSK), Madhya Pradesh  
**Technical & Evaluation Partner:** Peepul India  
**Target Scope:** Classes 6–8 Middle School Shikshak Samvad (52 Districts, 322 Blocks, 4,804 Mapped Clusters)  
**Total Target Universe (EMIS Sanctioned Base):** 68,427 Madhyamik Shikshak (Varg-2) Educators  
**Cycles Evaluated:** August 2026 Cycle & September 2026 Cycle  

---

## 1. Executive Summary & Why These Metrics Matter

Every metric presented in the Executive Visual Briefing serves a specific governance, administrative, or academic diagnostic purpose:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                               WHY WE TRACK EACH KEY METRIC                                       │
├───────────────────────────────┬───────────────────────────────┬──────────────────────────────────┤
│ METRIC                        │ REPORTED FIGURE               │ STRATEGIC PURPOSE FOR RSK        │
├───────────────────────────────┼───────────────────────────────┼──────────────────────────────────┤
│ 🏛️ Total Cadre Universe       │ 68,427 Varg-2 Teachers        │ State baseline for true coverage │
│ 🎯 Field Expected Target      │ 68,369 (Aug) | 67,222 (Sep)   │ Ground-level facilitator roster  │
│ 👨‍🏫 Actual Attending Teachers  │ 23,785 (Aug) | 23,169 (Sep)   │ Physical classroom teacher reach │
│ ⚠️ Non-Attendance Gap         │ ~44,500 Teachers / Cycle      │ Priority mobilization target     │
│ 🗺️ District Saturation        │ 50/52 (Aug) → 52/52 (Sep)     │ Administrative operationalization│
│ 🏫 Active Centres / Venues    │ 2,874 (Aug) → 2,861 (Sep)     │ Infrastructure delivery reach    │
│ 👔 District Officials (DO)    │ 4,454 (Aug) → 4,520 (Sep)     │ Cadre orientation & leadership   │
│ 🧑‍🏫 Master Facilitators       │ 4,891 (Aug) → 4,850 (Sep)     │ Academic delivery capacity       │
│ 👁️ Field Observers / Monitors │ 572 (Aug) → 560 (Sep)         │ Independent quality assurance    │
│ 🧠 Pedagogy Misconceptions    │ Q95, Q97, Q96, Q98            │ Diagnostic classroom practice    │
│ 📊 52-District Quadrants      │ Champions, Gaps, Priority     │ Targeted resource allocation     │
└───────────────────────────────┴───────────────────────────────┴──────────────────────────────────┘
```

---

## 2. Methodological Approach & Mathematical Framework

### 2.1 Single-Truth Denominator: Why We Use Total Varg-2 Universe (68,427)
- **Elimination of Artificial Subject Splits:** In preliminary drafts, an exploratory subset of 35,374 Math & Science teachers was examined. However, RSK administrative circulars mandate that **all middle school teachers (Madhyamik Shikshak Varg-2)** teaching Grades 6–8 participate in Shaikshik Samwaad.
- **Ground Verification:** Field cluster facilitators reported expected participants totaling **68,369** (August) and **67,222** (September)—matching the **68,427** sanctioned cadre (99.9% and 98.2% alignment).
- **Standardized Formula:**
  $$\text{Turnout \%} = \left( \frac{\text{Actual Attending Teachers}}{\text{Facilitator Expected Target}} \right) \times 100$$
  - **August 2026:** $\frac{23,785}{68,369} \times 100 = \mathbf{34.8\%}$
  - **September 2026:** $\frac{23,169}{67,222} \times 100 = \mathbf{34.5\%}$
  - **Consolidated:** $\frac{46,954}{135,591} \times 100 = \mathbf{34.6\%}$

### 2.2 District Operational Saturation (50/52 vs. 52/52)
- **August 2026 Scope:** In August, **Dewas and Sehore** had vacant/delayed cluster sessions and submitted 0 response rows at the cluster level. Thus, August cluster saturation was **50 / 52 (96.2%)**.
- **September 2026 Scope:** In September, both Dewas and Sehore conducted their cluster Samwaad sessions and reported full data, restoring **52 / 52 (100.0%)** saturation.

### 2.3 Strategic Quadrant Methodology
Districts are categorized into four distinct strategic groups based on:
1. **Turnout Rate Baseline:** State median turnout of **34.8%**.
2. **Pedagogy Quality Index Baseline:** State composite average accuracy of **50.5%** across core pedagogical questions.

---

## 3. Granular Data Origin & Source Lineage Table

Every figure in the Executive Briefing is directly traced below to the exact raw Excel file, sheet name, column identifier, and mathematical aggregation:

| Metric Name | Value | Exact Raw Source File | Sheet Name | Column Identifier | Mathematical Operation / Logic |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Total Sanctioned Cadre** | **68,427** | `Varg Wise Teacher Count.xlsx` | `Sheet1` | Column E (`Madhymik Shikshak Varg -2 (Total)`) | Sum of all 322 block rows across 52 districts |
| **August Expected Target** | **68,369** | `SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx` | `Facilitator` | Column O / Question `72` (*अपेक्षित प्रतिभागियों की संख्या*) | Sum of all cluster facilitator entries |
| **September Expected Target** | **67,222** | `September_2026_Raw_Data/SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx` | `Facilitator` | Column O / Question `72` | Sum of all cluster facilitator entries |
| **August Actual Teachers** | **23,785** | `SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx` | `Participants` | All rows where `RoleName = 'Participant'` | Exact count of valid teacher submission rows |
| **September Actual Teachers** | **23,169** | `September_2026_Raw_Data/SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx` | `Participants` | All rows where `RoleName = 'Participant'` | Exact count of valid teacher submission rows |
| **Consolidated Teachers** | **46,954** | Both Cluster Workbooks | `Participants` | Total teacher response rows | $23,785 + 23,169 = 46,954$ |
| **August Active Districts** | **50 / 52** | `SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx` | `Participants` | Column E (`DistrictName`) | Count of unique districts with $\ge 10$ submissions (Dewas & Sehore = 0) |
| **September Active Districts** | **52 / 52** | `September_2026_Raw_Data/SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx` | `Participants` | Column E (`DistrictName`) | Count of unique reporting districts (all 52 active) |
| **August Active Venues** | **2,874** | Both August Workbooks | `Participants` | `ClusterCode` (CLSS) + `DistrictCode` (DO) | 2,822 Active Clusters + 52 DIET Venues = 2,874 |
| **September Active Venues** | **2,861** | Both September Workbooks | `Participants` | `ClusterCode` (CLSS) + `DistrictCode` (DO) | 2,809 Active Clusters + 52 DIET Venues = 2,861 |
| **August DO Officials** | **4,454** | `SS_ResponseDetail_District Level_Grades 6-8_August.xlsx` | `Participants` | Total rows in Participants sheet | Exact count of oriented district officials |
| **September DO Officials** | **4,520** | `September_2026_Raw_Data/SS_ResponseDetail_District Level_Grades 6-8_September.xlsx` | `Participants` | Total rows in Participants sheet | Exact count of oriented district officials |
| **August Facilitators** | **4,891** | Both August Workbooks | `Facilitator` | Column A (`EmployeeCode`) | 4,814 Cluster Facilitators + 77 District Master Trainers |
| **September Facilitators** | **4,850** | Both September Workbooks | `Facilitator` | Column A (`EmployeeCode`) | 4,740 Cluster Facilitators + 110 District Master Trainers |
| **August Field Observers** | **572** | Both August Workbooks | `Monitor` | Column A (`EmployeeCode`) | 516 Cluster Observers + 56 District Monitors |
| **September Field Observers** | **560** | Both September Workbooks | `Monitor` | Column A (`EmployeeCode`) | 414 Cluster Observers + 146 District Monitors |
| **Q95: Hands-on TLM Purpose** | **51.9%** | August Cluster Workbook | `Participants` | Column `95` | Choice 1 (Mastery: 51.9%) vs Choice 2 (Activity Trap: 48.1%) |
| **Q97: Normalizing Struggle** | **33.9%** | August Cluster Workbook | `Participants` | Column `97` | Choice 1 (Mastery: 33.9%) vs Choice 2 (Praise Trap: 66.1%) |
| **Q96: Intellectual Safety** | **62.0%** | August Cluster Workbook | `Participants` | Column `96` | Choice 1 (Mastery: 62.0%) vs Choice 2 (Correction Trap: 38.0%) |
| **Q98: Peer Dialogue Structure** | **54.2%** | August Cluster Workbook | `Participants` | Column `98` | Choice 1 (Mastery: 54.2%) vs Choice 2 (Monologue Trap: 45.8%) |

---

## 4. Suggested High-Value Additions for Future Dashboards & Reports

To further enhance executive decision-making and diagnostic power for RSK leadership, the following high-value additions are recommended:

### 💡 Recommendation 1: Teacher Repeat Attendance & Retention Tracking
- **Concept:** Track how many individual teachers attended *both* August and September sessions versus those who only attended one cycle.
- **Value for RSK:** Distinguishes between a dedicated core cohort of teachers and occasional attendees, identifying schools with consistent vs. sporadic engagement.

### 💡 Recommendation 2: Cluster-Level Saturation Depth Map
- **Concept:** Visualize cluster coverage depth (e.g. Percentage of clusters in each block achieving $\ge 15$ attending teachers).
- **Value for RSK:** Enables BEOs and BACs to identify specific underperforming CRC clusters within high-performing districts.

### 💡 Recommendation 3: Misconception Trajectory Shift (Month-on-Month)
- **Concept:** For questions repeated across cycles, track the percentage shift in teachers falling into specific misconception traps (e.g. tracking whether the 66.1% praise trap on Q97 decreases following targeted facilitator micro-modules).
- **Value for RSK:** Provides quantifiable ROI on academic training interventions.

### 💡 Recommendation 4: Special Cohort Deep-Dives (Aspirational & Tribal Blocks)
- **Concept:** Dedicated automated breakdown for NITI Aayog Aspirational Blocks (8 districts) and Special Tribal Focus Blocks (15 districts).
- **Value for RSK:** Supports equity-focused resource allocation and targeted bilingual pedagogical support.

---

*Authored for Rajya Shiksha Kendra (RSK) Madhya Pradesh by Peepul India.*
