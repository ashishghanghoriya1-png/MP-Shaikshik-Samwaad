import pandas as pd
import json

aug_path = r'c:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx'
sep_path = r'c:\Master Dashboard for CLSS\September_2026_Raw_Data\SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx'
varg_path = r'c:\Master Dashboard for CLSS\Varg Wise Teacher Count.xlsx'

print("Loading data...")
df_aug = pd.read_excel(aug_path, sheet_name='Participants')
df_sep = pd.read_excel(sep_path, sheet_name='Participants')
df_varg = pd.read_excel(varg_path)

df_aug['EmpCode_Clean'] = df_aug['EmployeeCode'].astype(str).str.strip().str.upper()
df_sep['EmpCode_Clean'] = df_sep['EmployeeCode'].astype(str).str.strip().str.upper()
df_aug['District_Clean'] = df_aug['DistrictName'].astype(str).str.strip().str.title()
df_sep['District_Clean'] = df_sep['DistrictName'].astype(str).str.strip().str.title()

# Map Varg target math/science per district
varg_dist = df_varg.groupby('District').agg({
    'Madhymik Shikshak Varg -2 (Total)': 'sum',
    'Varg-2 Maths': 'sum',
    'Varg-2  Biology ': 'sum'
}).reset_index()
varg_dist['Target_Math_Sci'] = varg_dist['Varg-2 Maths'] + varg_dist['Varg-2  Biology ']
varg_dist['District_Clean'] = varg_dist['District'].astype(str).str.strip().str.title()

# Calculate district level cohort stats
aug_by_dist = df_aug.groupby('District_Clean')['EmpCode_Clean'].unique().to_dict()
sep_by_dist = df_sep.groupby('District_Clean')['EmpCode_Clean'].unique().to_dict()

all_dists = sorted(list(set(list(aug_by_dist.keys()) + list(sep_by_dist.keys()))))

district_cohorts = []
for d in all_dists:
    aug_set = set(aug_by_dist.get(d, [])) - {'NAN', '', 'NONE', 'NULL', '0', '0.0'}
    sep_set = set(sep_by_dist.get(d, [])) - {'NAN', '', 'NONE', 'NULL', '0', '0.0'}
    
    common = aug_set.intersection(sep_set)
    aug_only = aug_set - sep_set
    sep_only = sep_set - aug_set
    cumul = aug_set.union(sep_set)
    
    varg_row = varg_dist[varg_dist['District_Clean'] == d]
    target_universe = int(varg_row['Target_Math_Sci'].values[0]) if len(varg_row) > 0 else 0
    total_varg2 = int(varg_row['Madhymik Shikshak Varg -2 (Total)'].values[0]) if len(varg_row) > 0 else 0
    
    retention_rate = round(len(common) / len(aug_set) * 100, 1) if len(aug_set) > 0 else 0
    new_intake_rate = round(len(sep_only) / len(sep_set) * 100, 1) if len(sep_set) > 0 else 0
    saturation_rate = round(len(cumul) / target_universe * 100, 1) if target_universe > 0 else 0
    
    district_cohorts.append({
        'district': d,
        'aug_total': len(aug_set),
        'sep_total': len(sep_set),
        'common': len(common),
        'aug_only': len(aug_only),
        'sep_only': len(sep_only),
        'cumulative_unique': len(cumul),
        'target_math_sci': target_universe,
        'total_varg2': total_varg2,
        'retention_pct': retention_rate,
        'new_intake_pct': new_intake_rate,
        'saturation_pct': saturation_rate
    })

print(f"Computed cohort matrix for {len(district_cohorts)} districts.")
print("Sample district row:", district_cohorts[0])

with open(r'c:\Master Dashboard for CLSS\scratch\district_cohort_matrix.json', 'w', encoding='utf-8') as f:
    json.dump(district_cohorts, f, indent=2)
print("Saved to scratch/district_cohort_matrix.json")
