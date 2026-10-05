import openpyxl, os, glob, pandas as pd, sys
sys.stdout.reconfigure(encoding='utf-8')

print("="*70)
print("FORENSIC EXPLORATION OF ALL DATASETS & BASES")
print("="*70)

# 1. Inspect August Files
aug_clss_path = r'c:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx'
aug_dist_path = r'c:\Master Dashboard for CLSS\SS_ResponseDetail_District Level_Grades 6-8_August.xlsx'
sep_clss_path = r'c:\Master Dashboard for CLSS\September_2026_Raw_Data\SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx'
sep_dist_path = r'c:\Master Dashboard for CLSS\September_2026_Raw_Data\SS_ResponseDetail_District Level_Grades 6-8_September.xlsx'

files = [
    ("August Cluster Level (CLSS)", aug_clss_path),
    ("August District Level (DO)", aug_dist_path),
    ("September Cluster Level (CLSS)", sep_clss_path),
    ("September District Level (DO)", sep_dist_path),
]

for label, fpath in files:
    print(f"\n📁 FILE: {label}")
    print(f"   Path: {fpath}")
    if not os.path.exists(fpath):
        print("   [!] File does not exist!")
        continue
    
    wb = openpyxl.load_workbook(fpath, read_only=True)
    sheets = wb.sheetnames
    print(f"   Sheets: {sheets}")
    
    for sname in sheets:
        if sname == 'Question Master':
            continue
        df = pd.read_excel(fpath, sheet_name=sname)
        print(f"   --> Sheet '{sname}': Total Rows = {len(df):,}, Columns = {len(df.columns)}")
        if 'RoleName' in df.columns:
            roles = df['RoleName'].value_counts().to_dict()
            print(f"       RoleName breakdown: {roles}")
        if 'DesignationName' in df.columns:
            desigs = df['DesignationName'].value_counts().to_dict()
            print(f"       DesignationName top 5: {dict(list(desigs.items())[:5])}")
        if 'EmployeeCode' in df.columns:
            emp_clean = df['EmployeeCode'].dropna().astype(str).str.strip().str.upper()
            emp_clean = emp_clean[~emp_clean.isin(['NAN', 'NONE', 'NULL', '0', '0.0', ''])]
            print(f"       Unique Non-Empty Employee Codes: {emp_clean.nunique():,}")

