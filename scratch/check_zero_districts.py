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

print(f"Total Unique Districts in dataset: {len(all_districts)}")

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

print("\n--- ZERO RECORD CHECK ACROSS ALL 52 DISTRICTS ---")
print(f"Districts with 0 CLSS Teachers: {len(df_summary[df_summary['CLSS_Teachers'] == 0])}")
print(f"Districts with 0 CLSS Facilitators: {len(df_summary[df_summary['CLSS_Facilitators'] == 0])}")
print(f"Districts with 0 CLSS Monitors: {len(df_summary[df_summary['CLSS_Monitors'] == 0])}")
print(f"Districts with 0 DO Participants: {len(df_summary[df_summary['DO_Participants'] == 0])}")
print(f"Districts with 0 DO Facilitators: {len(df_summary[df_summary['DO_Facilitators'] == 0])}")
print(f"Districts with 0 DO Monitors: {len(df_summary[df_summary['DO_Monitors'] == 0])}")

print("\n--- DETAILED BREAKDOWN OF DISTRICTS WITH ZEROES ---")
zero_any = df_summary[(df_summary['CLSS_Teachers'] == 0) | 
                      (df_summary['CLSS_Facilitators'] == 0) | 
                      (df_summary['CLSS_Monitors'] == 0) | 
                      (df_summary['DO_Participants'] == 0) | 
                      (df_summary['DO_Facilitators'] == 0) | 
                      (df_summary['DO_Monitors'] == 0)]
print(zero_any.to_string(index=False))

# Also check official 55 MP districts against this dataset
official_55_mp = [
    "Agar Malwa", "Alirajpur", "Anuppur", "Ashoknagar", "Balaghat", "Barwani", "Betul", "Bhind", "Bhopal", 
    "Burhanpur", "Chhatarpur", "Chhindwara", "Damoh", "Datia", "Dewas", "Dhar", "Dindori", "Guna", "Gwalior", 
    "Harda", "Hoshangabad", "Narmadapuram", "Indore", "Jabalpur", "Jhabua", "Katni", "Khandwa", "Khargone", 
    "Maihar", "Mandla", "Mandsaur", "Mauganj", "Morena", "Narsinghpur", "Neemuch", "Niwari", "Pandhurna", 
    "Panna", "Raisen", "Rajgarh", "Ratlam", "Rewa", "Sagar", "Satna", "Sehore", "Seoni", "Shahdol", 
    "Shajapur", "Sheopur", "Shivpuri", "Sidhi", "Singrauli", "Tikamgarh", "Ujjain", "Umaria", "Vidisha"
]

missing_from_survey = [d for d in official_55_mp if d not in all_districts and (d != "Hoshangabad" or "Narmadapuram" not in all_districts)]
print(f"\nOfficial MP Districts completely missing from Survey dataset: {missing_from_survey}")
