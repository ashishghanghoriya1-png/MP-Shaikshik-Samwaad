import json
import re

dp = json.load(open('dataPackage.json', encoding='utf-8'))
html = open('index.html', encoding='utf-8').read()

# 1. Update embedded dataPackage in index.html
pos_dp = html.find('const dataPackage = ')
if pos_dp != -1:
    pos_end = html.find(';\n', pos_dp)
    if pos_end == -1:
        pos_end = html.find(';', pos_dp)
    print(f'Found embedded dataPackage from {pos_dp} to {pos_end}')
    new_dp_str = 'const dataPackage = ' + json.dumps(dp, ensure_ascii=False)
    html = html[:pos_dp] + new_dp_str + html[pos_end:]
    print('Embedded dataPackage replaced in HTML')

# 2. Update static KPI text
html = html.replace('/ 35,374', '/ 68,369')
html = html.replace('35,374 Expected', '68,369 Expected')
html = html.replace('35,374 अपेक्षित', '68,369 अपेक्षित')
html = html.replace('35,374 Target', '68,369 Expected Target')
html = html.replace('35,374 लक्षित', '68,369 लक्षित')
html = html.replace('of 35,374 Target', 'of 68,369 Expected')

# 3. Update dynamic slicer logic
html = re.sub(
    r'const sumTarget = sumUniverse > 0 \? Math\.round\(sumUniverse \* 0\.517\) : \(distCount === 52 \? 35374 : Math\.round\(clssTeachers \* 1\.48\)\);',
    r'const sumTarget = distList.reduce((acc, d) => acc + (d.expectedParticipants || d.targetCohort || 0), 0) || (distCount === 52 ? (typeof currentCycle !== "undefined" && currentCycle === "SEP" ? 67222 : 68369) : Math.round(clssTeachers * 2.87));',
    html
)

html = html.replace('distCount === 52 ? 35374', 'distCount === 52 ? (typeof currentCycle !== "undefined" && currentCycle === "SEP" ? 67222 : 68369)')
html = html.replace('clssTeachers / 35374', 'clssTeachers / (typeof currentCycle !== "undefined" && currentCycle === "SEP" ? 67222 : 68369)')

open('index.html', 'w', encoding='utf-8').write(html)
print('Successfully saved updated index.html')
