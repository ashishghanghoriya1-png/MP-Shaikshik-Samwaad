import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dataPackage.json', 'r', encoding='utf-8') as f:
    dp = json.load(f)

def get_dist_score(qid, code, dist_name):
    s = next((x for x in dp['surveys'] if str(x.get('questionId')) == str(qid)), None)
    if not s: return 0, 0
    row = next((r for r in s.get('districtData', []) if r.get('district') == dist_name), None)
    if not row: return 0, 0
    tot = row.get('totalRespondents', 0)
    cnt = row.get(code, 0)
    pct = round((cnt / tot * 100), 1) if tot > 0 else 0
    return cnt, pct

print(f"{'District':<16} | {'Teachers':<8} | {'Q91.1 %':<8} | {'Q89.1 %':<8} | {'Q90.1 %':<8} | {'Q88.1 %':<8}")
print("-" * 65)

for d in dp['districtSummary']:
    dist = d['district']
    teach = d['attendees']
    _, p91 = get_dist_score('91', '91.1', dist)
    _, p89 = get_dist_score('89', '89.1', dist)
    _, p90 = get_dist_score('90', '90.1', dist)
    _, p88 = get_dist_score('88', '88.1', dist)
    print(f"{dist:<16} | {teach:<8} | {p91:<8} | {p89:<8} | {p90:<8} | {p88:<8}")
