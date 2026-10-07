# Master Bilingual Dashboard User Guide Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create an exhaustive, simple, and beautifully structured User Guide for the RSK Master Dashboard in both **English and Hindi (हिंदी)**, explaining every tab (Tabs 1–11), slicer, chart, metric, calculation formula, and color token, available as a persistent markdown dossier, an in-dashboard interactive drawer/modal, and an executive printable PDF.

**Architecture:** 
1. Compile a comprehensive bilingual Markdown manual (`docs/RSK_Master_Dashboard_Complete_Bilingual_User_Guide.md`) with parallel English and Hindi sections for all 11 tabs, 5 slicers, 14 chart visuals, and 6 KPI cards.
2. Build an interactive, slide-out **Help & User Guide Drawer** directly into all 4 dashboard builds with instant search, tab deep-links, and seamless English/Hindi language toggles.
3. Generate a standalone, publication-grade executive PDF (`docs/RSK_Master_Dashboard_Complete_Bilingual_User_Guide.pdf`) via ReportLab with Devanagari typography support.

**Tech Stack:** HTML5, CSS3, JavaScript (Vanilla ES6), Python (ReportLab PDF Generation), Playwright (E2E Automated UI Verification).

**Spec:** [`docs/RSK_Executive_Dashboard_Design_System_Template.md`](file:///c:/Users/Ashish/OneDrive%20-%20Absolute%20Return%20For%20Kids/Master%20Dashboard%20for%20CLSS%20-%20Copy/docs/RSK_Executive_Dashboard_Design_System_Template.md) and [`docs/RSK_Master_CLSS_DO_Dashboard_Knowledge_Base.md`](file:///c:/Users/Ashish/OneDrive%20-%20Absolute%20Return%20For%20Kids/Master%20Dashboard%20for%20CLSS%20-%20Copy/docs/RSK_Master_CLSS_DO_Dashboard_Knowledge_Base.md).

## Global Constraints
- **Zero Omission**: Every tab (1–11), every slicer button, every chart canvas ID, every metric calculation, and every color code must be explained in both English and Hindi.
- **Tone & Clarity**: Simple, intuitive explanations suitable for district collectors, DPCs, block academic coordinators (BACs), and cluster resource persons (CACs).
- **Design Alignment**: Must follow the signature Peepul/RSK Executive Studio aesthetic (`--peepul-teal: #008aab`, `--font-sans: 'Plus Jakarta Sans'`, `--font-display: 'Comfortaa'`).

## Review Focus
1. Bilingual fidelity: Hindi translations must use standard, elegant RSK/Madhya Pradesh educational terminology (e.g., *शैक्षिक संवाद, संकुल, सहजकर्ता, अवलोकनकर्ता, संतृप्ति दर*).
2. Metric precision: Formulas for Gross Touchpoints vs Net Unique Reach and Universe Saturation % must match the exact mathematical definitions in `rsk-metric-auditor`.
3. Slicer explanations: Clear instructions on what changes when clicking *August 2026*, *September 2026*, or *Consolidated (Aug + Sep)*.
4. Chart interpretation: Specific guidance on how to read Radar charts, Scatter quadrants, and Trust heatmaps.
5. In-dashboard usability: The guide modal must open smoothly, support keyword searching, and not interfere with dashboard performance.

---

### Task 1: Master Bilingual Markdown User Guide Dossier
**Files:**
- Create: `docs/RSK_Master_Dashboard_Complete_Bilingual_User_Guide.md`

**Interfaces:**
- Consumes: All 11 tab structures from `index.html` and verified telemetry from `dataPackage.json`.
- Produces: Complete reference manual used by the in-dashboard modal and PDF generator.

- [ ] **Step 1: Draft the Comprehensive Bilingual Markdown Manual**
  - Section 1: Introduction & How to Access the Dashboard (डैशबोर्ड का परिचय और उपयोग).
  - Section 2: Global Controls & Slicers Explained (महीना, पद, जिला और भाषा स्लाइसर).
  - Section 3: Detailed Tab-by-Tab Walkthrough (Tabs 1 to 11 in English & Hindi).
  - Section 4: Key Metrics & Calculation Formulas (मुख्य मैट्रिक्स और गणना सूत्र).
  - Section 5: Chart & Visual Interpretation Guide (चार्ट और ग्राफ को कैसे समझें).
  - Section 6: Color Codes, Badges & Status Indicators (रंग और स्टेटस संकेत).
- [ ] **Step 2: Verify Markdown formatting and bilingual integrity**
- [ ] **Step 3: Commit `docs/RSK_Master_Dashboard_Complete_Bilingual_User_Guide.md`**

---

### Task 2: In-Dashboard Interactive Guide Drawer & Header Action
**Files:**
- Modify: `index.html`
- Modify: `deploy/index.html`
- Modify: `RSK_Master_CLSS_Executive_Dashboard.html`
- Modify: `RSK_Master_CLSS_Executive_Studio_Enhanced.html`

**Interfaces:**
- Consumes: User click on `📖 Help & Guide` in the top navigation ribbon.
- Produces: Slide-out drawer `#dashboardGuideDrawer` containing searchable bilingual guide cards, tab jump-links, and PDF download button.

- [ ] **Step 1: Add "📖 Dashboard Guide / गाइड" button to the top header ribbon**
- [ ] **Step 2: Inject the slide-out `#dashboardGuideDrawer` modal markup with interactive search input and English/Hindi toggle**
- [ ] **Step 3: Implement JavaScript functions `openDashboardGuide()`, `closeDashboardGuide()`, `filterGuideTopics()`, and `toggleGuideLanguage()`**
- [ ] **Step 4: Synchronize across all 4 target HTML files**
- [ ] **Step 5: Commit dashboard updates**

---

### Task 3: Publication-Grade Bilingual PDF Guide Generator
**Files:**
- Create: `generate_bilingual_guide_pdf.py`
- Create: `docs/RSK_Master_Dashboard_Complete_Bilingual_User_Guide.pdf`
- Create: `PDF_Reports/RSK_Master_Dashboard_Complete_Bilingual_User_Guide.pdf`

**Interfaces:**
- Consumes: Content from `docs/RSK_Master_Dashboard_Complete_Bilingual_User_Guide.md`.
- Produces: Multi-page formatted PDF with table of contents, diagrams, and clean typography.

- [ ] **Step 1: Write ReportLab generation script `generate_bilingual_guide_pdf.py`**
- [ ] **Step 2: Run Python script to compile the PDF**
- [ ] **Step 3: Verify PDF size, layout, and visual formatting**
- [ ] **Step 4: Commit generated PDF and script**

---

### Task 4: Playwright Automated E2E Verification
**Files:**
- Create: `scratch_verify_guide_playwright.js`

- [ ] **Step 1: Launch headless browser and test opening/closing the Guide Drawer**
- [ ] **Step 2: Test language switching between English and Hindi in the drawer**
- [ ] **Step 3: Test search filtering of guide sections**
- [ ] **Step 4: Capture verification screenshots**
- [ ] **Step 5: Run full test suite and confirm 100% pass rate**
