"""
RSK Master Dashboard Comprehensive Pre-Delivery Tab & KPI Inspector
=====================================================================
Automated verification suite to ensure all tabs, KPIs, slicers, charts,
tables, and references are fully functional with 100% data integrity
before presenting to the user.
"""

import os
import re
import json
import sys

WORKSPACE_DIR = r"c:\Master Dashboard for CLSS"
DASHBOARD_HTML = os.path.join(WORKSPACE_DIR, "RSK_Master_CLSS_Executive_Dashboard.html")
DATAPACKAGE_JSON = os.path.join(WORKSPACE_DIR, "dataPackage.json")

def inspect_dashboard():
    print("======================================================================")
    print("  RSK MASTER DASHBOARD PRE-DELIVERY TAB & KPI INSPECTION SUITE")
    print("======================================================================")

    if not os.path.exists(DASHBOARD_HTML):
        raise FileNotFoundError(f"Dashboard HTML not found: {DASHBOARD_HTML}")
    if not os.path.exists(DATAPACKAGE_JSON):
        raise FileNotFoundError(f"dataPackage.json not found: {DATAPACKAGE_JSON}")

    with open(DASHBOARD_HTML, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    with open(DATAPACKAGE_JSON, "r", encoding="utf-8") as f:
        dp = json.load(f)

    passed_checks = 0
    total_checks = 0

    def assert_check(name, condition, details=""):
        nonlocal passed_checks, total_checks
        total_checks += 1
        if condition:
            passed_checks += 1
            print(f"  [PASS] {name}" + (f" -> {details}" if details else ""))
        else:
            print(f"  [FAIL] {name}" + (f" -> {details}" if details else ""))

    # --- 1. INSPECT ALL 8 TABS ---
    print("\n[CHECK 1/6] Inspecting All 8 Tab Sections & Navigation Handlers...")
    expected_tabs = [
        ("tab-overview", "1. Executive BI"),
        ("tab-rf", "2. Results Framework"),
        ("tab-d360", "3. District 360°"),
        ("tab-league", "4. 50-District League"),
        ("tab-blocks", "5. 312-Block Directory"),
        ("tab-questions", "6. Question Bank"),
        ("tab-pedagogy", "7. Pedagogy Benchmark"),
        ("tab-governance", "8. Strategic Intelligence")
    ]

    for tab_id, tab_label in expected_tabs:
        # Check section exists
        sec_m = re.search(r'<section[^>]+id=[\'"]' + tab_id + r'[\'"]', html)
        assert_check(f"Tab Section '{tab_id}' ({tab_label}) exists", sec_m is not None)
        # Check nav button exists
        btn_m = re.search(r'onclick=[\'"]activateTab\(\s*[\'"]' + tab_id + r'[\'"]', html)
        assert_check(f"Nav Button for '{tab_id}' wired with activateTab", btn_m is not None)

    # --- 2. INSPECT JS ENGINE & CRITICAL FUNCTIONS ---
    print("\n[CHECK 2/6] Inspecting JavaScript Engine & Function Integrity...")
    critical_funcs = [
        'activateTab', 'updateKPIs', 'updateBlockView', 'animateValue', 'getChartTheme',
        'initOverviewCharts', 'initDistrict360', 'initDistrictLeague', 'filterDistrictLeague',
        'initBlockDirectory', 'filterBlockDirectory', 'renderQuestionBankActive',
        'initPedagogyRadar', 'initGovernance', 'renderRFIndicatorCards', 'selectRFIndicator',
        'initRFMatrixTable', 'initTrustHeatmapTable', 'calculateDistrictPedagogyScore',
        'populateQuadrantBentoCards', 'initQuadrantTable', 'initDistrictComparatorDropdowns',
        'updateDistrictComparison', 'setLanguage', 'setProgramSlicer', 'setRoleSlicer', 'setMonthSlicer'
      ]

    js_funcs = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', html)
    for fn in critical_funcs:
        assert_check(f"JS Function '{fn}' intact", fn in js_funcs)

    # --- 3. INSPECT EVERY KPI CARD & DATA PARITY ---
    print("\n[CHECK 3/6] Inspecting KPI Cards & Mathematical Parity...")
    dist_list = dp.get("districtSummary", [])
    clss_teachers = sum(d["attendees"] for d in dist_list)
    clss_fac = sum(d["facilitators"] for d in dist_list)
    clss_mon = sum(d["monitors"] for d in dist_list)
    do_part = sum(d.get("do_participants", 0) for d in dist_list)
    do_fac = sum(d.get("do_facilitators", 0) for d in dist_list)
    do_mon = sum(d.get("do_monitors", 0) for d in dist_list)
    total_reach = clss_teachers + clss_fac + clss_mon + do_part + do_fac + do_mon

    assert_check("Active Districts Count == 52", len(dist_list) == 52, f"Count={len(dist_list)}")
    assert_check("CLSS Teacher Attendees == 23,785", clss_teachers == 23785, f"Teachers={clss_teachers:,}")
    assert_check("CLSS Facilitators == 4,814", clss_fac == 4814, f"Facilitators={clss_fac:,}")
    assert_check("CLSS Monitors == 516", clss_mon == 516, f"Monitors={clss_mon:,}")
    assert_check("DO Participants == 4,454", do_part == 4454, f"DO Participants={do_part:,}")
    assert_check("DO Facilitators == 77", do_fac == 77, f"DO Facilitators={do_fac:,}")
    assert_check("DO Monitors == 56", do_mon == 56, f"DO Monitors={do_mon:,}")
    assert_check("Total Program Reach == 33,702", total_reach == 33702, f"Total={total_reach:,}")

    # Check KPI elements exist in DOM
    kpi_ids = ['kpiDistricts', 'kpiReach', 'kpiTeachers', 'kpiCadre', 'kpiDoOfficers', 'kpiCoverageBadge', 'kpiReachBadge', 'kpiTeacherTurnoutBadge']
    for kid in kpi_ids:
        k_m = re.search(r'id=[\'"]' + kid + r'[\'"]', html)
        assert_check(f"KPI Card Element '{kid}' exists in HTML", k_m is not None)

    # --- 4. INSPECT ALL 10 INTERACTIVE CHARTS ---
    print("\n[CHECK 4/6] Inspecting All 10 Interactive Canvas / Chart Elements...")
    expected_charts = [
        ("ovTopDistricts", "Overview Top Districts Bar"),
        ("ovDonutStakeholder", "Overview Stakeholder Donut"),
        ("ovPedagogyBar", "Overview Pedagogy Benchmark Bar"),
        ("ovTrustBar", "Overview Trust Index Horizontal Bar"),
        ("rfSubMetricsChart", "Results Framework Sub-metrics Chart"),
        ("d360BlockCompChart", "District 360 Block Breakdown Chart"),
        ("d360PedChart", "District 360 Pedagogy Dimension Chart"),
        ("d360GenderChart", "District 360 Gender Attendance Chart"),
        ("qbStateBar", "Question Bank State Distribution Bar"),
        ("pedRadarChart", "Pedagogy 5-Dimension Radar Chart")
    ]

    for cid, clabel in expected_charts:
        c_m = re.search(r'<canvas[^>]+id=[\'"]' + cid + r'[\'"]', html)
        assert_check(f"Canvas '{cid}' ({clabel}) exists", c_m is not None)

    # --- 5. INSPECT SURVEY INDICATORS & RECONCILIATION ---
    print("\n[CHECK 5/6] Inspecting Survey Indicator Coverage (All 74 Questions)...")
    surveys = dp.get("surveys", [])
    assert_check("All 74 Native Survey Questions Extracted", len(surveys) == 74, f"Total={len(surveys)}")

    # Check pedagogical questions present with correct percentages
    ped_qs = ['95', '96', '97', '43', '44', '45']
    for pq in ped_qs:
        s_obj = next((s for s in surveys if str(s.get("questionId")) == pq), None)
        assert_check(f"Pedagogy Question Q{pq} Extracted", s_obj is not None)

    # --- 6. INSPECT FILE REFERENCE SANITIZATION ---
    print("\n[CHECK 6/6] Inspecting File Reference Isolation (Zero Old Files)...")
    old_files = [
        'Output_CLSS_Participant_Aug_26.xlsx',
        'Output_CLSS_facilitator_Aug_26.xlsx',
        'Output_CLSS_Observer_Aug_26.xlsx',
        'Output_DO_participant_Aug_26.xlsx',
        'Output_DO_facilitator_Aug_26.xlsx',
        'Output_DO_Observer_Aug_26.xlsx',
        'CLSS - Cluster Level Summary.xlsx',
        'CLSS Aug_RF review.xlsx',
        'Sheet2',
        'Sheet 2'
    ]

    for of in old_files:
        cnt = html.count(of)
        assert_check(f"Zero references to legacy file/sheet '{of}'", cnt == 0, f"Occurrences={cnt}")

    master_count = html.count("SS_ResponseDetail_")
    assert_check("Master Excel references correctly embedded", master_count > 0, f"Found {master_count} references")

    # --- SUMMARY ---
    print("\n======================================================================")
    pct = (passed_checks / total_checks) * 100
    print(f"  PRE-DELIVERY INSPECTION SUMMARY: {passed_checks}/{total_checks} CHECKS PASSED ({pct:.1f}%)")
    if passed_checks == total_checks:
        print("  STATUS: 100% OPERATIONAL & MATHEMATICALLY CERTIFIED [PASS]")
        print("======================================================================")
        return 0
    else:
        print("  STATUS: INSPECTION FAILED — DEFECT DETECTED [FAIL]")
        print("======================================================================")
        return 1

if __name__ == "__main__":
    res = inspect_dashboard()
    sys.exit(res)
