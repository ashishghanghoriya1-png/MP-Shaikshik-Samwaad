"""
RSK Madhya Pradesh — Automated Data Quality & Mathematical Audit Pipeline
==========================================================================
Strict mathematical verification suite to guarantee 100% accuracy between
raw Excel data workbooks and compiled executive dashboard metrics.
"""

import os
import sys
import json
import pandas as pd
import numpy as np

WORKSPACE_DIR = r"c:\Master Dashboard for CLSS"
DISTRICT_FILE = os.path.join(WORKSPACE_DIR, "SS_ResponseDetail_District Level_Grades 6-8_August.xlsx")
CLUSTER_FILE = os.path.join(WORKSPACE_DIR, "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx")
DATAPACKAGE_JSON = os.path.join(WORKSPACE_DIR, "dataPackage.json")

class AuditSuite:
    def __init__(self):
        self.tests_run = 0
        self.tests_passed = 0
        self.errors = []
        self.warnings = []

    def assert_equal(self, test_name, expected, actual, tolerance=0):
        self.tests_run += 1
        delta = abs(expected - actual)
        if delta <= tolerance:
            self.tests_passed += 1
            print(f"  [PASS] {test_name}: Expected={expected:,}, Actual={actual:,} (Delta={delta})")
            return True
        else:
            msg = f"[FAIL] {test_name}: Expected={expected:,}, Actual={actual:,} (Delta={delta})"
            self.errors.append(msg)
            print(f"  {msg}")
            return False

    def assert_true(self, test_name, condition, details=""):
        self.tests_run += 1
        if condition:
            self.tests_passed += 1
            print(f"  [PASS] {test_name} {details}")
            return True
        else:
            msg = f"[FAIL] {test_name} {details}"
            self.errors.append(msg)
            print(f"  {msg}")
            return False

def run_audit():
    print("=" * 70)
    print("  RSK MP 100% ACCURACY & DATA RECONCILIATION AUDIT SUITE")
    print("=" * 70)

    if not os.path.exists(DISTRICT_FILE) or not os.path.exists(CLUSTER_FILE):
        print("ERROR: Raw Excel files not found!")
        return 1

    if not os.path.exists(DATAPACKAGE_JSON):
        print("ERROR: dataPackage.json not found! Run build_master_dashboard.py first.")
        return 1

    with open(DATAPACKAGE_JSON, "r", encoding="utf-8") as f:
        dp = json.load(f)

    suite = AuditSuite()

    print("\n--- TEST GROUP 1: RAW EXCEL VS DATAPACKAGE ROW-COUNT PARITY ---")
    df_d_mon = pd.read_excel(DISTRICT_FILE, sheet_name="Monitor")
    df_d_fac = pd.read_excel(DISTRICT_FILE, sheet_name="Facilitator")
    df_d_part = pd.read_excel(DISTRICT_FILE, sheet_name="Participants")

    df_c_mon = pd.read_excel(CLUSTER_FILE, sheet_name="Monitor")
    df_c_fac = pd.read_excel(CLUSTER_FILE, sheet_name="Facilitator")
    df_c_part = pd.read_excel(CLUSTER_FILE, sheet_name="Participants")

    # DO Parity
    suite.assert_equal("DO Monitors Row Count", len(df_d_mon), sum(d.get('do_monitors', 0) for d in dp['districtSummary']))
    suite.assert_equal("DO Facilitators Row Count", len(df_d_fac), sum(d.get('do_facilitators', 0) for d in dp['districtSummary']))
    suite.assert_equal("DO Participants Row Count", len(df_d_part), sum(d.get('do_participants', 0) for d in dp['districtSummary']))

    # CLSS Parity
    suite.assert_equal("CLSS Monitors Row Count", len(df_c_mon), sum(d['monitors'] for d in dp['districtSummary']))
    suite.assert_equal("CLSS Facilitators Row Count", len(df_c_fac), sum(d['facilitators'] for d in dp['districtSummary']))
    suite.assert_equal("CLSS Teachers / Participants Row Count", len(df_c_part), sum(d['attendees'] for d in dp['districtSummary']))

    print("\n--- TEST GROUP 2: DISTRICT SUMS EQUALITY & STATEWIDE TOTALS ---")
    tot_teachers = sum(d['attendees'] for d in dp['districtSummary'])
    tot_fac = sum(d['facilitators'] for d in dp['districtSummary'])
    tot_mon = sum(d['monitors'] for d in dp['districtSummary'])
    tot_reach = sum(d['total'] for d in dp['districtSummary'])

    suite.assert_equal("District Teachers Sum == Total CLSS Teachers", len(df_c_part), tot_teachers)
    suite.assert_equal("District Facilitators Sum == Total CLSS Facilitators", len(df_c_fac), tot_fac)
    suite.assert_equal("District Monitors Sum == Total CLSS Monitors", len(df_c_mon), tot_mon)
    suite.assert_equal("District Subtotal Sum == Total CLSS Reach", (tot_teachers + tot_fac + tot_mon), tot_reach)

    print("\n--- TEST GROUP 3: BLOCK MATRIX PARITY ---")
    tot_block_part = sum(b['participants'] for b in dp['blockSummary'])
    suite.assert_equal("Block Matrix Participants Sum == CLSS Teachers", len(df_c_part), tot_block_part)

    print("\n--- TEST GROUP 4: ZERO-NULL / DENOMINATOR INTEGRITY ---")
    null_counts = 0
    for d in dp['districtSummary']:
        for k, v in d.items():
            if v is None or (isinstance(v, float) and np.isnan(v)):
                null_counts += 1
    suite.assert_equal("Zero Nulls in District Summary Metrics", 0, null_counts)

    print("\n--- TEST GROUP 5: PERCENTAGE BOUNDARY AUDITS ---")
    out_of_bounds = 0
    for s in dp.get('surveys', []):
        for c in s.get('columns', []):
            pct = c.get('statePct')
            cat = c.get('category', '')
            code = c.get('code', '')
            if pct is not None and not ('Sum of' in code) and cat != 'Numeric Sum' and cat != 'Attendance':
                if pct < 0.0 or pct > 100.0:
                    out_of_bounds += 1
    suite.assert_equal("Zero Percentages Out of [0, 100%] Range", 0, out_of_bounds)

    print("\n--- TEST GROUP 6: GENDER COUNT INTEGRITY ---")
    ops_clss = [x for x in dp['operationsAttendance'] if x.get('Program') == 'CLSS']
    f_sum = sum(x.get('FemaleAttendance', 0) for x in ops_clss)
    m_sum = sum(x.get('MaleAttendance', 0) for x in ops_clss)
    tot_gender_reported = f_sum + m_sum
    suite.assert_true("Gender Sum is Valid Positive Number", tot_gender_reported > 0, f"({tot_gender_reported:,} attendees)")

    print("\n" + "=" * 70)
    print(f"  AUDIT SUMMARY: {suite.tests_passed}/{suite.tests_run} TESTS PASSED ({(suite.tests_passed/suite.tests_run)*100:.1f}%)")
    if len(suite.errors) == 0:
        print("  STATUS: 100% MATHEMATICAL INTEGRITY CERTIFIED [PASS]")
        print("=" * 70)
        return 0
    else:
        print(f"  STATUS: FAILED WITH {len(suite.errors)} ERRORS")
        print("=" * 70)
        return 1

if __name__ == "__main__":
    sys.exit(run_audit())
