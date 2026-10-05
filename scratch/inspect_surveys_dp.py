import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dataPackage.json', 'r', encoding='utf-8') as f:
    dp = json.load(f)

for qid in ['84', '82', '96', '95', '97', '88', '89', '90', '91', '76', '77', '71', '65', '51']:
    s = next((x for x in dp['surveys'] if str(x.get('questionId')) == str(qid)), None)
    if s:
        print(f"\nSurvey QuestionId={qid}: program={s.get('program')}, role={s.get('role')}, sheet={s.get('sheet')}")
        print(f"  Columns: {s.get('columns', [])}")
        if s.get('districtData') and len(s['districtData']) > 0:
            print(f"  Sample district row ({s['districtData'][0].get('district')}): {s['districtData'][0]}")
