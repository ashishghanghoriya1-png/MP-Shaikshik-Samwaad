with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('function calculateDistrictPedagogyScore')
if idx != -1:
    idx2 = html.find('function populateQuadrantBentoCards', idx)
    with open('scratch/ped_calc_inspect.js', 'w', encoding='utf-8') as out:
        out.write(html[idx:idx2])
    print("Found and saved ped calc functions.")
else:
    print("calculateDistrictPedagogyScore not found.")
