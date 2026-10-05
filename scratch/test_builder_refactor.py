"""
Test and refine compile_master_dashboard_html
"""
import os
import re
import json

WORKSPACE_DIR = r"c:\Master Dashboard for CLSS"
TEMPLATE_SOURCE = r"C:\My Files Work\CLSS RF BI\RSK_Executive_BI_ProMax.html"
OUTPUT_HTML = os.path.join(WORKSPACE_DIR, "RSK_Master_CLSS_Executive_Dashboard.html")

with open(TEMPLATE_SOURCE, "r", encoding="utf-8", errors="ignore") as f:
    template_html = f.read()

# 1. Clean old Excel references
replacements = [
    ('Output_CLSS_Participant_Aug_26.xlsx', 'SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheet: Participants]'),
    ('Output_CLSS_facilitator_Aug_26.xlsx', 'SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheet: Facilitator]'),
    ('Output_CLSS_Observer_Aug_26.xlsx', 'SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheet: Monitor]'),
    ('Output_DO_participant_Aug_26.xlsx', 'SS_ResponseDetail_District Level_Grades 6-8_August.xlsx [Sheet: Participants]'),
    ('Output_DO_facilitator_Aug_26.xlsx', 'SS_ResponseDetail_District Level_Grades 6-8_August.xlsx [Sheet: Facilitator]'),
    ('Output_DO_Observer_Aug_26.xlsx', 'SS_ResponseDetail_District Level_Grades 6-8_August.xlsx [Sheet: Monitor]'),
    ('CLSS - Cluster Level Summary.xlsx', 'SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx'),
    ('CLSS Aug_RF review.xlsx', 'SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx'),
    ('7 Field Telemetry Workbooks & Cluster Summary', 'Master District & Cluster Workbooks (52 Districts)'),
    ('7 Field Telemetry Workbooks', 'Master Workbooks (Cluster & District Level)'),
]

html_cleaned = template_html
for old, new in replacements:
    html_cleaned = html_cleaned.replace(old, new)

print("Old Excel references replaced. Checking counts of old files:")
for old, _ in replacements[:8]:
    print(f"  {old}: {html_cleaned.count(old)}")

# 2. Check functions in html_cleaned
funcs = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', html_cleaned)
print(f"Total functions in template: {len(funcs)}")
assert 'activateTab' in funcs, "activateTab must be present in template!"
print("activateTab is present in template.")
