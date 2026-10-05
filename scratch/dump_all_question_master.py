import io
import sys
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files = [
    ("August Cluster Level", r"C:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx"),
    ("August District Level", r"C:\Master Dashboard for CLSS\SS_ResponseDetail_District Level_Grades 6-8_August.xlsx"),
    ("September Cluster Level", r"C:\Master Dashboard for CLSS\September_2026_Raw_Data\SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx"),
    ("September District Level", r"C:\Master Dashboard for CLSS\September_2026_Raw_Data\SS_ResponseDetail_District Level_Grades 6-8_September.xlsx"),
]

for label, file_path in files:
    print("=" * 80)
    print(f"QUESTION MASTER FOR: {label}")
    print("=" * 80)
    try:
        xl = pd.ExcelFile(file_path)
        if 'Question Master' in xl.sheet_names:
            df = xl.parse('Question Master')
            for _, row in df.iterrows():
                qid = row.get('QuestionId')
                role = row.get('RoleName')
                qtext = row.get('QuestionText')
                print(f"[{qid}] ({role}): {qtext}")
        else:
            print("Sheets in this file:", xl.sheet_names)
            for s in xl.sheet_names:
                df_s = xl.parse(s, nrows=2)
                print(f"  Sheet '{s}': columns -> {list(df_s.columns[:8])}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

print("\n" + "=" * 80)
print("CRO DATASET SHEETS & HEADERS")
print("=" * 80)
cro_file = r"C:\My Files Work\CRO 24-25\Analysis_CRO Data_ MP CPD_ 25-26.xlsx"
xl_cro = pd.ExcelFile(cro_file)
print("CRO Sheet names:", xl_cro.sheet_names)
for s in xl_cro.sheet_names:
    df_c = xl_cro.parse(s, nrows=3)
    print(f"Sheet '{s}' -> Rows: {len(df_c)}, Cols: {len(df_c.columns)}")
    print("Columns:", [str(c) for c in df_c.columns[:10]])
