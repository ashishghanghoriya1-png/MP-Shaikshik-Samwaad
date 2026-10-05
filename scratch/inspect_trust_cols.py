import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dataPackage.json', 'r', encoding='utf-8') as f:
    dp = json.load(f)

for qid in ['91', '89', '90', '88', '84', '82']:
    s = next((x for x in dp['surveys'] if str(x.get('questionId')) == str(qid)), None)
    if s:
        print(f"\nQuestion {qid} (Role: {s.get('role')}):")
        for col in s.get('columns', []):
            print(f"  Code: {col['code']} | Pct: {col.get('statePct')}% | Label: {col.get('labelHi')[:60]}")
