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
  let currentCycleFilter = 'ALL';
  let currentTrajectoryFilter = 'ALL';
  let clusterMap = {};
  let blockMap = {};
  let isInitialized = false;

  // Question Descriptions and Best Practices Dictionary (with Strict Cycle Binding)
  const PEDAGOGY_BENCHMARKS = {
    PURPOSE: {
      cycle: 'BOTH',
      qNum: 'Q82',
      domainEn: 'Shaikshik Samwaad Purpose & Culture',
      domainHi: 'शैक्षिक संवाद का मूल उद्देश्य एवं संस्कृति',
      bestPracticeEn: 'Shaikshik Samwaad is a platform for peer academic exchange, collective problem-solving, and professional growth.',
      bestPracticeHi: 'शैक्षिक संवाद साथी शिक्षकों के साथ अकादमिक विमर्श, शिक्षण चुनौतियों के साझा समाधान और सीखने का मंच है।',
      misconceptionEn: 'Treating Samwaad as administrative reporting or ritual attendance.',
      misconceptionHi: 'संवाद को केवल औपचारिकता या प्रशासनिक बैठक समझना।'
    },
    DESIGN_30_70: {
      cycle: 'BOTH',
      qNum: 'Q86',
      domainEn: 'Session Design & 30:70 Practice',
      domainHi: 'सत्र संरचना एवं 30:70 सहभागिता नियम',
      bestPracticeEn: 'Teacher maintains a 30:70 balance: 30% guidance, 70% active student practice and peer reflection.',
      bestPracticeHi: 'शिक्षक 30:70 का संतुलन रखते हैं: 30% निर्देश और 70% बच्चों द्वारा सक्रिय अभ्यास व सहकर्मी विमर्श।',
      misconceptionEn: 'Teacher lecturing for over 80% of the period while students remain passive.',
      misconceptionHi: 'पूरी कक्षा में शिक्षक का 80% से अधिक बोलना और बच्चों को चुपचाप बैठाए रखना।'
    },
    // August Only Questions:
    STUDENT_AGENCY: {
      cycle: 'AUG',
      qNum: 'Q95',
      domainEn: 'Student Agency & Interests (August)',
      domainHi: 'विद्यार्थी सहभागिता एवं रुचियां (अगस्त सत्र)',
      bestPracticeEn: 'Build learning activities around children’s real interests, capabilities, and classroom context.',
      bestPracticeHi: 'बच्चों की रुचियों और क्षमताओं को जानकर उन्हें सीखने की वास्तविक गतिविधियों से जोड़ना।',
      misconceptionEn: 'Treating student activity as mere busywork without connection to concept goals.',
      misconceptionHi: 'गतिविधि को केवल समय बिताने का साधन समझना, अवधारणा से न जोड़ना।'
    },
    SAFETY: {
      cycle: 'AUG',
      qNum: 'Q96',
      domainEn: 'Psychological Safety & Mistakes (August)',
      domainHi: 'भयमुक्त वातावरण एवं गलतियों का स्वागत (अगस्त सत्र)',
      bestPracticeEn: 'Treat mistakes as normal and essential learning steps; guide students to discover corrections independently.',
      bestPracticeHi: 'गलतियों को सीखने का स्वाभाविक हिस्सा मानें और बच्चों को संकेत देकर स्वयं सुधार करने के लिए प्रेरित करें।',
      misconceptionEn: 'Ignoring or scolding errors, which makes children hesitant to participate in classroom discussions.',
      misconceptionHi: 'गलतियों पर डांटना या उन्हें अनदेखा करना, जिससे बच्चे कक्षा में बोलने से डरने लगते हैं।'
    },
    BELONGING: {
      cycle: 'AUG',
      qNum: 'Q97',
      domainEn: 'Classroom Belonging & Participation (August)',
      domainHi: 'कक्षा में अपनापन एवं सबकी सहभागिता (अगस्त सत्र)',
      bestPracticeEn: 'Involve every student in genuine classroom tasks and active pair work, not just the front-bench fast learners.',
      bestPracticeHi: 'केवल आगे बैठने वाले होशियार बच्चों को नहीं, बल्कि हर बच्चे को कक्षा की वास्तविक जिम्मेदारियों और समूह कार्य में जोड़ना।',
      misconceptionEn: 'Surface Praise: showering praise only on quick responders while shy or back-bench students remain passive.',
      misconceptionHi: 'केवल जल्दी उत्तर देने वाले 2-3 बच्चों की तारीफ करना, जबकि बाकी बच्चे मूकदर्शक बने रहें।'
    },
    // September Only Questions:
    TLM_CYCLE: {
      cycle: 'SEP',
      qNum: 'Q177',
      domainEn: 'Concrete to Abstract Learning - TLM (September)',
      domainHi: 'मूर्त से अमूर्त शिक्षण चक्र - TLM (सितंबर सत्र)',
      bestPracticeEn: 'Provide concrete experience with learning materials, followed by student reflection and concept consolidation.',
      bestPracticeHi: 'बच्चों को पहले सामग्री के साथ मूर्त अनुभव दें, फिर उस पर चिंतन कराएं और अंत में अवधारणा का समेकन करें।',
      misconceptionEn: 'Treating TLM as a decorative display or lecture prop held by the teacher rather than student-handled tools.',
      misconceptionHi: 'TLM को बच्चों के हाथों में देने के बजाय शिक्षक द्वारा केवल प्रदर्शन या सजावट की वस्तु समझना।'
    },
    PROBING: {
      cycle: 'SEP',
      qNum: 'Q178',
      domainEn: 'Inquiry & Probing Questions (September)',
      domainHi: 'सटीक एवं विचारोत्तेजक प्रश्न पूछना (सितंबर सत्र)',
      bestPracticeEn: 'When a student answers incorrectly, pause and ask probing questions to uncover their thinking rather than giving the answer.',
      bestPracticeHi: 'गलत उत्तर मिलने पर तुरंत सही उत्तर न बताएं, बल्कि पूरक प्रश्न पूछकर बच्चे की सोच और तर्क को बाहर लाएं।',
      misconceptionEn: 'Immediate answer dictation: providing the right answer right away so the lesson proceeds faster.',
      misconceptionHi: 'तुरंत सही उत्तर बता देना ताकि पाठ तेजी से आगे बढ़ सके, जिससे बच्चे की सोचने की प्रक्रिया रुक जाती है।'
    },
    CONSOLIDATION: {
      cycle: 'SEP',
      qNum: 'Q179',
      domainEn: 'Concept Consolidation (September)',
      domainHi: 'अवधारणा का समेकन (सितंबर सत्र)',
      bestPracticeEn: 'Conclude lessons by having students explain the central learning takeaway in their own words.',
      bestPracticeHi: 'पाठ के अंत में मुख्य सीख को स्पष्ट करना और बच्चों से अपने शब्दों में अवधारणा का सारांश कहलवाना।',
      misconceptionEn: 'Ending class abruptly without summarizing what was learned.',
      misconceptionHi: 'कक्षा को बिना यह जाने समाप्त कर देना कि बच्चों ने क्या सीखा।'
    }
  };

  const AUTH_STORAGE_KEY = 'rsk_teacher_studio_unlocked';
  // Strictly restricted to Teacher#2026.Support@MP only
  const VALID_TEACHER_HASHES = [
    'b3fad6589ccab501b7b87c331b435c14313a7bc3cc51a49214002d05a7021526' // Teacher#2026.Support@MP
  ];

  async function computeSha256(str) {
    if (window.crypto && crypto.subtle) {
      const msgUint8 = new TextEncoder().encode(str);
      const hashBuffer = await crypto.subtle.digest('SHA-256', msgUint8);
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    }
    return '';
  }

  window.isTeacherStudioUnlocked = function() {
    return sessionStorage.getItem(AUTH_STORAGE_KEY) === 'granted';
  };

  window.verifyTeacherStudioPasscode = async function() {
    const input = document.getElementById('tdPassInput');
    const err = document.getElementById('tdPassError');
    if (!input) return;
    const val = (input.value || '').trim();

    if (!val) {
      if (err) {
        err.style.display = 'block';
        err.innerText = (window.currentLang === 'hi') ? 'कृपया पासवर्ड दर्ज करें।' : 'Please enter the supervisor passcode.';
      }
      return;
    }

    const hash = await computeSha256(val);
    if (VALID_TEACHER_HASHES.includes(hash)) {
      sessionStorage.setItem(AUTH_STORAGE_KEY, 'granted');
      if (err) err.style.display = 'none';
      unlockTeacherStudioUI();
    } else {
      if (err) {
        err.style.display = 'block';
        err.innerText = (window.currentLang === 'hi') 
          ? '❌ अमान्य पासवर्ड (Invalid Passcode)। कृपया सही पासवर्ड दर्ज करें।' 
          : '❌ Invalid Passcode. Please check and re-enter.';
      }
      input.style.borderColor = '#dc2626';
      setTimeout(() => {
        if (input) input.style.borderColor = 'var(--border-subtle)';
      }, 1500);
    }
  };

  window.toggleTeacherPassVisibility = function() {
    const input = document.getElementById('tdPassInput');
    if (!input) return;
    input.type = (input.type === 'password') ? 'text' : 'password';
  };

  window.lockTeacherStudio = function() {
    sessionStorage.removeItem(AUTH_STORAGE_KEY);
    const gate = document.getElementById('tdSecurityGate');
    const content = document.getElementById('tdContentContainer');
    if (gate) gate.style.display = 'block';
    if (content) content.style.display = 'none';
    const input = document.getElementById('tdPassInput');
    if (input) {
      input.value = '';
      input.focus();
    }
    const err = document.getElementById('tdPassError');
    if (err) err.style.display = 'none';
  };

  function unlockTeacherStudioUI() {
    const gate = document.getElementById('tdSecurityGate');
    const content = document.getElementById('tdContentContainer');
    if (gate) gate.style.display = 'none';
    if (content) content.style.display = 'block';

    if (!isInitialized || allTeachers.length === 0) {
      loadTeacherDiagnosticsData();
    }
  }

  function loadTeacherDiagnosticsData() {
    if (isInitialized && allTeachers.length > 0) return;

    if (window.TEACHER_DIAGNOSTICS_DATA) {
      loadDataPayload(window.TEACHER_DIAGNOSTICS_DATA);
    } else {
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
  }

  /**
   * Initialize Tab Data & Controls
   */
  window.initTeacherDiagnosticsTab = function() {
    if (!window.isTeacherStudioUnlocked()) {
      const gate = document.getElementById('tdSecurityGate');
      const content = document.getElementById('tdContentContainer');
      if (gate) gate.style.display = 'block';
      if (content) content.style.display = 'none';
      
      const input = document.getElementById('tdPassInput');
      if (input && !input.hasAttribute('data-has-listener')) {
        input.setAttribute('data-has-listener', 'true');
        input.addEventListener('keydown', function(e) {
          if (e.key === 'Enter') {
            e.preventDefault();
            window.verifyTeacherStudioPasscode();
          }
        });
      }
      return;
    }

    unlockTeacherStudioUI();
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

    clusterMap = {};
    blockMap = {};

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

      // Trajectory calculation for persistent teachers
      let trajectory = 'SINGLE';
      let delta = null;
      if (cycle === 'BOTH' && augScore !== null && sepScore !== null) {
        delta = Math.round((sepScore - augScore) * 10) / 10;
        if (delta >= 20.0) {
          trajectory = 'RISING';
        } else if (augScore >= 80.0 && sepScore >= 80.0) {
          trajectory = 'CHAMPION';
        } else if (delta <= -20.0) {
          trajectory = 'DROP';
        } else if (augScore < 40.0 && sepScore < 40.0) {
          trajectory = 'PERSISTENT_SUPPORT';
        } else {
          trajectory = 'STABLE';
        }
      }

      const teacherObj = {
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
        traj: trajectory,
        delta: delta,
        g: gaps,
        t178: text178,
        t177: text177,
        t95: text95,
        t97: text97,
        // Pre-computed lowercase search tokens for ultra-fast filtering
        searchToken: (code + ' ' + name).toLowerCase()
      };

      if (clusterName) {
        if (!clusterMap[clusterName]) clusterMap[clusterName] = [];
        clusterMap[clusterName].push(teacherObj);
      }
      if (blockName) {
        if (!blockMap[blockName]) blockMap[blockName] = [];
        blockMap[blockName].push(teacherObj);
      }

      return teacherObj;
    });

    // Prioritize teachers who attended BOTH sessions first
    allTeachers.sort((a, b) => {
      const aBoth = (a.cy === 'BOTH') ? 1 : 0;
      const bBoth = (b.cy === 'BOTH') ? 1 : 0;
      if (aBoth !== bBoth) return bBoth - aBoth;
      if (b.sc !== a.sc) return b.sc - a.sc;
      return a.n.localeCompare(b.n);
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
   * Render Top Summary Bento KPI Metrics & Tier/Trajectory Pills dynamically
   */
  function updateDynamicMetrics(cohort, selectedDist, selectedBlock) {
    const isHi = (window.currentLang === 'hi');
    const total = cohort.length;

    let champ = 0, prof = 0, dev = 0, supp = 0, scoreSum = 0, persistent = 0;
    let trajRising = 0, trajChamp = 0, trajDrop = 0, trajSupp = 0;

    for (let i = 0; i < total; i++) {
      const t = cohort[i];
      if (t.t === 'CHAMPION') champ++;
      else if (t.t === 'PROFICIENT') prof++;
      else if (t.t === 'DEVELOPING') dev++;
      else if (t.t === 'SUPPORT_NEEDED') supp++;

      if (t.traj === 'RISING') trajRising++;
      else if (t.traj === 'CHAMPION') trajChamp++;
      else if (t.traj === 'DROP') trajDrop++;
      else if (t.traj === 'PERSISTENT_SUPPORT') trajSupp++;

      scoreSum += t.sc;
      if (t.cy === 'BOTH') persistent++;
    }

    const avgScore = total > 0 ? (scoreSum / total).toFixed(1) : '0.0';

    // Update Top Bento KPI Cards
    const elTotal = document.getElementById('tdKpiTotal');
    const elChamp = document.getElementById('tdKpiChampions');
    const elProf = document.getElementById('tdKpiProficient');
    const elDev = document.getElementById('tdKpiDeveloping');
    const elSupp = document.getElementById('tdKpiSupport');
    const elAvg = document.getElementById('tdKpiAvgScore');
    const elAvgLabel = document.getElementById('tdKpiAvgScoreLabel');
    const elAvgSub = document.getElementById('tdKpiAvgScoreSub');

    if (elTotal) elTotal.innerText = total.toLocaleString();
    if (elChamp) {
      const pct = total > 0 ? (champ * 100 / total).toFixed(1) : '0.0';
      elChamp.innerHTML = `${champ.toLocaleString()} <span style="font-size: 12px; font-weight: 500; color: var(--text-muted);">(${pct}%)</span>`;
    }
    if (elProf) {
      const pct = total > 0 ? (prof * 100 / total).toFixed(1) : '0.0';
      elProf.innerHTML = `${prof.toLocaleString()} <span style="font-size: 12px; font-weight: 500; color: var(--text-muted);">(${pct}%)</span>`;
    }
    if (elDev) {
      const pct = total > 0 ? (dev * 100 / total).toFixed(1) : '0.0';
      elDev.innerHTML = `${dev.toLocaleString()} <span style="font-size: 12px; font-weight: 500; color: var(--text-muted);">(${pct}%)</span>`;
    }
    if (elSupp) {
      const pct = total > 0 ? (supp * 100 / total).toFixed(1) : '0.0';
      elSupp.innerHTML = `${supp.toLocaleString()} <span style="font-size: 12px; font-weight: 500; color: var(--text-muted);">(${pct}%)</span>`;
    }
    if (elAvg) {
      elAvg.innerHTML = `${avgScore}% <span style="font-size: 12px; font-weight: 500; color: var(--text-muted);">(${persistent.toLocaleString()} persistent)</span>`;
    }
    if (elAvgLabel) {
      if (selectedBlock && selectedBlock !== 'ALL') {
        elAvgLabel.innerHTML = `<span>📊 ${selectedBlock.toUpperCase()} AVERAGE</span>`;
      } else if (selectedDist && selectedDist !== 'ALL') {
        elAvgLabel.innerHTML = `<span>📊 ${selectedDist.toUpperCase()} AVERAGE</span>`;
      } else {
        elAvgLabel.innerHTML = `<span>📊 STATE AVERAGE</span>`;
      }
    }
    if (elAvgSub) {
      if (selectedBlock && selectedBlock !== 'ALL') {
        elAvgSub.innerText = `${selectedBlock} Block Pedagogy Score`;
      } else if (selectedDist && selectedDist !== 'ALL') {
        elAvgSub.innerText = `${selectedDist} District Pedagogy Score`;
      } else {
        elAvgSub.innerText = 'Statewide Pedagogy Score';
      }
    }

    // Update Tier Pills dynamically
    const pillAll = document.getElementById('tdTierPillAll') || document.querySelector('.td-tier-pill[data-tier="ALL"]');
    const pillChamp = document.getElementById('tdTierPillChampion') || document.querySelector('.td-tier-pill[data-tier="CHAMPION"]');
    const pillProf = document.getElementById('tdTierPillProficient') || document.querySelector('.td-tier-pill[data-tier="PROFICIENT"]');
    const pillDev = document.getElementById('tdTierPillDeveloping') || document.querySelector('.td-tier-pill[data-tier="DEVELOPING"]');
    const pillSupp = document.getElementById('tdTierPillSupport') || document.querySelector('.td-tier-pill[data-tier="SUPPORT_NEEDED"]');

    if (pillAll) pillAll.innerText = isHi ? `सभी (${total.toLocaleString()})` : `All (${total.toLocaleString()})`;
    if (pillChamp) pillChamp.innerText = isHi ? `⭐ चैंपियन (${champ.toLocaleString()})` : `⭐ Champions (${champ.toLocaleString()})`;
    if (pillProf) pillProf.innerText = isHi ? `✓ प्रवीण (${prof.toLocaleString()})` : `✓ Proficient (${prof.toLocaleString()})`;
    if (pillDev) pillDev.innerText = isHi ? `⚡ विकासशील (${dev.toLocaleString()})` : `⚡ Developing (${dev.toLocaleString()})`;
    if (pillSupp) pillSupp.innerText = isHi ? `⚠️ प्राथमिक सहयोग (${supp.toLocaleString()})` : `⚠️ Priority Support (${supp.toLocaleString()})`;

    // Update Trajectory Pills dynamically
    const pillTrajAll = document.getElementById('tdTrajPillAll') || document.querySelector('.td-traj-pill[data-traj="ALL"]');
    const pillTrajRising = document.getElementById('tdTrajPillRising') || document.querySelector('.td-traj-pill[data-traj="RISING"]');
    const pillTrajChamp = document.getElementById('tdTrajPillChampion') || document.querySelector('.td-traj-pill[data-traj="CHAMPION"]');
    const pillTrajDrop = document.getElementById('tdTrajPillDrop') || document.querySelector('.td-traj-pill[data-traj="DROP"]');
    const pillTrajSupp = document.getElementById('tdTrajPillSupport') || document.querySelector('.td-traj-pill[data-traj="PERSISTENT_SUPPORT"]');

    if (pillTrajAll) pillTrajAll.innerText = isHi ? `सभी गतियां (${total.toLocaleString()})` : `All Trajectories (${total.toLocaleString()})`;
    if (pillTrajRising) pillTrajRising.innerText = isHi ? `📈 उगते सितारे (${trajRising.toLocaleString()})` : `📈 Rising Stars (${trajRising.toLocaleString()})`;
    if (pillTrajChamp) pillTrajChamp.innerText = isHi ? `🏆 सतत उत्कृष्ट (${trajChamp.toLocaleString()})` : `🏆 Consistent Champions (${trajChamp.toLocaleString()})`;
    if (pillTrajDrop) pillTrajDrop.innerText = isHi ? `📉 गिरावट चेतावनी (${trajDrop.toLocaleString()})` : `📉 Drop Alerts (${trajDrop.toLocaleString()})`;
    if (pillTrajSupp) pillTrajSupp.innerText = isHi ? `🚨 सतत सहयोग (${trajSupp.toLocaleString()})` : `🚨 Persistent Need (${trajSupp.toLocaleString()})`;
  }

  function renderSummaryMetrics() {
    updateDynamicMetrics(allTeachers, 'ALL', 'ALL');
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
   * Growth Trajectory Pill Filter Handler
   */
  window.setTeacherTrajectoryFilter = function(traj, btnEl) {
    currentTrajectoryFilter = traj;
    document.querySelectorAll('.td-traj-pill').forEach(btn => btn.classList.remove('active'));
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
    const cycleSelect = document.getElementById('tdCycleSelect');
    const selectedCycle = cycleSelect ? cycleSelect.value : 'ALL';

    // 1. Compute cohort based on District, Block, Cycle, and Search query (independent of active Tier & Trajectory)
    const baseCohort = allTeachers.filter(t => {
      // Cycle match
      if (selectedCycle !== 'ALL' && t.cy !== selectedCycle) {
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

    // 2. Dynamically update Top Bento Cards, Tier Pills, and Trajectory Pills based on the active cohort
    updateDynamicMetrics(baseCohort, selectedDist, selectedBlock);

    // 3. Filter down by active Tier AND active Trajectory
    filteredTeachers = baseCohort.filter(t => {
      if (currentTierFilter !== 'ALL' && t.t !== currentTierFilter) {
        return false;
      }
      if (currentTrajectoryFilter !== 'ALL' && t.traj !== currentTrajectoryFilter) {
        return false;
      }
      return true;
    });

    // 4. Prioritize teachers who attended BOTH sessions first, then score or trajectory delta
    filteredTeachers.sort((a, b) => {
      // 1. Both sessions priority
      const aBoth = (a.cy === 'BOTH') ? 1 : 0;
      const bBoth = (b.cy === 'BOTH') ? 1 : 0;
      if (aBoth !== bBoth) {
        return bBoth - aBoth; // BOTH comes first
      }

      // 2. Trajectory specific sorting
      if (currentTrajectoryFilter === 'RISING') {
        const dA = a.delta !== null ? a.delta : -999;
        const dB = b.delta !== null ? b.delta : -999;
        if (dB !== dA) return dB - dA; // highest positive gain first (+60%, +40%...)
      } else if (currentTrajectoryFilter === 'DROP') {
        const dA = a.delta !== null ? a.delta : 999;
        const dB = b.delta !== null ? b.delta : 999;
        if (dA !== dB) return dA - dB; // biggest negative drop first (-60%, -40%...)
      } else if (currentTierFilter === 'SUPPORT_NEEDED' || currentTrajectoryFilter === 'PERSISTENT_SUPPORT') {
        // In priority support, show teachers with lowest scores first (urgent intervention)
        if (a.sc !== b.sc) return a.sc - b.sc;
      } else {
        // In champions / general view, show highest scores first
        if (b.sc !== a.sc) return b.sc - a.sc;
      }

      // 3. Alphabetical name order
      return a.n.localeCompare(b.n);
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
    const cycleSelect = document.getElementById('tdCycleSelect');
    if (cycleSelect) cycleSelect.value = 'ALL';
    window.setTeacherTierFilter('ALL', document.querySelector('.td-tier-pill[data-tier="ALL"]'));
    window.setTeacherTrajectoryFilter('ALL', document.querySelector('.td-traj-pill[data-traj="ALL"]'));
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

      let trajBadge = '';
      if (t.cy === 'BOTH' && t.delta !== null) {
        if (t.delta > 0) {
          trajBadge = `<div style="font-size: 10px; font-weight: 800; color: #059669; margin-top: 3px;">+${t.delta}% 📈</div>`;
        } else if (t.delta < 0) {
          trajBadge = `<div style="font-size: 10px; font-weight: 800; color: #dc2626; margin-top: 3px;">${t.delta}% 📉</div>`;
        } else {
          trajBadge = `<div style="font-size: 10px; font-weight: 700; color: var(--text-muted); margin-top: 3px;">0% ➖</div>`;
        }
      }

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
          <td style="padding: 10px 12px; text-align: center;">
            ${cycleBadge}
            ${trajBadge}
          </td>
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

    // Pedagogical strengths & diagnosed gaps (Strictly Cycle-Aware)
    const masteredList = [];
    const gapsList = [];

    for (const k in PEDAGOGY_BENCHMARKS) {
      const benchmark = PEDAGOGY_BENCHMARKS[k];
      
      // Strict cycle isolation:
      // If teacher did NOT attend August, NEVER evaluate or show August-only questions
      if (benchmark.cycle === 'AUG' && teacher.cy === 'SEP') continue;
      // If teacher did NOT attend September, NEVER evaluate or show September-only questions
      if (benchmark.cycle === 'SEP' && teacher.cy === 'AUG') continue;

      if (teacher.g.includes(k)) {
        gapsList.push(benchmark);
      } else {
        masteredList.push(benchmark);
      }
    }

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
                ${teacher.cy === 'BOTH' ? (isHi ? 'संयुक्त शिक्षण प्राप्तांक' : 'Combined Pedagogy Score') : (teacher.cy === 'AUG' ? (isHi ? 'अगस्त शिक्षण प्राप्तांक' : 'August Pedagogy Score') : (isHi ? 'सितंबर शिक्षण प्राप्तांक' : 'September Pedagogy Score'))}
              </div>
              <div style="font-size: 26px; font-weight: 900; font-family: var(--font-mono); color: ${scoreColor}; margin-top: 2px;">
                ${teacher.sc.toFixed(1)}%
              </div>
              <div style="font-size: 9.5px; color: var(--text-muted); margin-top: 2px;">
                ${teacher.cy === 'BOTH' ? (isHi ? 'अगस्त व सितंबर का औसत' : 'Aug & Sep 5-Q Avg') : (teacher.cy === 'AUG' ? (isHi ? 'केवल अगस्त के 5 प्रश्न' : 'August 5 Questions') : (isHi ? 'केवल सितंबर के 5 प्रश्न' : 'September 5 Questions'))}
              </div>
            </div>
          </div>
        </div>

        <!-- Metrics Ribbon (4 Cards) -->
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; background: var(--border-hairline); border-bottom: 1px solid var(--border-subtle);">
          <div style="background: var(--bg-surface-1); padding: 12px 14px; text-align: center;">
            <div style="font-size: 10px; font-weight: 700; color: var(--text-muted);">${isHi ? 'अगस्त प्राप्तांक' : 'August Pedagogy'}</div>
            <div style="font-size: 15px; font-weight: 800; font-family: var(--font-mono); margin-top: 4px; color: ${teacher.as !== null ? 'var(--text-primary)' : 'var(--text-dim)'};">
              ${teacher.as !== null ? teacher.as.toFixed(1) + '%' : (isHi ? 'सत्र में उपस्थित नहीं' : 'Not Attended')}
            </div>
            ${teacher.as === null ? `<div style="font-size: 9px; color: var(--text-dim); margin-top: 2px;">${isHi ? 'कोई अंक नहीं' : 'Score: N/A'}</div>` : ''}
          </div>
          <div style="background: var(--bg-surface-1); padding: 12px 14px; text-align: center;">
            <div style="font-size: 10px; font-weight: 700; color: var(--text-muted);">${isHi ? 'सितंबर प्राप्तांक' : 'September Pedagogy'}</div>
            <div style="font-size: 15px; font-weight: 800; font-family: var(--font-mono); margin-top: 4px; color: ${teacher.ss !== null ? 'var(--text-primary)' : 'var(--text-dim)'};">
              ${teacher.ss !== null ? teacher.ss.toFixed(1) + '%' : (isHi ? 'सत्र में उपस्थित नहीं' : 'Not Attended')}
            </div>
            ${teacher.ss === null ? `<div style="font-size: 9px; color: var(--text-dim); margin-top: 2px;">${isHi ? 'कोई अंक नहीं' : 'Score: N/A'}</div>` : ''}
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
          
          <!-- Growth Trajectory Progression Card (Aug -> Sep) -->
          ${renderTrajectoryProgressionCard(teacher, isHi)}

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

          <!-- Geographic & Cluster Proximity Support Radar -->
          ${renderProximityRadarCard(teacher, isHi)}

        </div>

      </div>
    `;
  }

  /**
   * Render Selected Options from Survey Data (Strictly Cycle-Aware)
   */
  function renderSurveyResponseDetails(teacher, isHi) {
    const hasSep = (teacher.cy === 'BOTH' || teacher.cy === 'SEP');
    const hasAug = (teacher.cy === 'BOTH' || teacher.cy === 'AUG');

    if (!((hasSep && (teacher.t178 || teacher.t177)) || (hasAug && (teacher.t95 || teacher.t97)))) {
      return '';
    }

    return `
      <div style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 14px 16px;">
        <div style="font-size: 11px; font-weight: 800; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px;">
          ${isHi ? 'उपस्थित सत्र के वास्तविक सर्वेक्षण उत्तर (Survey Evidence From Attended Session)' : 'Survey Evidence From Attended Session'}
        </div>
        <div style="display: flex; flex-direction: column; gap: 10px; font-size: 11.5px;">
          ${(hasSep && teacher.t178) ? `
            <div style="border-left: 3px solid ${teacher.g.includes('PROBING') ? '#dc2626' : 'var(--accent-emerald)'}; padding-left: 10px;">
              <div style="font-weight: 700; color: var(--text-primary);">Q178 (सितंबर • ${isHi ? 'गलत उत्तर पर प्रतिक्रिया' : 'Reaction to Student Errors'}):</div>
              <div style="color: var(--text-secondary); margin-top: 2px;">
                ${isHi ? 'चुना गया विकल्प:' : 'Selected Response:'} "<em>${escapeHtml(teacher.t178)}</em>"
              </div>
            </div>
          ` : ''}

          ${(hasSep && teacher.t177) ? `
            <div style="border-left: 3px solid ${teacher.g.includes('TLM_CYCLE') ? '#dc2626' : 'var(--accent-emerald)'}; padding-left: 10px;">
              <div style="font-weight: 700; color: var(--text-primary);">Q177 (सितंबर • ${isHi ? 'TLM का उपयोग चक्र' : 'TLM Utilization Cycle'}):</div>
              <div style="color: var(--text-secondary); margin-top: 2px;">
                ${isHi ? 'चुना गया विकल्प:' : 'Selected Response:'} "<em>${escapeHtml(teacher.t177)}</em>"
              </div>
            </div>
          ` : ''}

          ${(hasAug && teacher.t95) ? `
            <div style="border-left: 3px solid ${teacher.g.includes('STUDENT_AGENCY') ? '#dc2626' : 'var(--accent-emerald)'}; padding-left: 10px;">
              <div style="font-weight: 700; color: var(--text-primary);">Q95 (अगस्त • ${isHi ? 'विद्यार्थी सहभागिता' : 'Student Agency'}):</div>
              <div style="color: var(--text-secondary); margin-top: 2px;">
                ${isHi ? 'चुना गया विकल्प:' : 'Selected Response:'} "<em>${escapeHtml(teacher.t95)}</em>"
              </div>
            </div>
          ` : ''}

          ${(hasAug && teacher.t97) ? `
            <div style="border-left: 3px solid ${teacher.g.includes('BELONGING') ? '#dc2626' : 'var(--accent-emerald)'}; padding-left: 10px;">
              <div style="font-weight: 700; color: var(--text-primary);">Q97 (अगस्त • ${isHi ? 'कक्षा में अपनापन' : 'Classroom Belonging'}):</div>
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
   * Render Growth Trajectory Progression Card (Aug vs Sep)
   */
  function renderTrajectoryProgressionCard(teacher, isHi) {
    if (teacher.cy !== 'BOTH' || teacher.as === null || teacher.ss === null) {
      const cyName = teacher.cy === 'AUG' ? (isHi ? 'केवल अगस्त सत्र' : 'August Session Only') : (isHi ? 'केवल सितंबर सत्र' : 'September Session Only');
      return `
        <div style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 12px 16px; display: flex; align-items: center; justify-content: space-between;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 16px;">⏱️</span>
            <div>
              <div style="font-size: 12px; font-weight: 700; color: var(--text-primary);">
                ${isHi ? 'मासिक प्रगति (Trajectory):' : 'Monthly Trajectory:'} <span style="font-weight: 500; color: var(--text-secondary);">${cyName}</span>
              </div>
              <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">
                ${isHi ? 'शिक्षक ने केवल एक सत्र में भाग लिया है। दो सत्रों की तुलना आगामी शैक्षिक संवाद के बाद सक्रिय होगी।' : 'Teacher attended a single monthly session. Progression tracking activates upon attending consecutive cycles.'}
              </div>
            </div>
          </div>
          <div style="font-family: var(--font-mono); font-weight: 800; font-size: 14px; color: ${getScoreColor(teacher.sc)};">
            ${teacher.sc.toFixed(1)}%
          </div>
        </div>
      `;
    }

    const delta = teacher.delta;
    let badgeColor = 'var(--text-muted)';
    let badgeBg = 'rgba(100, 116, 139, 0.1)';
    let badgeBorder = 'rgba(100, 116, 139, 0.25)';
    let badgeLabel = '';
    let explanation = '';

    if (teacher.traj === 'RISING') {
      badgeColor = '#059669';
      badgeBg = 'rgba(5, 150, 105, 0.12)';
      badgeBorder = 'rgba(5, 150, 105, 0.3)';
      badgeLabel = isHi ? `📈 तेजी से प्रगति (+${delta}% सुधार)` : `📈 Rising Star (+${delta}% gain)`;
      explanation = isHi
        ? `शिक्षक ने अगस्त (${teacher.as.toFixed(1)}%) की तुलना में सितंबर (${teacher.ss.toFixed(1)}%) में उत्कृष्ट सुधार दर्ज किया है। शिक्षण प्रक्रियाओं और कक्षा तकनीकों को तेजी से अपनाया जा रहा है।`
        : `Teacher showed strong positive momentum from August (${teacher.as.toFixed(1)}%) to September (${teacher.ss.toFixed(1)}%), adopting core questioning and student-led practices.`;
    } else if (teacher.traj === 'CHAMPION') {
      badgeColor = '#4f46e5';
      badgeBg = 'rgba(79, 70, 229, 0.12)';
      badgeBorder = 'rgba(79, 70, 229, 0.3)';
      badgeLabel = isHi ? '🏆 निरंतर अग्रणी (दोनों सत्र 80%+)' : '🏆 Consistent Champion (80%+ in both)';
      explanation = isHi
        ? `शिक्षक ने अगस्त (${teacher.as.toFixed(1)}%) और सितंबर (${teacher.ss.toFixed(1)}%) दोनों माह में लगातार 80% से अधिक अंक प्राप्त किए हैं। यह संकुल में आदर्श सहकर्मी मार्गदर्शक हैं।`
        : `Consistently achieved 80%+ in both August (${teacher.as.toFixed(1)}%) and September (${teacher.ss.toFixed(1)}%). Excellent candidate for cluster peer mentoring and live demo lessons.`;
    } else if (teacher.traj === 'DROP') {
      badgeColor = '#dc2626';
      badgeBg = 'rgba(220, 38, 38, 0.12)';
      badgeBorder = 'rgba(220, 38, 38, 0.3)';
      badgeLabel = isHi ? `📉 स्कोर में गिरावट (${delta}%)` : `📉 Score Drop Alert (${delta}%)`;
      explanation = isHi
        ? `शिक्षक का स्कोर अगस्त (${teacher.as.toFixed(1)}%) से सितंबर (${teacher.ss.toFixed(1)}%) में घटा है। सितंबर के विचारोत्तेजक प्रश्न (Q178) और सामग्री उपयोग में अतिरिक्त सहयोग की आवश्यकता है।`
        : `Performance dipped from August (${teacher.as.toFixed(1)}%) to September (${teacher.ss.toFixed(1)}%). In September, student error handling (Q178) posed difficulty. Needs supportive coaching on error routines.`;
    } else if (teacher.traj === 'PERSISTENT_SUPPORT') {
      badgeColor = '#b91c1c';
      badgeBg = 'rgba(185, 28, 28, 0.15)';
      badgeBorder = 'rgba(185, 28, 28, 0.35)';
      badgeLabel = isHi ? '🚨 निरंतर प्राथमिक सहयोग (<40%)' : '🚨 Persistent Support Needed (<40%)';
      explanation = isHi
        ? `शिक्षक दोनों सत्रों (अगस्त: ${teacher.as.toFixed(1)}%, सितंबर: ${teacher.ss.toFixed(1)}%) में 40% से नीचे रहे हैं। यह राज्य की सर्वोच्च प्राथमिकता वाली कोचिंग सूची में हैं। सीएसी द्वारा सीधा मार्गदर्शन अनिवार्य है।`
        : `Teacher scored below 40% in both evaluation cycles (August: ${teacher.as.toFixed(1)}%, September: ${teacher.ss.toFixed(1)}%). Flagged for high-priority academic mentoring and supportive co-teaching.`;
    } else {
      badgeColor = 'var(--peepul-teal)';
      badgeBg = 'rgba(0, 138, 171, 0.12)';
      badgeBorder = 'rgba(0, 138, 171, 0.3)';
      badgeLabel = isHi ? `➖ स्थिर प्रदर्शन (${delta >= 0 ? '+' : ''}${delta}%)` : `➖ Stable Progression (${delta >= 0 ? '+' : ''}${delta}%)`;
      explanation = isHi
        ? `शिक्षक का प्रदर्शन दोनों सत्रों में संतुलित रहा है (अगस्त: ${teacher.as.toFixed(1)}%, सितंबर: ${teacher.ss.toFixed(1)}%)।`
        : `Steady performance across consecutive cycles (August: ${teacher.as.toFixed(1)}%, September: ${teacher.ss.toFixed(1)}%). Focus on moving from developing to champion routines.`;
    }

    return `
      <div style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px 18px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 16px;">📈</span>
            <span style="font-size: 12px; font-weight: 800; color: var(--text-primary); text-transform: uppercase; letter-spacing: 0.5px;">
              ${isHi ? 'मासिक प्रगति ट्रैकिंग (August vs September Trajectory)' : 'Monthly Progression Trajectory (Aug vs Sep)'}
            </span>
          </div>
          <span style="font-size: 11px; font-weight: 800; color: ${badgeColor}; background: ${badgeBg}; border: 1px solid ${badgeBorder}; padding: 3px 9px; border-radius: 6px;">
            ${badgeLabel}
          </span>
        </div>

        <!-- Visual Two-Bar Comparison -->
        <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 12px; align-items: center; margin-bottom: 12px; background: var(--bg-surface-2); padding: 12px 14px; border-radius: 8px;">
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 11px; margin-bottom: 4px;">
              <span style="font-weight: 700; color: var(--text-muted);">${isHi ? 'अगस्त 2026' : 'August 2026'}</span>
              <span style="font-family: var(--font-mono); font-weight: 700; color: ${getScoreColor(teacher.as)};">${teacher.as.toFixed(1)}%</span>
            </div>
            <div style="background: rgba(148, 163, 184, 0.2); height: 8px; border-radius: 4px; overflow: hidden;">
              <div style="background: ${getScoreColor(teacher.as)}; width: ${Math.min(100, teacher.as)}%; height: 100%; border-radius: 4px;"></div>
            </div>
          </div>

          <div style="font-size: 18px; color: var(--text-muted); text-align: center; padding: 0 4px;">➔</div>

          <div>
            <div style="display: flex; justify-content: space-between; font-size: 11px; margin-bottom: 4px;">
              <span style="font-weight: 700; color: var(--text-muted);">${isHi ? 'सितंबर 2026' : 'September 2026'}</span>
              <span style="font-family: var(--font-mono); font-weight: 700; color: ${getScoreColor(teacher.ss)};">${teacher.ss.toFixed(1)}%</span>
            </div>
            <div style="background: rgba(148, 163, 184, 0.2); height: 8px; border-radius: 4px; overflow: hidden;">
              <div style="background: ${getScoreColor(teacher.ss)}; width: ${Math.min(100, teacher.ss)}%; height: 100%; border-radius: 4px;"></div>
            </div>
          </div>
        </div>

        <div style="font-size: 11.5px; color: var(--text-secondary); line-height: 1.5;">
          ${explanation}
        </div>
      </div>
    `;
  }

  /**
   * Render Geographic & Cluster Proximity Support Radar
   */
  function renderProximityRadarCard(teacher, isHi) {
    const clusterName = teacher.cl;
    const blockName = teacher.b;
    const clusterTeachers = (clusterName && clusterMap[clusterName]) ? clusterMap[clusterName] : [];
    const blockTeachers = (blockName && blockMap[blockName]) ? blockMap[blockName] : [];

    // Cluster level breakdown
    let cChamp = 0, cProf = 0, cDev = 0, cSupp = 0;
    clusterTeachers.forEach(t => {
      if (t.t === 'CHAMPION') cChamp++;
      else if (t.t === 'PROFICIENT') cProf++;
      else if (t.t === 'DEVELOPING') cDev++;
      else if (t.t === 'SUPPORT_NEEDED') cSupp++;
    });

    const isChampion = (teacher.t === 'CHAMPION');
    let buddyContent = '';

    if (!isChampion) {
      // Find nearest Champion in same cluster
      let buddies = clusterTeachers.filter(t => t.c !== teacher.c && t.t === 'CHAMPION');
      let buddyScope = isHi ? 'इसी संकुल में' : 'in same cluster';

      // Fallback to same block if none in cluster
      if (buddies.length === 0) {
        buddies = blockTeachers.filter(t => t.c !== teacher.c && t.t === 'CHAMPION');
        buddyScope = isHi ? `ब्लॉक ${teacher.b} में` : `in block ${teacher.b}`;
      }

      // If still none, fallback to Proficient in cluster
      if (buddies.length === 0) {
        buddies = clusterTeachers.filter(t => t.c !== teacher.c && t.t === 'PROFICIENT');
        buddyScope = isHi ? 'संकुल के प्रवीण शिक्षक' : 'proficient teacher in cluster';
      }

      if (buddies.length > 0) {
        // Pick highest scoring buddy
        buddies.sort((a, b) => b.sc - a.sc);
        const buddy = buddies[0];

        buddyContent = `
          <div style="background: rgba(5, 150, 105, 0.05); border: 1.5px dashed rgba(5, 150, 105, 0.35); border-radius: 8px; padding: 12px 14px; margin-top: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <span style="font-size: 11px; font-weight: 800; color: var(--accent-emerald); text-transform: uppercase;">
                🤝 ${isHi ? 'सुझावित सहकर्मी साथी (Recommended Peer Champion)' : 'Recommended Peer Champion Buddy'} (${buddyScope})
              </span>
              <span style="font-family: var(--font-mono); font-size: 10px; font-weight: 700; color: var(--accent-emerald); background: rgba(5, 150, 105, 0.1); padding: 2px 6px; border-radius: 4px;">
                ${buddy.c} • ${buddy.sc.toFixed(1)}%
              </span>
            </div>
            <div style="font-size: 12.5px; font-weight: 700; color: var(--text-primary);">
              ${escapeHtml(buddy.n)}
            </div>
            <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">
              ${isHi ? 'संकुल:' : 'Cluster:'} ${escapeHtml(buddy.cl)} | ${escapeHtml(buddy.b)}, ${escapeHtml(buddy.d)}
            </div>
            <div style="font-size: 11.5px; color: var(--text-secondary); margin-top: 6px; line-height: 1.45;">
              ${isHi
                ? `<strong>सहयोग सुझाव:</strong> ${escapeHtml(buddy.n)} के साथ सप्ताह में एक बार पाठ योजना की समीक्षा करवाएं। विशेषकर प्रश्न पूछने और बच्चों से चर्चा कराने की पद्धति पर सहयोगात्मक अभ्यास करें।`
                : `<strong>Mentorship Match:</strong> Pair with ${escapeHtml(buddy.n)} for weekly lesson co-planning and classroom observation, focusing on probing questions and error routines.`}
            </div>
          </div>
        `;
      } else {
        buddyContent = `
          <div style="font-size: 11.5px; color: var(--text-muted); margin-top: 8px; font-style: italic;">
            ${isHi ? 'संकुल अथवा ब्लॉक में कोई साथी शिक्षक अभी उपलब्ध नहीं है।' : 'No nearby peer champion found in the immediate block radius.'}
          </div>
        `;
      }
    } else {
      // Teacher is Champion: show potential mentees in cluster who need support!
      const mentees = clusterTeachers.filter(t => t.c !== teacher.c && (t.t === 'SUPPORT_NEEDED' || t.t === 'DEVELOPING'));
      mentees.sort((a, b) => a.sc - b.sc); // lowest first

      if (mentees.length > 0) {
        buddyContent = `
          <div style="background: rgba(79, 70, 229, 0.05); border: 1.5px dashed rgba(79, 70, 229, 0.35); border-radius: 8px; padding: 12px 14px; margin-top: 10px;">
            <div style="font-size: 11px; font-weight: 800; color: var(--peepul-indigo); text-transform: uppercase; margin-bottom: 6px;">
              🌟 ${isHi ? 'संकुल में मार्गदर्शन हेतु अनुशंसित सहकर्मी शिक्षक' : 'Recommended Cluster Mentees to Support'}
            </div>
            <div style="display: flex; flex-direction: column; gap: 6px;">
              ${mentees.slice(0, 2).map(m => `
                <div style="display: flex; justify-content: space-between; align-items: center; background: var(--bg-surface-1); padding: 6px 10px; border-radius: 6px; font-size: 11.5px;">
                  <div>
                    <span style="font-weight: 700; color: var(--text-primary);">${escapeHtml(m.n)}</span>
                    <span style="font-family: var(--font-mono); font-size: 10px; color: var(--text-muted); margin-left: 4px;">(${m.c})</span>
                  </div>
                  <span style="font-family: var(--font-mono); font-weight: 700; color: ${getScoreColor(m.sc)}; font-size: 11px;">
                    ${m.sc.toFixed(1)}% (${m.t === 'SUPPORT_NEEDED' ? (isHi ? 'सहयोग' : 'Support') : (isHi ? 'विकासशील' : 'Developing')})
                  </span>
                </div>
              `).join('')}
            </div>
            <div style="font-size: 11px; color: var(--text-secondary); margin-top: 6px;">
              ${isHi
                ? 'यह शिक्षक संकुल संवाद में इन साथियों के साथ बैठकर पाठ योजना और कक्षा संचालन के व्यावहारिक अनुभव साझा कर सकते हैं।'
                : 'This champion teacher can sit with these cluster colleagues during monthly Samwaad to guide their lesson planning and instructional routines.'}
            </div>
          </div>
        `;
      } else {
        buddyContent = `
          <div style="font-size: 11.5px; color: var(--accent-emerald); margin-top: 8px; font-weight: 600;">
            ✓ ${isHi ? 'इस संकुल के सभी उपस्थित शिक्षक प्रवीण या अग्रणी स्तर पर हैं।' : 'All participating teachers in this cluster are proficient or higher.'}
          </div>
        `;
      }
    }

    return `
      <div style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px 18px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 16px;">📍</span>
            <span style="font-size: 12px; font-weight: 800; color: var(--text-primary); text-transform: uppercase; letter-spacing: 0.5px;">
              ${isHi ? 'संकुल सहकर्मी सहायता तंत्र (Cluster Proximity Support Radar)' : 'Cluster Proximity & Peer Support Radar'}
            </span>
          </div>
          <span style="font-size: 11px; font-family: var(--font-mono); font-weight: 700; color: var(--peepul-teal);">
            ${clusterTeachers.length} ${isHi ? 'शिक्षक संकुल में मूल्यांकित' : 'Teachers in Cluster'}
          </span>
        </div>

        <!-- Cluster Location & Summary -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 8px; margin-bottom: 10px;">
          <div style="background: var(--bg-surface-2); padding: 8px 10px; border-radius: 6px; font-size: 11px;">
            <div style="color: var(--text-muted);">${isHi ? 'संकुल (Cluster)' : 'Cluster'}</div>
            <div style="font-weight: 700; color: var(--text-primary); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="${escapeHtml(clusterName)}">
              ${escapeHtml(clusterName || 'N/A')}
            </div>
          </div>
          <div style="background: var(--bg-surface-2); padding: 8px 10px; border-radius: 6px; font-size: 11px;">
            <div style="color: var(--text-muted);">${isHi ? 'ब्लॉक एवं जिला' : 'Block & District'}</div>
            <div style="font-weight: 700; color: var(--text-primary); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              ${escapeHtml(blockName || 'N/A')}, ${escapeHtml(teacher.d || '')}
            </div>
          </div>
        </div>

        <!-- Cluster Health Micro-Bar -->
        <div style="background: var(--bg-surface-2); border-radius: 8px; padding: 10px 12px; margin-bottom: 8px;">
          <div style="display: flex; justify-content: space-between; font-size: 11px; margin-bottom: 6px;">
            <span style="font-weight: 700; color: var(--text-muted);">${isHi ? 'संकुल में शिक्षक वितरण:' : 'Cluster Cohort Health:'}</span>
            <span style="font-family: var(--font-mono); font-size: 10.5px;">
              <span style="color: var(--accent-emerald); font-weight: 700;">${cChamp} ⭐</span> • 
              <span style="color: var(--peepul-teal); font-weight: 700;">${cProf} ✓</span> • 
              <span style="color: #d97706; font-weight: 700;">${cDev} ⚡</span> • 
              <span style="color: #dc2626; font-weight: 700;">${cSupp} ⚠️</span>
            </span>
          </div>
          <div style="display: flex; height: 8px; border-radius: 4px; overflow: hidden; background: rgba(148, 163, 184, 0.2);">
            ${clusterTeachers.length > 0 ? `
              <div style="width: ${(cChamp / clusterTeachers.length) * 100}%; background: var(--accent-emerald);" title="Champions: ${cChamp}"></div>
              <div style="width: ${(cProf / clusterTeachers.length) * 100}%; background: var(--peepul-teal);" title="Proficient: ${cProf}"></div>
              <div style="width: ${(cDev / clusterTeachers.length) * 100}%; background: #d97706;" title="Developing: ${cDev}"></div>
              <div style="width: ${(cSupp / clusterTeachers.length) * 100}%; background: #dc2626;" title="Support Needed: ${cSupp}"></div>
            ` : '<div style="width: 100%; background: var(--text-muted);"></div>'}
          </div>
        </div>

        <!-- Matched Peer Champion / Mentees -->
        ${buddyContent}
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
