import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos = content.find('function getDistrictSurveyVal')
if pos != -1:
    print(content[pos:pos+1500])
