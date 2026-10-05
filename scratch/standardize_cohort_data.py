import json, os, re

# Standardize cohort data with clean canonical keys
clean_cohort_data = []
with open(r'c:\Master Dashboard for CLSS\data\exports\cohort_matrix_52_districts.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

for row in raw_data:
    district = row.get('District') or row.get('district') or ''
    aug = int(row.get('August_Attendance') or row.get('aug_total') or 0)
    sep = int(row.get('September_Attendance') or row.get('sep_total') or 0)
    repeat = int(row.get('Persistent_Repeat_Teachers') or row.get('common') or 0)
    ret_pct = float(row.get('Retention_Rate_Pct') or row.get('retention_pct') or 0.0)
    new_intake = int(row.get('September_New_Intake') or row.get('sep_only') or 0)
    new_pct = float(row.get('New_Intake_Rate_Pct') or row.get('new_intake_pct') or 0.0)
    lapsed = int(row.get('August_Only_Lapsed') or row.get('aug_only') or 0)
    cumul = int(row.get('Cumulative_Unique_Teachers') or row.get('cumulative_unique') or 0)
    target_univ = int(row.get('Target_Math_Sci_Universe') or row.get('target_math_sci') or 0)
    total_varg2 = int(row.get('Total_Varg2_Universe') or row.get('total_varg2') or 0)
    sat_pct = float(row.get('Target_Saturation_Pct') or row.get('saturation_pct') or 0.0)

    clean_cohort_data.append({
        'district': district,
        'aug_total': aug,
        'sep_total': sep,
        'common': repeat,
        'retention_pct': ret_pct,
        'sep_only': new_intake,
        'new_intake_pct': new_pct,
        'aug_only': lapsed,
        'cumulative_unique': cumul,
        'target_math_sci': target_univ,
        'total_varg2': total_varg2,
        'saturation_pct': sat_pct
    })

# Save standardized JSON
with open(r'c:\Master Dashboard for CLSS\data\exports\cohort_matrix_52_districts.json', 'w', encoding='utf-8') as f:
    json.dump(clean_cohort_data, f, indent=2)

print(f"Standardized {len(clean_cohort_data)} district rows in JSON.")
