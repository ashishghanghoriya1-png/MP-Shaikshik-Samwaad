import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')
fc = 'SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx'
fd = 'SS_ResponseDetail_District Level_Grades 6-8_August.xlsx'

qm_c = pd.read_excel(fc, sheet_name='Question Master')
qm_d = pd.read_excel(fd, sheet_name='Question Master')

print("--- CLUSTER LEVEL QUESTION MASTER ---")
for q in [95, 96, 97, 76, 77, 71, 65, 86, 82]:
    r = qm_c[qm_c['QuestionId'] == q]
    if not r.empty:
        role = r.iloc[0]['RoleName']
        txt = r.iloc[0]['QuestionText']
        print(f"CLSS Q{q} (Role: {role}): {txt}")

print("\n--- DISTRICT LEVEL QUESTION MASTER ---")
for q in [51]:
    r = qm_d[qm_d['QuestionId'] == q]
    if not r.empty:
        role = r.iloc[0]['RoleName']
        txt = r.iloc[0]['QuestionText']
        print(f"DO Q{q} (Role: {role}): {txt}")
