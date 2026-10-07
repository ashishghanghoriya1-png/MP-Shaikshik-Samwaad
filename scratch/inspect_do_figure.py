import os
import pandas as pd

workspace = r"C:\Users\Peepul\OneDrive - Absolute Return For Kids\Master Dashboard for CLSS - Copy"

aug_dist_file = os.path.join(workspace, "SS_ResponseDetail_District Level_Grades 6-8_August.xlsx")
sep_dist_file = os.path.join(workspace, "September_2026_Raw_Data", "SS_ResponseDetail_District Level_Grades 6-8_September.xlsx")

df_aug_do = pd.read_excel(aug_dist_file, sheet_name="Participants")
df_sep_do = pd.read_excel(sep_dist_file, sheet_name="Participants")

print(f"August District Level Participants Row Count: {len(df_aug_do)}")
print(f"September District Level Participants Row Count: {len(df_sep_do)}")
print(f"Sum (8,974): {len(df_aug_do) + len(df_sep_do)}")

print("\n=== AUGUST DISTRICT LEVEL PARTICIPANTS DESIGNATION BREAKDOWN ===")
if 'DesignationName' in df_aug_do.columns:
    print(df_aug_do['DesignationName'].value_counts(dropna=False).head(15))
elif 'RoleName' in df_aug_do.columns:
    print(df_aug_do['RoleName'].value_counts(dropna=False).head(15))

print("\n=== SEPTEMBER DISTRICT LEVEL PARTICIPANTS DESIGNATION BREAKDOWN ===")
if 'DesignationName' in df_sep_do.columns:
    print(df_sep_do['DesignationName'].value_counts(dropna=False).head(15))
elif 'RoleName' in df_sep_do.columns:
    print(df_sep_do['RoleName'].value_counts(dropna=False).head(15))

# Check unique individuals across both
aug_do_emp = set(df_aug_do['EmployeeCode'].dropna().astype(str).str.strip())
sep_do_emp = set(df_sep_do['EmployeeCode'].dropna().astype(str).str.strip())
common_do_emp = aug_do_emp.intersection(sep_do_emp)
unique_do_emp = aug_do_emp.union(sep_do_emp)

print(f"\nUnique DO Individuals: {len(unique_do_emp)}")
print(f"Common DOs in both Aug & Sep: {len(common_do_emp)}")
