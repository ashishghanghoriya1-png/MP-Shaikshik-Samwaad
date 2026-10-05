# RSK Madhya Pradesh — Shaikshik Samwaad & DO Master BI Dashboard

Automated, bilingual, zero-dependency executive dashboard pipeline for **Madhya Pradesh Rajya Shiksha Kendra (RSK)** Shikshak Samvad & District Orientation (Grades 6–8).

---

## 🌟 Key Features

1. **Exact Mirror of CLSS RF BI Executive Studio**:
   - 7 Interactive Navigation Tabs (Overview & RF Scorecard, Stakeholder Cascade, District 360° Profile & Block Matrix, Pedagogy & Assessment Analytics, 7 Design Principles Triangulation, State League Table, and Question Explorer).
   - High-craft UI styling, Bento grid KPI ribbons, dark/light mode toggle, and print/PDF export.
2. **Instant Bilingual Switch (English $\leftrightarrow$ हिन्दी)**:
   - Dynamic localization for all cards, district names, metrics, charts, and question distributions.
3. **Data Integrity & Missing Values Safeguard**:
   - Strict omission of empty, null, and NaN responses from all percentage calculations and averages.
4. **Stakeholder Cascade Mapping**:
   - DO Monitors & Facilitators $\rightarrow$ CLSS Monitors
   - DO Participants (CACs / Teachers) $\rightarrow$ CLSS Facilitators
   - CLSS Participants $\rightarrow$ Classroom Teachers

---

## 🚀 How to Run and View the Dashboard

### 1. View the Interactive Dashboard
Double-click:
`c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Dashboard.html`

*Opens in Google Chrome, Microsoft Edge, Mozilla Firefox, or any modern web browser with zero external dependencies.*

---

## 🔄 How to Update Figures Every Month (Automated ETL)

Whenever a new cycle or month's data arrives with updated figures (while keeping the standard columns):

1. **Replace the Excel Files** in `c:\Master Dashboard for CLSS\`:
   - `SS_ResponseDetail_District Level_Grades 6-8_August.xlsx` *(or the new month's file with identical name)*
   - `SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx` *(or the new month's file with identical name)*

2. **Run the One-Click Build Script**:
   Open PowerShell or Terminal and execute:
   ```bash
   python "c:\Master Dashboard for CLSS\build_master_dashboard.py"
   ```

3. **Done!** The script will automatically:
   - Clean and parse all 74 questions and responses.
   - Recompute state totals, district rankings, and block matrices.
   - Refresh `dataPackage.json` and generate the updated `RSK_Master_CLSS_Executive_Dashboard.html`.
