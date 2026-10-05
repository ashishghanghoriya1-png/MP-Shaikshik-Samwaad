import pandas as pd, sys
sys.stdout.reconfigure(encoding='utf-8')

sep_file = r'c:\Master Dashboard for CLSS\September_2026_Raw_Data\SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx'

df_q = pd.read_excel(sep_file, sheet_name='Question Master')
df_p = pd.read_excel(sep_file, sheet_name='Participants')

print("--- QUESTION MASTER FOR Q177, Q178, Q179 ---")
for qid in [177, 178, 179]:
    q_rows = df_q[df_q['QuestionId'] == qid]
    print(f"\nQuestion ID {qid}:")
    for _, r in q_rows.iterrows():
        print(f"  Role: {r.get('RoleName')}, Question: {r.get('QuestionText')}")

print("\n--- PARTICIPANTS DISTRIBUTION FOR Q177, Q178, Q179 ---")
for col in ['177', '178', '179']:
    if col in df_p.columns:
        print(f"\nColumn {col} Value Counts (Total records = {len(df_p):,}):")
        vc = df_p[col].value_counts(dropna=False)
        for val, count in vc.items():
            pct = count / len(df_p) * 100
            print(f"  Option {val}: {count:,} ({pct:.2f}%)")
