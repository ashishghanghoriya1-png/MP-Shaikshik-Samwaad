# CLSS Dashboard KPI & Indicator Reference Workbook Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a clean, human-designed Excel reference workbook (`CLSS_Dashboard_KPI_Dictionary.xlsx`) documenting every metric, graph, calculation formula, and raw data source in the CLSS Master Dashboard based on Deepa's template.

**Architecture:** Python script using `openpyxl` that extracts verified metadata, question texts, mathematical derivations, and cohort rules from the project, applying executive styling (Navy `#1E3A8A` headers, `#F8FAFC` row striping, frozen headers, wrapped formulas, native number formats).

**Tech Stack:** Python 3.14, `openpyxl`, `pytest`

**Spec:** `docs/superpowers/specs/2026-11-06-clss-kpi-excel-dictionary-design.md`

## Global Constraints

- Output path: `CLSS_Dashboard_KPI_Dictionary.xlsx` in the workspace root.
- No artificial, neon, or AI-looking formatting. Palette restricted to Navy `#1E3A8A`, subtle `#F8FAFC` striping, `#E2E8F0` borders.
- No raw em dashes (—) or en dashes (–) in explanatory prose; use commas, colons, or parentheses.
- Explicit column width auto-fitting with safety margin (+4) so text never clips with `###`.
- Header freeze panes and auto-filter enabled on all 4 sheets.

## Review Focus

- Formula text accuracy: Ensure formulas match the JavaScript logic running in `index.html`.
- Denominator consistency: Single-cycle vs 2-cycle consolidated multiplier clearly distinguished.
- Pedagogy question mapping: Complete alignment with August (15 questions) and September (13 questions).
- File generation stability: Clean OpenXML generation with zero workbook repair warnings.

---

### Task 1: Data Model & Overview Sheet Builder

**Files:**
- Create: `scripts/generate_kpi_dictionary.py`
- Create: `tests/test_kpi_dictionary.py`

**Interfaces:**
- Produces: `build_overview_sheet(wb)` writing Sheet 1 (`Overview & Summary`) with identity, audience, cycle scope, and raw dataset lineage (S1 to S6).

- [ ] **Step 1: Write test for Sheet 1 generation**

```python
# tests/test_kpi_dictionary.py
import openpyxl
import os

def test_overview_sheet_structure():
    from scripts.generate_kpi_dictionary import build_workbook
    wb = build_workbook()
    assert "Overview & Summary" in wb.sheetnames
    sheet = wb["Overview & Summary"]
    assert sheet.cell(row=2, column=2).value is not None
    # Verify lineage table header exists
    found_lineage = any("Source ID" in str(sheet.cell(row=r, column=2).value) for r in range(1, 20))
    assert found_lineage
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_kpi_dictionary.py -v`  
Expected: FAIL (module not found)

- [ ] **Step 3: Implement `build_overview_sheet` in `scripts/generate_kpi_dictionary.py`**

Define dataset lineage (Varg-2 count, Cluster August/September, District Orientation, CRC lists, TPD mapping), layout metadata, and styles.

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_kpi_dictionary.py -k test_overview_sheet_structure -v`  
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add scripts/generate_kpi_dictionary.py tests/test_kpi_dictionary.py
git commit -m "feat: add overview and data lineage sheet builder"
```

---

### Task 2: Master KPIs & Visuals Dictionary Sheet

**Files:**
- Modify: `scripts/generate_kpi_dictionary.py`
- Modify: `tests/test_kpi_dictionary.py`

**Interfaces:**
- Produces: `build_kpi_dictionary_sheet(wb)` writing Sheet 2 (`KPIs & Visuals Dictionary`) with all 6 KPI cards, leaderboards, 4-quadrant scatter/map, and tables across 12 structured columns.

- [ ] **Step 1: Write test for Sheet 2**

```python
def test_kpi_dictionary_sheet():
    from scripts.generate_kpi_dictionary import build_workbook
    wb = build_workbook()
    assert "KPIs & Visuals Dictionary" in wb.sheetnames
    sheet = wb["KPIs & Visuals Dictionary"]
    # Verify 12 columns
    headers = [sheet.cell(row=4, column=c).value for c in range(1, 13)]
    assert "Component Name" in headers
    assert "Derivation & Calculation Formula" in headers
    assert "Raw Source File & Sheet" in headers
    # Verify at least 15 components documented
    assert sheet.max_row >= 18
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_kpi_dictionary.py -k test_kpi_dictionary_sheet -v`  
Expected: FAIL

- [ ] **Step 3: Implement `build_kpi_dictionary_sheet`**

Populate items:
- Top 6 KPI Ribbon Cards
- Participation & Reach Visuals (Leaderboard, Cadre Breakdown)
- 4-Quadrant Strategic Matrix & Map
- Scatter Plot Component
- District 360 Scorecard
- Block Directory
- Qualitative Voice Themes

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_kpi_dictionary.py -k test_kpi_dictionary_sheet -v`  
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add scripts/generate_kpi_dictionary.py tests/test_kpi_dictionary.py
git commit -m "feat: add master KPI and visuals dictionary sheet"
```

---

### Task 3: Pedagogy & Survey Questions Sheet

**Files:**
- Modify: `scripts/generate_kpi_dictionary.py`
- Modify: `tests/test_kpi_dictionary.py`

**Interfaces:**
- Produces: `build_pedagogy_sheet(wb)` writing Sheet 3 (`Pedagogy & Survey Questions`) with 15 August questions and 13 September questions, Hindi/English text, rubrics, and weightages.

- [ ] **Step 1: Write test for Sheet 3**

```python
def test_pedagogy_sheet():
    from scripts.generate_kpi_dictionary import build_workbook
    wb = build_workbook()
    assert "Pedagogy & Survey Questions" in wb.sheetnames
    sheet = wb["Pedagogy & Survey Questions"]
    # Check row count covers both cycles (>= 28 questions)
    assert sheet.max_row >= 28
    # Verify headers
    headers = [sheet.cell(row=4, column=c).value for c in range(1, 10)]
    assert "Question Text (Hindi)" in headers
    assert "Academic Domain" in headers
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_kpi_dictionary.py -k test_pedagogy_sheet -v`  
Expected: FAIL

- [ ] **Step 3: Implement `build_pedagogy_sheet`**

Map August (15 items) and September (13 items) questions across TLM, formative assessment, student engagement, wrap-up, and lesson planning.

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_kpi_dictionary.py -k test_pedagogy_sheet -v`  
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add scripts/generate_kpi_dictionary.py tests/test_kpi_dictionary.py
git commit -m "feat: add pedagogy questions mapping sheet"
```

---

### Task 4: Cohorts & Quadrants Logic Sheet

**Files:**
- Modify: `scripts/generate_kpi_dictionary.py`
- Modify: `tests/test_kpi_dictionary.py`

**Interfaces:**
- Produces: `build_cohorts_quadrants_sheet(wb)` writing Sheet 4 (`Cohorts & Quadrants Logic`) detailing 4-Quadrant thresholds and 2-cycle teacher deduplication.

- [ ] **Step 1: Write test for Sheet 4**

```python
def test_cohorts_quadrants_sheet():
    from scripts.generate_kpi_dictionary import build_workbook
    wb = build_workbook()
    assert "Cohorts & Quadrants Logic" in wb.sheetnames
    sheet = wb["Cohorts & Quadrants Logic"]
    # Verify content mentions key numbers
    content = [str(sheet.cell(row=r, column=c).value) for r in range(1, 35) for c in range(1, 10)]
    joined = " ".join(content)
    assert "35.0%" in joined or "0.35" in joined
    assert "56.0%" in joined or "0.56" in joined
    assert "33,866" in joined or "33866" in joined
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_kpi_dictionary.py -k test_cohorts_quadrants_sheet -v`  
Expected: FAIL

- [ ] **Step 3: Implement `build_cohorts_quadrants_sheet`**

Document quadrant boundaries (Turnout 35%, Pedagogy 56%, 27 consolidated priority support districts) and cohort math (46,954 gross, 33,866 net unique, 13,088 repeat).

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_kpi_dictionary.py -k test_cohorts_quadrants_sheet -v`  
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add scripts/generate_kpi_dictionary.py tests/test_kpi_dictionary.py
git commit -m "feat: add cohorts and quadrants logic sheet"
```

---

### Task 5: Formatting, Freezing Panes, Auto-Fit & File Generation

**Files:**
- Modify: `scripts/generate_kpi_dictionary.py`
- Output: `CLSS_Dashboard_KPI_Dictionary.xlsx`

**Interfaces:**
- Produces: `apply_executive_styling(sheet)` and main entry point saving `CLSS_Dashboard_KPI_Dictionary.xlsx`.

- [ ] **Step 1: Write test for full workbook styling & integrity**

```python
def test_full_workbook_output():
    import os
    from scripts.generate_kpi_dictionary import main
    main()
    assert os.path.exists("CLSS_Dashboard_KPI_Dictionary.xlsx")
    wb = openpyxl.load_workbook("CLSS_Dashboard_KPI_Dictionary.xlsx")
    assert len(wb.sheetnames) == 4
    for sname in wb.sheetnames:
        sheet = wb[sname]
        assert sheet.freeze_panes is not None
        # Check column dimensions are set
        assert len(sheet.column_dimensions) > 0
```

- [ ] **Step 2: Implement styling function and main execution**

Apply `#1E3A8A` headers, `#F8FAFC` row striping, auto-width calculation with padding, text wrap, and freeze panes.

- [ ] **Step 3: Run full test suite**

Run: `pytest tests/test_kpi_dictionary.py -v`  
Expected: ALL PASS

- [ ] **Step 4: Commit workbook and generation script**

```bash
git add CLSS_Dashboard_KPI_Dictionary.xlsx scripts/generate_kpi_dictionary.py tests/test_kpi_dictionary.py
git commit -m "feat: generate styled CLSS Dashboard KPI Dictionary workbook"
```
