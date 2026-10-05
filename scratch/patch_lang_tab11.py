with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_block = """        const btnResearch = document.getElementById('navTabResearch') || (navItems.length >= 10 ? navItems[9] : null);
        if (btnResearch) {
          btnResearch.innerHTML = t.navResearch || (lang === 'hi' ? '📚 10. गुणात्मक शोध' : '📚 10. Qualitative Research');
        }"""

replacement_block = """        const btnResearch = document.getElementById('navTabResearch') || (navItems.length >= 10 ? navItems[9] : null);
        if (btnResearch) {
          btnResearch.innerHTML = t.navResearch || (lang === 'hi' ? '📚 10. गुणात्मक शोध' : '📚 10. Qualitative Research');
        }
        const btnCohort = document.getElementById('navTabCohort') || (navItems.length >= 11 ? navItems[10] : null);
        if (btnCohort) {
          btnCohort.innerHTML = (lang === 'hi' ? '👥 11. शिक्षक समूह' : '👥 11. Teacher Cohorts');
        }
        const lblCohortTitle = document.getElementById('lblCohortTitle');
        if (lblCohortTitle) {
          lblCohortTitle.innerHTML = (lang === 'hi' ? 'शिक्षक समूह एवं उपस्थिति प्रवाह' : 'Teacher Attendance Cohorts &amp; Trajectory Intelligence');
        }
        const lblCohortSubtitle = document.getElementById('lblCohortSubtitle');
        if (lblCohortSubtitle) {
          lblCohortSubtitle.innerHTML = (lang === 'hi' ? 'अगस्त और सितंबर सत्रों के बीच अद्वितीय EmployeeCode मिलान। कोर प्रतिधारण (55.0%), नए शिक्षक आगमन (43.5%), और 52 जिलों में लक्ष्य संतृप्ति का विश्लेषण।' : 'Cross-month teacher tracking using unique EmployeeCode identifiers. Quantifies core retention (55.0%), fresh monthly inflow (43.5%), churn/drop-off calling pools, and cumulative progress toward statewide teacher saturation.');
        }"""

if target_block in html:
    html = html.replace(target_block, replacement_block, 1)
    print("[+] Successfully updated setLanguage for Tab 11.")
    with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'w', encoding='utf-8') as f:
        f.write(html)
else:
    print("[!] Target block not found in HTML.")
