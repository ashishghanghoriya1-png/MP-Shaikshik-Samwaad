import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Read current build_enhanced_studio.py
with open('build_enhanced_studio.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Read design_new_u360.py
with open('scratch/design_new_u360.py', 'r', encoding='utf-8') as f:
    dcode = f.read()

marker1 = "new_d360_js = r'''"
idx1 = dcode.find(marker1) + len(marker1)
marker2 = "'''\n\nprint("
idx2 = dcode.find(marker2, idx1)
new_d360_js = dcode[idx1:idx2]

# In build_enhanced_studio.py, let's find the section that builds enhanced_js
# From 'enhanced_js = motion_fallback_code + orig_js.replace' to 'old_en_nav_trans = '
old_init_d360_block_start = code.find("enhanced_js = motion_fallback_code + orig_js.replace('''function initDistrict360() {")
old_init_d360_block_end = code.find("# Refine translations.en nav labels")

assert old_init_d360_block_start != -1, "old_init_d360_block_start not found"
assert old_init_d360_block_end != -1, "old_init_d360_block_end not found"

replacement_enhanced_js_init = '''# Replace D360 block in orig_js with complete, responsive Block-Focus implementation
idx_d360_start = orig_js.find('function initDistrict360()')
idx_d360_end = orig_js.find('function initDistrictLeague()')
assert idx_d360_start != -1 and idx_d360_end != -1, "D360 block boundaries not found in orig_js"

d360_js_replacement = r"""''' + new_d360_js + '''"""

enhanced_js = motion_fallback_code + orig_js[:idx_d360_start] + d360_js_replacement + "\\n\\n    " + orig_js[idx_d360_end:]

# Tab-switching & hooks injection
enhanced_js = enhanced_js.replace("""      } else if (tabId === 'tab-d360') {
        updateDistrict360View();
        updateDistrictComparison();""", """      } else if (tabId === 'tab-d360') {
        if (typeof populateD360BlockDropdown === 'function') populateD360BlockDropdown();
        updateDistrict360View();
        updateDistrictComparison();""")

enhanced_js = enhanced_js.replace("""        const d360BlockLbl = document.querySelector('label[for="d360BlockDropdown"]');
        if (d360BlockLbl) d360BlockLbl.innerText = t.d360LblBlock;""", """        const d360BlockLbl = document.querySelector('label[for="d360BlockDropdown"]');
        if (d360BlockLbl) d360BlockLbl.innerText = t.d360LblBlock;
        if (typeof populateD360BlockDropdown === 'function') populateD360BlockDropdown();""")

enhanced_js = enhanced_js.replace("""      } else if (tabId === 'tab-governance') {
        initGovernance();
      } else if (tabId === 'tab-insights') {
        if (typeof initInsightsTab === 'function') initInsightsTab();
      }""", """      } else if (tabId === 'tab-governance') {
        initGovernance();
      } else if (tabId === 'tab-insights') {
        if (typeof initInsightsTab === 'function') initInsightsTab();
      } else if (tabId === 'tab-research') {
        if (typeof initResearchTab === 'function') initResearchTab();
      }""")

enhanced_js = enhanced_js.replace("""populateQuadrantBentoCards();""", """populateQuadrantBentoCards();
      if (typeof initResearchTab === 'function') initResearchTab();""")

'''

new_code = code[:old_init_d360_block_start] + replacement_enhanced_js_init + code[old_init_d360_block_end:]

with open('build_enhanced_studio.py', 'w', encoding='utf-8') as f:
    f.write(new_code)

print("Successfully updated build_enhanced_studio.py with clean D360 block replacement!")
