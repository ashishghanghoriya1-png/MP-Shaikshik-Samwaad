import io
import sys
import pandas as pd
import openpyxl

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def catalog_clss_august():
    f = r"C:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx"
    xl = pd.ExcelFile(f)
    print("=== AUGUST CLUSTER LEVEL SHEETS & COLUMNS ===")
    for s in xl.sheet_names:
        df = xl.parse(s, nrows=2)
        print(f"\nSheet: '{s}' (Cols: {len(df.columns)})")
        for col in df.columns[:15]: # first 15 cols
            print(f"  - {col}")
        if len(df.columns) > 15:
            print(f"  ... and {len(df.columns)-15} more columns")

def catalog_clss_september():
    f = r"C:\Master Dashboard for CLSS\September_2026_Raw_Data\SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx"
    xl = pd.ExcelFile(f)
    print("\n=== SEPTEMBER CLUSTER LEVEL SHEETS & COLUMNS ===")
    for s in xl.sheet_names:
        df = xl.parse(s, nrows=2)
        print(f"\nSheet: '{s}' (Cols: {len(df.columns)})")
        for col in df.columns[:15]:
            print(f"  - {col}")
        if len(df.columns) > 15:
            print(f"  ... and {len(df.columns)-15} more columns")

def catalog_cro_data():
    f = r"C:\My Files Work\CRO 24-25\Analysis_CRO Data_ MP CPD_ 25-26.xlsx"
    xl = pd.ExcelFile(f)
    print("\n=== CRO (CLASSROOM OBSERVATION) DATASET ===")
    df = xl.parse("Raw Data", nrows=3)
    print(f"Sheet 'Raw Data': {len(df.columns)} columns")
    for i, col in enumerate(df.columns):
        if not col.startswith("Unnamed") and not col.startswith("_"):
            print(f"  [{i+1}] {col}")

catalog_clss_august()
catalog_clss_september()
catalog_cro_data()
