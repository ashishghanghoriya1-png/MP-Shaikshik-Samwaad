def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix duplicated activeCohortTarget line
    old_target_decl = 'const activeCohortTarget = (typeof currentCycle !== "undefined" && currentCycle === "SEP") ? 67222 : (typeof currentCycle !== "undefined" && currentCycle === "CONSOLIDATED" ? 135591 : 68369); const activeCohortTarget = (typeof currentCycle !== "undefined" && currentCycle === "SEP") ? 67222 : (typeof currentCycle !== "undefined" && currentCycle === "CONSOLIDATED" ? 135591 : 68369); const sumTarget = distList.reduce((acc, d) => acc + (d.expectedParticipants || d.targetCohort || 0), 0) || (distCount === 52 ? activeCohortTarget : Math.round(clssTeachers * 2.87));'
    new_target_decl = 'const activeCohortTarget = (typeof currentCycle !== "undefined" && currentCycle === "SEP") ? 67222 : (typeof currentCycle !== "undefined" && currentCycle === "CONSOLIDATED" ? 135591 : 68369);\n      const sumTarget = distList.reduce((acc, d) => acc + (d.expectedParticipants || d.targetCohort || 0), 0) || (distCount === 52 ? activeCohortTarget : Math.round(clssTeachers * 2.87));'
    
    if old_target_decl in content:
        content = content.replace(old_target_decl, new_target_decl)
        print(f'Replaced old_target_decl in {filepath}')
    else:
        print(f'old_target_decl not found verbatim in {filepath}')

    # 2. Fix duplicated targetSpan and badge lines
    duplicate_snippet = """          const targetSpan = document.getElementById('kpiTeachersTargetSpan');
          if (targetSpan) targetSpan.innerText = '/ ' + sumTarget.toLocaleString();
          const targetSpan = document.getElementById('kpiTeachersTargetSpan');
          if (targetSpan) targetSpan.innerText = '/ ' + sumTarget.toLocaleString();
          if (kTeachDesc) kTeachDesc.innerText = isHi ? (clssTeachers.toLocaleString() + ' वास्तविक / ' + sumTarget.toLocaleString() + ' अपेक्षित शिक्षक (' + targetCovPct + '% सहभागिता' + archCohortLabel + ')') : (clssTeachers.toLocaleString() + ' Actual / ' + sumTarget.toLocaleString() + ' Expected Teachers (' + targetCovPct + '% Turnout' + archCohortLabel + ')');
          if (kTeachBadge) kTeachBadge.innerText = targetCovPct + '% Turnout';
          if (kTeachBadge) kTeachBadge.innerText = targetCovPct + '% Turnout';
          if (kTeachBadge) kTeachBadge.innerText = satPct + '% of Universe';"""

    clean_snippet = """          const targetSpan = document.getElementById('kpiTeachersTargetSpan');
          if (targetSpan) targetSpan.innerText = '/ ' + sumTarget.toLocaleString();
          if (kTeachDesc) kTeachDesc.innerText = isHi ? (clssTeachers.toLocaleString() + ' वास्तविक / ' + sumTarget.toLocaleString() + ' अपेक्षित शिक्षक (' + targetCovPct + '% सहभागिता' + archCohortLabel + ')') : (clssTeachers.toLocaleString() + ' Actual / ' + sumTarget.toLocaleString() + ' Expected Teachers (' + targetCovPct + '% Turnout' + archCohortLabel + ')');
          if (kTeachBadge) kTeachBadge.innerText = targetCovPct + '% Turnout';"""

    if duplicate_snippet in content:
        content = content.replace(duplicate_snippet, clean_snippet)
        print(f'Replaced duplicate_snippet in {filepath}')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_file('index.html')
fix_file('RSK_Master_CLSS_Executive_Studio_Enhanced.html')
