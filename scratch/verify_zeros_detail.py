import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

fc = 'SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx'
fd = 'SS_ResponseDetail_District Level_Grades 6-8_August.xlsx'

df_cpart = pd.read_excel(fc, sheet_name='Participants')
df_cfac = pd.read_excel(fc, sheet_name='Facilitator')
df_cmon = pd.read_excel(fc, sheet_name='Monitor')

df_dpart = pd.read_excel(fd, sheet_name='Participants')
df_dfac = pd.read_excel(fd, sheet_name='Facilitator')
df_dmon = pd.read_excel(fd, sheet_name='Monitor')

all_districts = sorted(list(set(
    df_cpart['DistrictName'].dropna().unique().tolist() + 
    df_dpart['DistrictName'].dropna().unique().tolist()
)))

rows = []
for d in all_districts:
    cp = len(df_cpart[df_cpart['DistrictName'] == d])
    cf = len(df_cfac[df_cfac['DistrictName'] == d])
    cm = len(df_cmon[df_cmon['DistrictName'] == d])
    dp = len(df_dpart[df_dpart['DistrictName'] == d])
    dfac = len(df_dfac[df_dfac['DistrictName'] == d])
    dmon = len(df_dmon[df_dmon['DistrictName'] == d])
    tot = cp + cf + cm + dp + dfac + dmon
    rows.append({
        'District': d,
        'CLSS_Teachers': cp,
        'CLSS_Facilitators': cf,
        'CLSS_Monitors': cm,
        'DO_Participants': dp,
        'DO_Facilitators': dfac,
        'DO_Monitors': dmon,
        'Total_Stakeholders': tot
    })

df_summary = pd.DataFrame(rows)

# Full list of 16 districts with 0 DO Monitors
print("Districts with 0 DO Monitors:")
print(df_summary[df_summary['DO_Monitors'] == 0]['District'].tolist())

# Full list of 8 districts with 0 DO Facilitators
print("\nDistricts with 0 DO Facilitators:")
print(df_summary[df_summary['DO_Facilitators'] == 0]['District'].tolist())

# Full list of 4 districts with 0 DO Participants
print("\nDistricts with 0 DO Participants:")
print(df_summary[df_summary['DO_Participants'] == 0]['District'].tolist())
