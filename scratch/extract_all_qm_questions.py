import pandas as pd

CLUSTER_FILE = r'c:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx'
DISTRICT_FILE = r'c:\Master Dashboard for CLSS\SS_ResponseDetail_District Level_Grades 6-8_August.xlsx'

qm_c = pd.read_excel(CLUSTER_FILE, sheet_name='Question Master')
qm_d = pd.read_excel(DISTRICT_FILE, sheet_name='Question Master')

with open('c:/Master Dashboard for CLSS/scratch/feedback_questions.txt', 'w', encoding='utf-8') as f:
    f.write("=== CLSS QUESTIONS ===\n")
    for _, r in qm_c.iterrows():
        f.write(f"Q{r['QuestionId']} [{r['RoleName']}]: {r['QuestionText']}\n")
    
    f.write("\n=== DO QUESTIONS ===\n")
    for _, r in qm_d.iterrows():
        f.write(f"Q{r['QuestionId']} [{r['RoleName']}]: {r['QuestionText']}\n")

print("Saved feedback_questions.txt!")
