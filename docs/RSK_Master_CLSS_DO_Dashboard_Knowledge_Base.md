# RSK Madhya Pradesh — Shaikshik Samwaad & District Orientation (CLSS & DO)
## Master Dashboard Knowledge Base & Provenance Reference Dossier

**Status**: Verified & Production-Synced  
**Last Updated**: October 2026  
**Primary Dataset Scope**: August 2026, September 2026, and Consolidated (Aug + Sep) Multi-Cycle Telemetry  
**Target Applications**: `index.html`, `deploy/index.html`, `RSK_Master_CLSS_Executive_Dashboard.html`, `RSK_Master_CLSS_Executive_Studio_Enhanced.html`, `dataPackage.json`

---

## 1. Executive Program Architecture & Data Lineage

### Primary Sourcing Workbooks (Zero External Mock Constants)
1. **Cluster Level (CLSS) Telemetry**:
   - `SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx` (`Participants`, `Facilitator`, `Monitor`)
   - `SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx` (`Participants`, `Facilitator`, `Monitor`)
2. **District Orientation (DO) Telemetry**:
   - `SS_ResponseDetail_District Level_Grades 6-8_August.xlsx` (`Participants`, `Facilitator`, `Monitor`)
   - `SS_ResponseDetail_District Level_Grades 6-8_September.xlsx` (`Participants`, `Facilitator`, `Monitor`)
3. **State Baseline Universes**:
   - `Varg Wise Teacher Count.xlsx`: Teacher Cadre Universe (Col D) = **68,427** Total Middle School Teachers (Grades 6–8).
   - State Scope: **52 Districts**, **322 Blocks**, **3,014 CRC Clusters**, **52 DIET Centers**.

---

## 2. Core Reconciled State Metrics Across Slicer Cycles

| KPI Metric Card | August 2026 Cycle | September 2026 Cycle | Consolidated (Aug + Sep) Multi-Cycle | Provenance Source |
| :--- | :--- | :--- | :--- | :--- |
| **1. District Coverage Rate** | **96.2%** (50 / 52 Active Districts) | **100.0%** (52 / 52 Active Districts) | **100.0%** (52 / 52 Active Districts) | Cluster & District Workbooks |
| **2. Training Venues** | **2,897** (2,847 CRC + 50 DIET) | **2,971** (2,920 CRC + 51 DIET) | **3,018 Gross \| 3,066 Unique** (3,014 CRC + 52 DIET) | Venue & Cluster Mapping |
| **3. Attending Teachers** | **23,785** / 68,369 (34.8% Turnout) | **23,169** / 67,222 (34.5% Turnout) | **46,954 Gross \| 33,866 Net Unique** (49.5% Net, 68.6% Gross) | CLSS `Participants` Sheet |
| **4. DO Participants** | **4,456** District Leaders | **4,432** District Leaders | **8,888 Gross \| 6,272 Unique** (58.7% Retention, 1,818 Fresh) | DO `Participants` Sheet |
| **5. Trainers & Observers** | **5,465** (4,888 Fac. + 577 Mon.) | **5,259** (4,740 Fac. + 414 Mon.) | **10,724 Gross \| 7,409 Unique** (6,658 Fac. + 681 Mon. + 164 DO) | CLSS & DO `Facilitator` & `Monitor` |
| **6. Teacher Universe** | **68,427** Base (34.8% Reach) | **68,427** Base (33.9% Reach) | **68,427** Base (**49.5% Net Reach \| 68.6% Gross Saturation**) | `Varg Wise Teacher Count.xlsx` |

---

## 3. Teacher Cohort Dynamics & Multi-Cycle Tracking

- **Gross Touchpoints**: `46,954` teacher-session instances across August (`23,785`) and September (`23,169`).
- **Net Unique Teachers Reached**: `33,866` individual teachers (verified via Unique Teacher ID matching against state master dataset).
- **Cohort Transition Breakdown**:
  - **Repeat Champions (Multi-Cycle Retained)**: `13,088` teachers attended both August & September (55.0% retention rate).
  - **August-Only Teachers**: `10,697` teachers attended August only.
  - **September Fresh Intake**: `10,081` new teachers onboarded in September.
  - **Unreached Universe**: `34,561` teachers remaining in the state pool.

---

## 4. Geographic & Granular Directory Aggregation

### State Aggregates
- **Total Blocks in Scope**: `322` administrative blocks across `52` revenue districts.
- **Consolidated Block Mobilization**:
  - **Participating Teachers**: `46,954 Gross | 33,866 Net Unique`
  - **Master Facilitators**: `9,554 Gross`
  - **Field Monitors / Observers**: `930 Gross`
  - **Total Block Cadre Mobilized**: `57,438`

---

## 5. UI/UX & Engineering Safeguards

### 1. Dual-Metric Typography Standard
- When reporting multi-touchpoint metrics (Gross vs Net Unique), both numbers must be rendered with equal typographic prominence (`32px` font-size: `<span class="val-gross">46,954 Gross</span> | <span class="val-net">33,866 Net Unique</span>`).
- Eliminates visual bias between gross session volume and individual human reach.

### 2. DOM Mutative Container Isolation
- Dynamic JavaScript updater functions (`updateKPIs()`) must target inner value slots (`#kpiTeachersContainer`, `#kpiVenuesContainer`), never calling `.parentElement.innerHTML` on composite card containers (`.bento-card`).
- Prevents wiping of header badges, micro-labels, and academic citations.

### 3. Number Animation Bypass Guardrails
- Number interpolation and count-up routines (`animateNumbersInContainer`) must inspect element content:
  ```javascript
  if (target.querySelectorAll('*').length > 0 || text.includes('|')) return;
  ```
- Prevents string stripping of formatted HTML spans and pipe delimiters.

### 4. Zero-Delta Reconciliation Mandate
- Every KPI card, chart series, and table cell must maintain mathematical parity with raw source spreadsheets with zero hardcoding.
