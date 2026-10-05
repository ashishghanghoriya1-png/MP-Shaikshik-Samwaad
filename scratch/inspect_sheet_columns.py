import pandas as pd

CLUSTER_FILE = r'c:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx'
DISTRICT_FILE = r'c:\Master Dashboard for CLSS\SS_ResponseDetail_District Level_Grades 6-8_August.xlsx'

for label, file_path in [('CLSS', CLUSTER_FILE), ('DO', DISTRICT_FILE)]:
    xl = pd.ExcelFile(file_path)
    print(f'=== {label} Sheets: {xl.sheet_names} ===')
    for sheet in xl.sheet_names:
        df = xl.parse(sheet, nrows=2)
        print(f'  Sheet {sheet}: {len(df.columns)} columns -> {list(df.columns)[:15]}')
