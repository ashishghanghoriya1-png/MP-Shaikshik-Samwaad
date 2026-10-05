with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('function populateQuadrantBentoCards')
if idx != -1:
    idx2 = html.find('function initQuadrantTable', idx)
    idx3 = html.find('function', idx2 + 20)
    with open('scratch/quadrant_inspect.js', 'w', encoding='utf-8') as out:
        out.write(html[idx:idx3])
    print("Found and saved quadrant functions.")
else:
    print("populateQuadrantBentoCards not found.")
