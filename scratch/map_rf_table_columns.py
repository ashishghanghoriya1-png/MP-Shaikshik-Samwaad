import sys
import re

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('const rfData =')
idx2 = text.find('function initRFMatrixTable', idx1)

rf_section = text[idx1:idx2]

# Extract all indicators
indicators = re.findall(r'\{\s*"id":\s*(\d+),\s*"code":\s*"([^"]+)",\s*"title":\s*"([^"]+)"', rf_section)
print(f"Total Indicators in rfData: {len(indicators)}")
for id_num, code, title in indicators:
    print(f"ID {id_num:2s} ({code}): {title}")

# Let's check sub-indicators for each
for m in re.finditer(r'"id":\s*(\d+).*?"subIndicators":\s*\[(.*?)\]', rf_section, re.DOTALL):
    ind_id = m.group(1)
    sub_raw = m.group(2)
    names = re.findall(r'"indicator_name":\s*"([^"]+)"', sub_raw)
    sources = re.findall(r'"dataSource":\s*"([^"]+)"', sub_raw)
    print(f"\n--- Indicator {ind_id} ---")
    for n, s in zip(names, sources):
        print(f"  • {n[:80]} | Source: {s[:60]}")
