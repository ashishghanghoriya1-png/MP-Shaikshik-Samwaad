import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Generating updated build_enhanced_studio.py with Tab 10: Qualitative Research & Ground Findings...")

with open('build_enhanced_studio.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Navigation Ribbon in build_enhanced_studio.py
old_nav = """new_nav_html = \"\"\"<!-- Navigation Ribbon -->
<nav class=\"studio-nav lang-fade-target\">
<button class=\"nav-item active\" onclick=\"activateTab('tab-overview', this)\">📊 1. Overview &amp; Summary</button>
<button class=\"nav-item\" onclick=\"activateTab('tab-rf', this)\">🎯 2. Key Goals &amp; RF</button>
<button class=\"nav-item\" onclick=\"activateTab('tab-d360', this)\">🔍 3. District Profile</button>
<button class=\"nav-item\" onclick=\"activateTab('tab-league', this)\">🗺️ 4. District Rankings</button>
<button class=\"nav-item\" onclick=\"activateTab('tab-blocks', this)\">🏢 5. Block Directory</button>
<button class=\"nav-item\" onclick=\"activateTab('tab-questions', this)\">📋 6. Survey Questions</button>
<button class=\"nav-item\" onclick=\"activateTab('tab-pedagogy', this)\">🧠 7. Teaching Quality</button>
<button class=\"nav-item\" onclick=\"activateTab('tab-governance', this)\">⚖️ 8. Key Actions</button>
<button class=\"nav-item\" id=\"navTabInsights\" onclick=\"activateTab('tab-insights', this)\">🤖 9. AI Insights</button>
</nav>\"\"\""""

new_nav = """new_nav_html = \"\"\"<!-- Navigation Ribbon -->
<nav class=\"studio-nav lang-fade-target\">
<button class=\"nav-item active\" onclick=\"activateTab('tab-overview', this)\">📊 1. Overview &amp; Summary</button>
<button class=\"nav-item\" onclick=\"activateTab('tab-rf', this)\">🎯 2. Key Goals &amp; RF</button>
<button class=\"nav-item\" onclick=\"activateTab('tab-d360', this)\">🔍 3. District Profile</button>
<button class=\"nav-item\" onclick=\"activateTab('tab-league', this)\">🗺️ 4. District Rankings</button>
<button class=\"nav-item\" onclick=\"activateTab('tab-blocks', this)\">🏢 5. Block Directory</button>
<button class=\"nav-item\" onclick=\"activateTab('tab-questions', this)\">📋 6. Survey Questions</button>
<button class=\"nav-item\" onclick=\"activateTab('tab-pedagogy', this)\">🧠 7. Teaching Quality</button>
<button class=\"nav-item\" onclick=\"activateTab('tab-governance', this)\">⚖️ 8. Key Actions</button>
<button class=\"nav-item\" id=\"navTabInsights\" onclick=\"activateTab('tab-insights', this)\">🤖 9. AI Insights</button>
<button class=\"nav-item\" id=\"navTabResearch\" onclick=\"activateTab('tab-research', this)\">📚 10. Qualitative Research</button>
</nav>\"\"\""""

assert old_nav in code, "old_nav not found in build_enhanced_studio.py"
code = code.replace(old_nav, new_nav)

# 2. Update translations in build_enhanced_studio.py
old_en_trans = """new_en_nav_trans = \"\"\"        navOverview: '📊 1. Overview & Summary',
        navRf: '🎯 2. Key Goals & RF',
        navD360: '🔍 3. District Profile',
        navLeague: '🗺️ 4. District Rankings',
        navBlocks: '🏢 5. Block Directory',
        navQuestions: '📋 6. Survey Questions',
        navPedagogy: '🧠 7. Teaching Quality',
        navGov: '⚖️ 8. Key Actions',
        navInsights: '🤖 9. AI Insights',\"\"\""""

new_en_trans = """new_en_nav_trans = \"\"\"        navOverview: '📊 1. Overview & Summary',
        navRf: '🎯 2. Key Goals & RF',
        navD360: '🔍 3. District Profile',
        navLeague: '🗺️ 4. District Rankings',
        navBlocks: '🏢 5. Block Directory',
        navQuestions: '📋 6. Survey Questions',
        navPedagogy: '🧠 7. Teaching Quality',
        navGov: '⚖️ 8. Key Actions',
        navInsights: '🤖 9. AI Insights',
        navResearch: '📚 10. Qualitative Research',\"\"\""""

assert old_en_trans in code, "old_en_trans not found in build_enhanced_studio.py"
code = code.replace(old_en_trans, new_en_trans)

old_hi_trans = """new_hi_nav_trans = \"\"\"        navOverview: '📊 1. अवलोकन एवं सारांश',
        navRf: '🎯 2. लक्ष्य एवं संकेतक (RF)',
        navD360: '🔍 3. जिला प्रोफाइल',
        navLeague: '🗺️ 4. जिला रैंकिंग',
        navBlocks: '🏢 5. ब्लॉक निर्देशिका',
        navQuestions: '📋 6. सर्वेक्षण प्रश्न',
        navPedagogy: '🧠 7. शिक्षण गुणवत्ता',
        navGov: '⚖️ 8. प्रमुख कार्य',
        navInsights: '🤖 9. एआई अंतर्दृष्टि',\"\"\""""

new_hi_trans = """new_hi_nav_trans = \"\"\"        navOverview: '📊 1. अवलोकन एवं सारांश',
        navRf: '🎯 2. लक्ष्य एवं संकेतक (RF)',
        navD360: '🔍 3. जिला प्रोफाइल',
        navLeague: '🗺️ 4. जिला रैंकिंग',
        navBlocks: '🏢 5. ब्लॉक निर्देशिका',
        navQuestions: '📋 6. सर्वेक्षण प्रश्न',
        navPedagogy: '🧠 7. शिक्षण गुणवत्ता',
        navGov: '⚖️ 8. प्रमुख कार्य',
        navInsights: '🤖 9. एआई अंतर्दृष्टि',
        navResearch: '📚 10. गुणात्मक शोध',\"\"\""""

assert old_hi_trans in code, "old_hi_trans not found in build_enhanced_studio.py"
code = code.replace(old_hi_trans, new_hi_trans)

# 3. Update setLanguage nav items logic
old_setlang_nav = """new_setlang_nav = \"\"\"        // 4. Navigation Ribbon (All 9 Tabs - Clean, Polished, Zero-Overlap)
        const navItems = document.querySelectorAll('.studio-nav .nav-item');
        if (navItems.length >= 8) {
          navItems[0].innerHTML = t.navOverview;
          navItems[1].innerHTML = t.navRf;
          navItems[2].innerHTML = t.navD360;
          navItems[3].innerHTML = t.navLeague;
          navItems[4].innerHTML = t.navBlocks;
          navItems[5].innerHTML = t.navQuestions;
          navItems[6].innerHTML = t.navPedagogy;
          navItems[7].innerHTML = t.navGov;
        }
        const btnInsights = document.getElementById('navTabInsights') || (navItems.length >= 9 ? navItems[8] : null);
        if (btnInsights) {
          btnInsights.innerHTML = t.navInsights || (lang === 'hi' ? '🤖 9. एआई अंतर्दृष्टि' : '🤖 9. AI Insights');
        }
        if (typeof initInsightsTab === 'function') {
          initInsightsTab();
        }\"\"\""""

new_setlang_nav = """new_setlang_nav = \"\"\"        // 4. Navigation Ribbon (All 10 Tabs - Clean, Polished, Zero-Overlap)
        const navItems = document.querySelectorAll('.studio-nav .nav-item');
        if (navItems.length >= 8) {
          navItems[0].innerHTML = t.navOverview;
          navItems[1].innerHTML = t.navRf;
          navItems[2].innerHTML = t.navD360;
          navItems[3].innerHTML = t.navLeague;
          navItems[4].innerHTML = t.navBlocks;
          navItems[5].innerHTML = t.navQuestions;
          navItems[6].innerHTML = t.navPedagogy;
          navItems[7].innerHTML = t.navGov;
        }
        const btnInsights = document.getElementById('navTabInsights') || (navItems.length >= 9 ? navItems[8] : null);
        if (btnInsights) {
          btnInsights.innerHTML = t.navInsights || (lang === 'hi' ? '🤖 9. एआई अंतर्दृष्टि' : '🤖 9. AI Insights');
        }
        const btnResearch = document.getElementById('navTabResearch') || (navItems.length >= 10 ? navItems[9] : null);
        if (btnResearch) {
          btnResearch.innerHTML = t.navResearch || (lang === 'hi' ? '📚 10. गुणात्मक शोध' : '📚 10. Qualitative Research');
        }
        if (typeof initInsightsTab === 'function') {
          initInsightsTab();
        }
        if (typeof initResearchTab === 'function') {
          initResearchTab();
        }\"\"\""""

assert old_setlang_nav in code, "old_setlang_nav not found in build_enhanced_studio.py"
code = code.replace(old_setlang_nav, new_setlang_nav)

with open('build_enhanced_studio.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated navigation and translation anchors in build_enhanced_studio.py.")
