import json

with open("scratch/full_qwen_raw_audit.json", "r", encoding="utf-8") as f:
    data = json.load(f)

lines = []
lines.append("=== CLSS FACILITATORS (Key Challenges & Needs) ===")
for q in data["CLSS_Facilitators"]:
    if q["qid"] in ['71', '72', '76', '77', '78', '79', '80', '81']:
        lines.append(f"\nQ{q['qid']}: {q['text']}")
        for opt, cnt in q["top_options"].items():
            lines.append(f"   -> {opt}: {cnt:,} ({(cnt/q['total_resp']*100):.1f}%)")

lines.append("\n=== CLSS MONITORS (Observation Findings) ===")
for q in data["CLSS_Monitors"]:
    if q["qid"] in ['55', '56', '57', '58', '59', '60', '65', '66']:
        lines.append(f"\nQ{q['qid']}: {q['text']}")
        for opt, cnt in q["top_options"].items():
            lines.append(f"   -> {opt}: {cnt:,} ({(cnt/q['total_resp']*100):.1f}%)")

lines.append("\n=== CLSS PARTICIPANTS (Pedagogy & Classroom Transfer) ===")
for q in data["CLSS_Participants"]:
    if q["qid"] in ['82', '83', '84', '85', '86', '94', '95', '96', '97']:
        lines.append(f"\nQ{q['qid']}: {q['text']}")
        for opt, cnt in q["top_options"].items():
            lines.append(f"   -> {opt}: {cnt:,} ({(cnt/q['total_resp']*100):.1f}%)")

with open("scratch/qwen_deep_insights.txt", "w", encoding="utf-8") as out:
    out.write("\n".join(lines))

print("Saved scratch/qwen_deep_insights.txt successfully.")
