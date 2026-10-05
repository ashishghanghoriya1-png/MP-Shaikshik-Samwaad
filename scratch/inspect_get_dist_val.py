with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('function getDistrictSurveyVal')
if idx != -1:
    print(html[idx:idx+800])
else:
    print("getDistrictSurveyVal not found!")
