import os
import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

workspace = r"C:\Users\Peepul\OneDrive - Absolute Return For Kids\Master Dashboard for CLSS - Copy"

aug_dist_file = os.path.join(workspace, "SS_ResponseDetail_District Level_Grades 6-8_August.xlsx")
sep_dist_file = os.path.join(workspace, "September_2026_Raw_Data", "SS_ResponseDetail_District Level_Grades 6-8_September.xlsx")

df_aug_do = pd.read_excel(aug_dist_file, sheet_name="Participants")
df_aug_fac = pd.read_excel(aug_dist_file, sheet_name="Facilitator")
df_aug_mon = pd.read_excel(aug_dist_file, sheet_name="Monitor")

df_sep_do = pd.read_excel(sep_dist_file, sheet_name="Participants")
df_sep_fac = pd.read_excel(sep_dist_file, sheet_name="Facilitator")
df_sep_mon = pd.read_excel(sep_dist_file, sheet_name="Monitor")

print("=== AUGUST DISTRICT LEVEL (DO) SHEETS ===")
print(f"Participants sheet rows: {len(df_aug_do)}")
print(f"Facilitator sheet rows: {len(df_aug_fac)}")
print(f"Monitor sheet rows: {len(df_aug_mon)}")
print(f"Total August DO records: {len(df_aug_do) + len(df_aug_fac) + len(df_aug_mon)}")

print("\n=== SEPTEMBER DISTRICT LEVEL (DO) SHEETS ===")
print(f"Participants sheet rows: {len(df_sep_do)}")
print(f"Facilitator sheet rows: {len(df_sep_fac)}")
print(f"Monitor sheet rows: {len(df_sep_mon)}")
print(f"Total September DO records: {len(df_sep_do) + len(df_sep_fac) + len(df_sep_mon)}")

print("\n=== AUGUST DO PARTICIPANTS DESIGNATION BREAKDOWN ===")
print(df_aug_do['DesignationName'].value_counts(dropna=False).to_string())

print("\n=== SEPTEMBER DO PARTICIPANTS DESIGNATION BREAKDOWN ===")
print(df_sep_do['DesignationName'].value_counts(dropna=False).to_string())

aug_emp = set(df_aug_do['EmployeeCode'].dropna().astype(str).str.strip())
sep_emp = set(df_sep_do['EmployeeCode'].dropna().astype(str).str.strip())
print(f"\nUnique DO Participants (Aug): {len(aug_emp)}")
print(f"Unique DO Participants (Sep): {len(sep_emp)}")
print(f"Common DO in both Aug & Sep: {len(aug_emp.intersection(sep_emp))}")
print(f"Total Unique DO Individuals across both: {len(aug_emp.union(sep_emp))}")
