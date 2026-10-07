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

GUIDE_BUTTON_HTML = """<button class="btn-tactile" onclick="toggleDashboardGuide(true)" style="background: linear-gradient(135deg, rgba(37,99,235,0.18) 0%, rgba(79,70,229,0.18) 100%); border: 1.5px solid #2563eb; color: #1d4ed8; font-weight: 800; font-size: 11.5px; padding: 6px 14px; border-radius: 6px; cursor: pointer; transition: all 0.2s ease;">
        📖 User Guide / मार्गदर्शिका
      </button>"""

GUIDE_DRAWER_HTML = """
<!-- ========================================================================= -->
<!-- 📖 INTERACTIVE BILINGUAL DASHBOARD USER GUIDE DRAWER & HELP CENTER       -->
<!-- ========================================================================= -->
<div id="guideDrawerOverlay" onclick="toggleDashboardGuide(false)" style="display: none; position: fixed; inset: 0; background: rgba(15, 23, 42, 0.65); backdrop-filter: blur(4px); z-index: 9998; transition: opacity 0.3s ease;"></div>

<aside id="guideDrawer" style="position: fixed; top: 0; right: -640px; width: 620px; max-width: 94vw; height: 100vh; background: var(--bg-surface-card); border-left: 1px solid var(--border-subtle); box-shadow: -8px 0 36px rgba(0,0,0,0.3); z-index: 9999; display: flex; flex-direction: column; transition: right 0.32s cubic-bezier(0.16, 1, 0.3, 1); overflow: hidden;">
  
  <!-- Drawer Header -->
  <div style="padding: 18px 22px; border-bottom: 1px solid var(--border-subtle); background: var(--bg-surface-2); display: flex; align-items: center; justify-content: space-between; gap: 12px;">
    <div>
      <div style="display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 20px;">📖</span>
        <h3 id="guideDrawerTitle" style="margin: 0; font-size: 16px; font-weight: 800; color: var(--text-primary); font-family: var(--font-brand);">
          Dashboard User Guide &amp; Reference Manual
        </h3>
      </div>
      <div id="guideDrawerSub" style="font-size: 11px; color: var(--text-muted); font-family: var(--font-mono); margin-top: 2px;">
        Complete Bilingual Guide for Tabs, Slicers, Graphs &amp; Metrics
      </div>
    </div>
    <div style="display: flex; align-items: center; gap: 8px;">
      <div style="display: flex; background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 6px; padding: 2px;">
        <button class="slicer-pill active" id="btnGuideLangEn" onclick="toggleGuideLang('en')" style="padding: 3px 8px; font-size: 11px; font-weight: 700;">EN</button>
        <button class="slicer-pill" id="btnGuideLangHi" onclick="toggleGuideLang('hi')" style="padding: 3px 8px; font-size: 11px; font-weight: 700;">हिन्दी</button>
      </div>
      <button onclick="toggleDashboardGuide(false)" style="background: none; border: none; font-size: 18px; cursor: pointer; color: var(--text-muted); padding: 4px 8px; border-radius: 4px;">✕</button>
    </div>
  </div>

  <!-- Search Filter & Quick Actions -->
  <div style="padding: 12px 22px; background: var(--bg-surface-1); border-bottom: 1px solid var(--border-hairline); display: flex; gap: 10px; align-items: center;">
    <div style="position: relative; flex: 1;">
      <input type="text" id="guideSearchInput" oninput="filterGuideCards()" placeholder="🔍 Search tabs, slicers, graphs, formulas... (खोजें)" style="width: 100%; padding: 7px 12px; font-size: 12px; border: 1px solid var(--border-subtle); border-radius: 6px; background: var(--bg-canvas); color: var(--text-primary); outline: none;">
    </div>
    <a href="docs/RSK_Master_Dashboard_Complete_Bilingual_User_Guide.pdf" target="_blank" style="text-decoration: none; padding: 6px 12px; font-size: 11.5px; font-weight: 700; background: var(--peepul-teal); color: #ffffff; border-radius: 6px; white-space: nowrap; display: inline-flex; align-items: center; gap: 4px;">
      📥 PDF Guide
    </a>
  </div>

  <!-- Scrollable Guide Content -->
  <div id="guideContentBody" style="flex: 1; overflow-y: auto; padding: 18px 22px; display: flex; flex-direction: column; gap: 16px;">
    
    <!-- Guide Topic 1: Global Slicers -->
    <div class="guide-card" data-keywords="slicer cycle august september consolidated role cadre district block month language भाषा स्लाइसर" style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 14px 16px;">
      <div style="font-weight: 800; font-size: 13.5px; color: var(--peepul-teal); margin-bottom: 6px; display: flex; align-items: center; gap: 6px;">
        <span>📅 Global Slicers &amp; Filters / ग्लोबल स्लाइसर और फिल्टर</span>
      </div>
      <div class="guide-text-en" style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        • <strong>Cycle Slicer:</strong> Toggle between <em>August</em>, <em>September</em>, and <em>Consolidated (Aug + Sep)</em>. Consolidated mode combines multi-cycle data and calculates unique deduplicated reach (49.5% Net Reach).<br/>
        • <strong>Cadre/Role Slicer:</strong> Isolates Teachers (👨‍🏫), Facilitators (🤝), or Monitors (👁️).<br/>
        • <strong>District &amp; Block Dropdowns:</strong> Drill down from state aggregates to any of the 52 districts or 322 blocks.<br/>
        • <strong>Language Toggle:</strong> Instant switch between English and Hindi.
      </div>
      <div class="guide-text-hi" style="display: none; font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        • <strong>मासिक चक्र स्लाइसर:</strong> <em>अगस्त</em>, <em>सितंबर</em> और <em>समेकित (Consolidated)</em> के बीच चयन करें। समेकित मोड शिक्षक आईडी द्वारा दोहराव हटाकर वास्तविक यूनिक पहुंच (49.5%) दिखाता है।<br/>
        • <strong>संवर्ग/पद स्लाइसर:</strong> शिक्षक, सहजकर्ता या जनशिक्षक/अवलोकनकर्ता के आधार पर डेटा फ़िल्टर करें।<br/>
        • <strong>जिला व ब्लॉक ड्रॉपडाउन:</strong> राज्य स्तर से किसी भी 52 जिलों या 322 विकासखंडों की व्यक्तिगत रिपोर्ट देखें।<br/>
        • <strong>भाषा बटन:</strong> अंग्रेजी व हिंदी के बीच तुरंत भाषा बदलें।
      </div>
    </div>

    <!-- Guide Topic 2: Tab 1 Overview -->
    <div class="guide-card" data-keywords="overview summary kpi reach gross net unique venues cards tab 1 समग्र अवलोकन" style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 14px 16px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
        <span style="font-weight: 800; font-size: 13.5px; color: var(--text-primary);">📊 Tab 1: Overview &amp; Summary / समग्र अवलोकन</span>
        <button onclick="jumpToTabFromGuide('tab-overview')" style="font-size: 11px; padding: 2px 8px; border-radius: 4px; background: rgba(0,138,171,0.1); color: var(--peepul-teal); border: 1px solid rgba(0,138,171,0.3); font-weight: 700; cursor: pointer;">Open Tab ➔</button>
      </div>
      <div class="guide-text-en" style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        Executive state dashboard displaying the 6 Core KPI Ribbon Cards: <strong>Coverage Rate</strong> (100%), <strong>Training Venues</strong> (3,018 Gross | 3,066 Unique), <strong>Attending Teachers</strong> (46,954 Gross | 33,866 Net Unique), <strong>District Orientation Leaders</strong> (8,888 Gross | 6,272 Unique), <strong>Master Facilitators</strong> (6,658 Unique), and <strong>Varg-2 Teacher Universe</strong> (68,427 Base).
      </div>
      <div class="guide-text-hi" style="display: none; font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        राज्य स्तरीय सारांश जो 6 मुख्य केपीआई कार्ड प्रदर्शित करता है: <strong>कवरेज दर</strong> (100%), <strong>प्रशिक्षण केंद्र</strong> (3,066 यूनिक), <strong>उपस्थित शिक्षक</strong> (46,954 कुल | 33,866 यूनिक), <strong>जिला उन्मुखीकरण</strong> (6,272 यूनिक अधिकारी), <strong>सहजकर्ता संवर्ग</strong> (6,658), और <strong>वर्ग-2 शिक्षक आधार</strong> (68,427 कुल शिक्षक)।
      </div>
    </div>

    <!-- Guide Topic 3: Tab 2 RF Matrix -->
    <div class="guide-card" data-keywords="rf risk friction matrix goals targets tab 2 लक्ष्य जोखिम" style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 14px 16px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
        <span style="font-weight: 800; font-size: 13.5px; color: var(--text-primary);">🎯 Tab 2: Key Goals &amp; RF Matrix / लक्ष्य व जोखिम</span>
        <button onclick="jumpToTabFromGuide('tab-rf')" style="font-size: 11px; padding: 2px 8px; border-radius: 4px; background: rgba(0,138,171,0.1); color: var(--peepul-teal); border: 1px solid rgba(0,138,171,0.3); font-weight: 700; cursor: pointer;">Open Tab ➔</button>
      </div>
      <div class="guide-text-en" style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        Maps strategic program milestones against the 2x2 <strong>Risk &amp; Friction Matrix</strong>. Identifies operational friction points (cluster travel distance, guide availability) and pedagogical risks.
      </div>
      <div class="guide-text-hi" style="display: none; font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        रणनीतिक लक्ष्यों की प्रगति और 2x2 <strong>जोखिम व घर्षण मैट्रिक्स (RF Matrix)</strong> प्रदर्शित करता है। संकुल स्तर पर यात्रा की दूरी, समय पर सामग्री उपलब्धता और शैक्षणिक बाधाओं का विश्लेषण।
      </div>
    </div>

    <!-- Guide Topic 4: Tab 3 District Profile & Radar -->
    <div class="guide-card" data-keywords="district profile radar spider 360 diagnostic turnout target tab 3 जिला प्रोफाइल" style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 14px 16px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
        <span style="font-weight: 800; font-size: 13.5px; color: var(--text-primary);">🔍 Tab 3: District Profile (360° Explorer) / जिला प्रोफाइल</span>
        <button onclick="jumpToTabFromGuide('tab-d360')" style="font-size: 11px; padding: 2px 8px; border-radius: 4px; background: rgba(0,138,171,0.1); color: var(--peepul-teal); border: 1px solid rgba(0,138,171,0.3); font-weight: 700; cursor: pointer;">Open Tab ➔</button>
      </div>
      <div class="guide-text-en" style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        Interactive 360° deep-dive for any selected district. Features the <strong>5-Spoke Stakeholder Radar Chart</strong> plotting Attendance, Facilitator Preparedness, Monitor Visits, Pedagogical Clarity, and Venue Utilization.
      </div>
      <div class="guide-text-hi" style="display: none; font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        चुने गए जिले का 360° सम्पूर्ण विश्लेषण। इसमें <strong>5-धुरी वाला रडार चार्ट (Radar Chart)</strong> शामिल है जो शिक्षक उपस्थिति, सहजकर्ता तैयारी, मॉनिटरिंग भ्रमण, शैक्षणिक स्पष्टता और केंद्र उपयोगिता को मापता है।
      </div>
    </div>

    <!-- Guide Topic 5: Tab 4 District Rankings & Quadrants -->
    <div class="guide-card" data-keywords="rankings league quadrants q1 q2 q3 q4 performance leaderboard tab 4 जिला रैंकिंग" style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 14px 16px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
        <span style="font-weight: 800; font-size: 13.5px; color: var(--text-primary);">🗺️ Tab 4: District Rankings &amp; Quadrants / रैंकिंग व क्वाड्रेंट</span>
        <button onclick="jumpToTabFromGuide('tab-league')" style="font-size: 11px; padding: 2px 8px; border-radius: 4px; background: rgba(0,138,171,0.1); color: var(--peepul-teal); border: 1px solid rgba(0,138,171,0.3); font-weight: 700; cursor: pointer;">Open Tab ➔</button>
      </div>
      <div class="guide-text-en" style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        Ranks all 52 districts by turnout and saturation. Classifies districts into <strong>4 Strategic Quadrants</strong>: Q1 Benchmark Models (22 Dist), Q2 Resilient Frontier (11 Dist), Q3 Critical Bottlenecks (14 Dist), and Q4 Under-Leveraged (5 Dist).
      </div>
      <div class="guide-text-hi" style="display: none; font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        सभी 52 जिलों की उपस्थिति व संतृप्ति दर के आधार पर रैंकिंग। जिलों को <strong>4 रणनीतिक श्रेणियों</strong> में वर्गीकृत किया गया है: Q1 मॉडल जिले (22), Q2 दुर्गम व सक्रिय जिले (11), Q3 चुनौतीपूर्ण जिले (14), और Q4 सुस्त जिले (5)।
      </div>
    </div>

    <!-- Guide Topic 6: Tab 5 Block Directory -->
    <div class="guide-card" data-keywords="blocks block directory table search csv export 322 blocks tab 5 ब्लॉक डायरेक्टरी" style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 14px 16px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
        <span style="font-weight: 800; font-size: 13.5px; color: var(--text-primary);">🏢 Tab 5: Block Directory (322 Blocks) / ब्लॉक डायरेक्टरी</span>
        <button onclick="jumpToTabFromGuide('tab-blocks')" style="font-size: 11px; padding: 2px 8px; border-radius: 4px; background: rgba(0,138,171,0.1); color: var(--peepul-teal); border: 1px solid rgba(0,138,171,0.3); font-weight: 700; cursor: pointer;">Open Tab ➔</button>
      </div>
      <div class="guide-text-en" style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        Granular searchable database of all 322 blocks in MP. Filter by block name or district, view monitors, facilitators, teachers attending, universe saturation %, and export to CSV.
      </div>
      <div class="guide-text-hi" style="display: none; font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        मध्य प्रदेश के सभी 322 विकासखंडों का विस्तृत सर्च करने योग्य डेटाबेस। ब्लॉक नाम या जिले से खोजें, शिक्षक उपस्थिति व संतृप्ति देखें, और एक्सेल/CSV में डाउनलोड करें।
      </div>
    </div>

    <!-- Guide Topic 7: Tab 7 Pedagogy & Misconceptions -->
    <div class="guide-card" data-keywords="pedagogy teaching quality math science fractions heat misconceptions facilitators tab 7 शिक्षाशास्त्र" style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 14px 16px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
        <span style="font-weight: 800; font-size: 13.5px; color: var(--text-primary);">🧠 Tab 7: Teaching Quality &amp; Pedagogy / शिक्षण गुणवत्ता</span>
        <button onclick="jumpToTabFromGuide('tab-pedagogy')" style="font-size: 11px; padding: 2px 8px; border-radius: 4px; background: rgba(0,138,171,0.1); color: var(--peepul-teal); border: 1px solid rgba(0,138,171,0.3); font-weight: 700; cursor: pointer;">Open Tab ➔</button>
      </div>
      <div class="guide-text-en" style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        Evaluates classroom pedagogical translation across 5 subject domains (State Baseline: 58.4%). Breaks down key misconceptions in <strong>Fraction Division (38.2% error)</strong> and <strong>Thermodynamics (42.1% error)</strong>, and highlights the Master Facilitator multiplier (+18.4% engagement).
      </div>
      <div class="guide-text-hi" style="display: none; font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        कक्षा शिक्षण गुणवत्ता का 5 मुख्य विषयों में मूल्यांकन (राज्य औसत: 58.4%)। <strong>भिन्न विभाजन (38.2% त्रुटि)</strong> और <strong>ऊष्मा व तापमान (42.1% त्रुटि)</strong> में शिक्षकों की सामान्य भ्रांतियों का विश्लेषण और मास्टर सहजकर्ताओं का प्रभाव।
      </div>
    </div>

    <!-- Guide Topic 8: Tab 9 AI Insights & Roadmap -->
    <div class="guide-card" data-keywords="ai insights strategic dossier roadmap 30 60 90 recommendations pmu tab 9 एआई अंतर्दृष्टि" style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 14px 16px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
        <span style="font-weight: 800; font-size: 13.5px; color: var(--text-primary);">🤖 Tab 9: AI Insights &amp; Roadmap / रणनीतिक डॉसियर</span>
        <button onclick="jumpToTabFromGuide('tab-insights')" style="font-size: 11px; padding: 2px 8px; border-radius: 4px; background: rgba(0,138,171,0.1); color: var(--peepul-teal); border: 1px solid rgba(0,138,171,0.3); font-weight: 700; cursor: pointer;">Open Tab ➔</button>
      </div>
      <div class="guide-text-en" style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        State strategic intelligence hub containing the Reconciled Multi-Cycle Telemetry Matrix, Dual-Metric Policy Paradigm analysis, and the <strong>Actionable 30–60–90 Day Operational Roadmap</strong> for RSK leadership.
      </div>
      <div class="guide-text-hi" style="display: none; font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        राज्य स्तरीय रणनीतिक डॉसियर जिसमें समेकित टेलीमेट्री मैट्रिक्स, दोहरी-मैट्रिक्स नीति विश्लेषण, और राज्य नेतृत्व के लिए <strong>30-60-90 दिवसीय कार्य योजना (Roadmap)</strong> शामिल है।
      </div>
    </div>

    <!-- Guide Topic 9: Tab 11 Teacher Cohorts & Retention -->
    <div class="guide-card" data-keywords="cohorts retention champions fresh intake dropouts trajectory model tab 11 शिक्षक निरंतरता" style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 14px 16px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
        <span style="font-weight: 800; font-size: 13.5px; color: var(--text-primary);">👥 Tab 11: Teacher Cohorts &amp; Retention / शिक्षक निरंतरता</span>
        <button onclick="jumpToTabFromGuide('tab-cohort')" style="font-size: 11px; padding: 2px 8px; border-radius: 4px; background: rgba(0,138,171,0.1); color: var(--peepul-teal); border: 1px solid rgba(0,138,171,0.3); font-weight: 700; cursor: pointer;">Open Tab ➔</button>
      </div>
      <div class="guide-text-en" style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        Longitudinal teacher tracking: <strong>13,088 Repeat Champions</strong> (55.0% retention), <strong>10,081 Fresh Intake</strong> in Sep, and <strong>10,697 Single-Session Dropouts</strong>. Includes the Mathematical Saturation Trajectory Model forecasting 81.5% unique reach by Dec 2026.
      </div>
      <div class="guide-text-hi" style="display: none; font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        शिक्षकों की मासिक निरंतरता ट्रैकर: <strong>13,088 नियमित शिक्षक (Repeat Champions)</strong> (55.0% प्रतिधारण), <strong>10,081 नए शिक्षक</strong>, और <strong>10,697 फॉलो-अप वाले शिक्षक</strong>। साथ ही दिसंबर तक 81.5% पहुंच का गणितीय मॉडल।
      </div>
    </div>

    <!-- Guide Topic 10: Formulas & Metrics -->
    <div class="guide-card" data-keywords="formulas metrics calculations saturation math सूत्र गणना प्रतिशत" style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 14px 16px;">
      <div style="font-weight: 800; font-size: 13.5px; color: #1d4ed8; margin-bottom: 6px;">
        📐 Key Calculation Formulas / मुख्य गणना सूत्र
      </div>
      <div class="guide-text-en" style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        • <strong>Universe Saturation %:</strong> <code>(CLSS Teachers / 68,427) × 100</code>.<br/>
        • <strong>Gross vs Net Unique:</strong> Gross counts total session touchpoints (46,954); Net counts deduplicated individual teachers (33,866 = 49.5% Reach).<br/>
        • <strong>Retention Rate %:</strong> <code>(13,088 Repeat Champions / 23,785 August Base) × 100 = 55.0%</code>.
      </div>
      <div class="guide-text-hi" style="display: none; font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
        • <strong>संतृप्ति दर (Saturation %):</strong> <code>(उपस्थित शिक्षक / 68,427 कुल शिक्षक) × 100</code>.<br/>
        • <strong>कुल बनाम यूनिक पहुंच:</strong> कुल उपस्थिति में दोनों महीनों का योग (46,954) शामिल है; यूनिक पहुंच में विशिष्ट शिक्षकों की संख्या (33,866 = 49.5%) गिनी जाती है।<br/>
        • <strong>प्रतिधारण दर (Retention %):</strong> <code>(13,088 नियमित शिक्षक / 23,785 अगस्त उपस्थिति) × 100 = 55.0%</code>.
      </div>
    </div>

  </div>

</aside>

<script>
  function toggleDashboardGuide(show) {
    const drawer = document.getElementById('guideDrawer');
    const overlay = document.getElementById('guideDrawerOverlay');
    if (!drawer || !overlay) return;
    if (show) {
      overlay.style.display = 'block';
      setTimeout(() => {
        overlay.style.opacity = '1';
        drawer.style.right = '0px';
      }, 10);
    } else {
      overlay.style.opacity = '0';
      drawer.style.right = '-640px';
      setTimeout(() => { overlay.style.display = 'none'; }, 320);
    }
  }

  function toggleGuideLang(lang) {
    const btnEn = document.getElementById('btnGuideLangEn');
    const btnHi = document.getElementById('btnGuideLangHi');
    if (btnEn) btnEn.classList.toggle('active', lang === 'en');
    if (btnHi) btnHi.classList.toggle('active', lang === 'hi');

    document.querySelectorAll('.guide-text-en').forEach(el => el.style.display = (lang === 'en' ? 'block' : 'none'));
    document.querySelectorAll('.guide-text-hi').forEach(el => el.style.display = (lang === 'hi' ? 'block' : 'none'));

    const titleEl = document.getElementById('guideDrawerTitle');
    const subEl = document.getElementById('guideDrawerSub');
    if (titleEl) titleEl.innerText = (lang === 'hi' ? 'डैशबोर्ड उपयोगकर्ता मार्गदर्शिका' : 'Dashboard User Guide & Reference Manual');
    if (subEl) subEl.innerText = (lang === 'hi' ? 'सभी 11 टैब, स्लाइसर, चार्ट व मैट्रिक्स की द्विभाषी गाइड' : 'Complete Bilingual Guide for Tabs, Slicers, Graphs & Metrics');
  }

  function filterGuideCards() {
    const query = (document.getElementById('guideSearchInput')?.value || '').toLowerCase().trim();
    document.querySelectorAll('.guide-card').forEach(card => {
      const keywords = (card.getAttribute('data-keywords') || '').toLowerCase();
      const text = card.innerText.toLowerCase();
      card.style.display = (keywords.includes(query) || text.includes(query)) ? 'block' : 'none';
    });
  }

  function jumpToTabFromGuide(tabId) {
    toggleDashboardGuide(false);
    if (typeof activateTab === 'function') {
      const btn = document.querySelector(`button[onclick*="${tabId}"]`);
      activateTab(tabId, btn);
    } else if (typeof switchTab === 'function') {
      switchTab(tabId);
    }
  }
</script>
"""

def inject_guide_into_file(filepath):
    print(f"[*] Processing {filepath}...", flush=True)
    if not os.path.exists(filepath):
        print(f"[-] File not found: {filepath}")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject Guide button next to Briefing button
    if 'User Guide / मार्गदर्शिका' not in content:
        # Match briefing button container
        pattern = r'(<button class="btn-tactile"[^>]*onclick="toggleBriefingDrawer\(true\)"[^>]*>[\s\S]*?</button>)'
        match = re.search(pattern, content)
        if match:
            new_btn_block = match.group(1) + "\n      " + GUIDE_BUTTON_HTML
            content = content[:match.start()] + new_btn_block + content[match.end():]
            print("  [+] Injected Guide Button into Top Slicer Ribbon")
        else:
            print("  [-] Could not find briefing button to insert guide button next to")

    # 2. Inject Guide Drawer modal right after briefing drawer
    if 'id="guideDrawer"' not in content:
        # Find closing of briefingDrawer: </aside>
        pattern = r'(<aside id="briefingDrawer"[\s\S]*?</aside>)'
        match = re.search(pattern, content)
        if match:
            new_aside_block = match.group(1) + "\n" + GUIDE_DRAWER_HTML
            content = content[:match.start()] + new_aside_block + content[match.end():]
            print("  [+] Injected Guide Drawer Modal & JavaScript Handlers")
        else:
            print("  [-] Could not find briefingDrawer to inject guide drawer after")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[✓] Successfully updated {filepath}")
    return True

def main():
    print("===================================================================")
    print(" Injecting Interactive Bilingual Guide Drawer Across Dashboard Targets")
    print("===================================================================")
    for target in TARGET_FILES:
        inject_guide_into_file(target)
    print("\n[✓] All target files updated with interactive guide drawer!")

if __name__ == '__main__':
    main()
