import io, sys, json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_dp = text.find('const dataPackage =')
pos_dp_end = text.find(';\n', pos_dp)

dp_raw = text[pos_dp+20:pos_dp_end].strip()
data = json.loads(dp_raw)

print("dataPackage Top-Level Keys:", list(data.keys()))
for k in data.keys():
    v = data[k]
    if isinstance(v, list):
        print(f"  • {k}: List of {len(v)} items")
    elif isinstance(v, dict):
        print(f"  • {k}: Dict with keys {list(v.keys())[:8]}")
    else:
        print(f"  • {k}: {type(v)} -> {str(v)[:50]}")

if 'surveys' in data:
    print(f"\nSurveys Count: {len(data['surveys'])}")
    for i, s in enumerate(data['surveys'][:15]):
        print(f"  [{i+1}] Q{s.get('questionId')} ({s.get('role')}) - {s.get('program')}: {s.get('questionText')[:50]}...")
