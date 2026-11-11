/**
 * RSK Madhya Pradesh - Teacher Performance & Support Engine
 * High-performance, client-side diagnostics and coaching recommendations
 * Built for 33,866 teachers across 52 districts and 320 blocks.
 */

(function() {
  'use strict';

  // Module State
  let diagnosticsData = null;
  let allTeachers = [];
  let filteredTeachers = [];
  let currentPage = 1;
  const pageSize = 20;
  let activeTeacherCode = null;
  let searchDebounceTimer = null;
  let currentTierFilter = 'ALL';
  let isInitialized = false;

  // Question Descriptions and Best Practices Dictionary
  const PEDAGOGY_BENCHMARKS = {
    TLM_CYCLE: {
      qNum: 'Q177',
      domainEn: 'Concrete to Abstract Learning (TLM)',
      domainHi: 'मूर्त से अमूर्त शिक्षण (TLM चक्र)',
      bestPracticeEn: 'Provide concrete experience with learning materials, followed by student reflection and concept consolidation.',
      bestPracticeHi: 'बच्चों को पहले सामग्री के साथ मूर्त अनुभव दें, फिर उस पर चिंतन कराएं और अंत में अवधारणा का समेकन करें।',
      misconceptionEn: 'Treating TLM as a decorative display or lecture prop held by the teacher rather than student-handled tools.',
      misconceptionHi: 'TLM को बच्चों के हाथों में देने के बजाय शिक्षक द्वारा केवल प्रदर्शन या सजावट की वस्तु समझना।'
    },
    PROBING: {
      qNum: 'Q178',
      domainEn: 'Inquiry & Probing Questions',
      domainHi: 'सटीक एवं विचारोत्तेजक प्रश्न पूछना',
      bestPracticeEn: 'When a student answers incorrectly, pause and ask probing questions to uncover their thinking rather than giving the answer.',
      bestPracticeHi: 'गलत उत्तर मिलने पर तुरंत सही उत्तर न बताएं, बल्कि पूरक प्रश्न पूछकर बच्चे की सोच और तर्क को बाहर लाएं।',
      misconceptionEn: 'Immediate answer dictation: providing the right answer right away so the lesson proceeds faster.',
      misconceptionHi: 'तुरंत सही उत्तर बता देना ताकि पाठ तेजी से आगे बढ़ सके, जिससे बच्चे की सोचने की प्रक्रिया रुक जाती है।'
    },
    SAFETY: {
      qNum: 'Q96',
      domainEn: 'Psychological Safety & Mistakes',
      domainHi: 'भयमुक्त वातावरण एवं गलतियों का स्वागत',
      bestPracticeEn: 'Treat mistakes as normal and essential learning steps; guide students to discover corrections independently.',
      bestPracticeHi: 'गलतियों को सीखने का स्वाभाविक हिस्सा मानें और बच्चों को संकेत देकर स्वयं सुधार करने के लिए प्रेरित करें।',
      misconceptionEn: 'Ignoring or scolding errors, which makes children hesitant to participate in classroom discussions.',
      misconceptionHi: 'गलतियों पर डांटना या उन्हें अनदेखा करना, जिससे बच्चे कक्षा में बोलने से डरने लगते हैं।'
    },
    BELONGING: {
      qNum: 'Q97',
      domainEn: 'Classroom Belonging & Participation',
      domainHi: 'कक्षा में अपनापन एवं सबकी सहभागिता',
      bestPracticeEn: 'Involve every student in genuine classroom tasks and active pair work, not just the front-bench fast learners.',
      bestPracticeHi: 'केवल आगे बैठने वाले होशियार बच्चों को नहीं, बल्कि हर बच्चे को कक्षा की वास्तविक जिम्मेदारियों और समूह कार्य में जोड़ना।',
      misconceptionEn: 'Surface Praise: showering praise only on quick responders while shy or back-bench students remain passive.',
      misconceptionHi: 'केवल जल्दी उत्तर देने वाले 2-3 बच्चों की तारीफ करना, जबकि बाकी बच्चे मूकदर्शक बने रहें।'
    },
    PURPOSE: {
      qNum: 'Q82',
      domainEn: 'Shaikshik Samwaad Purpose & Culture',
      domainHi: 'शैक्षिक संवाद का मूल उद्देश्य एवं संस्कृति',
      bestPracticeEn: 'Shaikshik Samwaad is a platform for peer academic exchange, collective problem-solving, and professional growth.',
      bestPracticeHi: 'शैक्षिक संवाद साथी शिक्षकों के साथ अकादमिक विमर्श, शिक्षण चुनौतियों के साझा समाधान और सीखने का मंच है।',
      misconceptionEn: 'Treating Samwaad as administrative reporting or ritual attendance.',
      misconceptionHi: 'संवाद को केवल औपचारिकता या प्रशासनिक बैठक समझना।'
    }
  };

  /**
   * Initialize Tab Data & Controls
   */
  window.initTeacherDiagnosticsTab = function() {
    if (isInitialized && allTeachers.length > 0) return;

    // Check if data is preloaded via script tag
    if (window.TEACHER_DIAGNOSTICS_DATA) {
      loadDataPayload(window.TEACHER_DIAGNOSTICS_DATA);
    } else {
      // Lazy fetch from compact JSON file
      const statusEl = document.getElementById('teacherLoadStatus');
      if (statusEl) statusEl.innerText = 'Loading teacher dataset (33,866 records)...';
      
      fetch('data/teacher_diagnostics_compact.json')
        .then(response => {
          if (!response.ok) throw new Error('Network error loading teacher diagnostics');
          return response.json();
        })
        .then(data => {
          loadDataPayload(data);
        })
        .catch(err => {
          console.error('Failed to load teacher diagnostics:', err);
          if (statusEl) {
            statusEl.innerHTML = '<span style="color: var(--accent-rose);">Dataset file not found. Please run the DuckDB pipeline first.</span>';
          }
        });
    }
  };

  /**
   * Parse Compact Payload into Searchable Records
   */
  function loadDataPayload(payload) {
    diagnosticsData = payload;
    const districts = payload.districts || [];
    const blocks = payload.blocks || [];
    const opt178 = payload.opt178 || [];
    const opt177 = payload.opt177 || [];
    const opt95 = payload.opt95 || [];
    const opt97 = payload.opt97 || [];

    // Map 2D compact array into structured objects
    allTeachers = payload.teachers.map((row, idx) => {
      const code = row[0];
      const name = row[1];
      const distName = districts[row[2]] || 'Unknown';
      const blockName = blocks[row[3]] || 'Unknown';
      const clusterName = row[4] || '';
      const cycle = row[5] || 'AUG';
      const augScore = row[6] !== null ? Number(row[6]) : null;
      const sepScore = row[7] !== null ? Number(row[7]) : null;
      const overallScore = Number(row[8]);
      const tier = row[9];
      const gaps = row[10] ? row[10].split(',').filter(Boolean) : [];
      const text178 = opt178[row[11]] || '';
      const text177 = opt177[row[12]] || '';
      const text95 = opt95[row[13]] || '';
      const text97 = opt97[row[14]] || '';
      const trustScore = row[15] !== undefined ? Number(row[15]) : 100.0;

      return {
        id: idx,
        c: code,
        n: name,
        d: distName,
        b: blockName,
        cl: clusterName,
        cy: cycle,
        as: augScore,
        ss: sepScore,
        sc: overallScore,
        tr: trustScore,
        t: tier,
        g: gaps,
        t178: text178,
        t177: text177,
        t95: text95,
        t97: text97,
        // Pre-computed lowercase search tokens for ultra-fast filtering
        searchToken: (code + ' ' + name).toLowerCase()
      };
    });

    isInitialized = true;
    populateFilterDropdowns();
    renderSummaryMetrics();
    applyTeacherFilters();

    // Select first teacher automatically
    if (allTeachers.length > 0) {
      selectTeacherProfile(allTeachers[0].c);
    }
  }

  /**
   * Render Top Summary Bento KPI Metrics
   */
  function renderSummaryMetrics() {
    const summary = diagnosticsData.summary || {};
    const total = summary.totalTeachers || allTeachers.length || 33866;
    const champ = summary.champions || 11143;
    const prof = summary.proficient || 19570;
    const dev = summary.developing || 3033;
    const supp = summary.prioritySupport || 120;
    const avgScore = summary.avgScore || 76.4;
    const persistent = summary.persistent || 13088;

    const elTotal = document.getElementById('tdKpiTotal');
    const elChamp = document.getElementById('tdKpiChampions');
    const elProf = document.getElementById('tdKpiProficient');
    const elDev = document.getElementById('tdKpiDeveloping');
    const elSupp = document.getElementById('tdKpiSupport');
    const elAvg = document.getElementById('tdKpiAvgScore');

    if (elTotal) elTotal.innerText = Number(total).toLocaleString();
    if (elChamp) elChamp.innerHTML = `${Number(champ).toLocaleString()} <span style="font-size: 13px; font-weight: 500; color: var(--text-muted);">(${(champ*100/total).toFixed(1)}%)</span>`;
    if (elProf) elProf.innerHTML = `${Number(prof).toLocaleString()} <span style="font-size: 13px; font-weight: 500; color: var(--text-muted);">(${(prof*100/total).toFixed(1)}%)</span>`;
    if (elDev) elDev.innerHTML = `${Number(dev).toLocaleString()} <span style="font-size: 13px; font-weight: 500; color: var(--text-muted);">(${(dev*100/total).toFixed(1)}%)</span>`;
    if (elSupp) elSupp.innerHTML = `${Number(supp).toLocaleString()} <span style="font-size: 13px; font-weight: 500; color: var(--text-muted);">(${(supp*100/total).toFixed(1)}%)</span>`;
    if (elAvg) elAvg.innerHTML = `${avgScore}% <span style="font-size: 13px; font-weight: 500; color: var(--text-muted);">(${Number(persistent).toLocaleString()} persistent)</span>`;
  }

  /**
   * Populate District and Block Selectors
   */
  function populateFilterDropdowns() {
    const distSelect = document.getElementById('tdDistrictSelect');
    if (!distSelect || !diagnosticsData) return;

    distSelect.innerHTML = '<option value="ALL">All 52 Districts (सभी 52 जिले)</option>';
    (diagnosticsData.districts || []).forEach(d => {
      const opt = document.createElement('option');
      opt.value = d;
      opt.textContent = d;
      distSelect.appendChild(opt);
    });

    updateBlockDropdown();
  }

  window.updateBlockDropdown = function() {
    const distSelect = document.getElementById('tdDistrictSelect');
    const blockSelect = document.getElementById('tdBlockSelect');
    if (!distSelect || !blockSelect || !diagnosticsData) return;

    const selectedDist = distSelect.value;
    blockSelect.innerHTML = '<option value="ALL">All Blocks (सभी ब्लॉक)</option>';

    let availableBlocks = [];
    if (selectedDist === 'ALL') {
      availableBlocks = diagnosticsData.blocks || [];
    } else {
      const set = new Set();
      allTeachers.forEach(t => {
        if (t.d === selectedDist) set.add(t.b);
      });
      availableBlocks = Array.from(set).sort();
    }

    availableBlocks.forEach(b => {
      const opt = document.createElement('option');
      opt.value = b;
      opt.textContent = b;
      blockSelect.appendChild(opt);
    });

    applyTeacherFilters();
  };

  /**
   * Tier Pill Filter Handler
   */
  window.setTeacherTierFilter = function(tier, btnEl) {
    currentTierFilter = tier;
    document.querySelectorAll('.td-tier-pill').forEach(btn => btn.classList.remove('active'));
    if (btnEl) btnEl.classList.add('active');
    applyTeacherFilters();
  };

  /**
   * Search Input Debounce (150ms)
   */
  window.debouncedTeacherSearch = function() {
    clearTimeout(searchDebounceTimer);
    searchDebounceTimer = setTimeout(() => {
      applyTeacherFilters();
    }, 150);
  };

  /**
   * Master Filtering Function
   */
  function applyTeacherFilters() {
    const t0 = performance.now();
    const searchInput = document.getElementById('tdSearchInput');
    const query = searchInput ? searchInput.value.trim().toLowerCase() : '';
    const distSelect = document.getElementById('tdDistrictSelect');
    const selectedDist = distSelect ? distSelect.value : 'ALL';
    const blockSelect = document.getElementById('tdBlockSelect');
    const selectedBlock = blockSelect ? blockSelect.value : 'ALL';

    filteredTeachers = allTeachers.filter(t => {
      // Tier match
      if (currentTierFilter !== 'ALL' && t.t !== currentTierFilter) {
        return false;
      }
      // District match
      if (selectedDist !== 'ALL' && t.d !== selectedDist) {
        return false;
      }
      // Block match
      if (selectedBlock !== 'ALL' && t.b !== selectedBlock) {
        return false;
      }
      // Search query match (Code or Name)
      if (query && !t.searchToken.includes(query)) {
        return false;
      }
      return true;
    });

    const elapsed = (performance.now() - t0).toFixed(1);
    currentPage = 1;
    renderTeacherTable();
    updateResultMetrics(elapsed);
  }

  window.clearTeacherFilters = function() {
    const searchInput = document.getElementById('tdSearchInput');
    if (searchInput) searchInput.value = '';
    const distSelect = document.getElementById('tdDistrictSelect');
    if (distSelect) distSelect.value = 'ALL';
    window.setTeacherTierFilter('ALL', document.querySelector('.td-tier-pill[data-tier="ALL"]'));
    window.updateBlockDropdown();
  };

  /**
   * Render Filter Status Metric Bar
   */
  function updateResultMetrics(elapsedMs) {
    const countEl = document.getElementById('tdFilteredCount');
    if (countEl) {
      const isHi = (window.currentLang === 'hi');
      const totalCount = allTeachers.length;
      const filteredCount = filteredTeachers.length;
      countEl.innerHTML = isHi
        ? `कुल <strong>${totalCount.toLocaleString()}</strong> में से <strong>${filteredCount.toLocaleString()}</strong> शिक्षक प्रदर्शित (${elapsedMs} मिलीसेकंड में)`
        : `Showing <strong>${filteredCount.toLocaleString()}</strong> of <strong>${totalCount.toLocaleString()}</strong> teachers (filtered in ${elapsedMs}ms)`;
    }
  }

  /**
   * Render Paginated Table (20 items)
   */
  function renderTeacherTable() {
    const tbody = document.getElementById('tdTeacherTableBody');
    if (!tbody) return;

    if (filteredTeachers.length === 0) {
      const isHi = (window.currentLang === 'hi');
      tbody.innerHTML = `
        <tr>
          <td colspan="7" style="text-align: center; padding: 36px 16px; color: var(--text-muted);">
            <div style="font-size: 28px; margin-bottom: 8px;">🔍</div>
            <div style="font-weight: 700; font-size: 14px; color: var(--text-secondary);">
              ${isHi ? 'कोई शिक्षक नहीं मिला' : 'No matching teachers found'}
            </div>
            <div style="font-size: 12px; margin-top: 4px;">
              ${isHi ? 'कृपया खोज शब्द या जिला/ब्लॉक फ़िल्टर बदलकर पुनः प्रयास करें।' : 'Try modifying your search code, name, or filter criteria.'}
            </div>
          </td>
        </tr>
      `;
      renderPaginationControls(0);
      return;
    }

    const startIdx = (currentPage - 1) * pageSize;
    const pageItems = filteredTeachers.slice(startIdx, startIdx + pageSize);

    let html = '';
    pageItems.forEach((t, index) => {
      const isSelected = (t.c === activeTeacherCode);
      const rowNum = startIdx + index + 1;
      const tierBadge = getTierBadge(t.t);
      const cycleBadge = getCycleBadge(t.cy);

      html += `
        <tr class="td-teacher-row ${isSelected ? 'selected' : ''}" onclick="selectTeacherProfile('${t.c}')" style="cursor: pointer; transition: background 0.15s ease;">
          <td style="padding: 10px 12px; font-size: 11px; font-family: var(--font-mono); color: var(--text-muted); text-align: center;">${rowNum}</td>
          <td style="padding: 10px 12px;">
            <div style="font-weight: 700; font-size: 13px; color: var(--text-primary);">${escapeHtml(t.n)}</div>
            <div style="font-size: 11px; font-family: var(--font-mono); color: var(--peepul-teal); font-weight: 600; margin-top: 2px;">${t.c}</div>
          </td>
          <td style="padding: 10px 12px; font-size: 12px; color: var(--text-secondary);">
            <div style="font-weight: 600;">${escapeHtml(t.d)}</div>
            <div style="font-size: 11px; color: var(--text-muted);">${escapeHtml(t.b)}</div>
          </td>
          <td style="padding: 10px 12px; text-align: center;">${cycleBadge}</td>
          <td style="padding: 10px 12px; text-align: right; font-family: var(--font-mono); font-weight: 700; font-size: 13px;">
            <span style="color: ${getScoreColor(t.sc)};">${t.sc.toFixed(1)}%</span>
          </td>
          <td style="padding: 10px 12px; text-align: center;">${tierBadge}</td>
          <td style="padding: 10px 12px; text-align: center;">
            <button class="td-action-btn" onclick="event.stopPropagation(); selectTeacherProfile('${t.c}')" style="padding: 4px 10px; font-size: 11px; border-radius: 6px; border: 1px solid var(--border-subtle); background: var(--bg-surface-2); font-weight: 700; color: var(--peepul-teal); cursor: pointer;">
              ${window.currentLang === 'hi' ? 'निदान देखें' : 'View Dossier'}
            </button>
          </td>
        </tr>
      `;
    });

    tbody.innerHTML = html;
    renderPaginationControls(filteredTeachers.length);
  }

  /**
   * Pagination Controls
   */
  function renderPaginationControls(totalItems) {
    const totalPages = Math.ceil(totalItems / pageSize) || 1;
    const container = document.getElementById('tdPaginationControls');
    if (!container) return;

    const isHi = (window.currentLang === 'hi');
    const startNum = totalItems === 0 ? 0 : (currentPage - 1) * pageSize + 1;
    const endNum = Math.min(currentPage * pageSize, totalItems);

    container.innerHTML = `
      <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; padding: 12px 16px; border-top: 1px solid var(--border-subtle); background: var(--bg-surface-1);">
        <div style="font-size: 12px; color: var(--text-muted);">
          ${isHi ? `<strong>${startNum} - ${endNum}</strong> (कुल <strong>${totalItems.toLocaleString()}</strong> में से)` : `Showing <strong>${startNum} - ${endNum}</strong> of <strong>${totalItems.toLocaleString()}</strong>`}
        </div>
        <div style="display: flex; align-items: center; gap: 6px;">
          <button class="td-page-btn" ${currentPage <= 1 ? 'disabled style="opacity: 0.4; cursor: not-allowed;"' : ''} onclick="changeTeacherPage(${currentPage - 1})">
            ◀ ${isHi ? 'पिछला' : 'Prev'}
          </button>
          <span style="font-size: 12px; font-weight: 700; padding: 0 8px; font-family: var(--font-mono);">
            ${currentPage} / ${totalPages}
          </span>
          <button class="td-page-btn" ${currentPage >= totalPages ? 'disabled style="opacity: 0.4; cursor: not-allowed;"' : ''} onclick="changeTeacherPage(${currentPage + 1})">
            ${isHi ? 'अगला' : 'Next'} ▶
          </button>
        </div>
      </div>
    `;
  }

  window.changeTeacherPage = function(newPage) {
    const totalPages = Math.ceil(filteredTeachers.length / pageSize) || 1;
    if (newPage < 1 || newPage > totalPages) return;
    currentPage = newPage;
    renderTeacherTable();
    // Scroll roster table smoothly to top
    const wrapper = document.getElementById('tdRosterWrapper');
    if (wrapper) wrapper.scrollTop = 0;
  };

  /**
   * Select a Teacher & Render Full Right-Pane Dossier
   */
  window.selectTeacherProfile = function(empCode) {
    activeTeacherCode = empCode;
    const teacher = allTeachers.find(t => t.c === empCode);
    if (!teacher) return;

    // Highlight row in left table
    document.querySelectorAll('.td-teacher-row').forEach(r => r.classList.remove('selected'));
    const rows = document.querySelectorAll('.td-teacher-row');
    rows.forEach(r => {
      if (r.innerHTML.includes(empCode)) r.classList.add('selected');
    });

    renderTeacherDossier(teacher);
  };

  /**
   * Render Active Teacher Dossier and Qwen Coaching Prescription
   */
  function renderTeacherDossier(teacher) {
    const dossierPane = document.getElementById('tdActiveDossierPane');
    if (!dossierPane) return;

    const isHi = (window.currentLang === 'hi');
    const tierBadge = getTierBadge(teacher.t, true);
    const cycleBadge = getCycleBadge(teacher.cy, true);
    const scoreColor = getScoreColor(teacher.sc);

    // Pedagogical strengths & diagnosed gaps
    const masteredList = [];
    const gapsList = [];

    ['TLM_CYCLE', 'PROBING', 'SAFETY', 'BELONGING', 'PURPOSE'].forEach(k => {
      const benchmark = PEDAGOGY_BENCHMARKS[k];
      if (teacher.g.includes(k)) {
        gapsList.push(benchmark);
      } else {
        masteredList.push(benchmark);
      }
    });

    // Generate Qwen Mentor Prescription based on exact tier & identified gaps
    const prescription = generateQwenPrescription(teacher, isHi);

    dossierPane.innerHTML = `
      <div style="background: var(--bg-surface-card); border: 1.5px solid var(--border-subtle); border-radius: var(--radius-md); box-shadow: var(--shadow-ambient); overflow: hidden;">
        
        <!-- Dossier Header -->
        <div style="padding: 18px 22px; background: linear-gradient(135deg, rgba(0, 138, 171, 0.08), rgba(99, 208, 223, 0.03)); border-bottom: 1.5px solid var(--border-hairline);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 14px; flex-wrap: wrap;">
            <div>
              <div style="display: flex; align-items: center; gap: 8px;">
                <h3 style="margin: 0; font-size: 18px; font-weight: 800; color: var(--text-primary); font-family: var(--font-editorial);">${escapeHtml(teacher.n)}</h3>
                ${tierBadge}
              </div>
              <div style="display: flex; align-items: center; gap: 12px; margin-top: 6px; font-size: 12px; color: var(--text-muted); flex-wrap: wrap;">
                <span>ID: <strong style="font-family: var(--font-mono); color: var(--peepul-teal);">${teacher.c}</strong></span>
                <span>•</span>
                <span>${escapeHtml(teacher.d)} (${escapeHtml(teacher.b)})</span>
                <span>•</span>
                <span>${cycleBadge}</span>
              </div>
              <div style="font-size: 11px; color: var(--text-dim); margin-top: 4px;">
                ${isHi ? 'संकुल केन्द्र:' : 'Cluster Centre:'} ${escapeHtml(teacher.cl || 'N/A')}
              </div>
            </div>

            <div style="text-align: right; background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 10px 16px; box-shadow: var(--shadow-tactile);">
              <div style="font-size: 10px; font-weight: 800; letter-spacing: 0.5px; color: var(--text-muted); text-transform: uppercase;">
                ${isHi ? 'शिक्षाशास्त्र प्राप्तांक' : 'Pedagogy Score'}
              </div>
              <div style="font-size: 26px; font-weight: 900; font-family: var(--font-mono); color: ${scoreColor}; margin-top: 2px;">
                ${teacher.sc.toFixed(1)}%
              </div>
            </div>
          </div>
        </div>

        <!-- Metrics Ribbon (4 Cards) -->
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; background: var(--border-hairline); border-bottom: 1px solid var(--border-subtle);">
          <div style="background: var(--bg-surface-1); padding: 12px 14px; text-align: center;">
            <div style="font-size: 10px; font-weight: 700; color: var(--text-muted);">${isHi ? 'अगस्त प्राप्तांक' : 'August Pedagogy'}</div>
            <div style="font-size: 15px; font-weight: 800; font-family: var(--font-mono); margin-top: 4px; color: ${teacher.as !== null ? 'var(--text-primary)' : 'var(--text-dim)'};">
              ${teacher.as !== null ? teacher.as.toFixed(1) + '%' : (isHi ? 'अनुपस्थित' : 'Not Attended')}
            </div>
          </div>
          <div style="background: var(--bg-surface-1); padding: 12px 14px; text-align: center;">
            <div style="font-size: 10px; font-weight: 700; color: var(--text-muted);">${isHi ? 'सितंबर प्राप्तांक' : 'September Pedagogy'}</div>
            <div style="font-size: 15px; font-weight: 800; font-family: var(--font-mono); margin-top: 4px; color: ${teacher.ss !== null ? 'var(--text-primary)' : 'var(--text-dim)'};">
              ${teacher.ss !== null ? teacher.ss.toFixed(1) + '%' : (isHi ? 'अनुपस्थित' : 'Not Attended')}
            </div>
          </div>
          <div style="background: var(--bg-surface-1); padding: 12px 14px; text-align: center;">
            <div style="font-size: 10px; font-weight: 700; color: var(--text-muted);">${isHi ? 'उपस्थिति चक्र' : 'Attendance Cycle'}</div>
            <div style="font-size: 12px; font-weight: 800; margin-top: 4px; color: var(--peepul-teal);">
              ${teacher.cy === 'BOTH' ? (isHi ? 'दोनों सत्र' : 'Both Cycles') : (teacher.cy === 'AUG' ? (isHi ? 'केवल अगस्त' : 'August Only') : (isHi ? 'केवल सितंबर' : 'September Only'))}
            </div>
          </div>
          <div style="background: var(--bg-surface-1); padding: 12px 14px; text-align: center;">
            <div style="font-size: 10px; font-weight: 700; color: var(--text-muted);">${isHi ? 'कक्षा उपयोगिता व विश्वास' : 'Trust & Utility'}</div>
            <div style="font-size: 15px; font-weight: 800; font-family: var(--font-mono); margin-top: 4px; color: var(--peepul-indigo);">
              ${teacher.tr !== undefined ? teacher.tr.toFixed(0) + '%' : '100%'}
            </div>
          </div>
        </div>

        <div style="padding: 20px 22px; display: flex; flex-direction: column; gap: 20px;">
          
          <!-- Competency Status (Mastered vs Learning Gaps) -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
            
            <!-- Mastered Strengths -->
            <div style="background: rgba(5, 150, 105, 0.04); border: 1px solid rgba(5, 150, 105, 0.2); border-radius: 8px; padding: 14px 16px;">
              <div style="font-size: 11px; font-weight: 800; color: var(--accent-emerald); text-transform: uppercase; letter-spacing: 0.5px; display: flex; align-items: center; gap: 6px;">
                <span>✅</span> ${isHi ? 'सिद्ध शिक्षण दक्षताएं' : 'Mastered Pedagogical Strengths'} (${masteredList.length})
              </div>
              <div style="margin-top: 10px; display: flex; flex-direction: column; gap: 8px;">
                ${masteredList.length === 0 ? `<div style="font-size: 11.5px; color: var(--text-muted); font-style: italic;">${isHi ? 'प्राथमिकताएं सुधार के चरण में हैं।' : 'Focus areas in development phase.'}</div>` : ''}
                ${masteredList.map(m => `
                  <div style="font-size: 12px; color: var(--text-primary); display: flex; align-items: flex-start; gap: 8px;">
                    <span style="color: var(--accent-emerald); font-weight: 900; line-height: 1;">✓</span>
                    <div>
                      <strong>${isHi ? m.domainHi : m.domainEn}</strong>
                      <span style="font-size: 10px; font-family: var(--font-mono); color: var(--text-muted); margin-left: 4px;">(${m.qNum})</span>
                    </div>
                  </div>
                `).join('')}
              </div>
            </div>

            <!-- Focus Gaps -->
            <div style="background: rgba(220, 38, 38, 0.04); border: 1px solid rgba(220, 38, 38, 0.2); border-radius: 8px; padding: 14px 16px;">
              <div style="font-size: 11px; font-weight: 800; color: #dc2626; text-transform: uppercase; letter-spacing: 0.5px; display: flex; align-items: center; gap: 6px;">
                <span>🎯</span> ${isHi ? 'सहयोग एवं मार्गदर्शन हेतु क्षेत्र' : 'Focus Areas for Coaching'} (${gapsList.length})
              </div>
              <div style="margin-top: 10px; display: flex; flex-direction: column; gap: 8px;">
                ${gapsList.length === 0 ? `<div style="font-size: 11.5px; color: var(--accent-emerald); font-weight: 700;">🌟 ${isHi ? 'सभी प्रमुख शिक्षण मानकों में उत्कृष्ट प्रदर्शन!' : 'Full mastery achieved across core competencies!'}</div>` : ''}
                ${gapsList.map(g => `
                  <div style="font-size: 12px; color: var(--text-primary); display: flex; align-items: flex-start; gap: 8px;">
                    <span style="color: #dc2626; font-weight: 900; line-height: 1;">•</span>
                    <div>
                      <strong>${isHi ? g.domainHi : g.domainEn}</strong>
                      <span style="font-size: 10px; font-family: var(--font-mono); color: var(--text-muted); margin-left: 4px;">(${g.qNum})</span>
                      <div style="font-size: 11px; color: var(--text-secondary); margin-top: 2px;">
                        ${isHi ? g.bestPracticeHi : g.bestPracticeEn}
                      </div>
                    </div>
                  </div>
                `).join('')}
              </div>
            </div>

          </div>

          <!-- Exact Survey Responses vs Best Practice (if gaps exist) -->
          ${renderSurveyResponseDetails(teacher, isHi)}

          <!-- Qwen Field Coaching Prescription -->
          <div style="background: var(--bg-surface-2); border: 1.5px solid rgba(0, 138, 171, 0.25); border-left: 4px solid var(--peepul-teal); border-radius: 10px; padding: 18px 20px;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
              <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">📋</span>
                <h4 style="margin: 0; font-size: 14px; font-weight: 800; color: var(--peepul-teal); text-transform: uppercase; letter-spacing: 0.5px;">
                  ${isHi ? 'मार्गदर्शक एवं सीएसी हेतु कार्ययोजना (Coaching Prescription)' : 'Mentor & BRC Action Plan (Field Prescription)'}
                </h4>
              </div>
              <span style="font-size: 10.5px; font-family: var(--font-mono); background: rgba(0, 138, 171, 0.1); color: var(--peepul-teal); padding: 3px 8px; border-radius: 6px; font-weight: 700;">
                Tier: ${teacher.t}
              </span>
            </div>

            <div style="font-size: 12px; color: var(--text-secondary); line-height: 1.5; margin-bottom: 14px;">
              ${prescription.overview}
            </div>

            <div style="display: flex; flex-direction: column; gap: 10px;">
              <div style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 10px 14px;">
                <div style="font-size: 11.5px; font-weight: 800; color: var(--peepul-teal);">
                  1. ${isHi ? 'अगले स्कूल भ्रमण पर प्रत्यक्ष प्रदर्शन (Live Classroom Modeling):' : 'Live Classroom Modeling on Next Visit:'}
                </div>
                <div style="font-size: 12px; color: var(--text-primary); margin-top: 4px; line-height: 1.45;">
                  ${prescription.step1}
                </div>
              </div>

              <div style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 10px 14px;">
                <div style="font-size: 11.5px; font-weight: 800; color: var(--peepul-indigo);">
                  2. ${isHi ? 'शिक्षक के साथ संवाद सूत्र (Guiding Inquiry Question for Reflection):' : 'Guiding Inquiry Question for Reflection:'}
                </div>
                <div style="font-size: 12px; color: var(--text-primary); margin-top: 4px; line-height: 1.45; font-style: italic;">
                  "${prescription.step2}"
                </div>
              </div>

              <div style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 10px 14px;">
                <div style="font-size: 11.5px; font-weight: 800; color: var(--accent-emerald);">
                  3. ${isHi ? 'संकुल में सहकर्मी सहयोग (Peer Learning Match):' : 'Cluster Peer Learning Match:'}
                </div>
                <div style="font-size: 12px; color: var(--text-primary); margin-top: 4px; line-height: 1.45;">
                  ${prescription.step3}
                </div>
              </div>
            </div>

          </div>

        </div>

      </div>
    `;
  }

  /**
   * Render Selected Options from Survey Data
   */
  function renderSurveyResponseDetails(teacher, isHi) {
    if (!teacher.t178 && !teacher.t177 && !teacher.t95 && !teacher.t97) {
      return '';
    }

    return `
      <div style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 14px 16px;">
        <div style="font-size: 11px; font-weight: 800; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px;">
          ${isHi ? 'सर्वेक्षण में शिक्षक द्वारा चुने गए उत्तर (Survey Response Evidence)' : 'Recorded Survey Responses vs. Best Practice'}
        </div>
        <div style="display: flex; flex-direction: column; gap: 10px; font-size: 11.5px;">
          ${teacher.t178 ? `
            <div style="border-left: 3px solid ${teacher.g.includes('PROBING') ? '#dc2626' : 'var(--accent-emerald)'}; padding-left: 10px;">
              <div style="font-weight: 700; color: var(--text-primary);">Q178 (${isHi ? 'गलत उत्तर पर प्रतिक्रिया' : 'Reaction to Student Errors'}):</div>
              <div style="color: var(--text-secondary); margin-top: 2px;">
                ${isHi ? 'चुना गया विकल्प:' : 'Selected Response:'} "<em>${escapeHtml(teacher.t178)}</em>"
              </div>
            </div>
          ` : ''}

          ${teacher.t177 ? `
            <div style="border-left: 3px solid ${teacher.g.includes('TLM_CYCLE') ? '#dc2626' : 'var(--accent-emerald)'}; padding-left: 10px;">
              <div style="font-weight: 700; color: var(--text-primary);">Q177 (${isHi ? 'TLM का उपयोग चक्र' : 'TLM Utilization Cycle'}):</div>
              <div style="color: var(--text-secondary); margin-top: 2px;">
                ${isHi ? 'चुना गया विकल्प:' : 'Selected Response:'} "<em>${escapeHtml(teacher.t177)}</em>"
              </div>
            </div>
          ` : ''}

          ${teacher.t95 ? `
            <div style="border-left: 3px solid ${teacher.g.includes('TLM_CYCLE') ? '#dc2626' : 'var(--accent-emerald)'}; padding-left: 10px;">
              <div style="font-weight: 700; color: var(--text-primary);">Q95 (${isHi ? 'विद्यार्थी सहभागिता' : 'Student Agency'}):</div>
              <div style="color: var(--text-secondary); margin-top: 2px;">
                ${isHi ? 'चुना गया विकल्प:' : 'Selected Response:'} "<em>${escapeHtml(teacher.t95)}</em>"
              </div>
            </div>
          ` : ''}

          ${teacher.t97 ? `
            <div style="border-left: 3px solid ${teacher.g.includes('BELONGING') ? '#dc2626' : 'var(--accent-emerald)'}; padding-left: 10px;">
              <div style="font-weight: 700; color: var(--text-primary);">Q97 (${isHi ? 'कक्षा में अपनापन' : 'Classroom Belonging'}):</div>
              <div style="color: var(--text-secondary); margin-top: 2px;">
                ${isHi ? 'चुना गया विकल्प:' : 'Selected Response:'} "<em>${escapeHtml(teacher.t97)}</em>"
              </div>
            </div>
          ` : ''}
        </div>
      </div>
    `;
  }

  /**
   * Plain-Language Qwen Mentor Action Plan
   * Humanized, natural language; zero buzzwords, zero em dashes.
   */
  function generateQwenPrescription(teacher, isHi) {
    const tier = teacher.t;
    const gaps = teacher.g;

    if (tier === 'CHAMPION') {
      return {
        overview: isHi
          ? 'यह शिक्षक शिक्षण के मूल सिद्धांतों में पूरी तरह निपुण हैं। यह कक्षा में बच्चों को सोचने और करके सीखने के भरपूर अवसर प्रदान करते हैं। इनका उपयोग संकुल स्तर पर अन्य शिक्षकों के मार्गदर्शन हेतु करें।'
          : 'This teacher demonstrates outstanding pedagogical mastery across purpose, concrete materials, inquiry questioning, and student belonging. Position them as a lead peer practitioner across their cluster.',
        step1: isHi
          ? 'आगामी संकुल शैक्षिक संवाद में इस शिक्षक को 15 मिनट का लाइव शिक्षण प्रदर्शन प्रस्तुत करने के लिए आमंत्रित करें, ताकि अन्य शिक्षक देख सकें कि बच्चों से विचारोत्तेजक प्रश्न कैसे पूछे जाते हैं।'
          : 'Invite this teacher to deliver a 15-minute live demonstration during the upcoming Cluster Shaikshik Samwaad, showing how probing questions spark genuine student dialogue.',
        step2: isHi
          ? 'आपने अपनी कक्षा में बच्चों को गलतियों से सीखने के लिए इतना सहज कैसे बनाया? क्या इसका कोई उदाहरण आप साथी शिक्षकों के साथ साझा कर सकते हैं?'
          : 'How do you structure classroom discussions so children feel safe admitting mistakes? Could you share a quick example of a student breakthrough with other teachers?',
        step3: isHi
          ? 'इसी संकुल के 1-2 विकासशील शिक्षकों के साथ इस शिक्षक की जोड़ी बनाएं, जिससे वे आपस में पाठ योजना और TLM उपयोग पर विचार साझा कर सकें।'
          : 'Pair this teacher with 1-2 developing colleagues from neighboring schools within the same cluster to exchange practical lesson plans and material ideas.'
      };
    }

    if (tier === 'PROFICIENT') {
      return {
        overview: isHi
          ? 'शिक्षक के पास अच्छा विषय ज्ञान और कक्षा में उच्च विश्वास है। कक्षा में सीखने का स्तर और बेहतर करने के लिए शिक्षक को व्याख्यान कम करके बच्चों को अधिक बोलने का अवसर देने पर ध्यान देना चाहिए।'
          : 'The teacher has solid foundational competence and high classroom rapport. The primary growth opportunity is shifting classroom balance from teacher lecturing toward deeper student reflection.',
        step1: isHi
          ? '30:70 का नियम लागू करें: शिक्षक कक्षा में 30% समय ही निर्देश दें और 70% समय बच्चों को आपस में चर्चा करने और अभ्यास करने के लिए उपलब्ध कराएं।'
          : 'Model the 30:70 rule: keep teacher explanations under 30% of the period, giving students the remaining 70% of time to talk in pairs and work through exercises.',
        step2: isHi
          ? 'जब किसी बच्चे ने सही उत्तर दिया, तो क्या आपने उससे पूछा कि वह इस निष्कर्ष तक कैसे पहुंचा?'
          : 'When a student gives an answer, did you ask them to walk through the exact steps of how they arrived at that conclusion?',
        step3: isHi
          ? 'संकुल के चैंपियन शिक्षक के साथ मिलकर गणित या भाषा की एक गतिविधि की योजना बनाएं, जिसमें बच्चे अपने शब्दों में नियम समझाएं।'
          : 'Connect with a cluster champion teacher to co-design one hands-on activity where students summarize the core concept in their own everyday language.'
      };
    }

    if (tier === 'DEVELOPING') {
      // Check specific gap
      const hasProbing = gaps.includes('PROBING');
      const hasTLM = gaps.includes('TLM_CYCLE');

      return {
        overview: isHi
          ? 'शिक्षक कक्षा में सक्रिय रहते हैं लेकिन जब बच्चे अटकते हैं तो शिक्षक तुरंत सही उत्तर बता देते हैं, जिससे बच्चों की सोचने की प्रक्रिया पूरी नहीं हो पाती।'
          : 'The teacher is earnest and dedicated, but tends to give answers too quickly when children hesitate, which unintentionally shuts down student thinking.',
        step1: isHi
          ? hasTLM
            ? 'मूर्त से अमूर्त का चक्र: ब्लैकबोर्ड पर सूत्र लिखने से पहले कम से कम 10 मिनट कंकड़, तीली या कार्ड देकर बच्चों से जोड़-घटाव या शब्द रचना करवाएं।'
            : '5 सेकंड का ठहराव: प्रश्न पूछने के तुरंत बाद 5 सेकंड रुकें। अगर बच्चा गलत बोले, तो सीधे उत्तर न बताएं बल्कि पूछें: "आपने ऐसा क्यों सोचा?"'
          : hasTLM
            ? 'Concrete to Abstract Cycle: Give students concrete counters or cards to manipulate for 10 minutes before writing rules on the board.'
            : 'The 5-Second Wait Routine: Pause for 5 full seconds after asking a question. If an answer is incorrect, ask: "Walk me through what made you think that?"',
        step2: isHi
          ? 'क्या आज कक्षा में बच्चों ने आपकी बात सुनने के अलावा खुद भी आपस में 10 मिनट चर्चा की?'
          : 'Did children have at least 10 minutes today to explain an exercise to their bench partner before you wrote the solution?',
        step3: isHi
          ? 'सीएसी महोदय अगली स्कूल विजिट पर शिक्षक की कक्षा में 20 मिनट का एक संयुक्त शिक्षण सत्र करें, जिसमें शिक्षक केवल प्रश्न पूछने का अभ्यास करें।'
          : 'Academic mentor should conduct a 20-minute co-teaching visit, helping the teacher practice probing questions while the mentor guides small groups.'
      };
    }

    // PRIORITY SUPPORT (<40%)
    return {
      overview: isHi
        ? 'शिक्षक को शिक्षण की मूलभूत प्रक्रियाओं में प्राथमिक सहयोग की आवश्यकता है। शिक्षक को बिना किसी आलोचना के सरल, व्यवहारिक और स्पष्ट सहयोग उपलब्ध कराया जाए।'
        : 'The teacher requires patient, targeted, no-blame support on basic classroom routines. Focus on one single habit at a time rather than overwhelming them with multiple goals.',
      step1: isHi
        ? 'कक्षा में पूरा 20 मिनट का लाइव आदर्श पाठ प्रस्तुत करें: सीएसी स्वयं कक्षा में जाकर बच्चों को पढ़ाएं और शिक्षक को पास बैठाकर दिखाएं कि बच्चों को समूह में काम कैसे कराया जाता है।'
        : 'Conduct a full 20-minute live model lesson: The academic mentor teaches the class while the teacher observes how simple questions draw out quiet students.',
      step2: isHi
        ? 'आज की कक्षा में कौन सी एक बात आपको सबसे अच्छी लगी और किस एक जगह आपको बच्चों को समझाने में सबसे ज्यादा मुश्किल आई?'
        : 'What was the single most enjoyable moment in your lesson today, and what specific step felt most challenging?',
      step3: isHi
        ? 'आस-पास के विद्यालय के एक सहयोगी शिक्षक को नियुक्त करें जो सप्ताह में एक बार फोन पर पाठ योजना साझा कर सकें।'
        : 'Assign a compassionate mentor teacher from a neighboring school to check in weekly by phone and share simple, ready-to-use lesson ideas.'
    };
  }

  // Helpers
  function getTierBadge(tier, large = false) {
    const isHi = (window.currentLang === 'hi');
    const size = large ? 'font-size: 11.5px; padding: 4px 10px;' : 'font-size: 10px; padding: 3px 8px;';
    
    switch(tier) {
      case 'CHAMPION':
        return `<span style="background: rgba(5, 150, 105, 0.12); color: var(--accent-emerald); border: 1px solid rgba(5, 150, 105, 0.3); border-radius: 6px; font-weight: 800; ${size} text-transform: uppercase;">⭐ ${isHi ? 'चैंपियन (80%+)' : 'Champion (80%+)'}</span>`;
      case 'PROFICIENT':
        return `<span style="background: rgba(0, 138, 171, 0.12); color: var(--peepul-teal); border: 1px solid rgba(0, 138, 171, 0.3); border-radius: 6px; font-weight: 800; ${size} text-transform: uppercase;">✓ ${isHi ? 'प्रवीण (60-79%)' : 'Proficient (60-79%)'}</span>`;
      case 'DEVELOPING':
        return `<span style="background: rgba(217, 119, 6, 0.12); color: #d97706; border: 1px solid rgba(217, 119, 6, 0.3); border-radius: 6px; font-weight: 800; ${size} text-transform: uppercase;">⚡ ${isHi ? 'विकासशील (40-59%)' : 'Developing (40-59%)'}</span>`;
      default:
        return `<span style="background: rgba(220, 38, 38, 0.12); color: #dc2626; border: 1px solid rgba(220, 38, 38, 0.3); border-radius: 6px; font-weight: 800; ${size} text-transform: uppercase;">⚠️ ${isHi ? 'प्राथमिक सहयोग (<40%)' : 'Priority Support (<40%)'}</span>`;
    }
  }

  function getCycleBadge(cycle, large = false) {
    const isHi = (window.currentLang === 'hi');
    const size = large ? 'font-size: 11px; padding: 3px 8px;' : 'font-size: 9.5px; padding: 2px 6px;';
    
    if (cycle === 'BOTH') {
      return `<span style="background: rgba(79, 70, 229, 0.1); color: var(--peepul-indigo); border: 1px solid rgba(79, 70, 229, 0.25); border-radius: 4px; font-weight: 700; ${size}">AUG + SEP</span>`;
    } else if (cycle === 'AUG') {
      return `<span style="background: rgba(0, 138, 171, 0.08); color: var(--peepul-teal); border: 1px solid rgba(0, 138, 171, 0.2); border-radius: 4px; font-weight: 700; ${size}">AUG</span>`;
    } else {
      return `<span style="background: rgba(99, 208, 223, 0.15); color: #0284c7; border: 1px solid rgba(99, 208, 223, 0.3); border-radius: 4px; font-weight: 700; ${size}">SEP</span>`;
    }
  }

  function getScoreColor(score) {
    if (score >= 80) return 'var(--accent-emerald)';
    if (score >= 60) return 'var(--peepul-teal)';
    if (score >= 40) return '#d97706';
    return '#dc2626';
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  /**
   * Bilingual updates on language change
   */
  window.updateTeacherDiagnosticsLang = function() {
    if (!isInitialized) return;
    renderSummaryMetrics();
    renderTeacherTable();
    if (activeTeacherCode) {
      selectTeacherProfile(activeTeacherCode);
    }
  };

})();
