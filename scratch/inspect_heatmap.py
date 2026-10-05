import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos = content.find('function initTrustHeatmapTable')
if pos != -1:
    print(content[pos:pos+3000])

pos2 = content.find('function toggleTrustView')
if pos2 != -1:
    print(content[pos2:pos2+1000])
