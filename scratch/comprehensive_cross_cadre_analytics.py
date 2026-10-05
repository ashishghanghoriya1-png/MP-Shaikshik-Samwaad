import io
import sys
import pandas as pd
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Generating comprehensive statistical breakdown across all cadres...")

# 1. August Cluster Level
aug_file = r"C:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx"
xl_aug = pd.ExcelFile(aug_file)

print("\n=== AUGUST CLUSTER CADRE SIZES ===")
for sheet in ['Participants', 'Facilitator', 'Monitor']:
    df = xl_aug.parse(sheet)
    print(f"Sheet '{sheet}': {len(df):,} records, {len(df.columns)} columns")

# 2. September Cluster Level
sep_file = r"C:\Master Dashboard for CLSS\September_2026_Raw_Data\SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx"
xl_sep = pd.ExcelFile(sep_file)
print("\n=== SEPTEMBER CLUSTER CADRE SIZES ===")
for sheet in ['Participants', 'Facilitator', 'Monitor']:
    df = xl_sep.parse(sheet)
    print(f"Sheet '{sheet}': {len(df):,} records, {len(df.columns)} columns")

# 3. CRO Classroom Observations
cro_file = r"C:\My Files Work\CRO 24-25\Analysis_CRO Data_ MP CPD_ 25-26.xlsx"
xl_cro = pd.ExcelFile(cro_file)
df_sampled = xl_cro.parse('Sampled Observations')
print(f"\n=== CRO CLASSROOM OBSERVATIONS ===")
print(f"Total Sampled Classrooms: {len(df_sampled):,}")
print("Districts covered:", df_sampled['District'].nunique() if 'District' in df_sampled.columns else "N/A")
print("Blocks covered:", df_sampled['Block'].nunique() if 'Block' in df_sampled.columns else "N/A")

# Technique use summary
if 'Technique`s use calculation' in xl_cro.sheet_names:
    df_tech = xl_cro.parse('Technique`s use calculation')
    print("\nTechnique use columns:", list(df_tech.columns[:8]))
    for col in list(df_tech.columns[:8]):
        val_mean = pd.to_numeric(df_tech[col], errors='coerce').mean() * 100
        print(f"  • {col}: {val_mean:.1f}% adoption in observed classrooms")

