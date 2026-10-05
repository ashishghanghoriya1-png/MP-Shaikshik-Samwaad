import pandas as pd
import json

WORKSPACE_DIR = r"c:\Master Dashboard for CLSS"
DISTRICT_FILE = r"c:\Master Dashboard for CLSS\SS_ResponseDetail_District Level_Grades 6-8_August.xlsx"
CLUSTER_FILE = r"c:\Master Dashboard for CLSS\SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx"

df_cqm = pd.read_excel(CLUSTER_FILE, sheet_name="Question Master")
df_cmon = pd.read_excel(CLUSTER_FILE, sheet_name="Monitor")
df_cfac = pd.read_excel(CLUSTER_FILE, sheet_name="Facilitator")
df_cpart = pd.read_excel(CLUSTER_FILE, sheet_name="Participants")

df_dqm = pd.read_excel(DISTRICT_FILE, sheet_name="Question Master")
df_dmon = pd.read_excel(DISTRICT_FILE, sheet_name="Monitor")
df_dfac = pd.read_excel(DISTRICT_FILE, sheet_name="Facilitator")
df_dpart = pd.read_excel(DISTRICT_FILE, sheet_name="Participants")

analysis = {}

# Analyze CLSS Participant questions (82 to 97)
analysis["CLSS_Participants"] = []
for _, r in df_cqm[df_cqm['RoleName'].astype(str).str.contains('प्रतिभागी')].iterrows():
    qid = str(r['QuestionId']).strip()
    qtext = str(r['QuestionText']).strip()
    if qid in df_cpart.columns:
        val_counts = df_cpart[qid].value_counts().head(5).to_dict()
        analysis["CLSS_Participants"].append({
            "qid": qid,
            "text": qtext,
            "total_resp": int(df_cpart[qid].dropna().count()),
            "top_options": {str(k): int(v) for k, v in val_counts.items()}
        })

# Analyze CLSS Facilitator questions (67 to 81)
analysis["CLSS_Facilitators"] = []
for _, r in df_cqm[df_cqm['RoleName'].astype(str).str.contains('सहजकर्ता')].iterrows():
    qid = str(r['QuestionId']).strip()
    qtext = str(r['QuestionText']).strip()
    if qid in df_cfac.columns:
        val_counts = df_cfac[qid].value_counts().head(5).to_dict()
        analysis["CLSS_Facilitators"].append({
            "qid": qid,
            "text": qtext,
            "total_resp": int(df_cfac[qid].dropna().count()),
            "top_options": {str(k): int(v) for k, v in val_counts.items()}
        })

# Analyze CLSS Monitor questions (55 to 66)
analysis["CLSS_Monitors"] = []
for _, r in df_cqm[df_cqm['RoleName'].astype(str).str.contains('अवलोकनकर्ता')].iterrows():
    qid = str(r['QuestionId']).strip()
    qtext = str(r['QuestionText']).strip()
    if qid in df_cmon.columns:
        val_counts = df_cmon[qid].value_counts().head(5).to_dict()
        analysis["CLSS_Monitors"].append({
            "qid": qid,
            "text": qtext,
            "total_resp": int(df_cmon[qid].dropna().count()),
            "top_options": {str(k): int(v) for k, v in val_counts.items()}
        })

# Analyze DO Monitor (25, 46 to 52)
analysis["DO_Monitors"] = []
for _, r in df_dqm[df_dqm['RoleName'].astype(str).str.contains('अवलोकनकर्ता')].iterrows():
    qid = str(r['QuestionId']).strip()
    qtext = str(r['QuestionText']).strip()
    if qid in df_dmon.columns:
        val_counts = df_dmon[qid].value_counts().head(5).to_dict()
        analysis["DO_Monitors"].append({
            "qid": qid,
            "text": qtext,
            "total_resp": int(df_dmon[qid].dropna().count()),
            "top_options": {str(k): int(v) for k, v in val_counts.items()}
        })

with open("scratch/full_qwen_raw_audit.json", "w", encoding="utf-8") as f:
    json.dump(analysis, f, ensure_ascii=False, indent=2)

print("Saved scratch/full_qwen_raw_audit.json successfully.")
