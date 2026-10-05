import pandas as pd
import json

CLUSTER_FILE = r'c:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx'
DISTRICT_FILE = r'c:\Master Dashboard for CLSS\SS_ResponseDetail_District Level_Grades 6-8_August.xlsx'

c_fac = pd.read_excel(CLUSTER_FILE, sheet_name='Facilitator')
c_mon = pd.read_excel(CLUSTER_FILE, sheet_name='Monitor')
c_part = pd.read_excel(CLUSTER_FILE, sheet_name='Participants')
d_mon = pd.read_excel(DISTRICT_FILE, sheet_name='Monitor')
d_part = pd.read_excel(DISTRICT_FILE, sheet_name='Participants')

# 1. Observation Deficit (Q76)
no_obs_cnt = int(sum(1 for x in c_fac['76'].dropna() if 'कोई भी अवलोकनकर्ता उपस्थित नहीं' in str(x)))
half_obs_cnt = int(sum(1 for x in c_fac['76'].dropna() if 'आधे संवाद के लिए' in str(x)))
tot_fac = len(c_fac)

# 2. Facilitator Academic Content Support (Q77)
need_info_cnt = int(sum(1 for x in c_fac['77'].dropna() if 'अतिरिक्त जानकारी की आवश्यकता' in str(x)))
low_att_cnt = int(sum(1 for x in c_fac['77'].dropna() if 'उपस्थिति कम थी' in str(x)))

# 3. Printed Guide Status (Q71 & Q34)
clss_no_guide = int(sum(1 for x in c_fac['71'].dropna() if 'नहीं' in str(x)))
clss_soft_only = int(sum(1 for x in c_fac['71'].dropna() if 'सॉफ्ट कॉपी' in str(x) and 'प्रिंट आउट' not in str(x)))
do_no_guide = int(sum(1 for x in d_part['34'].dropna() if 'नहीं' in str(x)))

# 4. Core Committee Meeting (Q51)
do_postponed_cc = int(sum(1 for x in d_mon['51'].dropna() if 'आयोजित नहीं' in str(x)))

# 5. Observed Passive Engagement Bands (Q59)
passive_bands = int(sum(1 for x in c_mon['59'].dropna() if '50-80%' in str(x) or '0-50%' in str(x)))

print(f"Observation Deficit: {no_obs_cnt} clusters without observer ({((no_obs_cnt/tot_fac)*100):.1f}%)")
print(f"Facilitator Knowledge Needs: {need_info_cnt} facilitators")
print(f"Low Attendance Flagged: {low_att_cnt} facilitators")
print(f"No Guide in CLSS: {clss_no_guide}, Soft copy only: {clss_soft_only}")
print(f"DO Core Committee Postponed: {do_postponed_cc} districts")
print(f"Observed Sub-80% Participation: {passive_bands} clusters")
