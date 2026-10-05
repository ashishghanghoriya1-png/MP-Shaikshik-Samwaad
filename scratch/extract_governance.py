import re

with open('c:/Master Dashboard for CLSS/RSK_Master_CLSS_Executive_Dashboard.html', encoding='utf-8') as f:
    text = f.read()

m_sec = re.search(r'<section[^>]+id=["\']tab-governance["\'][\s\S]*?</section>', text)
if m_sec:
    with open('c:/Master Dashboard for CLSS/scratch/tab_governance_html.txt', 'w', encoding='utf-8') as f:
        f.write(m_sec.group(0))
    print('Wrote tab_governance_html.txt! Size:', len(m_sec.group(0)))

m_js = re.search(r'function initGovernance[\s\S]*?\n    function', text)
if m_js:
    with open('c:/Master Dashboard for CLSS/scratch/init_governance_js.txt', 'w', encoding='utf-8') as f:
        f.write(m_js.group(0))
    print('Wrote init_governance_js.txt! Size:', len(m_js.group(0)))
