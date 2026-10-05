function updateKPIs() {
      const isHi = (currentLang === 'hi');
      const t = translations[currentLang] || translations.en;

      const kDist = document.getElementById('kpiDistricts');
      const kDistDesc = document.getElementById('kpiDistDesc');
      const kReach = document.getElementById('kpiReach');
      const kReachDesc = document.getElementById('kpiReachDesc');
      const kReachBadge = document.getElementById('kpiReachBadge');

      const kTeach = document.getElementById('kpiTeachers');
      const kTeachDesc = document.getElementById('kpiTeachersDesc');
      const kTeachBadge = document.getElementById('kpiTeacherTurnoutBadge');
      const kDoOff = document.getElementById('kpiDoOfficers');
      const kDoOffDesc = document.getElementById('kpiDoOfficersDesc');
      const kCadre = document.getElementById('kpiCadre');
      const kCadreDesc = document.getElementById('kpiCadreDesc');

      if (kDistDesc) kDistDesc.innerText = t.kpiDistDesc;

      if (activeProgram === 'DO') {
        if (kReachBadge) kReachBadge.innerText = '48 DIETs';
        animateValue('kpiReach', 0, 48);
        if (kReachDesc) kReachDesc.innerText = isHi ? 'जिला संसाधन केंद्र (48 डायट)' : 'District Resource Centers (48 DIETs)';

        if (activeRole === 'Participant') {
          animateValue('kpiTeachers', 0, 0);
          if (kTeachDesc) kTeachDesc.innerText = isHi ? 'डीओ में कोई कक्षा शिक्षक नहीं' : 'No Classroom Teachers in DO';
          if (kTeachBadge) kTeachBadge.innerText = '0.0%';
          animateValue('kpiDoOfficers', 0, 4454);
          if (kDoOffDesc) kDoOffDesc.innerText = isHi ? 'सक्रिय डीओ प्रतिभागी (4,454)' : 'Active DO Participants (4,454)';
          animateValue('kpiCadre', 0, 0);
          if (kCadreDesc) kCadreDesc.innerText = isHi ? 'प्रशिक्षक बाहर किए गए' : 'Trainers Sliced Out';
        } else if (activeRole === 'Facilitator') {
          animateValue('kpiTeachers', 0, 0);
          if (kTeachDesc) kTeachDesc.innerText = isHi ? 'डीओ में कोई कक्षा शिक्षक नहीं' : 'No Classroom Teachers in DO';
          if (kTeachBadge) kTeachBadge.innerText = '0.0%';
          animateValue('kpiDoOfficers', 0, 0);
          if (kDoOffDesc) kDoOffDesc.innerText = isHi ? 'प्रतिभागी बाहर किए गए' : 'Participants Sliced Out';
          animateValue('kpiCadre', 0, 77);
          if (kCadreDesc) kCadreDesc.innerText = isHi ? 'डीओ मास्टर फैसिलिटेटर' : 'DO Master Facilitators';
        } else if (activeRole === 'Observer') {
          animateValue('kpiTeachers', 0, 0);
          if (kTeachDesc) kTeachDesc.innerText = isHi ? 'डीओ में कोई कक्षा शिक्षक नहीं' : 'No Classroom Teachers in DO';
          if (kTeachBadge) kTeachBadge.innerText = '0.0%';
          animateValue('kpiDoOfficers', 0, 0);
          if (kDoOffDesc) kDoOffDesc.innerText = isHi ? 'प्रतिभागी बाहर किए गए' : 'Participants Sliced Out';
          animateValue('kpiCadre', 0, 56);
          if (kCadreDesc) kCadreDesc.innerText = isHi ? 'डीओ पर्यवेक्षक / मॉनिटर' : 'DO Observers / Monitors';
        } else {
          animateValue('kpiTeachers', 0, 0);
          if (kTeachDesc) kTeachDesc.innerText = isHi ? 'डीओ में कोई कक्षा शिक्षक नहीं' : 'No Classroom Teachers in DO';
          if (kTeachBadge) kTeachBadge.innerText = '0.0%';
          animateValue('kpiDoOfficers', 0, 4454);
          if (kDoOffDesc) kDoOffDesc.innerText = isHi ? 'जिला प्रतिभागी (DO)' : 'District Participants (DO)';
          animateValue('kpiCadre', 0, 133);
          if (kCadreDesc) kCadreDesc.innerText = isHi ? '77 फैसिलिटेटर + 56 मॉनिटर' : '77 Fac. + 56 Observers';
        }
        const topTitle = document.getElementById('overviewTopChartTitle');
        if (topTitle) topTitle.innerText = t.ovTopTitleDO;
      } else if (activeProgram === 'CLSS') {
        if (kReachBadge) kReachBadge.innerText = '92.0%';
        animateValue('kpiReach', 0, 2851);
        if (kReachDesc) kReachDesc.innerText = isHi ? 'संकुल केंद्र (312 ब्लॉक)' : 'CRC Clusters (312 Blocks)';

        if (activeRole === 'Participant') {
          animateValue('kpiTeachers', 0, 23785);
          if (kTeachDesc) kTeachDesc.innerText = isHi ? '23,785 वास्तविक / 35,374 अपेक्षित शिक्षक' : '23,785 Actual / 35,374 Expected Teachers';
          if (kTeachBadge) kTeachBadge.innerText = '67.2%';
          animateValue('kpiDoOfficers', 0, 0);
          if (kDoOffDesc) kDoOffDesc.innerText = isHi ? 'डीओ शैक्षिक संवाद में नहीं' : 'DO Not in CLSS Scope';
          animateValue('kpiCadre', 0, 0);
          if (kCadreDesc) kCadreDesc.innerText = isHi ? 'कैडर बाहर किया गया' : 'Cadre Sliced Out';
        } else if (activeRole === 'Facilitator') {
          animateValue('kpiTeachers', 0, 0);
          if (kTeachDesc) kTeachDesc.innerText = isHi ? 'शिक्षक बाहर किए गए' : 'Teachers Sliced Out';
          if (kTeachBadge) kTeachBadge.innerText = '-';
          animateValue('kpiDoOfficers', 0, 0);
          if (kDoOffDesc) kDoOffDesc.innerText = isHi ? 'डीओ शैक्षिक संवाद में नहीं' : 'DO Not in CLSS Scope';
          animateValue('kpiCadre', 0, 4841);
          if (kCadreDesc) kCadreDesc.innerText = isHi ? 'शैक्षिक संवाद मास्टर फैसिलिटेटर' : 'CLSS Master Facilitators';
        } else if (activeRole === 'Observer') {
          animateValue('kpiTeachers', 0, 0);
          if (kTeachDesc) kTeachDesc.innerText = isHi ? 'शिक्षक बाहर किए गए' : 'Teachers Sliced Out';
          if (kTeachBadge) kTeachBadge.innerText = '-';
          animateValue('kpiDoOfficers', 0, 0);
          if (kDoOffDesc) kDoOffDesc.innerText = isHi ? 'डीओ शैक्षिक संवाद में नहीं' : 'DO Not in CLSS Scope';
          animateValue('kpiCadre', 0, 516);
          if (kCadreDesc) kCadreDesc.innerText = isHi ? 'शैक्षिक संवाद पर्यवेक्षक' : 'CLSS Field Observers';
        } else {
          animateValue('kpiTeachers', 0, 23785);
          if (kTeachDesc) kTeachDesc.innerText = isHi ? '23,785 वास्तविक / 35,374 अपेक्षित शिक्षक' : '23,785 Actual / 35,374 Expected Teachers';
          if (kTeachBadge) kTeachBadge.innerText = '67.2%';
          animateValue('kpiDoOfficers', 0, 0);
          if (kDoOffDesc) kDoOffDesc.innerText = isHi ? 'डीओ शैक्षिक संवाद में नहीं' : 'DO Not in CLSS Scope';
          animateValue('kpiCadre', 0, 5357);
          if (kCadreDesc) kCadreDesc.innerText = isHi ? '4,841 फैसिलिटेटर + 516 मॉनिटर' : '4,841 Fac. + 516 Observers';
        }
        const topTitle = document.getElementById('overviewTopChartTitle');
        if (topTitle) topTitle.innerText = t.ovTopTitleCLSS;
      } else {
        // Consolidated ('ALL') Program View
        if (kReachBadge) kReachBadge.innerText = isHi ? 'राज्य कुल' : 'State Total';
        animateValue('kpiReach', 0, 2851);
        if (kReachDesc) kReachDesc.innerText = isHi ? 'संकुल केंद्र + 48 डायट स्थल' : 'Clusters + 48 DIET Venues';

        if (activeRole === 'Participant') {
          animateValue('kpiTeachers', 0, 23785);
          if (kTeachDesc) kTeachDesc.innerText = isHi ? '23,785 वास्तविक / 35,374 अपेक्षित शिक्षक' : '23,785 Actual / 35,374 Expected Teachers';
          if (kTeachBadge) kTeachBadge.innerText = '67.2%';
          animateValue('kpiDoOfficers', 0, 4454);
          if (kDoOffDesc) kDoOffDesc.innerText = isHi ? '4,454 जिला प्रतिभागी (DO)' : '4,454 District Participants (DO)';
          animateValue('kpiCadre', 0, 0);
          if (kCadreDesc) kCadreDesc.innerText = isHi ? 'प्रशिक्षक बाहर किए गए' : 'Trainers Sliced Out';
        } else if (activeRole === 'Facilitator') {
          animateValue('kpiTeachers', 0, 0);
          if (kTeachDesc) kTeachDesc.innerText = isHi ? 'शिक्षक बाहर किए गए' : 'Teachers Sliced Out';
          if (kTeachBadge) kTeachBadge.innerText = '-';
          animateValue('kpiDoOfficers', 0, 4454);
          if (kDoOffDesc) kDoOffDesc.innerText = isHi ? '4,454 जिला प्रतिभागी (DO)' : '4,454 District Participants (DO)';
          animateValue('kpiCadre', 0, 4918);
          if (kCadreDesc) kCadreDesc.innerText = isHi ? '4,841 शैक्षिक संवाद + 77 डीओ फैसिलिटेटर' : '4,841 CLSS + 77 DO Facilitators';
        } else if (activeRole === 'Observer') {
          animateValue('kpiTeachers', 0, 0);
          if (kTeachDesc) kTeachDesc.innerText = isHi ? 'शिक्षक बाहर किए गए' : 'Teachers Sliced Out';
          if (kTeachBadge) kTeachBadge.innerText = '-';
          animateValue('kpiDoOfficers', 0, 0);
          if (kDoOffDesc) kDoOffDesc.innerText = isHi ? 'प्रतिभागी बाहर किए गए' : 'Participants Sliced Out';
          animateValue('kpiCadre', 0, 572);
          if (kCadreDesc) kCadreDesc.innerText = isHi ? '516 शैक्षिक संवाद + 56 डीओ मॉनिटर' : '516 CLSS + 56 DO Observers';
        } else {
          animateValue('kpiTeachers', 0, 23785);
          if (kTeachDesc) kTeachDesc.innerText = isHi ? '23,785 वास्तविक / 35,374 अपेक्षित शिक्षक' : '23,785 Actual / 35,374 Expected Teachers';
          if (kTeachBadge) kTeachBadge.innerText = '67.2%';
          animateValue('kpiDoOfficers', 0, 4454);
          if (kDoOffDesc) kDoOffDesc.innerText = isHi ? 'जिला प्रतिभागी (DO)' : 'District Participants (DO)';
          animateValue('kpiCadre', 0, 5490);
          if (kCadreDesc) kCadreDesc.innerText = isHi ? '4,918 फैसिलिटेटर + 572 मॉनिटर' : '4,918 Fac. + 572 Monitors';
        }
        const topTitle = document.getElementById('overviewTopChartTitle');
        if (topTitle) topTitle.innerText = t.ovTopTitleALL;
      }
    }

    function updateBlockView() {
      const notice = document.getElementById('blockNotice');
      if (notice) {
        notice.style.display = (activeProgram === 'DO') ? 'block' : 'none';
      }
    }

    function animateValue(elemId, start, end, duration = 450, suffix = '') {
      const obj = document.getElementById(elemId);
      if (!obj) return;
      if (window.Motion && window.Motion.animate) {
        window.Motion.animate(start, end, {
          duration: duration / 1000,
          ease: [0.16, 1, 0.3, 1],
          onUpdate: (latest) => {
            obj.innerText = Math.round(latest).toLocaleString() + suffix;
          }
        });
      } else {
        obj.innerText = end.toLocaleString() + suffix;
      }
    }

    function activateTab(tabId, el) {
      document.querySelectorAll('.tab-section').forEach(s => s.classList.remove('active'));
      document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
      const activeSec = document.getElementById(tabId);
      if (activeSec) activeSec.classList.add('active');
      if (el) el.classList.add('active');

      if (window.Motion && window.Motion.animate && activeSec) {
        const targets = activeSec.querySelectorAll('.bento-card, .chart-card, .panel-box, .ind-card');
        if (targets.length > 0) {
          window.Motion.animate(targets, { opacity: [0.75, 1] }, { duration: 0.22, ease: [0.16, 1, 0.3, 1] });
        }
      }

      if (tabId === 'tab-rf') {
        selectRFIndicator(activeRFIndicatorId);
        if (typeof renderRFIndicatorCards === 'function') renderRFIndicatorCards();
        if (typeof initRFMatrixTable === 'function') initRFMatrixTable();
      } else if (tabId === 'tab-d360') {
        updateDistrict360View();
        updateDistrictComparison();
      } else if (tabId === 'tab-questions') {
        renderQuestionBankActive();
      } else if (tabId === 'tab-league') {
        initDistrictLeague();
      } else if (tabId === 'tab-blocks') {
        filterBlockDirectory();
      } else if (tabId === 'tab-pedagogy') {
        initPedagogyRadar();
      } else if (tabId === 'tab-overview') {
        initOverviewCharts();
        populateQuadrantBentoCards();
      }
    }

    function getChartTheme