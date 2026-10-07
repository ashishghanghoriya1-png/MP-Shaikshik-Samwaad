import os
import sys
import shutil
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

workspace = r"C:\Users\Peepul\OneDrive - Absolute Return For Kids\Master Dashboard for CLSS - Copy"
tpd_orig = os.path.join(workspace, "TPD reach_User mapping_till 20260926.xlsx")
tpd_downloads = r"C:\Users\Peepul\Downloads\TPD reach_User mapping_till 20260926.xlsx"
tpd_temp = os.path.join(workspace, "scratch", "temp_tpd_copy.xlsx")

# Try to copy from downloads or orig
if os.path.exists(tpd_downloads):
    shutil.copy2(tpd_downloads, tpd_temp)
    tpd_file = tpd_temp
else:
    tpd_file = tpd_orig

aug_file = os.path.join(workspace, "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx")
sep_file = os.path.join(workspace, "September_2026_Raw_Data", "SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx")

print(f"Reading TPD from: {tpd_file}")
df_tpd = pd.read_excel(tpd_file, sheet_name=0)
print(f"TPD Total Rows: {len(df_tpd)}")
print(f"TPD Columns: {list(df_tpd.columns)}")

# Check column D (index 3)
col_d = df_tpd.columns[3]
print(f"\nColumn D (Index 3): '{col_d}'")

# Clean TPD unique IDs
tpd_ids_raw = df_tpd[col_d].dropna().astype(str).str.strip()
tpd_ids = set(x[:-2] if x.endswith('.0') else x for x in tpd_ids_raw if x and x.lower() != 'nan')
print(f"Unique TPD Teacher IDs in Column D: {len(tpd_ids):,}")

# Read August
print("\nReading August Participants...")
df_aug = pd.read_excel(aug_file, sheet_name="Participants")
aug_ids_raw = df_aug['EmployeeCode'].dropna().astype(str).str.strip()
aug_ids = set(x[:-2] if x.endswith('.0') else x for x in aug_ids_raw if x and x.lower() != 'nan')
print(f"August Total Attendee Rows: {len(df_aug):,}")
print(f"August Unique Teacher IDs: {len(aug_ids):,}")

# Read September
print("\nReading September Participants...")
df_sep = pd.read_excel(sep_file, sheet_name="Participants")
sep_ids_raw = df_sep['EmployeeCode'].dropna().astype(str).str.strip()
sep_ids = set(x[:-2] if x.endswith('.0') else x for x in sep_ids_raw if x and x.lower() != 'nan')
print(f"September Total Attendee Rows: {len(df_sep):,}")
print(f"September Unique Teacher IDs: {len(sep_ids):,}")

# Cross-matching
samwaad_unique_ids = aug_ids.union(sep_ids)
samwaad_both_ids = aug_ids.intersection(sep_ids)

tpd_in_aug = tpd_ids.intersection(aug_ids)
tpd_in_sep = tpd_ids.intersection(sep_ids)
tpd_in_both = tpd_ids.intersection(samwaad_both_ids)
tpd_in_either = tpd_ids.intersection(samwaad_unique_ids)
tpd_in_aug_only = tpd_in_aug - tpd_in_sep
tpd_in_sep_only = tpd_in_sep - tpd_in_aug
tpd_not_in_samwaad = tpd_ids - samwaad_unique_ids

print("\n" + "="*85)
print("              TPD REACH USER MAPPING vs. SHAIKSHIK SAMWAAD CROSS-MATCH")
print("="*85)
print(f"1. Total Unique Teacher IDs in TPD Column D:      {len(tpd_ids):,}")
print(f"2. Matched in August 2026 Samwaad:                 {len(tpd_in_aug):,} ({len(tpd_in_aug)/len(tpd_ids)*100:.2f}%)")
print(f"3. Matched in September 2026 Samwaad:              {len(tpd_in_sep):,} ({len(tpd_in_sep)/len(tpd_ids)*100:.2f}%)")
print(f"4. Matched in BOTH August & September (Core):      {len(tpd_in_both):,} ({len(tpd_in_both)/len(tpd_ids)*100:.2f}%)")
print(f"5. Matched in August ONLY (Churned in Sep):        {len(tpd_in_aug_only):,} ({len(tpd_in_aug_only)/len(tpd_ids)*100:.2f}%)")
print(f"6. Matched in September ONLY (New Inflow in Sep):  {len(tpd_in_sep_only):,} ({len(tpd_in_sep_only)/len(tpd_ids)*100:.2f}%)")
print(f"7. Matched in EITHER Cycle (Total Active Samwaad): {len(tpd_in_either):,} ({len(tpd_in_either)/len(tpd_ids)*100:.2f}%)")
print(f"8. NOT Found in Either Samwaad Cycle (Unreached):  {len(tpd_not_in_samwaad):,} ({len(tpd_not_in_samwaad)/len(tpd_ids)*100:.2f}%)")
print("="*85)

# Also check reverse mapping (What % of Samwaad attendees are in TPD?)
print("\n" + "="*85)
print("              REVERSE CHECK: SAMWAAD ATTENDEES IN TPD DATABASE")
print("="*85)
print(f"• August Unique Teachers in TPD:    {len(aug_ids.intersection(tpd_ids)):,} / {len(aug_ids):,} ({len(aug_ids.intersection(tpd_ids))/len(aug_ids)*100:.2f}%)")
print(f"• September Unique Teachers in TPD: {len(sep_ids.intersection(tpd_ids)):,} / {len(sep_ids):,} ({len(sep_ids.intersection(tpd_ids))/len(sep_ids)*100:.2f}%)")
print(f"• All Unique Samwaad in TPD:        {len(samwaad_unique_ids.intersection(tpd_ids)):,} / {len(samwaad_unique_ids):,} ({len(samwaad_unique_ids.intersection(tpd_ids))/len(samwaad_unique_ids)*100:.2f}%)")
print("="*85)
