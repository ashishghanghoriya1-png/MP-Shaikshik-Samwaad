with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '[Ref:' in line or 'Ref:' in line or 'Output_' in line or '7 Output' in line or 'Sheet1' in line:
        print(f"Line {i+1}: {line.strip()[:140]}")
