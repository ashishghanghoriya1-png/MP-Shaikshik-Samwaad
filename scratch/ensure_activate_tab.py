import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('build_enhanced_studio.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Check if activateTab has tab-research
if "tabId === 'tab-research'" not in code:
    old_act = """      } else if (tabId === 'tab-insights') {
        if (typeof initInsightsTab === 'function') initInsightsTab();
      }"""
    new_act = """      } else if (tabId === 'tab-insights') {
        if (typeof initInsightsTab === 'function') initInsightsTab();
      } else if (tabId === 'tab-research') {
        if (typeof initResearchTab === 'function') initResearchTab();
      }"""
    
    code = code.replace(
        "enhanced_js = motion_fallback_code + orig_js",
        f"enhanced_js = motion_fallback_code + orig_js.replace('''{old_act}''', '''{new_act}''')"
    )
    with open('build_enhanced_studio.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Added activateTab replace step in build_enhanced_studio.py!")
else:
    print("activateTab already handles tab-research in build_enhanced_studio.py.")
