import os, json, pandas as pd, sys
sys.stdout.reconfigure(encoding='utf-8')

print("=== VERIFICATION OF COHORT DATA ASSETS ===")

# 1. Verify CSV export file existence and line counts
csv_files = {
    "September_New_Teachers_Intake.csv": 10081,
    "August_Lapsed_Dropout_Calling_List.csv": 10697,
    "August_September_Persistent_Champions.csv": 13088,
    "52_District_Teacher_Cohort_Matrix.csv": 52
}

for fname, expected_rows in csv_files.items():
    fpath = os.path.join(r"c:\Master Dashboard for CLSS\data\exports", fname)
    assert os.path.exists(fpath), f"File {fpath} does not exist!"
    df = pd.read_csv(fpath)
    actual_rows = len(df)
    assert actual_rows == expected_rows, f"{fname}: Expected {expected_rows}, got {actual_rows}"
    print(f"[OK] {fname}: Validated {actual_rows:,} rows (Exact Match!)")

# 2. Verify HTML integrity
html_path = r"c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

assert 'id="tab-cohort"' in html_content, "tab-cohort section missing!"
assert 'id="navTabCohort"' in html_content, "navTabCohort missing!"
assert 'cohortDistrictData' in html_content, "cohortDistrictData missing!"
assert 'renderCohortTab' in html_content, "renderCohortTab function missing!"
assert '33,866' in html_content, "Cumulative count 33,866 missing in HTML!"
assert '13,088' in html_content, "Persistent count 13,088 missing in HTML!"
assert '10,081' in html_content, "New intake count 10,081 missing in HTML!"
assert '10,697' in html_content, "Lapsed count 10,697 missing in HTML!"

print("[OK] Master Dashboard HTML: All Tab 11 components and data bindings verified!")
print("==========================================")
print("ALL AUTOMATED VERIFICATION CHECKS PASSED!")
