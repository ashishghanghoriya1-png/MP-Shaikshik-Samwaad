with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

funcs = ['calculateDistrictPedagogyScore', 'getDistrictQuadrantInfo', 'populateQuadrantBentoCards', 'initQuadrantTable']
for fn in funcs:
    print(f"Function {fn} in HTML: {('function ' + fn) in html}")
