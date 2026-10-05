import re

def main():
    file_path = 'RSK_Master_CLSS_Executive_Studio_Enhanced.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update HTML Markup of the 4-Quadrant Section
    old_html_pattern = r'<!-- 4-Quadrant District Priority Matrix -->.*?<!-- 2\. RESULTS FRAMEWORK'
    new_html = '''<!-- 4-Quadrant District Priority Matrix -->
      <div class="panel-box" style="margin-top: 24px;">
        <div class="panel-head" style="flex-wrap: wrap; gap: 10px;">
          <div>
            <div class="panel-head-title" id="ovQuadrantMatrixTitle">📊 Statewide 4-Quadrant District Priority Matrix (Turnout vs. Pedagogy Accuracy)</div>
            <div id="ovQuadrantChartRef" style="font-size: 10.5px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 2px;">
              [Ref: Turnout from <em>CLSS Participant Attendance</em> vs Composite Pedagogy Score from <em>Key Subject Questions (Q82, Q84, Q95, Q96, Q97)</em>]
            </div>
          </div>
          <div style="display: flex; gap: 6px; flex-wrap: wrap;">
            <button class="slicer-btn active" id="btnQuadAll" onclick="filterQuadrant('ALL')">All 52 Districts</button>
            <button class="slicer-btn" id="btnQuad1" onclick="filterQuadrant('Q1')" style="color: var(--accent-emerald);">🏆 High Att. & High Score (<span id="q1BtnCount">15</span>)</button>
            <button class="slicer-btn" id="btnQuad2" onclick="filterQuadrant('Q2')" style="color: var(--peepul-teal);">📈 High Att., Needs Pedagogy (<span id="q2BtnCount">10</span>)</button>
            <button class="slicer-btn" id="btnQuad3" onclick="filterQuadrant('Q3')" style="color: var(--accent-indigo);">🎯 High Score, Needs Att. (<span id="q3BtnCount">13</span>)</button>
            <button class="slicer-btn" id="btnQuad4" onclick="filterQuadrant('Q4')" style="color: var(--accent-rose);">🚨 Priority Support Zone (<span id="q4BtnCount">14</span>)</button>
          </div>
        </div>

        <!-- Dynamic 4-Quadrant Interactive Bento Cards -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-top: 14px;">
          <div id="cardQuad1" onclick="filterQuadrant('Q1')" style="background: rgba(5, 150, 105, 0.06); border: 1px solid rgba(5, 150, 105, 0.25); border-left: 4px solid var(--accent-emerald); padding: 14px; border-radius: var(--radius-md); cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <div style="font-weight: 800; color: var(--accent-emerald); font-size: 12px;">🏆 Q1: HIGH ATTENDANCE & HIGH SCORE</div>
              <span class="pill-badge" id="q1Badge" style="background: rgba(5, 150, 105, 0.18); color: var(--accent-emerald); font-weight: 700;">15 Districts</span>
            </div>
            <div style="font-size: 10.5px; color: var(--text-secondary); margin-bottom: 8px;">High Attendance (≥450) + High Teaching Score (≥56%)</div>
            <div id="q1Chips" style="display: flex; flex-wrap: wrap; gap: 4px; max-height: 140px; overflow-y: auto; padding-right: 2px;"></div>
          </div>

          <div id="cardQuad2" onclick="filterQuadrant('Q2')" style="background: rgba(0, 138, 171, 0.06); border: 1px solid rgba(0, 138, 171, 0.25); border-left: 4px solid var(--peepul-teal); padding: 14px; border-radius: var(--radius-md); cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <div style="font-weight: 800; color: var(--peepul-teal); font-size: 12px;">📈 Q2: HIGH ATTENDANCE, NEEDS PEDAGOGY FOCUS</div>
              <span class="pill-badge" id="q2Badge" style="background: rgba(0, 138, 171, 0.18); color: var(--peepul-teal); font-weight: 700;">10 Districts</span>
            </div>
            <div style="font-size: 10.5px; color: var(--text-secondary); margin-bottom: 8px;">High Attendance (≥450) + Teaching Score Gap (&lt;56%)</div>
            <div id="q2Chips" style="display: flex; flex-wrap: wrap; gap: 4px; max-height: 140px; overflow-y: auto; padding-right: 2px;"></div>
          </div>

          <div id="cardQuad3" onclick="filterQuadrant('Q3')" style="background: rgba(79, 70, 229, 0.06); border: 1px solid rgba(79, 70, 229, 0.25); border-left: 4px solid var(--accent-indigo); padding: 14px; border-radius: var(--radius-md); cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <div style="font-weight: 800; color: var(--accent-indigo); font-size: 12px;">🎯 Q3: HIGH SCORE, NEEDS ATTENDANCE BOOST</div>
              <span class="pill-badge" id="q3Badge" style="background: rgba(79, 70, 229, 0.18); color: var(--accent-indigo); font-weight: 700;">13 Districts</span>
            </div>
            <div style="font-size: 10.5px; color: var(--text-secondary); margin-bottom: 8px;">High Teaching Score (≥56%) + Attendance &lt;450</div>
            <div id="q3Chips" style="display: flex; flex-wrap: wrap; gap: 4px; max-height: 140px; overflow-y: auto; padding-right: 2px;"></div>
          </div>

          <div id="cardQuad4" onclick="filterQuadrant('Q4')" style="background: rgba(220, 38, 38, 0.06); border: 1px solid rgba(220, 38, 38, 0.25); border-left: 4px solid var(--accent-rose); padding: 14px; border-radius: var(--radius-md); cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <div style="font-weight: 800; color: var(--accent-rose); font-size: 12px;">🚨 Q4: PRIORITY SUPPORT ZONE</div>
              <span class="pill-badge" id="q4Badge" style="background: rgba(220, 38, 38, 0.18); color: var(--accent-rose); font-weight: 700;">14 Districts</span>
            </div>
            <div style="font-size: 10.5px; color: var(--text-secondary); margin-bottom: 8px;">Low Attendance &lt;450 + Teaching Score Gap (&lt;56%)</div>
            <div id="q4Chips" style="display: flex; flex-wrap: wrap; gap: 4px; max-height: 140px; overflow-y: auto; padding-right: 2px;"></div>
          </div>
        </div>

        <!-- Full Interactive Quadrant Table -->
        <div style="background: var(--bg-surface-card); border: 1px solid var(--border-hairline); border-radius: var(--radius-md); padding: 16px; margin-top: 14px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; flex-wrap: wrap; gap: 8px;">
            <div>
              <div id="quadrantTableTitle" style="font-size: 13px; font-weight: 800; color: var(--text-primary);">
                Districts in Selected Quadrant: All 52 Districts
              </div>
              <div style="font-size: 11px; color: var(--text-muted);">
                Showing all districts with real-time turnout, composite pedagogy accuracy, and tailored action recommendations.
              </div>
            </div>
            <input class="search-input" id="quadSearchInput" oninput="filterQuadrantTableSearch()" placeholder="🔍 Search district in matrix..." style="min-width: 220px; font-size: 11.5px;" type="text"/>
          </div>
          <div class="table-viewport" style="max-height: 420px;">
            <table class="kowalski-table" id="quadrantDistTable">
              <thead>
                <tr>
                  <th>S.No</th>
                  <th>District</th>
                  <th>Quadrant Classification</th>
                  <th>CLSS Turnout</th>
                  <th>Pedagogy Score</th>
                  <th>Blocks</th>
                  <th>Clusters</th>
                  <th>Avg / Cluster</th>
                  <th>Recommended State Action</th>
                  <th style="text-align: right;">Action</th>
                </tr>
              </thead>
              <tbody>
                <!-- dynamically populated -->
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. RESULTS FRAMEWORK'''

    content = re.sub(old_html_pattern, new_html, content, flags=re.DOTALL)

    # 2. Update the JavaScript Implementation of the 4-Quadrant Priority Matrix
    target_start = content.find('let currentQuadFilter = \'ALL\';')
    target_end = content.find('// SIDE-BY-SIDE DISTRICT COMPARATOR', target_start)

    new_js = '''let currentQuadFilter = 'ALL';
    const TURNOUT_BENCHMARK = 450;
    const PEDAGOGY_BENCHMARK = 56;

    function calculateDistrictPedagogyScore(dname) {
      const surveys = (typeof getActiveSurveys === 'function') ? getActiveSurveys() : ((dataPackage && dataPackage.surveys) || []);
      if (!surveys || surveys.length === 0) return 55;

      function getQScore(qid, colOverride) {
        const s = surveys.find(x => 
          (x.program === 'CLSS' || (typeof activeProgram !== 'undefined' && x.program === activeProgram)) && 
          (String(x.questionId) === String(qid) || String(x.questionId).replace('Q', '') === String(qid))
        );
        if (!s || !s.districtData) return 55;
        const row = s.districtData.find(d => d.district === dname);
        if (!row) return 55;
        const tot = row.totalRespondents || 1;

        if (colOverride && row[colOverride] !== undefined) {
          return (row[colOverride] / tot) * 100;
        }

        const corrCol = s.columns ? s.columns.find(c => c.isCorrect) : null;
        let val = 0;
        if (corrCol && row[corrCol.code] !== undefined) {
          val = row[corrCol.code];
        } else if (String(qid) === '84' && row['Q84.1'] !== undefined) {
          val = row['Q84.1'];
        } else if (String(qid) === '178' && row['Q178.2'] !== undefined) {
          val = row['Q178.2'];
        } else {
          val = row['Q' + qid + '.1'] || row[qid + '.1'] || row[qid + '_Correct'] || 0;
        }
        return (val / tot) * 100;
      }

      if (currentCycle === 'SEP') {
        const p177 = getQScore('177', 'Q177.1');
        const p178 = getQScore('178', 'Q178.2');
        const p179 = getQScore('179', 'Q179.1');
        const p82 = getQScore('82', 'Q82.1');
        return Math.round((p177 + p178 + p179 + p82) / 4);
      } else {
        const p82 = getQScore('82', 'Q82.1');
        const p84 = getQScore('84', 'Q84.1');
        const p95 = getQScore('95', 'Q95.2');
        const p96 = getQScore('96', 'Q96.1');
        const p97 = getQScore('97', 'Q97.1');
        return Math.round((p82 + p84 + p95 + p96 + p97) / 5);
      }
    }

    function getDistrictQuadrantInfo(turnout, pedScore) {
      if (turnout >= TURNOUT_BENCHMARK && pedScore >= PEDAGOGY_BENCHMARK) {
        return {
          quad: 'Q1',
          label: 'Q1: Benchmark Champion',
          color: 'var(--accent-emerald)',
          bgChip: 'background: rgba(5, 150, 105, 0.12); color: var(--accent-emerald); border: 1px solid rgba(5, 150, 105, 0.3);',
          action: 'Document & scale peer dialogue best practices'
        };
      } else if (turnout >= TURNOUT_BENCHMARK && pedScore < PEDAGOGY_BENCHMARK) {
        return {
          quad: 'Q2',
          label: 'Q2: Scale, Pedagogy Gap',
          color: 'var(--peepul-teal)',
          bgChip: 'background: rgba(0, 138, 171, 0.12); color: var(--peepul-teal); border: 1px solid rgba(0, 138, 171, 0.3);',
          action: 'Conduct targeted refresher on core competencies'
        };
      } else if (turnout < TURNOUT_BENCHMARK && pedScore >= PEDAGOGY_BENCHMARK) {
        return {
          quad: 'Q3',
          label: 'Q3: Mobilization Need',
          color: 'var(--accent-indigo)',
          bgChip: 'background: rgba(79, 70, 229, 0.12); color: var(--accent-indigo); border: 1px solid rgba(79, 70, 229, 0.3);',
          action: 'Drive teacher attendance & CAC monitoring'
        };
      } else {
        return {
          quad: 'Q4',
          label: 'Q4: Priority Support Zone',
          color: 'var(--accent-rose)',
          bgChip: 'background: rgba(220, 38, 38, 0.12); color: var(--accent-rose); border: 1px solid rgba(220, 38, 38, 0.3);',
          action: 'Urgent administrative resolution & CAC appointment'
        };
      }
    }

    function populateQuadrantBentoCards() {
      const q1Container = document.getElementById('q1Chips');
      const q2Container = document.getElementById('q2Chips');
      const q3Container = document.getElementById('q3Chips');
      const q4Container = document.getElementById('q4Chips');

      if (!q1Container || !q2Container || !q3Container || !q4Container) return;

      q1Container.innerHTML = '';
      q2Container.innerHTML = '';
      q3Container.innerHTML = '';
      q4Container.innerHTML = '';

      let c1 = 0, c2 = 0, c3 = 0, c4 = 0;
      const dists = (typeof getActiveCycleSummary === 'function') ? getActiveCycleSummary() : ((dataPackage && dataPackage.districtSummary) || []);

      dists.forEach(d => {
        const ped = calculateDistrictPedagogyScore(d.district);
        const t = d.attendees;
        const qInfo = getDistrictQuadrantInfo(t, ped);

        let targetCont = q4Container;
        if (qInfo.quad === 'Q1') { targetCont = q1Container; c1++; }
        else if (qInfo.quad === 'Q2') { targetCont = q2Container; c2++; }
        else if (qInfo.quad === 'Q3') { targetCont = q3Container; c3++; }
        else { targetCont = q4Container; c4++; }

        const chip = document.createElement('span');
        chip.style.cssText = `${qInfo.bgChip} font-size: 10.5px; font-weight: 600; padding: 3px 7px; border-radius: 4px; cursor: pointer; white-space: nowrap; transition: transform 0.15s ease;`;
        chip.title = `${d.district}: Turnout = ${t.toLocaleString()} teachers | Pedagogy Accuracy = ${ped}%. Click to view 360 profile.`;
        chip.innerHTML = `${d.district} <span style="opacity: 0.75; font-size: 9.5px;">(${t.toLocaleString()})</span>`;
        chip.onclick = () => openDistrictIn360(d.district);
        targetCont.appendChild(chip);
      });

      // Dynamically update card badges and slicer button counts
      const b1 = document.getElementById('q1Badge'); if (b1) b1.innerText = `${c1} Districts`;
      const b2 = document.getElementById('q2Badge'); if (b2) b2.innerText = `${c2} Districts`;
      const b3 = document.getElementById('q3Badge'); if (b3) b3.innerText = `${c3} Districts`;
      const b4 = document.getElementById('q4Badge'); if (b4) b4.innerText = `${c4} Districts`;

      const btn1 = document.getElementById('q1BtnCount'); if (btn1) btn1.innerText = `${c1}`;
      const btn2 = document.getElementById('q2BtnCount'); if (btn2) btn2.innerText = `${c2}`;
      const btn3 = document.getElementById('q3BtnCount'); if (btn3) btn3.innerText = `${c3}`;
      const btn4 = document.getElementById('q4BtnCount'); if (btn4) btn4.innerText = `${c4}`;
    }

    function initQuadrantTable() {
      populateQuadrantBentoCards();
      if (typeof initResearchTab === 'function') initResearchTab();

      const tbody = document.querySelector('#quadrantDistTable tbody');
      if (!tbody) return;
      tbody.innerHTML = '';

      let idx = 1;
      const dists = (typeof getActiveCycleSummary === 'function') ? getActiveCycleSummary() : ((dataPackage && dataPackage.districtSummary) || []);

      const filtered = dists.filter(d => {
        const pedScore = calculateDistrictPedagogyScore(d.district);
        const turnout = d.attendees;
        const qInfo = getDistrictQuadrantInfo(turnout, pedScore);
        return (currentQuadFilter === 'ALL' || qInfo.quad === currentQuadFilter);
      });

      filtered.forEach(d => {
        const pedScore = calculateDistrictPedagogyScore(d.district);
        const turnout = d.attendees;
        const avgPerCluster = d.totalClusters > 0 ? (d.attendees / d.totalClusters).toFixed(1) : '-';
        const qInfo = getDistrictQuadrantInfo(turnout, pedScore);

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td class="font-mono">${idx++}</td>
          <td><strong style="color: var(--text-primary); cursor: pointer;" onclick="openDistrictIn360('${d.district}')">${d.district}</strong></td>
          <td><span style="color: ${qInfo.color}; font-weight: 700; font-size: 11px; background: rgba(0,0,0,0.03); padding: 3px 7px; border-radius: 4px; border: 1px solid var(--border-hairline);">${qInfo.label}</span></td>
          <td class="font-mono" style="color: var(--peepul-blue); font-weight: 700;">${turnout.toLocaleString()}</td>
          <td class="font-mono" style="color: ${pedScore >= PEDAGOGY_BENCHMARK ? 'var(--accent-emerald)' : 'var(--accent-rose)'}; font-weight: 700;">${pedScore}%</td>
          <td class="font-mono">${d.totalBlocks}</td>
          <td class="font-mono">${d.totalClusters}</td>
          <td class="font-mono">${avgPerCluster}</td>
          <td style="font-size: 11px; color: var(--text-secondary); max-width: 260px;">${qInfo.action}</td>
          <td style="text-align: right;"><button class="slicer-btn" style="padding: 2px 8px; font-size: 10.5px;" onclick="openDistrictIn360('${d.district}')">View 360°</button></td>
        `;
        tbody.appendChild(tr);
      });
    }

    function filterQuadrant(q) {
      currentQuadFilter = q;
      document.querySelectorAll('#btnQuadAll, #btnQuad1, #btnQuad2, #btnQuad3, #btnQuad4').forEach(b => b.classList.remove('active'));
      if (q === 'ALL') document.getElementById('btnQuadAll').classList.add('active');
      else if (q === 'Q1') document.getElementById('btnQuad1').classList.add('active');
      else if (q === 'Q2') document.getElementById('btnQuad2').classList.add('active');
      else if (q === 'Q3') document.getElementById('btnQuad3').classList.add('active');
      else if (q === 'Q4') document.getElementById('btnQuad4').classList.add('active');

      const cardMap = { 'Q1': 'cardQuad1', 'Q2': 'cardQuad2', 'Q3': 'cardQuad3', 'Q4': 'cardQuad4' };
      ['cardQuad1', 'cardQuad2', 'cardQuad3', 'cardQuad4'].forEach(cid => {
        const el = document.getElementById(cid);
        if (el) {
          el.style.transform = 'scale(1)';
          el.style.boxShadow = 'none';
        }
      });
      if (cardMap[q]) {
        const activeCard = document.getElementById(cardMap[q]);
        if (activeCard) {
          activeCard.style.transform = 'scale(1.02)';
          activeCard.style.boxShadow = '0 8px 24px -4px rgba(0, 138, 171, 0.25), inset 0 0 0 2px var(--peepul-teal)';
        }
      }

      const dists = (typeof getActiveCycleSummary === 'function') ? getActiveCycleSummary() : ((dataPackage && dataPackage.districtSummary) || []);
      const countMap = {
        'ALL': dists.length,
        'Q1': dists.filter(d => getDistrictQuadrantInfo(d.attendees, calculateDistrictPedagogyScore(d.district)).quad === 'Q1').length,
        'Q2': dists.filter(d => getDistrictQuadrantInfo(d.attendees, calculateDistrictPedagogyScore(d.district)).quad === 'Q2').length,
        'Q3': dists.filter(d => getDistrictQuadrantInfo(d.attendees, calculateDistrictPedagogyScore(d.district)).quad === 'Q3').length,
        'Q4': dists.filter(d => getDistrictQuadrantInfo(d.attendees, calculateDistrictPedagogyScore(d.district)).quad === 'Q4').length,
      };

      const quadTitleMap = {
        'ALL': `All ${dists.length} Districts`,
        'Q1': `Q1: Benchmark Champions (${countMap.Q1} Districts)`,
        'Q2': `Q2: High Attendance, Needs Pedagogy Focus (${countMap.Q2} Districts)`,
        'Q3': `Q3: High Score, Needs Attendance Boost (${countMap.Q3} Districts)`,
        'Q4': `Q4: Priority Support Zone (${countMap.Q4} Districts)`
      };
      const titleEl = document.getElementById('quadrantTableTitle');
      if (titleEl) {
        titleEl.innerText = `Districts in Selected Quadrant: ${quadTitleMap[q] || `All ${dists.length} Districts`}`;
      }

      initQuadrantTable();
    }

    function filterQuadrantTableSearch() {
      const q = document.getElementById('quadSearchInput').value.toLowerCase();
      document.querySelectorAll('#quadrantDistTable tbody tr').forEach(tr => {
        tr.style.display = tr.innerText.toLowerCase().includes(q) ? '' : 'none';
      });
    }

    '''

    content = content[:target_start] + new_js + content[target_end:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated RSK_Master_CLSS_Executive_Studio_Enhanced.html successfully!')

    # Sync to index.html and deploy/index.html
    for dest in ['index.html', 'deploy/index.html', 'RSK_Master_CLSS_Executive_Dashboard.html']:
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Synced to {dest} successfully!')

if __name__ == '__main__':
    main()
