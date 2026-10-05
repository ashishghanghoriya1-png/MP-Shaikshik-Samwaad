import io
import sys
import openpyxl
import pandas as pd
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files_to_inspect = [
    r"C:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx",
    r"C:\Master Dashboard for CLSS\SS_ResponseDetail_District Level_Grades 6-8_August.xlsx",
    r"C:\Master Dashboard for CLSS\September_2026_Raw_Data\SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx",
    r"C:\Master Dashboard for CLSS\September_2026_Raw_Data\SS_ResponseDetail_District Level_Grades 6-8_September.xlsx",
    r"C:\My Files Work\CRO 24-25\Analysis_CRO Data_ MP CPD_ 25-26.xlsx",
    r"C:\My Files Work\Gravity\statewide_master_qualitative_transcripts.xlsx",
]

for file_path in files_to_inspect:
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    print("=" * 80)
    print(f"FILE: {os.path.basename(file_path)}")
    print(f"PATH: {file_path}")
    print("=" * 80)
    
    xl = pd.ExcelFile(file_path)
    for sheet_name in xl.sheet_names:
        df = xl.parse(sheet_name, nrows=5)
        # also get total rows
        wb = openpyxl.load_workbook(file_path, read_only=True)
        ws = wb[sheet_name]
        total_rows = ws.max_row
        wb.close()
        
        print(f"\n--- Sheet: '{sheet_name}' (Total Rows: {total_rows}, Total Cols: {len(df.columns)}) ---")
        print("Columns:")
        for idx, col in enumerate(df.columns):
            sample_val = df[col].dropna().iloc[0] if not df[col].dropna().empty else "N/A"
            print(f"  [{idx+1}] {col} | Sample: {str(sample_val)[:50]}")
