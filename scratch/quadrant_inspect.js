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

      dataPackage.districtSummary.forEach(d => {
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
        chip.innerHTML = `${d.district} <span style="opacity: 0.85; font-family: var(--font-mono); font-size: 9.5px; font-weight: 700;">(${t})</span>`;
        chip.onmouseenter = () => { chip.style.transform = 'scale(1.05)'; };
        chip.onmouseleave = () => { chip.style.transform = 'scale(1)'; };
        chip.onclick = (e) => {
          e.stopPropagation();
          openDistrictIn360(d.district);
        };
        targetCont.appendChild(chip);
      });

      document.getElementById('q1Badge').innerText = `${c1} Districts`;
      document.getElementById('q2Badge').innerText = `${c2} Districts`;
      document.getElementById('q3Badge').innerText = `${c3} Districts`;
      document.getElementById('q4Badge').innerText = `${c4} Districts`;

      if (document.getElementById('q1BtnCount')) document.getElementById('q1BtnCount').innerText = c1;
      if (document.getElementById('q2BtnCount')) document.getElementById('q2BtnCount').innerText = c2;
      if (document.getElementById('q3BtnCount')) document.getElementById('q3BtnCount').innerText = c3;
      if (document.getElementById('q4BtnCount')) document.getElementById('q4BtnCount').innerText = c4;
    }

    function initQuadrantTable() {
      populateQuadrantBentoCards();

      const tbody = document.querySelector('#quadrantDistTable tbody');
      if (!tbody) return;
      tbody.innerHTML = '';

      let idx = 1;
      dataPackage.districtSummary.forEach(d => {
        const pedScore = calculateDistrictPedagogyScore(d.district);
        const turnout = d.attendees;
        const avgPerCluster = d.totalClusters > 0 ? (d.attendees / d.totalClusters).toFixed(1) : '-';
        const qInfo = getDistrictQuadrantInfo(turnout, pedScore);

        if (currentQuadFilter !== 'ALL' && qInfo.quad !== currentQuadFilter) return;

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
          <td style="font-size: 11.5px; color: var(--text-secondary);">${qInfo.action}</td>
        `;
        tbody.appendChild(tr);
      });
    }

    