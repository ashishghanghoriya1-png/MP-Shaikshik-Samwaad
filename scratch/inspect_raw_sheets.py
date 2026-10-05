import pandas as pd
import os

WORKSPACE_DIR = r"c:\Master Dashboard for CLSS"
DISTRICT_FILE = os.path.join(WORKSPACE_DIR, "SS_ResponseDetail_District Level_Grades 6-8_August.xlsx")
CLUSTER_FILE = os.path.join(WORKSPACE_DIR, "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx")

print("=== INSPECTING CLUSTER LEVEL WORKBOOK ===")
xl_c = pd.ExcelFile(CLUSTER_FILE)
print("Sheet names:", xl_c.sheet_names)
for s in xl_c.sheet_names:
    df = xl_c.parse(s)
    print(f"Sheet '{s}': shape={df.shape}")
    print("  Columns:", df.columns[:15].tolist())

print("\n=== INSPECTING DISTRICT LEVEL WORKBOOK ===")
xl_d = pd.ExcelFile(DISTRICT_FILE)
print("Sheet names:", xl_d.sheet_names)
for s in xl_d.sheet_names:
    df = xl_d.parse(s)
    print(f"Sheet '{s}': shape={df.shape}")
    print("  Columns:", df.columns[:15].tolist())
