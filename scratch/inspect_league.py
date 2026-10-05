import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos_league = content.find('function initDistrictLeague')
if pos_league != -1:
    print('=== LEAGUE ===')
    print(content[pos_league:pos_league+2500])

pos_filter = content.find('function filterDistrictLeague')
if pos_filter != -1:
    print('\n=== FILTER LEAGUE ===')
    print(content[pos_filter:pos_filter+1000])

pos_d360 = content.find('function updateDistrict360View')
if pos_d360 != -1:
    print('\n=== UPDATE D360 ===')
    print(content[pos_d360:pos_d360+1500])
