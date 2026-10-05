import pandas as pd

qm_c = pd.read_excel(r'c:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx', sheet_name='Question Master')
qm_d = pd.read_excel(r'c:\Master Dashboard for CLSS\SS_ResponseDetail_District Level_Grades 6-8_August.xlsx', sheet_name='Question Master')

with open('c:/Master Dashboard for CLSS/scratch/qm_roles.txt', 'w', encoding='utf-8') as f:
    f.write(f'CLSS QM Roles: {qm_c["RoleName"].value_counts().to_dict()}\n')
    f.write(f'DO QM Roles: {qm_d["RoleName"].value_counts().to_dict()}\n')

print('Wrote qm_roles.txt successfully.')
