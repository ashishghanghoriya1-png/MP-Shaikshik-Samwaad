import json, os, re, shutil

# 1. Backup original file
source_html_path = r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html'
backup_path = r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.bak.html'
shutil.copyfile(source_html_path, backup_path)
print(f"Backed up to {backup_path}")

with open(source_html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Load 52-district data
with open(r'c:\Master Dashboard for CLSS\data\exports\cohort_matrix_52_districts.json', 'r', encoding='utf-8') as f:
    district_cohorts = json.load(f)

# --- 1. Nav Bar Update ---
nav_target = '<button class="nav-item" id="navTabResearch" onclick="activateTab(\'tab-research\', this)">📚 10. Qualitative Research</button>'
nav_replacement = '<button class="nav-item" id="navTabResearch" onclick="activateTab(\'tab-research\', this)">📚 10. Qualitative Research</button>\n<button class="nav-item" id="navTabCohort" onclick="activateTab(\'tab-cohort\', this)">👥 11. Teacher Cohorts</button>'

if nav_target in html:
    html = html.replace(nav_target, nav_replacement, 1)
    print("[+] Successfully updated Nav Bar.")
else:
    print("[!] Nav target not found!")

# --- 2. HTML Section Injection ---
from cohort_tab_block import cohort_html

# Insert right after </section> of tab-research
res_idx = html.find('id="tab-research"')
res_close_idx = html.find('</section>', res_idx) + len('</section>')

html = html[:res_close_idx] + "\n\n" + cohort_html + html[res_close_idx:]
print("[+] Successfully injected Tab 11 HTML section.")

# --- 3. JavaScript Logic Injection ---
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

    const searchTerm = (document.getElementById('cohortDistrictSearch')?.value || '').toLowerCase().trim();
    
    let filtered = cohortDistrictData.filter(d => {{
      const matchesSearch = d.district.toLowerCase().includes(searchTerm);
      if (!matchesSearch) return false;
      
      if (currentCohortFilterType === 'HIGH_RET') return d.retention_pct >= 60.0;
      if (currentCohortFilterType === 'HIGH_NEW') return d.new_intake_pct >= 50.0;
      if (currentCohortFilterType === 'LAGGING') return d.saturation_pct < 80.0;
      return true;
    }});

    // Sorting
    filtered.sort((a, b) => {{
      let valA, valB;
      switch (currentCohortSort.col) {{
        case 0: valA = a.district; valB = b.district; break;
        case 1: valA = a.aug_total; valB = b.aug_total; break;
        case 2: valA = a.sep_total; valB = b.sep_total; break;
        case 3: valA = a.common; valB = b.common; break;
        case 4: valA = a.retention_pct; valB = b.retention_pct; break;
        case 5: valA = a.sep_only; valB = b.sep_only; break;
        case 6: valA = a.new_intake_pct; valB = b.new_intake_pct; break;
        case 7: valA = a.aug_only; valB = b.aug_only; break;
        case 8: valA = a.cumulative_unique; valB = b.cumulative_unique; break;
        case 9: valA = a.target_math_sci; valB = b.target_math_sci; break;
        case 10: valA = a.saturation_pct; valB = b.saturation_pct; break;
        default: valA = a.district; valB = b.district;
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
      let satBadge = '';
      if (d.saturation_pct >= 100) {{
        satBadge = `<span class="badge" style="background: rgba(5,150,105,0.15); color: #059669; font-weight: 800; border: 1px solid rgba(5,150,105,0.3); font-size: 11px;">${{d.saturation_pct}}% Saturated</span>`;
      }} else if (d.saturation_pct >= 80) {{
        satBadge = `<span class="badge" style="background: rgba(0,138,171,0.15); color: var(--peepul-teal); font-weight: 800; border: 1px solid rgba(0,138,171,0.3); font-size: 11px;">${{d.saturation_pct}}% On Track</span>`;
      }} else {{
        satBadge = `<span class="badge" style="background: rgba(217,119,6,0.15); color: #d97706; font-weight: 800; border: 1px solid rgba(217,119,6,0.3); font-size: 11px;">${{d.saturation_pct}}% Lagging</span>`;
      }}

      return `
        <tr style="border-bottom: 1px solid var(--border-hairline); transition: background 0.15s;" onmouseover="this.style.background='var(--bg-surface-2)'" onmouseout="this.style.background='transparent'">
          <td style="padding: 10px 14px; font-weight: 700; color: var(--text-primary);">${{d.district}}</td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); color: var(--text-secondary);">${{d.aug_total.toLocaleString()}}</td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); color: var(--text-secondary);">${{d.sep_total.toLocaleString()}}</td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); font-weight: 700; color: #059669;">${{d.common.toLocaleString()}}</td>
          <td style="padding: 10px 12px; text-align: right;">
            <span style="font-family: var(--font-mono); font-weight: 800; color: #059669;">${{d.retention_pct}}%</span>
          </td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); font-weight: 700; color: #2563eb;">${{d.sep_only.toLocaleString()}}</td>
          <td style="padding: 10px 12px; text-align: right;">
            <span style="font-family: var(--font-mono); font-weight: 800; color: #2563eb;">${{d.new_intake_pct}}%</span>
          </td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); font-weight: 700; color: #d97706;">${{d.aug_only.toLocaleString()}}</td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); font-weight: 800; color: var(--peepul-teal);">${{d.cumulative_unique.toLocaleString()}}</td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); color: var(--text-muted);">${{d.target_math_sci.toLocaleString()}}</td>
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

  // Hook into DOMContentLoaded
  document.addEventListener('DOMContentLoaded', () => {{
    setTimeout(renderCohortTab, 500);
  }});
"""

# Inject before the closing </script> tag
last_script_close = html.rfind('</script>')
if last_script_close != -1:
    html = html[:last_script_close] + "\n" + js_logic + "\n" + html[last_script_close:]
    print("[+] Successfully injected JavaScript logic.")
else:
    print("[!] Closing script tag not found!")

# Save back to file
with open(source_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"[+] Written updated HTML to: {source_html_path}")
