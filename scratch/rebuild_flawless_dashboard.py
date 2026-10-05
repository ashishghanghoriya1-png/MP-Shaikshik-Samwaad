import json, os, re, shutil

# Read backup
backup_path = r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.bak.html'
with open(backup_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Load standardized 52-district data
with open(r'c:\Master Dashboard for CLSS\data\exports\cohort_matrix_52_districts.json', 'r', encoding='utf-8') as f:
    district_cohorts = json.load(f)

# --- 1. Nav Bar Update ---
nav_target = '<button class="nav-item" id="navTabResearch" onclick="activateTab(\'tab-research\', this)">📚 10. Qualitative Research</button>'
nav_replacement = '<button class="nav-item" id="navTabResearch" onclick="activateTab(\'tab-research\', this)">📚 10. Qualitative Research</button>\n<button class="nav-item" id="navTabCohort" onclick="activateTab(\'tab-cohort\', this)">👥 11. Teacher Cohorts</button>'

if nav_target in html:
    html = html.replace(nav_target, nav_replacement, 1)
    print("[+] Nav bar updated.")
else:
    print("[!] Nav target not found!")

# --- 2. HTML Section Injection ---
from cohort_tab_block import cohort_html

res_idx = html.find('id="tab-research"')
res_close_idx = html.find('</section>', res_idx) + len('</section>')

html = html[:res_close_idx] + "\n\n" + cohort_html + html[res_close_idx:]
print("[+] Tab 11 HTML injected.")

# --- 3. Update setLanguage for bilingual support ---
target_block = """        const btnResearch = document.getElementById('navTabResearch') || (navItems.length >= 10 ? navItems[9] : null);
        if (btnResearch) {
          btnResearch.innerHTML = t.navResearch || (lang === 'hi' ? '📚 10. गुणात्मक शोध' : '📚 10. Qualitative Research');
        }"""

replacement_block = """        const btnResearch = document.getElementById('navTabResearch') || (navItems.length >= 10 ? navItems[9] : null);
        if (btnResearch) {
          btnResearch.innerHTML = t.navResearch || (lang === 'hi' ? '📚 10. गुणात्मक शोध' : '📚 10. Qualitative Research');
        }
        const btnCohort = document.getElementById('navTabCohort') || (navItems.length >= 11 ? navItems[10] : null);
        if (btnCohort) {
          btnCohort.innerHTML = (lang === 'hi' ? '👥 11. शिक्षक समूह' : '👥 11. Teacher Cohorts');
        }
        const lblCohortTitle = document.getElementById('lblCohortTitle');
        if (lblCohortTitle) {
          lblCohortTitle.innerHTML = (lang === 'hi' ? 'शिक्षक समूह एवं उपस्थिति प्रवाह (Teacher Cohort Intelligence)' : 'Teacher Attendance Cohorts &amp; Trajectory Intelligence');
        }
        const lblCohortSubtitle = document.getElementById('lblCohortSubtitle');
        if (lblCohortSubtitle) {
          lblCohortSubtitle.innerHTML = (lang === 'hi' ? 'अगस्त और सितंबर सत्रों के बीच अद्वितीय EmployeeCode मिलान। कोर प्रतिधारण (55.0%), नए शिक्षक आगमन (43.5%), और 52 जिलों में लक्ष्य संतृप्ति का विश्लेषण।' : 'Cross-month teacher tracking using unique EmployeeCode identifiers. Quantifies core retention (55.0%), fresh monthly inflow (43.5%), churn/drop-off calling pools, and cumulative progress toward statewide teacher saturation.');
        }"""

if target_block in html:
    html = html.replace(target_block, replacement_block, 1)
    print("[+] Bilingual translation updated.")

# --- 4. Update activateTab ---
old_activate = """function activateTab(tabId, el) {
      document.querySelectorAll('.tab-section').forEach(s => s.classList.remove('active'));
      document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
      const activeSec = document.getElementById(tabId);
      if (activeSec) activeSec.classList.add('active');
      if (el) el.classList.add('active');"""

new_activate = """function activateTab(tabId, el) {
      document.querySelectorAll('.tab-section').forEach(s => s.classList.remove('active'));
      document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
      const activeSec = document.getElementById(tabId);
      if (activeSec) activeSec.classList.add('active');
      if (el) el.classList.add('active');

      if (tabId === 'tab-cohort' && typeof renderCohortTab === 'function') {
        renderCohortTab();
      }"""

if old_activate in html:
    html = html.replace(old_activate, new_activate, 1)
    print("[+] activateTab updated.")

# --- 5. Robust JavaScript Engine for Tab 11 ---
js_logic = f"""
  // =========================================================================
  // TAB 11: TEACHER COHORT & TRAJECTORY JAVASCRIPT ENGINE
  // =========================================================================
  const cohortDistrictData = {json.dumps(district_cohorts, indent=2)};
  let currentCohortSort = {{ col: 0, asc: true }};
  let currentCohortFilterType = 'ALL';

  function renderCohortTab() {{
    const tbody = document.getElementById('cohortMatrixBody');
    if (!tbody) return;

    const searchInput = document.getElementById('cohortDistrictSearch');
    const searchTerm = (searchInput && searchInput.value) ? searchInput.value.toLowerCase().trim() : '';
    
    let filtered = cohortDistrictData.filter(d => {{
      const dName = String(d.district || '').toLowerCase();
      const matchesSearch = !searchTerm || dName.includes(searchTerm);
      if (!matchesSearch) return false;
      
      const retPct = Number(d.retention_pct || 0);
      const newPct = Number(d.new_intake_pct || 0);
      const satPct = Number(d.saturation_pct || 0);

      if (currentCohortFilterType === 'HIGH_RET') return retPct >= 60.0;
      if (currentCohortFilterType === 'HIGH_NEW') return newPct >= 50.0;
      if (currentCohortFilterType === 'LAGGING') return satPct < 80.0;
      return true;
    }});

    // Sorting
    filtered.sort((a, b) => {{
      let valA, valB;
      switch (currentCohortSort.col) {{
        case 0: valA = String(a.district || ''); valB = String(b.district || ''); break;
        case 1: valA = Number(a.aug_total || 0); valB = Number(b.aug_total || 0); break;
        case 2: valA = Number(a.sep_total || 0); valB = Number(b.sep_total || 0); break;
        case 3: valA = Number(a.common || 0); valB = Number(b.common || 0); break;
        case 4: valA = Number(a.retention_pct || 0); valB = Number(b.retention_pct || 0); break;
        case 5: valA = Number(a.sep_only || 0); valB = Number(b.sep_only || 0); break;
        case 6: valA = Number(a.new_intake_pct || 0); valB = Number(b.new_intake_pct || 0); break;
        case 7: valA = Number(a.aug_only || 0); valB = Number(b.aug_only || 0); break;
        case 8: valA = Number(a.cumulative_unique || 0); valB = Number(b.cumulative_unique || 0); break;
        case 9: valA = Number(a.target_math_sci || 0); valB = Number(b.target_math_sci || 0); break;
        case 10: valA = Number(a.saturation_pct || 0); valB = Number(b.saturation_pct || 0); break;
        default: valA = String(a.district || ''); valB = String(b.district || '');
      }}
      if (typeof valA === 'string') {{
        return currentCohortSort.asc ? valA.localeCompare(valB) : valB.localeCompare(valA);
      }} else {{
        return currentCohortSort.asc ? valA - valB : valB - valA;
      }}
    }});

    const countEl = document.getElementById('cohortVisibleCount');
    if (countEl) countEl.textContent = filtered.length;

    tbody.innerHTML = filtered.map(d => {{
      const satVal = Number(d.saturation_pct || 0);
      let satBadge = '';
      if (satVal >= 100) {{
        satBadge = `<span class="badge" style="background: rgba(5,150,105,0.15); color: #059669; font-weight: 800; border: 1px solid rgba(5,150,105,0.3); font-size: 11px;">${{satVal}}% Saturated</span>`;
      }} else if (satVal >= 80) {{
        satBadge = `<span class="badge" style="background: rgba(0,138,171,0.15); color: var(--peepul-teal); font-weight: 800; border: 1px solid rgba(0,138,171,0.3); font-size: 11px;">${{satVal}}% On Track</span>`;
      }} else {{
        satBadge = `<span class="badge" style="background: rgba(217,119,6,0.15); color: #d97706; font-weight: 800; border: 1px solid rgba(217,119,6,0.3); font-size: 11px;">${{satVal}}% Lagging</span>`;
      }}

      return `
        <tr style="border-bottom: 1px solid var(--border-hairline); transition: background 0.15s;" onmouseover="this.style.background='var(--bg-surface-2)'" onmouseout="this.style.background='transparent'">
          <td style="padding: 10px 14px; font-weight: 700; color: var(--text-primary);">${{d.district}}</td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); color: var(--text-secondary);">${{Number(d.aug_total||0).toLocaleString()}}</td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); color: var(--text-secondary);">${{Number(d.sep_total||0).toLocaleString()}}</td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); font-weight: 700; color: #059669;">${{Number(d.common||0).toLocaleString()}}</td>
          <td style="padding: 10px 12px; text-align: right;">
            <span style="font-family: var(--font-mono); font-weight: 800; color: #059669;">${{d.retention_pct}}%</span>
          </td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); font-weight: 700; color: #2563eb;">${{Number(d.sep_only||0).toLocaleString()}}</td>
          <td style="padding: 10px 12px; text-align: right;">
            <span style="font-family: var(--font-mono); font-weight: 800; color: #2563eb;">${{d.new_intake_pct}}%</span>
          </td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); font-weight: 700; color: #d97706;">${{Number(d.aug_only||0).toLocaleString()}}</td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); font-weight: 800; color: var(--peepul-teal);">${{Number(d.cumulative_unique||0).toLocaleString()}}</td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); color: var(--text-muted);">${{Number(d.target_math_sci||0).toLocaleString()}}</td>
          <td style="padding: 10px 14px; text-align: right;">${{satBadge}}</td>
        </tr>
      `;
    }}).join('');
  }}

  function filterCohortTable() {{
    renderCohortTab();
  }}

  function setCohortFilter(type, btn) {{
    currentCohortFilterType = type;
    document.querySelectorAll('#cohortFilterPills .slicer-btn').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
    renderCohortTab();
  }}

  function sortCohortTable(colIdx) {{
    if (currentCohortSort.col === colIdx) {{
      currentCohortSort.asc = !currentCohortSort.asc;
    }} else {{
      currentCohortSort.col = colIdx;
      currentCohortSort.asc = (colIdx === 0);
    }}
    renderCohortTab();
  }}

  function downloadCohortMatrixCSV() {{
    const headers = ["District", "August_Attendance", "September_Attendance", "Persistent_Repeat_Teachers", "Retention_Rate_Pct", "September_New_Intake", "New_Intake_Rate_Pct", "August_Only_Lapsed", "Cumulative_Unique_Teachers", "Target_Math_Sci_Universe", "Total_Varg2_Universe", "Target_Saturation_Pct"];
    const rows = cohortDistrictData.map(d => [
      `"${{d.district}}"`,
      d.aug_total,
      d.sep_total,
      d.common,
      d.retention_pct,
      d.sep_only,
      d.new_intake_pct,
      d.aug_only,
      d.cumulative_unique,
      d.target_math_sci,
      d.total_varg2,
      d.saturation_pct
    ]);

    const csvContent = "data:text/csv;charset=utf-8," + [headers.join(","), ...rows.map(e => e.join(","))].join("\\n");
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "52_District_Teacher_Cohort_Matrix.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }}

  // Initialize on load
  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', () => {{ setTimeout(renderCohortTab, 200); }});
  }} else {{
    setTimeout(renderCohortTab, 200);
  }}
"""

# Insert js_logic cleanly right before </script>
last_script_idx = html.rfind('</script>')
html = html[:last_script_idx] + "\n" + js_logic + "\n" + html[last_script_idx:]
print("[+] Flawless JavaScript engine injected.")

# Save to both target files
enhanced_path = r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html'
index_path = r'c:\Master Dashboard for CLSS\index.html'

with open(enhanced_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"[+] Saved to {enhanced_path}")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"[+] Saved to {index_path}")
