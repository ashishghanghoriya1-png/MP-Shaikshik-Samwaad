import io, sys, json, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_s = text.find('"surveys": [')
pos_end = text.find('], "districtSummary"', pos_s)
if pos_end == -1:
    pos_end = text.find(']', pos_s)

surveys_json = text[pos_s+11:pos_end+1]
print("Surveys JSON substring length:", len(surveys_json))
surveys = json.loads(surveys_json)
print(f"Total surveys in master dataPackage: {len(surveys)}")
for i, s in enumerate(surveys[:10]):
    print(f"  [{i+1}] Q{s.get('questionId')} ({s.get('role')} - {s.get('program')}): {s.get('questionText')[:60]}...")
