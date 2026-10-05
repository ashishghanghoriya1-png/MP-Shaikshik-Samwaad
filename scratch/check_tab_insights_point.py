# Let's inspect where tab-insights ends in orig HTML and how we can insert tab-research cleanly
with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    orig = f.read()

import re
pos_tab_insights_end = orig.find('</section>\n\n    <!-- Tab 9 / Insights section ends -->')
if pos_tab_insights_end == -1:
    # search for closing tag of tab-insights
    m = re.search(r'<section class="tab-section" id="tab-insights">.*?</section>', orig, re.DOTALL)
    if m:
        print("Found tab-insights end at:", m.end())
        print("Following text:", orig[m.end():m.end()+150])
