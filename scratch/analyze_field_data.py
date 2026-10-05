import pandas as pd
import json

CLUSTER_FILE = r'c:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx'
DISTRICT_FILE = r'c:\Master Dashboard for CLSS\SS_ResponseDetail_District Level_Grades 6-8_August.xlsx'

c_mon = pd.read_excel(CLUSTER_FILE, sheet_name='Monitor')
c_fac = pd.read_excel(CLUSTER_FILE, sheet_name='Facilitator')
c_part = pd.read_excel(CLUSTER_FILE, sheet_name='Participants')

d_mon = pd.read_excel(DISTRICT_FILE, sheet_name='Monitor')
d_fac = pd.read_excel(DISTRICT_FILE, sheet_name='Facilitator')
d_part = pd.read_excel(DISTRICT_FILE, sheet_name='Participants')

analysis = {}

# 1. Q77 Challenges faced by CLSS Facilitators
if '77' in c_fac.columns:
    s77 = c_fac['77'].dropna().astype(str)
    analysis['Q77_CLSS_Facilitator_Challenges'] = s77.value_counts().head(10).to_dict()

# 2. Q71 Printed Guide Distribution (CLSS Facilitators)
if '71' in c_fac.columns:
    s71 = c_fac['71'].dropna().astype(str)
    analysis['Q71_CLSS_Printed_Guide_Status'] = s71.value_counts().to_dict()

# 3. Q76 Observer Presence in CLSS
if '76' in c_fac.columns:
    s76 = c_fac['76'].dropna().astype(str)
    analysis['Q76_Observer_Present_At_Cluster'] = s76.value_counts().to_dict()

# 4. Q34 Printed Guide Distribution (DO Participants)
if '34' in d_part.columns:
    s34 = d_part['34'].dropna().astype(str)
    analysis['Q34_DO_Printed_Guide_Status'] = s34.value_counts().to_dict()

# 5. Q51 & Q31 Core Committee Meeting Follow-through
if '51' in d_mon.columns:
    analysis['Q51_DO_Core_Committee_Plan'] = d_mon['51'].dropna().astype(str).value_counts().to_dict()

# 6. Q59 Active Participation Band observed by Monitors
if '59' in c_mon.columns:
    analysis['Q59_Active_Participation_Bands'] = c_mon['59'].dropna().astype(str).value_counts().to_dict()

# 7. Q63 Agenda & Guide Adherence observed by Monitors
if '63' in c_mon.columns:
    analysis['Q63_Agenda_Fidelity'] = c_mon['63'].dropna().astype(str).value_counts().to_dict()

with open('c:/Master Dashboard for CLSS/scratch/qwen_field_analysis_raw.json', 'w', encoding='utf-8') as f:
    json.dump(analysis, f, ensure_ascii=False, indent=2)

print('Analysis dumped to qwen_field_analysis_raw.json!')
