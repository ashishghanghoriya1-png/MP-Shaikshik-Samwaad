import re
import json

with open('c:/Master Dashboard for CLSS/RSK_Master_CLSS_Executive_Dashboard.html', encoding='utf-8') as f:
    text = f.read()

out = []
# 1. Nav items and tab sections
nav_items = re.findall(r'<button[^>]*class="[^"]*nav-item[^"]*"[^>]*>.*?</button>', text)
out.append(f'Nav buttons found: {len(nav_items)}')
for n in nav_items:
    out.append('  ' + n)

tab_sections = re.findall(r'<div[^>]*class="[^"]*tab-section[^"]*"[^>]*>', text)
out.append(f'Tab sections found: {len(tab_sections)}')
for ts in tab_sections:
    out.append('  ' + ts)

# 2. Check activateTab function
m = re.search(r'function activateTab\s*\([^)]*\)\s*\{[\s\S]*?\n    function', text)
if m:
    out.append('\nactivateTab function:\n' + m.group(0))

with open('c:/Master Dashboard for CLSS/scratch/tab_inspect_result.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))


# 3. Check what reference sheet names or excel references are in the HTML
print('\nSearching for reference sheet names or excel names in HTML:')
excel_refs = re.findall(r'(\b[A-Za-z0-9_\-\s]+\.xlsx\b)', text, re.IGNORECASE)
print('Excel file mentions in HTML:', set(excel_refs))

sheet_refs = re.findall(r'([A-Za-z0-9_\-\s]+Sheet[A-Za-z0-9_\-\s]*)', text, re.IGNORECASE)
print('Sheet mentions:', set(sheet_refs)[:10])

# Check Question Bank sheet / reference names
with open('c:/Master Dashboard for CLSS/dataPackage.json', encoding='utf-8') as f:
    dp = json.load(f)

print('\nSample survey entries in dataPackage:')
for s in dp.get('surveys', [])[:5]:
    print(f"  Q{s.get('questionId')}: sheet={s.get('sheet')}, program={s.get('program')}, role={s.get('role')}")
