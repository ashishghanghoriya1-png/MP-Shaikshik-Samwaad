import pandas as pd

CLUSTER_FILE = r'c:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx'
DISTRICT_FILE = r'c:\Master Dashboard for CLSS\SS_ResponseDetail_District Level_Grades 6-8_August.xlsx'

qm_c = pd.read_excel(CLUSTER_FILE, sheet_name='Question Master')
p_c = pd.read_excel(CLUSTER_FILE, sheet_name='Participants')
f_c = pd.read_excel(CLUSTER_FILE, sheet_name='Facilitator')
m_c = pd.read_excel(CLUSTER_FILE, sheet_name='Monitor')

qm_d = pd.read_excel(DISTRICT_FILE, sheet_name='Question Master')
p_d = pd.read_excel(DISTRICT_FILE, sheet_name='Participants')
f_d = pd.read_excel(DISTRICT_FILE, sheet_name='Facilitator')
m_d = pd.read_excel(DISTRICT_FILE, sheet_name='Monitor')

def count_matches(qm_df, m_df, f_df, p_df):
    cnt = 0
    for _, r in qm_df.iterrows():
        qid = str(r['QuestionId']).strip()
        role = str(r['RoleName']).strip()
        if any(k in role for k in ['Facilitator', 'सहजकर्ता', 'फैसिलिटेटर']):
            df = f_df
        elif any(k in role for k in ['Monitor', 'Observer', 'अवलोकनकर्ता', 'मॉनिटर', 'पर्यवेक्षक']):
            df = m_df
        else:
            df = p_df
        col_match = next((c for c in df.columns if str(c).strip() == qid), None)
        if col_match is not None:
            cnt += 1
    return cnt

print('CLSS matches:', count_matches(qm_c, m_c, f_c, p_c))
print('DO matches:', count_matches(qm_d, m_d, f_d, p_d))
