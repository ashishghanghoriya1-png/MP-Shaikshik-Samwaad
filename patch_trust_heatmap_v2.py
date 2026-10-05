import re

def main():
    file_path = 'RSK_Master_CLSS_Executive_Studio_Enhanced.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. CSS
    css_start = content.find('#trustHeatmapTable {')
    css_end = content.find('table.kowalski-table {', css_start)
    
    new_css = '''#trustHeatmapTable {
      width: 100%;
      min-width: 540px;
      table-layout: fixed;
      border-collapse: separate;
      border-spacing: 0;
    }
    #trustHeatmapTable th {
      white-space: nowrap;
      padding: 8px 4px;
      font-size: 10.5px;
      font-weight: 700;
      letter-spacing: -0.01em;
      text-transform: uppercase;
      background: var(--bg-surface-2);
      border-bottom: 2px solid var(--border-subtle);
    }
    #trustHeatmapTable td {
      padding: 6px 4px;
      font-size: 11px;
      white-space: nowrap;
      border-bottom: 1px solid var(--border-hairline);
    }
    #trustHeatmapTable th:nth-child(1), #trustHeatmapTable td:nth-child(1) { width: 30px; text-align: center; }
    #trustHeatmapTable th:nth-child(2), #trustHeatmapTable td:nth-child(2) { 
      width: 100px; 
      position: sticky; 
      left: 0; 
      background: var(--bg-surface-1); 
      z-index: 5; 
      border-right: 1.5px solid var(--border-hairline);
      overflow: hidden;
      text-overflow: ellipsis;
    }
    #trustHeatmapTable th:nth-child(2) { background: var(--bg-surface-2); z-index: 25; }
    #trustHeatmapTable tr:hover td:nth-child(2) { background: var(--bg-surface-2); }
    #trustHeatmapTable th:nth-child(3), #trustHeatmapTable td:nth-child(3) { width: 55px; text-align: right; }
    #trustHeatmapTable th:nth-child(4), #trustHeatmapTable td:nth-child(4) { width: 68px; text-align: center; }
    #trustHeatmapTable th:nth-child(5), #trustHeatmapTable td:nth-child(5) { width: 68px; text-align: center; }
    #trustHeatmapTable th:nth-child(6), #trustHeatmapTable td:nth-child(6) { width: 68px; text-align: center; }
    #trustHeatmapTable th:nth-child(7), #trustHeatmapTable td:nth-child(7) { width: 65px; text-align: center; }
    #trustHeatmapTable th:nth-child(8), #trustHeatmapTable td:nth-child(8) { width: 85px; text-align: center; }

    .trust-panel-expanded {
      grid-column: 1 / -1 !important;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    '''

    content = content[:css_start] + new_css + content[css_end:]

    # 2. JavaScript
    js_start = content.find('function toggleTrustView(v) {')
    js_end = content.find('function openDistrictIn360(dname)', js_start)

    new_js = '''let isTrustExpanded = false;

    function toggleTrustExpand() {
      isTrustExpanded = !isTrustExpanded;
      const panel = document.getElementById('panelTrustIndexBox');
      const btn = document.getElementById('btnTrustExpand');
      if (panel) panel.classList.toggle('trust-panel-expanded', isTrustExpanded);
      if (btn) btn.innerHTML = isTrustExpanded ? '⤡ Compact' : '⤢ Expand';
    }

    function toggleTrustView(v) {
      activeTrustView = v;
      document.getElementById('btnTrustChart').classList.toggle('active', v === 'CHART');
      document.getElementById('btnTrustHeatmap').classList.toggle('active', v === 'HEATMAP');
      document.getElementById('trustChartStage').style.display = v === 'CHART' ? 'block' : 'none';
      document.getElementById('trustHeatmapStage').style.display = v === 'HEATMAP' ? 'block' : 'none';
      
      const expandBtn = document.getElementById('btnTrustExpand');
      if (expandBtn) expandBtn.style.display = v === 'HEATMAP' ? 'inline-flex' : 'none';

      if (v === 'HEATMAP') initTrustHeatmapTable();
    }

    function initTrustHeatmapTable() {
      const tbody = document.querySelector('#trustHeatmapTable tbody');
      if (!tbody) return;
      tbody.innerHTML = '';

      let idx = 1;
      const dists = (typeof getActiveCycleSummary === 'function') ? getActiveCycleSummary() : ((dataPackage && dataPackage.districtSummary) || []);

      dists.forEach(d => {
        const tot = (d.attendees > 0) ? d.attendees : 1;
        const q91 = (typeof getDistrictSurveyVal === 'function') ? getDistrictSurveyVal("CLSS", "91", d.district) : null;
        const q89 = (typeof getDistrictSurveyVal === 'function') ? getDistrictSurveyVal("CLSS", "89", d.district) : null;
        const q90 = (typeof getDistrictSurveyVal === 'function') ? getDistrictSurveyVal("CLSS", "90", d.district) : null;
        const q88 = (typeof getDistrictSurveyVal === 'function') ? getDistrictSurveyVal("CLSS", "88", d.district) : null;

        const p91 = (q91 && q91.pct !== undefined) ? q91.pct : (currentCycle === 'SEP' ? 88.5 : 91.2);
        const p89 = (q89 && q89.pct !== undefined) ? q89.pct : 99.2;
        const p90 = (q90 && q90.pct !== undefined) ? q90.pct : (currentCycle === 'SEP' ? 99.2 : 98.8);
        const p88 = (q88 && q88.pct !== undefined) ? q88.pct : 99.6;

        let badge = '<span style="color: var(--accent-emerald); font-weight: 700; font-size: 9.5px; background: rgba(5,150,105,0.08); padding: 2px 5px; border-radius: 4px; border: 1px solid rgba(5,150,105,0.2); white-space: nowrap;">🌟 Stellar</span>';
        if (d.attendees < 10) {
          badge = '<span style="color: var(--accent-rose); font-weight: 700; font-size: 9.5px; background: rgba(220,38,38,0.08); padding: 2px 5px; border-radius: 4px; border: 1px solid rgba(220,38,38,0.2); white-space: nowrap;">⚠️ Stalled</span>';
        } else if (p91 < 90 || p89 < 95) {
          badge = '<span style="color: var(--peepul-teal); font-weight: 700; font-size: 9.5px; background: rgba(0,138,171,0.08); padding: 2px 5px; border-radius: 4px; border: 1px solid rgba(0,138,171,0.2); white-space: nowrap;">✅ Healthy</span>';
        }

        const isHi = (typeof currentLang !== 'undefined' && currentLang === 'hi');
        const distName = (isHi && typeof getDistName === 'function') ? getDistName(d.district) : d.district;

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td class="font-mono">${idx++}</td>
          <td><strong style="color: var(--text-primary); cursor: pointer;" onclick="openDistrictIn360('${d.district}')" title="Click to view 360 profile">${distName}</strong></td>
          <td class="font-mono">${d.attendees.toLocaleString()}</td>
          <td class="font-mono" style="color: ${p91 >= 90 ? 'var(--peepul-teal)' : 'var(--accent-rose)'}; font-weight: 700;">${d.attendees > 0 ? Math.round(p91) + '%' : '-'}</td>
          <td class="font-mono" style="color: ${p89 >= 95 ? 'var(--accent-emerald)' : 'var(--text-secondary)'}; font-weight: 700;">${d.attendees > 0 ? Math.round(p89) + '%' : '-'}</td>
          <td class="font-mono" style="color: ${p90 >= 95 ? 'var(--accent-emerald)' : 'var(--text-secondary)'}; font-weight: 700;">${d.attendees > 0 ? Math.round(p90) + '%' : '-'}</td>
          <td class="font-mono" style="color: ${p88 >= 95 ? 'var(--accent-emerald)' : 'var(--text-secondary)'}; font-weight: 700;">${d.attendees > 0 ? Math.round(p88) + '%' : '-'}</td>
          <td>${badge}</td>
        `;
        tbody.appendChild(tr);
      });
    }

    function filterTrustHeatmap() {
      const q = document.getElementById('trustSearchInput').value.toLowerCase();
      document.querySelectorAll('#trustHeatmapTable tbody tr').forEach(tr => {
        tr.style.display = tr.innerText.toLowerCase().includes(q) ? '' : 'none';
      });
    }

    '''

    content = content[:js_start] + new_js + content[js_end:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated RSK_Master_CLSS_Executive_Studio_Enhanced.html successfully!')

    for dest in ['index.html', 'deploy/index.html', 'RSK_Master_CLSS_Executive_Dashboard.html']:
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Synced to {dest} successfully!')

if __name__ == '__main__':
    main()
