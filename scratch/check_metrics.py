import json

with open('c:/Master Dashboard for CLSS/dataPackage.json', encoding='utf-8') as f:
    dp = json.load(f)

for s in dp['surveys']:
    if s['questionId'] in ['95', '96', '97', '43', '44', '45', '82', '84', '86', '88', '89']:
        print(f"Q{s['questionId']} ({s['program']} - {s['role']}):")
        for c in s['columns']:
            print(f"   [{c['code']}] count={c['stateTotal']}, pct={c['statePct']}%")
