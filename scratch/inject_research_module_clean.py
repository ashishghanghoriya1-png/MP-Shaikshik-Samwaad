import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('build_enhanced_studio.py', 'r', encoding='utf-8') as f:
    code = f.read()

research_js_definition = '''
    // ==========================================
    // TAB 10: QUALITATIVE RESEARCH MODULE
    // ==========================================
    let currentAbstractLang = 'en';
    let activeResearchTheme = 'ALL';

    const researchQuotesData = [
      {
        theme: 'ACADEMIC',
        themeNameEn: 'Academic Utility & Classroom Application',
        themeNameHi: 'अकादमिक एवं कक्षा अनुप्रयोग',
        quoteHi: 'शैक्षणिक स्तर पर इसका उपयोग करेंगे, बच्चों की जिज्ञासा को ध्यान में रखना चाहिए।',
        quoteEn: 'We will utilize these pedagogical tools at the classroom level, keeping students\\\' innate curiosity at the core.',
        speakerHi: 'माध्यमिक शिक्षक, छिंदवाड़ा',
        speakerEn: 'Middle School Teacher, Chhindwara',
        tag: 'Pedagogy',
        tagColor: 'var(--peepul-teal)'
      },
      {
        theme: 'ACADEMIC',
        themeNameEn: 'Academic Utility & Classroom Application',
        themeNameHi: 'अकादमिक एवं कक्षा अनुप्रयोग',
        quoteHi: 'पाठ योजना निर्माण में सहकर्मियों के अनुभवों से कठिन अवधारणाओं को सरल बनाने में बहुत मदद मिली।',
        quoteEn: 'Shared experiences from peers substantially aided in deconstructing difficult mathematical concepts during lesson planning.',
        speakerHi: 'गणित शिक्षक, सीहोर',
        speakerEn: 'Math Teacher, Sehore',
        tag: 'Lesson Design',
        tagColor: 'var(--peepul-teal)'
      },
      {
        theme: 'JOYFUL',
        themeNameEn: 'Joyful Pedagogies & Student Agency',
        themeNameHi: 'आनंददायी शिक्षण और बच्चों की व्यक्तिगतता',
        quoteHi: 'बच्चों को एक अच्छा माहौल तैयार करने के लिए प्रेरित करना एवं उनके ज्ञान के अनुसार शिक्षण कार्य में व्यस्त रखना।',
        quoteEn: 'Motivating students by establishing an inviting classroom environment and engaging them according to their prior knowledge.',
        speakerHi: 'विज्ञान शिक्षक, देवास',
        speakerEn: 'Science Teacher, Dewas',
        tag: 'Joyful Learning',
        tagColor: '#10b981'
      },
      {
        theme: 'JOYFUL',
        themeNameEn: 'Joyful Pedagogies & Student Agency',
        themeNameHi: 'आनंददायी शिक्षण और बच्चों की व्यक्तिगतता',
        quoteHi: 'गतिविधि-आधारित शिक्षण से बच्चों में झिझक खत्म हुई और वे स्वयं आगे आकर प्रश्न पूछने लगे।',
        quoteEn: 'Activity-based pedagogies dismantled learner hesitation, encouraging students to step forward and ask inquiry questions.',
        speakerHi: 'माध्यमिक शिक्षिका, जबलपुर',
        speakerEn: 'Middle School Teacher, Jabalpur',
        tag: 'Student Agency',
        tagColor: '#10b981'
      },
      {
        theme: 'INFRA',
        themeNameEn: 'Infrastructure & Tech Constraints',
        themeNameHi: 'अधोसंरचना, समय-सारणी एवं तकनीकी बाधाएं',
        quoteHi: 'बिजली और प्रोजेक्टर की समस्या के कारण PPT का पूरा लाभ नहीं मिल सका।',
        quoteEn: 'Due to cluster power outages and projector constraints, the full visual potential of PPT decks could not be realized.',
        speakerHi: 'संकुल समन्वयक (CAC), बड़वानी',
        speakerEn: 'Cluster Academic Coordinator, Barwani',
        tag: 'Hardware Gap',
        tagColor: '#f59e0b'
      },
      {
        theme: 'INFRA',
        themeNameEn: 'Infrastructure & Tech Constraints',
        themeNameHi: 'अधोसंरचना, समय-सारणी एवं तकनीकी बाधाएं',
        quoteHi: 'ग्रामीण क्षेत्रों में नेटवर्क समस्या के कारण सामग्री को ऑफलाइन मोड में उपलब्ध कराना अत्यंत आवश्यक है।',
        quoteEn: 'Given rural connectivity challenges, pre-downloading and caching instructional modules in offline format is essential.',
        speakerHi: 'शिक्षक, डिंडोरी',
        speakerEn: 'Teacher, Dindori',
        tag: 'Digital Offline',
        tagColor: '#f59e0b'
      },
      {
        theme: 'MOTIVATION',
        themeNameEn: 'Practitioner Emotional Topology & Motivation',
        themeNameHi: 'शिक्षकों की भावनात्मक स्थिति एवं प्रेरणा',
        quoteHi: 'संवाद को और अधिक प्रभावी बनाया जाए, बिंदुओं पर अधिक से अधिक चर्चा होना चाहिए।',
        quoteEn: 'The dialogue format should be made even more interactive, dedicating maximum session time to open peer deliberation.',
        speakerHi: 'वरिष्ठ शिक्षक, सागर',
        speakerEn: 'Senior Teacher, Sagar',
        tag: 'Peer Dialogue',
        tagColor: '#8b5cf6'
      },
      {
        theme: 'MOTIVATION',
        themeNameEn: 'Practitioner Emotional Topology & Motivation',
        themeNameHi: 'शिक्षकों की भावनात्मक स्थिति एवं प्रेरणा',
        quoteHi: 'बिना किसी प्रशासनिक दबाव के जब हम अपनी कक्षागत कठिनाइयों पर बात करते हैं, तो आत्मविश्वास बढ़ता है।',
        quoteEn: 'Discussing classroom struggles in a non-evaluative, supportive atmosphere significantly bolsters our pedagogical confidence.',
        speakerHi: 'शिक्षिका, रीवा',
        speakerEn: 'Teacher, Rewa',
        tag: 'Psych Safety',
        tagColor: '#8b5cf6'
      }
    ];

    function toggleAbstractLang(lang) {
      currentAbstractLang = lang || 'en';
      document.getElementById('btnAbstractEn')?.classList.toggle('active', currentAbstractLang === 'en');
      document.getElementById('btnAbstractHi')?.classList.toggle('active', currentAbstractLang === 'hi');

      const box = document.getElementById('resAbstractBox');
      if (!box) return;

      if (currentAbstractLang === 'hi') {
        box.innerHTML = `
          <div style="font-weight: 700; color: var(--peepul-teal); margin-bottom: 6px; font-family: var(--font-mono); font-size: 11px; text-transform: uppercase;">
            📋 हिंदी सारांश (Executive Hindi Abstract):
          </div>
          <p style="margin: 0; text-align: justify;">
            इस शोध पत्र में मध्य प्रदेश के <strong>RSK शिक्षक संवाद कार्यक्रम</strong> का अनुभवजन्य एवं गुणात्मक अध्ययन प्रस्तुत किया गया है, जो भारत में शिक्षकों के सतत व्यावसायिक विकास (CPD) को रूपांतरित करने की एक राज्यव्यापी पहल है। यह कार्यक्रम पारंपरिक शीर्ष-से-नीचे (Cascade) प्रशिक्षण मॉडल से हटकर विकेंद्रीकृत, सहकर्मी-आधारित व्यावसायिक शिक्षण समुदाय (PLC) मॉडल को स्थापित करता है, जो सात मूलभूत डिज़ाइन सिद्धांतों पर आधारित है। <strong>33,702 शिक्षकों एवं अकादमिक नेतृत्वकर्ताओं</strong> (23,785 माध्यमिक शिक्षक, 4,814 संकुल समन्वयक, 4,454 जिला अधिकारी, 572 स्वतंत्र पर्यवेक्षक) के बहु-स्तरीय डेटासेट पर आधारित यह अध्ययन कक्षा शिक्षण में आनंददायी अधिगम और बच्चों की सहभागिता पर पड़े प्रभावों का विश्लेषण करता है। मुख्य निष्कर्ष दर्शाते हैं कि भयमुक्त वातावरण (Psychological Safety), स्व-निर्धारण सिद्धांत (Autonomy, Competence, Relatedness) तथा वाइगोत्स्की के समीपस्थ विकास क्षेत्र (ZPD) पर आधारित सहकर्मी संवाद शिक्षकों की कक्षागत दक्षता में उल्लेखनीय वृद्धि करते हैं।
          </p>
        `;
      } else {
        box.innerHTML = `
          <div style="font-weight: 700; color: var(--peepul-teal); margin-bottom: 6px; font-family: var(--font-mono); font-size: 11px; text-transform: uppercase;">
            📋 English Abstract (Peer-Reviewed Monograph):
          </div>
          <p style="margin: 0; text-align: justify;">
            This research paper explores the Madhya Pradesh RSK Shikshak Samvad program, a pioneering initiative aimed at transforming teacher continuous professional development (CPD) in India. The program shifts from traditional cascade-style training to a decentralized, peer-led professional learning community (PLC) model grounded in constructivist design principles. Based on a statewide dataset of <strong>33,702 educators</strong> (23,785 middle school teachers, 4,814 cluster facilitators, 4,454 district leaders, and 572 observers across 52 districts), this study investigates the impact of peer dialogue on classroom engagement and joyful learning. Key findings indicate substantial gains in teacher self-efficacy and pedagogical cognition, demonstrating strong alignment with the National Education Policy (NEP 2020) mandate. The research highlights the decisive role of adult psychological safety, intrinsic motivation, and structured micro-scaffolding in sustaining pedagogical transformation.
          </p>
        `;
      }
    }
    window.toggleAbstractLang = toggleAbstractLang;

    function filterResearchThemes(themeKey, btn) {
      activeResearchTheme = themeKey || 'ALL';
      document.querySelectorAll('#resThemeFilterPills .slicer-pill').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderResearchQuotes();
    }
    window.filterResearchThemes = filterResearchThemes;

    function renderResearchQuotes() {
      const c = document.getElementById('resQuotesGrid');
      if (!c) return;

      const isHi = (typeof currentLang !== 'undefined' && currentLang === 'hi');
      const filtered = activeResearchTheme === 'ALL' 
        ? researchQuotesData 
        : researchQuotesData.filter(q => q.theme === activeResearchTheme);

      if (filtered.length === 0) {
        c.innerHTML = `<div style="grid-column: 1 / -1; padding: 24px; text-align: center; color: var(--text-muted);">${isHi ? 'कोई उद्धरण नहीं मिला।' : 'No quotes match this filter.'}</div>`;
        return;
      }

      c.innerHTML = filtered.map(q => {
        return `
          <div class="bento-card" style="display: flex; flex-direction: column; justify-content: space-between; border-left: 3px solid ${q.tagColor}; padding: 14px 16px;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span class="pill-badge" style="background: rgba(0, 138, 171, 0.08); color: ${q.tagColor}; font-size: 10.5px; font-weight: 700;">
                  ${isHi ? q.themeNameHi : q.themeNameEn}
                </span>
                <span class="badge" style="background: var(--bg-surface-2); font-size: 10px; font-family: var(--font-mono); color: var(--text-muted);">${q.tag}</span>
              </div>
              <div style="font-size: 13px; font-weight: 600; color: var(--text-primary); line-height: 1.5; margin-bottom: 6px;">
                "${q.quoteHi}"
              </div>
              ${!isHi ? `<div style="font-size: 11.5px; color: var(--text-secondary); line-height: 1.45; font-style: italic;">"${q.quoteEn}"</div>` : ''}
            </div>
            <div style="margin-top: 12px; padding-top: 8px; border-top: 1px solid var(--border-hairline); display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 11px; font-weight: 600; color: var(--text-muted); font-family: var(--font-mono);">
                📍 ${isHi ? q.speakerHi : q.speakerEn}
              </span>
              <span style="font-size: 10px; color: #059669; font-weight: 700;">✓ Verified Voice</span>
            </div>
          </div>
        `;
      }).join('');
    }
    window.renderResearchQuotes = renderResearchQuotes;

    function initResearchTab() {
      const isHi = (typeof currentLang !== 'undefined' && currentLang === 'hi');
      
      // 1. Init Abstract
      toggleAbstractLang(currentAbstractLang);

      // 2. Init Filter Pills
      const pillsContainer = document.getElementById('resThemeFilterPills');
      if (pillsContainer) {
        pillsContainer.innerHTML = `
          <button class="slicer-pill ${activeResearchTheme === 'ALL' ? 'active' : ''}" onclick="filterResearchThemes('ALL', this)">
            🌐 ${isHi ? 'सभी थीम (16,310+)' : 'All Themes (16,310+)'}
          </button>
          <button class="slicer-pill ${activeResearchTheme === 'ACADEMIC' ? 'active' : ''}" onclick="filterResearchThemes('ACADEMIC', this)">
            📖 ${isHi ? 'अकादमिक अनुप्रयोग (36.6%)' : 'Academic Utility (36.6%)'}
          </button>
          <button class="slicer-pill ${activeResearchTheme === 'JOYFUL' ? 'active' : ''}" onclick="filterResearchThemes('JOYFUL', this)">
            ✨ ${isHi ? 'आनंददायी शिक्षण (12.7%)' : 'Joyful Pedagogies (12.7%)'}
          </button>
          <button class="slicer-pill ${activeResearchTheme === 'INFRA' ? 'active' : ''}" onclick="filterResearchThemes('INFRA', this)">
            ⚡ ${isHi ? 'तकनीकी बाधाएं (3.5%)' : 'Infra & Tech (3.5%)'}
          </button>
          <button class="slicer-pill ${activeResearchTheme === 'MOTIVATION' ? 'active' : ''}" onclick="filterResearchThemes('MOTIVATION', this)">
            ❤️ ${isHi ? 'शिक्षकों की प्रेरणा (0.9%)' : 'Motivation (0.9%)'}
          </button>
        `;
      }

      // 3. Render Quotes
      renderResearchQuotes();
    }
    window.initResearchTab = initResearchTab;
'''

# We inject research_js_definition into enhanced_js right before the end of script
target_footer_line = "# 7. Enhance Footer & Script 2 (Motion One)"
if target_footer_line in code:
    code = code.replace(
        target_footer_line,
        f'enhanced_js += r"""{research_js_definition}"""\n\n' + target_footer_line
    )
    print("Injected research_js_definition into build_enhanced_studio.py successfully!")

with open('build_enhanced_studio.py', 'w', encoding='utf-8') as f:
    f.write(code)

