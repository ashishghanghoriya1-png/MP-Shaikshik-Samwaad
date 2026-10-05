import json, os, re

with open(r'c:\Master Dashboard for CLSS\data\exports\cohort_matrix_52_districts.json', 'r', encoding='utf-8') as f:
    district_data = json.load(f)

print(f"Loaded {len(district_data)} district rows.")

# Let's inspect the existing translations and activateTab in RSK_Master_CLSS_Executive_Studio_Enhanced.html
with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's verify nav tab insertion point
nav_old = '<button class="nav-item" id="navTabResearch" onclick="activateTab(\'tab-research\', this)">📚 10. Qualitative Research</button>'
nav_new = '<button class="nav-item" id="navTabResearch" onclick="activateTab(\'tab-research\', this)">📚 10. Qualitative Research</button>\n<button class="nav-item" id="navTabCohort" onclick="activateTab(\'tab-cohort\', this)">👥 11. Teacher Cohorts</button>'

if nav_old in html:
    print("Found navTabResearch in HTML!")
else:
    print("WARNING: navTabResearch not found verbatim.")
