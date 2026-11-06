# Design Specification: CLSS Dashboard KPI & Indicator Reference Workbook

**Date:** 2026-11-06  
**Document:** `docs/superpowers/specs/2026-11-06-clss-kpi-excel-dictionary-design.md`  
**Output Target:** `CLSS_Dashboard_KPI_Dictionary.xlsx`  
**Reference Benchmark:** `C:\RR\CLSS_Dashboard_KPI_Reviewed_by_Ashish.xlsx` / Deepa Raghuwanshi's IPT KPI Template  

---

## 1. Executive Summary & Objective

The Shaikshik Samwaad (CLSS) Master Dashboard (Grades 6–8 Math & Science) serves the Madhya Pradesh Rajya Shiksha Kendra (RSK) and 52 district teams. While the dashboard visualizes participation, cascade delivery, and pedagogical quality across cycles (August, September, and Consolidated), stakeholders require a definitive, human-readable Excel reference workbook. 

This workbook documents:
1. **What each metric/visual means** in plain English.
2. **Where the data originates** (exact source files, worksheets, question IDs, and admin tables).
3. **How each indicator is derived** (mathematical formulas, numerators, denominators, and boundary rules).
4. **How the composite indices function** (Pedagogy Score calculation and the 4-Quadrant Strategic Matrix).

The design prioritizes simplicity, clarity, and institutional formatting—avoiding synthetic, auto-generated styles in favor of clean executive typography, proper column auto-sizing, and frozen headers.

---

## 2. Workbook Architecture (4 Dedicated Sheets)

### Sheet 1: `Overview & Summary`
* **Purpose:** Sets the foundation, user roles, data collection mechanisms, and global slicer behavior.
* **Sections:**
  1. **Dashboard Identity & Governance:**
     * Name: RSK Madhya Pradesh Shaikshik Samwaad (CLSS) Executive Dashboard
     * Target Audience: State Leadership (RSK Apex, TEA), District Core Committees (DPC, APC, DIET Principals), Block/Cluster Leaders (CACs, Facilitators)
     * Refresh Cadence: Monthly post-Samwaad workshop cycles
     * Scope: 52 Districts, 313 Blocks, 2,822 CRC Clusters, Grades 6–8 Math & Science
  2. **Raw Data Lineage Table:**
     * `S1: Cadre Universe Master` -> `Varg Wise Teacher Count.xlsx` (68,427 Varg-2 Middle School teachers)
     * `S2: Training Venues Master` -> `Madhya_Pradesh_All_Clusters_Master_List.xlsx` (2,822 CRCs + 50 DIETs = 2,872 venues)
     * `S3: August Cluster Responses` -> `SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx` (23,785 teachers, 5,463 facilitators, 577 monitors)
     * `S4: September Cluster Responses` -> `SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx` (23,169 teachers, 5,618 facilitators, 612 monitors)
     * `S5: District Orientation Form` -> `SS_ResponseDetail_District Level_Grades 6-8_August.xlsx` (4,454 participants)
     * `S6: State Teacher Database (DIKSHA / TPD)` -> `TPD reach_User mapping_till 20260926.xlsx` (Unified teacher credentials)
  3. **Global Filter & View Hierarchy:**
     * August 2026 Cycle: 50 active reporting districts (Dewas and Sehore non-reporting).
     * September 2026 Cycle: 52 active reporting districts (100% state coverage).
     * Consolidated Multi-Cycle: Cumulative gross attendees with 2-cycle universe multiplier (`2 * 68,427 = 136,854`).

---

### Sheet 2: `KPIs & Visuals Dictionary`
* **Purpose:** The master inventory of every visual element, card, chart, and table in the dashboard.
* **Table Schema (12 Columns):**
  1. `Tab / Location` (e.g., Overview Ribbon, State Participation, District 360, Block Directory)
  2. `Item #` (Sequential tracking code: `KPI-01` to `KPI-06`, `VIS-01` to `VIS-15`)
  3. `Component Name` (Official business name)
  4. `Component Type` (KPI Ribbon Card, Horizontal Bar, Donut, SVG Map, Scatter Plot, Table)
  5. `Data Type` (Quantitative Count, Percentage Rate, Categorical, Spatial)
  6. `What It Tells Leadership` (Plain-English executive explanation of what this measures and why it matters)
  7. `Raw Source File & Sheet` (Exact source workbook and tab)
  8. `Raw Field / Question ID` (Specific column header or survey question)
  9. `Derivation & Calculation Formula` (Full mathematical expression: Numerator / Denominator * 100)
  10. `Denominator & Universe Standard` (Rules for expected count vs target)
  11. `Edge Cases & Exclusions` (Handling of stalled districts, null responses, duplicates)
  12. `Status on Live Dashboard` (Verified Active)

* **Key Elements Mapped:**
  * **KPI-01: Coverage Rate** -> Active reporting districts / 52 total districts (96.2% Aug, 100% Sept).
  * **KPI-02: Training Venues** -> Distinct operational CRC clusters + DIET locations (2,872 state total).
  * **KPI-03: Attending Teachers** -> Total verified teachers attending CLSS workshops (23,785 Aug, 23,169 Sept).
  * **KPI-04: District Orientation Participants & Cascade** -> DO attendees (4,454) and cascade deployment rate (3,387 deployed, 76.0% cascade).
  * **KPI-05: Trainers & Observers** -> Facilitators (5,463) + Monitors (577), DO-trained ratio (70.4%).
  * **KPI-06: Total Teacher Universe** -> Base Varg-2 teacher population pool from Shiksha Portal (68,427 state base).
  * **VIS-01: District Turnout Leaderboard** -> Sorted bar chart of teacher turnout % against expected target.
  * **VIS-02: Participant Cadre Breakdown** -> Split across Middle School Teachers, Primary Teachers, Headmasters, and Guest Teachers.
  * **VIS-03: 4-Quadrant Strategic Distribution** -> Categorization of districts into Frontrunners, Pedagogy Focus, Participation Drive, Priority Support.
  * **VIS-04: Interactive 52-District SVG Map** -> Spatial choropleth color-coded by 4 quadrants with red-alert indicator for low pedagogy (<56%).
  * **VIS-05: Turnout vs Pedagogy Scatter Plot** -> 2D coordinate plot with crosshairs at 35% Turnout and 56% Pedagogy.
  * **VIS-06: District 360 Scorecard** -> Composite district deep-dive metrics, rank, and cluster-level breakdown.
  * **VIS-07: Block Directory & Scale Matrix** -> Block-level attendance and cluster density metrics.
  * **VIS-08: Qualitative Teacher Voice Themes** -> Semantic classification of open-text feedback (Academic utility 39.5%, Joyful pedagogy 14.0%, etc.).

---

### Sheet 3: `Pedagogy & Survey Questions`
* **Purpose:** Item-level breakdown of all pedagogical questions across August and September forms that compose the Pedagogy Index.
* **Table Schema (9 Columns):**
  1. `Cycle` (August 2026 / September 2026)
  2. `Question Code` (`AUG-PED-01` to `AUG-PED-15`, `SEPT-PED-01` to `SEPT-PED-13`)
  3. `Question Text (Hindi)` (Original vernacular prompt from field form)
  4. `Question Text (English)` (Clear translation)
  5. `Academic Domain` (TLM & Teaching Aids, Formative Assessment / Checking for Understanding, Student Engagement, Lesson Planning, Wrap-up & Consolidation)
  6. `Scoring Rubric & Benchmark Key` (Definition of 1.0 positive score vs 0.0)
  7. `State Average Baseline %` (Statewide positive response rate)
  8. `Academic Weightage (%)` (Allocated weight based on academic priority matrix)
  9. `District Aggregation Formula` (Average of respondent scores within each district)

---

### Sheet 4: `Cohorts & Quadrants Logic`
* **Purpose:** Detailed mathematical explanation for advanced analytical constructs.
* **Sections:**
  1. **4-Quadrant Matrix Derivation:**
     * X-Axis: Teacher Turnout Rate (% of Expected Denominator), Benchmark = **35.0%**
     * Y-Axis: Composite Pedagogy Score (% Constructivist Practice), Benchmark = **56.0%**
     * Quadrant 1 (Q1): Frontrunners ($\text{Turnout} \ge 35\%$, $\text{Pedagogy} \ge 56\%$)
     * Quadrant 2 (Q2): Pedagogical Focus ($\text{Turnout} < 35\%$, $\text{Pedagogy} \ge 56\%$)
     * Quadrant 3 (Q3): Participation Drive ($\text{Turnout} \ge 35\%$, $\text{Pedagogy} < 56\%$)
     * Quadrant 4 (Q4): Priority Support Zone ($\text{Turnout} < 35\%$, $\text{Pedagogy} < 56\%$)
     * *Consolidated Footprint Rule:* Exactly 27 districts in Priority Support Zone when evaluated over 2 cycles.
  2. **Multi-Cycle Teacher Mobilization & Deduplication:**
     * Gross Attending Teachers: 46,954 (23,785 in Aug + 23,169 in Sept)
     * Net Unique Teachers Reached: 33,866 unique individuals
     * Retained Teachers (Both Cycles): 13,088 teachers (55.0% retention rate of August cohort)
     * Fresh Joiners (September Only): 10,081 teachers
     * Churn / Single-Cycle Attendees (August Only): 10,697 teachers
     * Multi-Cycle Denominator Standard: Base universe multiplied by cycles (`2 * 68,427 = 136,854`) for gross percentage calculation.

---

## 3. Formatting, Typography & Aesthetics (Anti-AI Rules)

To ensure the workbook looks authored by a senior education analyst rather than generated by a generic AI script:
* **Font Family:** Aptos or Calibri, uniform across all sheets.
* **Palette:**
  * Headers: Deep Executive Navy (`#1E3A8A`), 11pt bold, white text.
  * Sheet Title Blocks: Clean white card style with subtle dark border, 14pt bold navy text.
  * Zebra Striping: Soft off-white (`#F8FAFC`) on even rows, pure white (`#FFFFFF`) on odd rows.
  * Hairline Gridlines: Clean `#E2E8F0` thin cell borders.
  * Accent Pills / Badges: Muted slate (`#F1F5F9`), soft blue (`#E0F2FE`), soft amber (`#FEF3C7`), soft emerald (`#ECFDF5`). No fluorescent colors.
* **Layout Mechanics:**
  * Header freeze enabled on all sheets (`freeze_panes = 'C5'` or appropriate).
  * Auto-filter enabled on all table header rows.
  * Explicit column width calculations with safety padding (+4 characters) to prevent `###` overflow.
  * Long text columns (Formulas, Descriptions, Questions) set to `wrap_text=True` with cell vertical alignment set to top/center.
  * Formatted numbers: Integers with commas (`#,##0`), percentages with one decimal (`0.0%`).

---

## 4. Verification & Validation Criteria

1. **Completeness:** All 6 KPI ribbon cards, all 8 primary dashboard charts/maps, all 28 pedagogy questions, and both cohort deduplication models must be fully represented.
2. **Formula Accuracy:** Every formula string must match the JavaScript calculation running in `index.html`.
3. **Data Provenance:** Every row must identify the exact raw file, sheet name, and column name.
4. **File Integrity:** Generated `.xlsx` must open cleanly in Excel without repair prompts or XML warnings.
