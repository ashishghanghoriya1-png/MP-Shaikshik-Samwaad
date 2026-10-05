import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\dataPackage.json', 'r', encoding='utf-8') as f:
    pkg = json.load(f)

print("dataPackage keys:", pkg.keys())
print("\n--- Summary Totals in dataPackage.json ---")
for k in ['stateSummary', 'augustSummary', 'septemberSummary', 'cadreBreakdown', 'cycleSummary']:
    if k in pkg:
        print(f"\n{k}:\n", json.dumps(pkg[k], indent=2, ensure_ascii=False)[:600])

if 'districtSummary' in pkg:
    print(f"\nTotal districts in districtSummary: {len(pkg['districtSummary'])}")
    sample = pkg['districtSummary'][0]
    print("Sample district keys:", sample.keys())
    print("Sample district:", json.dumps(sample, indent=2, ensure_ascii=False)[:400])
