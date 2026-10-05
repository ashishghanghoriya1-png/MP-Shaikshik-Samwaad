"""
Extract and calculate all granular KPI metrics:
- Total participants (Cluster + District)
- Total districts covered
- Total training centres / clusters / venues
- Total observers (Monitors)
- Total DO (District Officers / District Officials / Facilitators)
"""

import pandas as pd
import json

cl_part = pd.read_excel('SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx', sheet_name='Participants')
cl_mon = pd.read_excel('SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx', sheet_name='Monitor')
cl_fac = pd.read_excel('SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx', sheet_name='Facilitator')

dist_part = pd.read_excel('SS_ResponseDetail_District Level_Grades 6-8_August.xlsx', sheet_name='Participants')
dist_mon = pd.read_excel('SS_ResponseDetail_District Level_Grades 6-8_August.xlsx', sheet_name='Monitor')
dist_fac = pd.read_excel('SS_ResponseDetail_District Level_Grades 6-8_August.xlsx', sheet_name='Facilitator')

varg_df = pd.read_excel('Varg Wise Teacher Count.xlsx')

data_summary = {
    "total_varg2_universe": int(varg_df['Total Teachers'].sum()), # 68,427
    "total_target_cohort": 35374, # Math & Science specialist base
    "cluster_level": {
        "participants_turnout": len(cl_part), # 23,785
        "unique_participants": int(cl_part['EmployeeCode'].nunique()), # 23,785
        "districts_covered": int(cl_part['DistrictName'].nunique()), # 52
        "blocks_covered": int(cl_part['BlockName'].nunique()), # 312 blocks with turnout out of 322
        "training_centres_clusters_active": int(cl_part['ClusterName'].nunique()), # 2,822 active cluster centres
        "total_state_clusters": 4804,
        "observers_monitors_count": len(cl_mon), # 516
        "unique_observers": int(cl_mon['EmployeeCode'].nunique()), # 516
        "facilitators_count": len(cl_fac), # 4,814
        "unique_facilitators": int(cl_fac['EmployeeCode'].nunique()) # 4,814
    },
    "district_level": {
        "do_participants_count": len(dist_part), # 4,454
        "unique_do_participants": int(dist_part['EmployeeCode'].nunique()), # 4,454
        "districts_covered": int(dist_part['DistrictName'].nunique()), # 52
        "training_centres_district_venues": 52,
        "do_observers_monitors_count": len(dist_mon), # 56
        "unique_do_observers": int(dist_mon['EmployeeCode'].nunique()), # 56
        "do_facilitators_count": len(dist_fac), # 77
        "unique_do_facilitators": int(dist_fac['EmployeeCode'].nunique()) # 77
    },
    "grand_totals": {
        "total_districts": 52, # 100% of MP
        "total_blocks": 322,
        "total_training_centres_statewide": 4804, # 4,804 Cluster Centres + 52 District Venues = 4,856
        "active_training_centres_conducted": 2822 + 52, # 2,874 Active Centres
        "total_teacher_participants": len(cl_part), # 23,785 Middle School Teachers
        "total_district_officials_participants": len(dist_part), # 4,454 District Officials (DO)
        "total_stakeholders_surveyed": len(cl_part) + len(dist_part) + len(cl_mon) + len(dist_mon) + len(cl_fac) + len(dist_fac), # 23785+4454+516+56+4814+77 = 33,702
        "total_observers_monitors": len(cl_mon) + len(dist_mon), # 516 + 56 = 572 Observers
        "total_facilitators": len(cl_fac) + len(dist_fac) # 4,814 + 77 = 4,891 Facilitators
    }
}

with open('scratch/granular_kpi_metrics.json', 'w', encoding='utf-8') as f:
    json.dump(data_summary, f, indent=2)

print("Saved granular KPI metrics to scratch/granular_kpi_metrics.json")
