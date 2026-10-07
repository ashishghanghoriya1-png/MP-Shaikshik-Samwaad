import os
import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

workspace = r"C:\Users\Peepul\OneDrive - Absolute Return For Kids\Master Dashboard for CLSS - Copy"

aug_dist_file = os.path.join(workspace, "SS_ResponseDetail_District Level_Grades 6-8_August.xlsx")
sep_dist_file = os.path.join(workspace, "September_2026_Raw_Data", "SS_ResponseDetail_District Level_Grades 6-8_September.xlsx")

df_aug_part = pd.read_excel(aug_dist_file, sheet_name="Participants")
df_aug_fac = pd.read_excel(aug_dist_file, sheet_name="Facilitator")
df_aug_mon = pd.read_excel(aug_dist_file, sheet_name="Monitor")

df_sep_part = pd.read_excel(sep_dist_file, sheet_name="Participants")
df_sep_fac = pd.read_excel(sep_dist_file, sheet_name="Facilitator")
df_sep_mon = pd.read_excel(sep_dist_file, sheet_name="Monitor")

print("=== AUGUST DISTRICT TIER BREAKDOWN ===")
print(f"Participants: {len(df_aug_part)}")
print(f"Facilitators (Master Trainers): {len(df_aug_fac)}")
print(f"Monitors (District Observers): {len(df_aug_mon)}")
print(f"Subtotal August: {len(df_aug_part) + len(df_aug_fac) + len(df_aug_mon)}")

print("\n=== SEPTEMBER DISTRICT TIER BREAKDOWN ===")
print(f"Participants: {len(df_sep_part)}")
print(f"Facilitators (Master Trainers): {len(df_sep_fac)}")
print(f"Monitors (District Observers): {len(df_sep_mon)}")
print(f"Subtotal September: {len(df_sep_part) + len(df_sep_fac) + len(df_sep_mon)}")

# Designation aggregation for Participants
df_aug_part['Cycle'] = 'August'
df_sep_part['Cycle'] = 'September'
df_all_do_part = pd.concat([df_aug_part, df_sep_part], ignore_index=True)

print("\n=== COMBINED DESIGNATION BIFURCATION (PARTICIPANTS SHEET) ===")
summary = df_all_do_part.groupby(['DesignationName', 'Cycle']).size().unstack(fill_value=0)
summary['Total'] = summary['August'] + summary['September']
summary['Percentage'] = (summary['Total'] / len(df_all_do_part) * 100).round(2)
summary = summary.sort_values(by='Total', ascending=False)
print(summary.to_string())

# Unique Individuals Breakdown
aug_emps = set(df_aug_part['EmployeeCode'].dropna().astype(str).str.strip())
sep_emps = set(df_sep_part['EmployeeCode'].dropna().astype(str).str.strip())
common_emps = aug_emps.intersection(sep_emps)
aug_only_emps = aug_emps - sep_emps
sep_only_emps = sep_emps - aug_emps
all_unique_emps = aug_emps.union(sep_emps)

print(f"\nUnique Individuals:")
print(f"Total Unique People: {len(all_unique_emps)}")
print(f"Attended Both Cycles (Core): {len(common_emps)} ({len(common_emps)/len(all_unique_emps)*100:.2f}%)")
print(f"Attended August Only: {len(aug_only_emps)} ({len(aug_only_emps)/len(all_unique_emps)*100:.2f}%)")
print(f"Attended September Only: {len(sep_only_emps)} ({len(sep_only_emps)/len(all_unique_emps)*100:.2f}%)")
