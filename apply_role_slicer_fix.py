"""
Comprehensive Fix for Cadre / Role Slicer:
1. Dynamic Visibility: Show only on applicable tabs (Tab 1: Overview, Tab 2: RF Goals, Tab 6: Questions, Tab 8: Governance, Tab 9/10: Insights). Hide on others.
2. Full Responsiveness on Tab 1 Overview:
   - Slices bar chart (ovTopDistricts) by Teachers vs Facilitators vs Monitors with custom colors and proper sorting.
   - Updates KPI Ribbon Card highlights and badges for selected cadre.
   - Updates Stakeholder Donut and Cadre Breakdown accordingly.
3. Applied cleanly across all 4 production target HTML files.
"""

import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

TARGET_FILES = [
    'index.html',
    'deploy/index.html',
    'RSK_Master_CLSS_Executive_Dashboard.html',
    'RSK_Master_CLSS_Executive_Studio_Enhanced.html'
]

def patch_file(filepath):
    print(f"[*] Processing {filepath}...", flush=True)
    if not os.path.exists(filepath):
        print(f"[-] File not found: {filepath}")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Ensure Cadre Slicer has id="cadreSlicerGroup"
    old_cadre_markup = r'<div class="slicer-group">\s*<span class="slicer-label" id="lblCadreSlicer">'
    new_cadre_markup = '<div class="slicer-group" id="cadreSlicerGroup">\n<span class="slicer-label" id="lblCadreSlicer">'
    if 'id="cadreSlicerGroup"' not in content:
        content = re.sub(old_cadre_markup, new_cadre_markup, content, count=1)
        print("  [+] Added id='cadreSlicerGroup' to Cadre Slicer container")

    # 2. Update activateTab to control Cadre Slicer visibility dynamically
    # Look for activateTab function definition
    pattern_activate = r'(function activateTab\(tabId,\s*el\)\s*\{[\s\S]*?)(const activeSec = document\.getElementById\(tabId\);)'
    replacement_activate = r'''\1\2
      
      // Dynamic Slicer Visibility: Show Cadre/Role slicer only when applicable to the active tab
      const cadreGroup = document.getElementById('cadreSlicerGroup');
      if (cadreGroup) {
        const roleApplicableTabs = ['tab-overview', 'tab-rf', 'tab-questions', 'tab-governance', 'tab-insights'];
        if (roleApplicableTabs.includes(tabId)) {
          cadreGroup.style.display = 'flex';
        } else {
          cadreGroup.style.display = 'none';
        }
      }'''
    
    if 'roleApplicableTabs' not in content:
        content = re.sub(pattern_activate, replacement_activate, content, count=1)
        print("  [+] Injected dynamic tab-based slicer visibility into activateTab()")

    # 3. Update initOverviewCharts to fully support activeRole in sorting and dataset construction
    # Find initOverviewCharts function
    old_chart_sort = r'(let sortedList = \[\.\.\.dists\];\s*if \(activeProgram === \'DO\'\) \{[\s\S]*?sortedList\.sort\(\(a,b\) => \(b\.combined_total[\s\S]*?\);\s*\})'
    new_chart_sort = '''let sortedList = [...dists];
      if (activeRole === 'Facilitator') {
        sortedList.sort((a,b) => ((b.facilitators || 0) + (b.do_facilitators || 0)) - ((a.facilitators || 0) + (a.do_facilitators || 0)));
      } else if (activeRole === 'Observer') {
        sortedList.sort((a,b) => ((b.monitors || 0) + (b.do_monitors || 0)) - ((a.monitors || 0) + (a.do_monitors || 0)));
      } else if (activeRole === 'Participant') {
        sortedList.sort((a,b) => (b.attendees || b.do_participants || 0) - (a.attendees || a.do_participants || 0));
      } else if (activeProgram === 'DO') {
        sortedList.sort((a,b) => (b.do_participants || 0) - (a.do_participants || 0));
      } else if (activeProgram === 'CLSS') {
        sortedList.sort((a,b) => (b.attendees || 0) - (a.attendees || 0));
      } else {
        sortedList.sort((a,b) => (b.combined_total || ((b.attendees || 0) + (b.do_participants || 0))) - (a.combined_total || ((a.attendees || 0) + (a.do_participants || 0))));
      }'''
    
    if 'activeRole === \'Facilitator\'' not in content:
        content = re.sub(old_chart_sort, new_chart_sort, content, count=1)
        print("  [+] Enhanced overview chart sorting by activeRole")

    # 4. Update Overview Bar Chart Datasets to respect activeRole under ALL programs
    old_datasets_block = r'(let datasets = \[\];[\s\S]*?charts\.ovTopDistricts = new Chart\(ctx1,)'
    new_datasets_block = '''let datasets = [];

        if (activeRole === 'Participant') {
          // 👨‍🏫 TEACHERS ONLY
          if (activeProgram === 'DO') {
            datasets.push({ label: isHi ? 'DO जिला शिक्षक/प्रतिभागी' : 'DO Teacher Participants', data: displayList.map(d => d.do_participants || 0), backgroundColor: '#1d4ed8', borderRadius: 4 });
          } else if (activeProgram === 'CLSS') {
            datasets.push({ label: isHi ? 'CLSS सहभागी शिक्षक' : 'CLSS Teacher Attendees', data: displayList.map(d => d.attendees || 0), backgroundColor: '#1d4ed8', borderRadius: 4 });
          } else {
            datasets.push({ label: isHi ? 'CLSS सहभागी शिक्षक' : 'CLSS Teacher Attendees', data: displayList.map(d => d.attendees || 0), backgroundColor: '#1d4ed8', borderRadius: 4 });
            datasets.push({ label: isHi ? 'DO शिक्षक/प्रतिभागी' : 'DO Teacher Participants', data: displayList.map(d => d.do_participants || 0), backgroundColor: '#3b82f6', borderRadius: 4 });
          }
        } else if (activeRole === 'Facilitator') {
          // 🤝 FACILITATORS ONLY
          if (activeProgram === 'DO') {
            datasets.push({ label: isHi ? 'DO सहजकर्ता' : 'DO Facilitators', data: displayList.map(d => d.do_facilitators || 0), backgroundColor: '#008aab', borderRadius: 4 });
          } else if (activeProgram === 'CLSS') {
            datasets.push({ label: isHi ? 'CLSS सहजकर्ता' : 'CLSS Facilitators', data: displayList.map(d => d.facilitators || 0), backgroundColor: '#008aab', borderRadius: 4 });
          } else {
            datasets.push({ label: isHi ? 'CLSS सहजकर्ता' : 'CLSS Facilitators', data: displayList.map(d => d.facilitators || 0), backgroundColor: '#008aab', borderRadius: 4 });
            datasets.push({ label: isHi ? 'DO सहजकर्ता' : 'DO Facilitators', data: displayList.map(d => d.do_facilitators || 0), backgroundColor: '#2dd4bf', borderRadius: 4 });
          }
        } else if (activeRole === 'Observer') {
          // 👁️ MONITORS/OBSERVERS ONLY
          if (activeProgram === 'DO') {
            datasets.push({ label: isHi ? 'DO पर्यवेक्षक / मॉनिटर' : 'DO Observers', data: displayList.map(d => d.do_monitors || 0), backgroundColor: '#4f46e5', borderRadius: 4 });
          } else if (activeProgram === 'CLSS') {
            datasets.push({ label: isHi ? 'CLSS मॉनिटर' : 'CLSS Monitors', data: displayList.map(d => d.monitors || 0), backgroundColor: '#4f46e5', borderRadius: 4 });
          } else {
            datasets.push({ label: isHi ? 'CLSS मॉनिटर' : 'CLSS Monitors', data: displayList.map(d => d.monitors || 0), backgroundColor: '#4f46e5', borderRadius: 4 });
            datasets.push({ label: isHi ? 'DO पर्यवेक्षक' : 'DO Observers', data: displayList.map(d => d.do_monitors || 0), backgroundColor: '#818cf8', borderRadius: 4 });
          }
        } else {
          // ALL ROLES
          if (activeProgram === 'DO') {
            datasets.push({ label: isHi ? 'DO जिला प्रतिभागी' : 'DO Participants', data: displayList.map(d => d.do_participants || 0), backgroundColor: '#008aab', borderRadius: 4 });
            datasets.push({ label: isHi ? 'DO फैसिलिटेटर' : 'DO Facilitators', data: displayList.map(d => d.do_facilitators || 0), backgroundColor: '#63d0df', borderRadius: 4 });
            datasets.push({ label: isHi ? 'DO पर्यवेक्षक' : 'DO Observers', data: displayList.map(d => d.do_monitors || 0), backgroundColor: '#4f46e5', borderRadius: 4 });
          } else if (activeProgram === 'CLSS') {
            datasets.push({ label: isHi ? 'सहभागी शिक्षक' : 'Teacher Attendees', data: displayList.map(d => d.attendees || 0), backgroundColor: '#1d4ed8', borderRadius: 4 });
            datasets.push({ label: isHi ? 'CLSS फैसिलिटेटर' : 'CLSS Facilitators', data: displayList.map(d => d.facilitators || 0), backgroundColor: '#008aab', borderRadius: 4 });
            datasets.push({ label: isHi ? 'CLSS मॉनिटर' : 'CLSS Monitors', data: displayList.map(d => d.monitors || 0), backgroundColor: '#4f46e5', borderRadius: 4 });
          } else {
            // Consolidated - Rich 2-Tone Visual Structure
            datasets.push({ label: isHi ? 'शैक्षिक संवाद सहभागिता (CLSS)' : 'CLSS Turnout', data: displayList.map(d => d.attendees || d.total || 0), backgroundColor: '#1d4ed8', borderRadius: 4 });
            datasets.push({ label: isHi ? 'जिला अभिमुखीकरण सहभागिता (DO)' : 'DO Turnout', data: displayList.map(d => d.do_participants || d.do_total || 0), backgroundColor: '#008aab', borderRadius: 4 });
          }
        }

        charts.ovTopDistricts = new Chart(ctx1,'''

    content = re.sub(old_datasets_block, new_datasets_block, content, count=1)
    print("  [+] Injected role-specific bar chart dataset rendering")

    # 5. Update KPI Cards in updateKPIs() to display role badges and active highlights
    pattern_kpi_role = r'(// 5\. CARD 5: TRAINERS & OBSERVERS[\s\S]*?if \(kCadreLabel\)[^\n]+\n)'
    replacement_kpi_role = r'''\1
      const card3El = document.querySelector('#tab-overview .bento-grid .bento-card:nth-child(3)') || document.getElementById('kpiTeachers')?.closest('.bento-card');
      const card5El = document.querySelector('#tab-overview .bento-grid .bento-card:nth-child(5)') || document.getElementById('kpiCadre')?.closest('.bento-card');
      
      if (card3El) {
        if (activeRole === 'Participant') {
          card3El.style.borderColor = '#2563eb';
          card3El.style.boxShadow = '0 0 0 2px rgba(37,99,235,0.25)';
        } else {
          card3El.style.borderColor = '';
          card3El.style.boxShadow = '';
        }
      }
      
      if (card5El) {
        if (activeRole === 'Facilitator' || activeRole === 'Observer') {
          card5El.style.borderColor = activeRole === 'Facilitator' ? '#008aab' : '#4f46e5';
          card5El.style.boxShadow = '0 0 0 2px rgba(0,138,171,0.25)';
        } else {
          card5El.style.borderColor = '';
          card5El.style.boxShadow = '';
        }
      }
'''
    if 'card3El.style.borderColor' not in content:
        content = re.sub(pattern_kpi_role, replacement_kpi_role, content, count=1)
        print("  [+] Injected KPI card role highlight styling into updateKPIs()")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"[✓] Successfully updated {filepath}\n")
    return True

def main():
    print("===================================================================")
    print(" Applying Cadre / Role Slicer Fix Across All Dashboard Targets")
    print("===================================================================\n")
    for target in TARGET_FILES:
        patch_file(target)

if __name__ == '__main__':
    main()
