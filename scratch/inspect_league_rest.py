import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos_league = content.find('function initDistrictLeague')
if pos_league != -1:
    print(content[pos_league+1000:pos_league+3500])
