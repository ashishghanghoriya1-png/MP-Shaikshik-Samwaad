import re

with open('c:/Master Dashboard for CLSS/RSK_Master_CLSS_Executive_Dashboard.html', encoding='utf-8') as f:
    text = f.read()

tabs = ['tab-overview', 'tab-rf', 'tab-d360', 'tab-league', 'tab-blocks', 'tab-questions', 'tab-pedagogy', 'tab-governance']
results = []
for t in tabs:
    m = re.search(r'<[^>]+id=[\'"]' + t + r'[\'"][^>]*>', text)
    results.append(f"{t} -> {m.group(0) if m else 'NOT FOUND'}")

# Also check activateTab function body
m_act = re.search(r'function activateTab\s*\([^)]*\)\s*\{[\s\S]*?\n    function', text)
if m_act:
    results.append('\n' + m_act.group(0))

with open('c:/Master Dashboard for CLSS/scratch/tab_elements_found.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print('Wrote tab_elements_found.txt')
