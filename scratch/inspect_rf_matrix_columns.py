import sys
import json
import re

# Read dataPackage.json
with open('dataPackage.json', 'r', encoding='utf-8') as f:
    dp = json.load(f)

print("dataPackage keys:", list(dp.keys()))

# Read RSK_Master_CLSS_Executive_Dashboard.html
with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('const rfData =')
idx2 = text.find('const rfDataSep =', idx1)
if idx2 == -1:
    idx2 = text.find('function initRFMatrixTable', idx1)

rf_str = text[idx1+15:idx2].strip()
while rf_str.endswith(';') or rf_str.endswith('\n'):
    rf_str = rf_str[:-1].strip()

try:
    rf_obj = json.loads(rf_str)
    print("\n--- August rfData Indicators ---")
    for ind in rf_obj.get('indicators', []):
        print(f"ID: {ind.get('id'):2d} | Code: {ind.get('code')} | Title: {ind.get('title')}")
except Exception as e:
    print("Could not parse rfData as JSON directly:", e)

idx_sep = text.find('const rfDataSep =')
if idx_sep != -1:
    idx_sep_end = text.find('function ', idx_sep)
    rf_sep_str = text[idx_sep+18:idx_sep_end].strip()
    while rf_sep_str.endswith(';') or rf_sep_str.endswith('\n'):
        rf_sep_str = rf_sep_str[:-1].strip()
    try:
        rf_sep_obj = json.loads(rf_sep_str)
        print("\n--- September rfDataSep Indicators ---")
        for ind in rf_sep_obj.get('indicators', []):
            print(f"ID: {ind.get('id'):2d} | Code: {ind.get('code')} | Title: {ind.get('title')}")
    except Exception as e:
        print("Could not parse rfDataSep:", e)

# Also check surveys available in dataPackage
surveys = dp.get('surveys', [])
print(f"\nTotal Surveys in dataPackage: {len(surveys)}")
for s in surveys:
    print(f"Program: {s.get('program')} | Code: {s.get('code')} | Title: {s.get('title')} | Cols: {[c.get('code') for c in s.get('columns', [])]}")
