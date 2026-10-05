import io
import sys
import pandas as pd
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 90)
print("EXHAUSTIVE QUESTION AUDIT & CADRE CROSS-EXAMINATION")
print("=" * 90)

def audit_file_questions(file_path, cycle_name, tier_name):
    xl = pd.ExcelFile(file_path)
    qm_dict = {}
    if 'Question Master' in xl.sheet_names:
        df_qm = xl.parse('Question Master')
        for _, r in df_qm.iterrows():
            qm_dict[str(r.get('QuestionId'))] = (r.get('RoleName'), r.get('QuestionText'))
    
    print(f"\n>>> [{cycle_name} - {tier_name}] Total Sheets: {len(xl.sheet_names)}")
    for s in xl.sheet_names:
        if s == 'Question Master': continue
        df = xl.parse(s)
        print(f"\n--- Sheet: '{s}' (Rows: {len(df):,}, Cols: {len(df.columns)}) ---")
        
        # Check numeric question columns
        for c in df.columns:
            c_str = str(c).strip()
            role, qtext = qm_dict.get(c_str, ("N/A", "N/A"))
            if role != "N/A":
                non_null = df[c].dropna()
                val_counts = non_null.value_counts().head(5).to_dict()
                print(f"  • Col '{c}' | Role: {role} | Total Resp: {len(non_null):,}")
                print(f"    Text: {qtext}")
                print(f"    Top Dist: {val_counts}")

audit_file_questions(r"C:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx", "August 2026", "Cluster Level")
audit_file_questions(r"C:\Master Dashboard for CLSS\SS_ResponseDetail_District Level_Grades 6-8_August.xlsx", "August 2026", "District Level")
audit_file_questions(r"C:\Master Dashboard for CLSS\September_2026_Raw_Data\SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx", "September 2026", "Cluster Level")
audit_file_questions(r"C:\Master Dashboard for CLSS\September_2026_Raw_Data\SS_ResponseDetail_District Level_Grades 6-8_September.xlsx", "September 2026", "District Level")
