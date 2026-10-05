import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Read design_new_u360.py
with open('scratch/design_new_u360.py', 'r', encoding='utf-8') as f:
    dcode = f.read()

marker1 = "new_d360_js = r'''"
idx1 = dcode.find(marker1) + len(marker1)
marker2 = "'''\n\nprint("
idx2 = dcode.find(marker2, idx1)
new_d360_js = dcode[idx1:idx2]

print(f"Extracted new_d360_js: {len(new_d360_js)} chars")

# Read RSK_Master_CLSS_Executive_Dashboard.html
with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    orig = f.read()

style_start = orig.find('<style>')
style_end = orig.find('</style>')
s1_start = orig.find('<script>', style_end)
s1_end = orig.find('</script>', s1_start)
m_active = re.search(r'\n\s*let activeProgram\s*=', orig[s1_start:s1_end])
dp_end = s1_start + m_active.start()
orig_js = orig[dp_end:s1_end]

idx_d360_start = orig_js.find('function initDistrict360()')
idx_d360_end = orig_js.find('function initDistrictLeague()')

print(f"orig_js D360 indices: {idx_d360_start} to {idx_d360_end}")
assert idx_d360_start != -1 and idx_d360_end != -1, "D360 block not found in orig_js"

replaced_js = orig_js[:idx_d360_start] + new_d360_js + "\n\n    " + orig_js[idx_d360_end:]
print(f"Replaced JS length: {len(replaced_js)}")
