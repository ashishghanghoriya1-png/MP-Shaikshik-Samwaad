import json

with open("dataPackage.json", "r", encoding="utf-8") as f:
    dp = json.load(f)

# Let's see what surveys exist
print("Available surveys:")
for s in dp["surveys"][:10]:
    print(f"  Program={s['program']}, Role={s['role']}, QID={s['questionId']}, cols={[c['code'] for c in s['columns']]}")

def get_survey_score(qid, dist_name):
    s = next((x for x in dp["surveys"] if x["program"] == "CLSS" and str(x["questionId"]) == str(qid)), None)
    if not s:
        return 0
    row = next((d for d in s["districtData"] if d["district"] == dist_name), None)
    if not row:
        return 0
    # check for correct column or top option
    col = f"{qid}_Correct"
    if col in row:
        cnt = row[col]
    elif f"{qid}.1" in row:
        cnt = row[f"{qid}.1"]
    else:
        # sum of numeric keys
        cnt = sum(v for k, v in row.items() if k != "district" and k != "totalRespondents")
    tot = row.get("totalRespondents", 1)
    return round((cnt / tot * 100), 1) if tot > 0 else 0

TURNOUT_BENCHMARK = 350
PEDAGOGY_BENCHMARK = 60

q_counts = {"Q1": [], "Q2": [], "Q3": [], "Q4": []}

for d in dp["districtSummary"]:
    dname = d["district"]
    t = d["attendees"]
    p95 = get_survey_score("95", dname)
    p96 = get_survey_score("96", dname)
    p97 = get_survey_score("97", dname)
    p86 = get_survey_score("86", dname)
    p82 = get_survey_score("82", dname)
    ped = round((p95 + p96 + p97 + p86 + p82) / 5, 1)

    if t >= TURNOUT_BENCHMARK and ped >= PEDAGOGY_BENCHMARK:
        q_counts["Q1"].append((dname, t, ped))
    elif t >= TURNOUT_BENCHMARK and ped < PEDAGOGY_BENCHMARK:
        q_counts["Q2"].append((dname, t, ped))
    elif t < TURNOUT_BENCHMARK and ped >= PEDAGOGY_BENCHMARK:
        q_counts["Q3"].append((dname, t, ped))
    else:
        q_counts["Q4"].append((dname, t, ped))

print("\n=== QUADRANT DISTRIBUTION WITH FIXED SCORING ===")
for q, dists in q_counts.items():
    print(f"{q} Count: {len(dists)}")
    print(f"  Districts: {dists[:5]}...")
