import json
import re

with open("dataPackage.json", "r", encoding="utf-8") as f:
    dp = json.load(f)

with open("RSK_Master_CLSS_Executive_Dashboard.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's verify that the dynamic quadrant functions are inside the HTML
funcs = ['calculateDistrictPedagogyScore', 'getDistrictQuadrantInfo', 'populateQuadrantBentoCards', 'initQuadrantTable']
for fn in funcs:
    print(f"Function {fn} in HTML:", f"function {fn}" in html)

# Let's check the quadrant distribution
TURNOUT_BENCHMARK = 350
PEDAGOGY_BENCHMARK = 58

q_res = {"Q1": [], "Q2": [], "Q3": [], "Q4": []}

for d in dp["districtSummary"]:
    dname = d["district"]
    t = d["attendees"]
    
    # Calculate pedagogy score
    scores = []
    for qid in ['95', '96', '97', '86', '82']:
        s = next((x for x in dp["surveys"] if x["program"] == "CLSS" and str(x["questionId"]) == str(qid)), None)
        if s and s["districtData"]:
            row = next((r for r in s["districtData"] if r["district"] == dname), None)
            if row:
                tot = row.get("totalRespondents", 1)
                col = f"{qid}_Correct"
                if col in row:
                    scores.append(min(100, round((row[col] / tot) * 100)))
                elif f"{qid}.1" in row:
                    scores.append(min(100, round((row[f"{qid}.1"] / tot) * 100)))
                else:
                    scores.append(55)
            else:
                scores.append(55)
        else:
            scores.append(55)
    
    pedScore = round(sum(scores) / len(scores))
    
    if t >= TURNOUT_BENCHMARK and pedScore >= PEDAGOGY_BENCHMARK:
        q_res["Q1"].append((dname, t, pedScore))
    elif t >= TURNOUT_BENCHMARK and pedScore < PEDAGOGY_BENCHMARK:
        q_res["Q2"].append((dname, t, pedScore))
    elif t < TURNOUT_BENCHMARK and pedScore >= PEDAGOGY_BENCHMARK:
        q_res["Q3"].append((dname, t, pedScore))
    else:
        q_res["Q4"].append((dname, t, pedScore))

print("\n--- QUADRANT COUNTS ---")
for q, dists in q_res.items():
    print(f"{q} ({len(dists)} Districts): {[d[0] for d in dists[:6]]}...")
