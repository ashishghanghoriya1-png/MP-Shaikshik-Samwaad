with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update activateTab to trigger renderCohortTab when tab-cohort is selected
old_activate = """function activateTab(tabId, el) {
      document.querySelectorAll('.tab-section').forEach(s => s.classList.remove('active'));
      document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
      const activeSec = document.getElementById(tabId);
      if (activeSec) activeSec.classList.add('active');
      if (el) el.classList.add('active');"""

new_activate = """function activateTab(tabId, el) {
      document.querySelectorAll('.tab-section').forEach(s => s.classList.remove('active'));
      document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
      const activeSec = document.getElementById(tabId);
      if (activeSec) activeSec.classList.add('active');
      if (el) el.classList.add('active');

      if (tabId === 'tab-cohort') {
        renderCohortTab();
      }"""

if old_activate in html:
    html = html.replace(old_activate, new_activate, 1)
    print("[+] Successfully updated activateTab.")
else:
    print("[!] old_activate not found exactly, let's check.")

# Add bilingual nav translation
old_nav_hi = "const navResearch = document.getElementById('navTabResearch'); if (navResearch) navResearch.innerHTML = t.navTabResearch;"
new_nav_hi = """const navResearch = document.getElementById('navTabResearch'); if (navResearch) navResearch.innerHTML = t.navTabResearch;
        const navCohort = document.getElementById('navTabCohort'); if (navCohort) navCohort.innerHTML = (lang === 'hi') ? '👥 11. शिक्षक समूह' : '👥 11. Teacher Cohorts';
        const lblCohortTitle = document.getElementById('lblCohortTitle'); if (lblCohortTitle) lblCohortTitle.innerHTML = (lang === 'hi') ? 'शिक्षक समूह एवं उपस्थिति प्रवाह (Teacher Cohort Intelligence)' : 'Teacher Attendance Cohorts &amp; Trajectory Intelligence';"""

if old_nav_hi in html:
    html = html.replace(old_nav_hi, new_nav_hi, 1)
    print("[+] Successfully updated bilingual switcher.")
else:
    print("[!] old_nav_hi not found exactly.")

with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("[+] Updated HTML successfully.")
