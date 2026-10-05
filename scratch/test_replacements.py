import re

with open(r"C:\My Files Work\CLSS RF BI\RSK_Executive_BI_ProMax.html", "r", encoding="utf-8") as f:
    template = f.read()

# Test replacements
test = template
replacements = [
    # Card 1
    (r'<div style="font-size: 9\.5px; font-family: var\(--font-mono\); color: var\(--text-muted\); margin-top: 6px; border-top: 1px dashed var\(--border-hairline\); padding-top: 4px;">\s*\[Ref: <em>Output_CLSS_Participant_Aug_26\.xlsx</em>\]\s*</div>',
     '<div id="kpiCoverageRef" style="font-size: 9.5px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 6px; border-top: 1px dashed var(--border-hairline); padding-top: 4px;">[Ref: <em>Both Workbooks: SS_ResponseDetail_Cluster Level & District Level_Grades 6-8_August.xlsx</em>]</div>'),
    
    # Card 2
    (r'<div style="font-size: 9\.5px; font-family: var\(--font-mono\); color: var\(--text-muted\); margin-top: 6px; border-top: 1px dashed var\(--border-hairline\); padding-top: 4px;">\s*\[Ref: <em>CLSS - Cluster Level Summary\.xlsx</em> \| Sheet1\]\s*</div>',
     '<div id="kpiReachRef" style="font-size: 9.5px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 6px; border-top: 1px dashed var(--border-hairline); padding-top: 4px;">[Ref: <em>Both Workbooks</em> (2,822 CRC Clusters + 52 DIET Venues)]</div>'),
    
    # Card 3
    (r'<div style="font-size: 9\.5px; font-family: var\(--font-mono\); color: var\(--text-muted\); margin-top: 6px; border-top: 1px dashed var\(--border-hairline\); padding-top: 4px;">\s*\[Ref: <em>Output_CLSS_Participant_Aug_26\.xlsx</em> \| Summary\]\s*</div>',
     '<div id="kpiTeachersRef" style="font-size: 9.5px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 6px; border-top: 1px dashed var(--border-hairline); padding-top: 4px;">[Ref: <em>SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheet: Participants]</em>]</div>'),
    
    # Card 4
    (r'<div style="font-size: 9\.5px; font-family: var\(--font-mono\); color: var\(--text-muted\); margin-top: 6px; border-top: 1px dashed var\(--border-hairline\); padding-top: 4px;">\s*\[Ref: <em>Output_DO_participant_Aug_26\.xlsx</em> • DIET Orientation\]\s*</div>',
     '<div id="kpiDoOfficersRef" style="font-size: 9.5px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 6px; border-top: 1px dashed var(--border-hairline); padding-top: 4px;">[Ref: <em>SS_ResponseDetail_District Level_Grades 6-8_August.xlsx [Sheet: Participants]</em>]</div>'),
    
    # Card 5
    (r'<div style="font-size: 9\.5px; font-family: var\(--font-mono\); color: var\(--text-muted\); margin-top: 6px; border-top: 1px dashed var\(--border-hairline\); padding-top: 4px;">\s*\[Ref: <em>Output_CLSS_facilitator_Aug_26\.xlsx</em> & Observers\]\s*</div>',
     '<div id="kpiCadreRef" style="font-size: 9.5px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 6px; border-top: 1px dashed var(--border-hairline); padding-top: 4px;">[Ref: <em>Both Workbooks</em> [Cluster & District Sheets: Facilitator & Monitor]]</div>'),
]

for pat, repl in replacements:
    matches = re.findall(pat, test)
    print(f"Pattern '{pat[:40]}...': {len(matches)} matches")
