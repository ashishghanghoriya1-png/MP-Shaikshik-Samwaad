import os
import pandas as pd

workspace = r"C:\Users\Peepul\OneDrive - Absolute Return For Kids\Master Dashboard for CLSS - Copy"

aug_cluster_file = os.path.join(workspace, "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx")
sep_cluster_file = os.path.join(workspace, "September_2026_Raw_Data", "SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx")
aug_dist_file = os.path.join(workspace, "SS_ResponseDetail_District Level_Grades 6-8_August.xlsx")
sep_dist_file = os.path.join(workspace, "September_2026_Raw_Data", "SS_ResponseDetail_District Level_Grades 6-8_September.xlsx")

# Read Cluster Facilitator sheets
df_aug_fac = pd.read_excel(aug_cluster_file, sheet_name="Facilitator")
df_sep_fac = pd.read_excel(sep_cluster_file, sheet_name="Facilitator")

aug_emp = set(df_aug_fac['EmployeeCode'].dropna().astype(str).str.strip())
sep_emp = set(df_sep_fac['EmployeeCode'].dropna().astype(str).str.strip())

common_emp = aug_emp.intersection(sep_emp)
aug_only_emp = aug_emp - sep_emp
sep_only_emp = sep_emp - aug_emp
total_unique_emp = aug_emp.union(sep_emp)

print("=== CLUSTER FACILITATOR ANALYSIS ===")
print(f"August Cluster Facilitator Records: {len(df_aug_fac)}")
print(f"August Unique Facilitators: {len(aug_emp)}")
print(f"September Cluster Facilitator Records: {len(df_sep_fac)}")
print(f"September Unique Facilitators: {len(sep_emp)}")
print(f"Common Facilitators (Facilitated BOTH Aug & Sep): {len(common_emp)} ({len(common_emp)/len(aug_emp)*100:.2f}% of Aug, {len(common_emp)/len(sep_emp)*100:.2f}% of Sep)")
print(f"August-only Facilitators (Churn): {len(aug_only_emp)} ({len(aug_only_emp)/len(aug_emp)*100:.2f}%)")
print(f"September-only Facilitators (New Intake): {len(sep_only_emp)} ({len(sep_only_emp)/len(sep_emp)*100:.2f}%)")
print(f"Total Unique Facilitators across 2 Cycles: {len(total_unique_emp)}")

# Let's also check with DO Master Trainers included if applicable
df_aug_do_fac = pd.read_excel(aug_dist_file, sheet_name="Facilitator")
df_sep_do_fac = pd.read_excel(sep_dist_file, sheet_name="Facilitator")

aug_all_fac = aug_emp.union(set(df_aug_do_fac['EmployeeCode'].dropna().astype(str).str.strip()))
sep_all_fac = sep_emp.union(set(df_sep_do_fac['EmployeeCode'].dropna().astype(str).str.strip()))
common_all_fac = aug_all_fac.intersection(sep_all_fac)
total_unique_all_fac = aug_all_fac.union(sep_all_fac)

print("\n=== COMBINED (CLUSTER + DO MASTER TRAINERS) FACILITATOR ANALYSIS ===")
print(f"August All Facilitator Records: {len(df_aug_fac) + len(df_aug_do_fac)}")
print(f"August All Unique Facilitators: {len(aug_all_fac)}")
print(f"September All Facilitator Records: {len(df_sep_fac) + len(df_sep_do_fac)}")
print(f"September All Unique Facilitators: {len(sep_all_fac)}")
print(f"Common All Facilitators (BOTH Aug & Sep): {len(common_all_fac)} ({len(common_all_fac)/len(aug_all_fac)*100:.2f}%)")
print(f"Total Unique Facilitators across 2 Cycles: {len(total_unique_all_fac)}")
