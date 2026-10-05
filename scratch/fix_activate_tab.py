import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('build_enhanced_studio.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update activateTab replacement in build_enhanced_studio.py
old_governance_block = """      } else if (tabId === 'tab-governance') {
        initGovernance();
      } else if (tabId === 'tab-insights') {
        if (typeof initInsightsTab === 'function') initInsightsTab();
      }
    }"""

new_governance_block = """      } else if (tabId === 'tab-governance') {
        initGovernance();
      } else if (tabId === 'tab-insights') {
        if (typeof initInsightsTab === 'function') initInsightsTab();
      } else if (tabId === 'tab-research') {
        if (typeof initResearchTab === 'function') initResearchTab();
      }
    }"""

# Check if old_governance_block is in code or if we can do enhanced_js = enhanced_js.replace(...)
if "enhanced_js = enhanced_js.replace(old_governance_block, new_governance_block)" not in code:
    code = code.replace(
        "enhanced_js = motion_fallback_code + orig_js",
        f"enhanced_js = motion_fallback_code + orig_js.replace('''{old_governance_block}''', '''{new_governance_block}''')"
    )

# 2. Also ensure initResearchTab() is called in DOMContentLoaded / window.onload
old_init_dashboard = "populateQuadrantBentoCards();"
new_init_dashboard = "populateQuadrantBentoCards();\n      if (typeof initResearchTab === 'function') initResearchTab();"
code = code.replace(
    f"enhanced_js = enhanced_js.replace('{old_init_dashboard}', '{new_init_dashboard}')",
    "" # reset if previously added
)
# Add clean replacement
code = code.replace(
    "enhanced_js = motion_fallback_code + orig_js",
    f"enhanced_js = motion_fallback_code + orig_js.replace('''{old_governance_block}''', '''{new_governance_block}''').replace('''{old_init_dashboard}''', '''{new_init_dashboard}''')"
)

with open('build_enhanced_studio.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_enhanced_studio.py with activateTab & initResearchTab on load!")
