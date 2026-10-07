import json
import re

dp = json.load(open('dataPackage.json', encoding='utf-8'))
dp_json_str = 'const dataPackage = ' + json.dumps(dp, ensure_ascii=False)

for fname in ['index.html', 'RSK_Master_CLSS_Executive_Studio_Enhanced.html']:
    html = open(fname, encoding='utf-8').read()
    
    # 1. Replace embedded dataPackage
    pos_dp = html.find('const dataPackage = ')
    if pos_dp != -1:
        pos_end = html.find(';\n', pos_dp)
        if pos_end == -1:
            pos_end = html.find(';', pos_dp)
        html = html[:pos_dp] + dp_json_str + html[pos_end:]
        print(f'Embedded dataPackage updated in {fname}')
    
    # 2. Add id="kpiTeachersTargetSpan" to target span if not present
    html = re.sub(
        r'<span style="font-size: 14px; color: var\(--text-muted\); font-weight: 600;">/ [0-9,]+</span>',
        r'<span style="font-size: 14px; color: var(--text-muted); font-weight: 600;" id="kpiTeachersTargetSpan">/ 68,369</span>',
        html
    )
    
    # 3. Enhance updateOverviewKPIs logic so sumTarget reflects the active cycle target
    # Replace sumTarget computation
    html = re.sub(
        r'const sumTarget = [^;]+;',
        r'const activeCohortTarget = (typeof currentCycle !== "undefined" && currentCycle === "SEP") ? 67222 : (typeof currentCycle !== "undefined" && currentCycle === "CONSOLIDATED" ? 135591 : 68369); const sumTarget = distList.reduce((acc, d) => acc + (d.expectedParticipants || d.targetCohort || 0), 0) || (distCount === 52 ? activeCohortTarget : Math.round(clssTeachers * 2.87));',
        html,
        count=1
    )
    
    # Update targetSpan and kTeachDesc
    old_kteach_block = "if (kTeachDesc) kTeachDesc.innerText = isHi ? (clssTeachers.toLocaleString() + ' वास्तविक / ' + sumTarget.toLocaleString() + ' लक्षित (' + satPct + '% यूनिवर्स' + archCohortLabel + ')') : (clssTeachers.toLocaleString() + ' Actual / ' + sumTarget.toLocaleString() + ' Target (' + satPct + '% of Universe' + archCohortLabel + ')');"
    new_kteach_block = """const targetSpan = document.getElementById('kpiTeachersTargetSpan');
          if (targetSpan) targetSpan.innerText = '/ ' + sumTarget.toLocaleString();
          if (kTeachDesc) kTeachDesc.innerText = isHi ? (clssTeachers.toLocaleString() + ' वास्तविक / ' + sumTarget.toLocaleString() + ' अपेक्षित शिक्षक (' + targetCovPct + '% सहभागिता' + archCohortLabel + ')') : (clssTeachers.toLocaleString() + ' Actual / ' + sumTarget.toLocaleString() + ' Expected Teachers (' + targetCovPct + '% Turnout' + archCohortLabel + ')');
          if (kTeachBadge) kTeachBadge.innerText = targetCovPct + '% Turnout';"""
    
    if old_kteach_block in html:
        html = html.replace(old_kteach_block, new_kteach_block)
        print(f'Replaced old_kteach_block in {fname}')
    else:
        # regex replace all occurrences
        html = re.sub(
            r'if \(kTeachDesc\) kTeachDesc\.innerText = isHi \? \(clssTeachers\.toLocaleString\(\) \+ \' वास्तविक / \' \+ sumTarget\.toLocaleString\(\) \+ [^;]+;',
            new_kteach_block,
            html
        )
        print(f'Regex replaced kTeachDesc in {fname}')

    open(fname, 'w', encoding='utf-8').write(html)
    print(f'Saved {fname}')
