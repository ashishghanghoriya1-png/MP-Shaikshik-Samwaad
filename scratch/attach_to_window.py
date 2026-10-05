import re

# Update rebuild_flawless_dashboard.py to explicitly attach all functions to window
with open(r'c:\Master Dashboard for CLSS\scratch\rebuild_flawless_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

target = """  // Initialize on load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => { setTimeout(renderCohortTab, 200); });
  } else {
    setTimeout(renderCohortTab, 200);
  }"""

replacement = """  // Explicitly attach to window for global access
  window.renderCohortTab = renderCohortTab;
  window.filterCohortTable = filterCohortTable;
  window.setCohortFilter = setCohortFilter;
  window.sortCohortTable = sortCohortTable;
  window.downloadCohortMatrixCSV = downloadCohortMatrixCSV;

  // Initialize on load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => { setTimeout(renderCohortTab, 200); });
  } else {
    setTimeout(renderCohortTab, 200);
  }"""

code = code.replace(target, replacement, 1)

with open(r'c:\Master Dashboard for CLSS\scratch\rebuild_flawless_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated rebuild_flawless_dashboard.py with window attachments.")
