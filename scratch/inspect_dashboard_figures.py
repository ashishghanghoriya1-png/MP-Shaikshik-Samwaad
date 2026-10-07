import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

workspace = r"C:\Users\Peepul\OneDrive - Absolute Return For Kids\Master Dashboard for CLSS - Copy"

with open(os.path.join(workspace, 'dataPackage.json'), 'r', encoding='utf-8') as f:
    dp = json.load(f)

print("=== DATAPACKAGE.JSON TOP-LEVEL & CYCLES KPIS ===")
for cycle_key in ['AUG', 'SEP', 'CONSOLIDATED']:
    if cycle_key in dp.get('cycles', {}):
        c_data = dp['cycles'][cycle_key]
        print(f"\n--- CYCLE: {cycle_key} ---")
        if 'varg2Metrics' in c_data:
            print("varg2Metrics:", c_data['varg2Metrics'])
        if 'kpis' in c_data:
            print("kpis:", c_data['kpis'])
        if 'operationsAttendance' in c_data:
            print(f"operationsAttendance district count: {len(c_data['operationsAttendance'])}")

with open(os.path.join(workspace, 'index.html'), 'r', encoding='utf-8') as f:
    html_text = f.read()

# Search for KPI cards in index.html
print("\n=== SEARCHING KPI CARDS & LABELS IN INDEX.HTML ===")
kpi_matches = re.findall(r'<div[^>]*class="[^"]*kpi-[^"]*"[^>]*>([\s\S]*?)<\/div>', html_text)
for m in kpi_matches[:10]:
    clean = re.sub(r'<[^>]+>', ' ', m).strip()
    print("KPI Match:", ' '.join(clean.split()))

# Look for specific text like "District", "DO", "Officials", "4,454", "4,520", "8,888", "8,974"
for num in ["4,454", "4454", "4,520", "4520", "8,974", "8974", "8,888", "8888", "District Officials", "District Level"]:
    cnt = html_text.count(num)
    if cnt > 0:
        print(f"Found '{num}' in index.html: {cnt} occurrences")
