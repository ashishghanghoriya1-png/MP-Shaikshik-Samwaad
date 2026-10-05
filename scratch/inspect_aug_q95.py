import pandas as pd, sys
sys.stdout.reconfigure(encoding='utf-8')

aug_file = r'c:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx'
df_p_aug = pd.read_excel(aug_file, sheet_name='Participants')

print("--- AUGUST PEDAGOGICAL QUESTIONS (Q95, Q96, Q97) ---")
for col in ['95', '96', '97']:
    if col in df_p_aug.columns:
        print(f"\nAugust Column {col} Value Counts (Total = {len(df_p_aug):,}):")
        vc = df_p_aug[col].value_counts(dropna=False)
        for val, count in vc.items():
            pct = count / len(df_p_aug) * 100
            print(f"  Option {val}: {count:,} ({pct:.2f}%)")
