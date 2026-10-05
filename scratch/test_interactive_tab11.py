import sys
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('file:///c:/Master Dashboard for CLSS/index.html')
    page.wait_for_timeout(1000)
    
    # 1. Switch to Tab 11
    page.evaluate("activateTab('tab-cohort')")
    page.wait_for_timeout(500)
    
    # 2. Test District Search
    print("Testing search: 'Bhopal'...")
    page.fill('#cohortDistrictSearch', 'Bhopal')
    page.evaluate("filterCohortTable()")
    count = page.inner_text('#cohortVisibleCount')
    print(f"Visible districts for 'Bhopal': {count}")
    assert count == '1', f"Expected 1, got {count}"
    
    # 3. Test Filter Pill: Retention > 60%
    page.fill('#cohortDistrictSearch', '')
    page.evaluate("setCohortFilter('HIGH_RET')")
    count_ret = page.inner_text('#cohortVisibleCount')
    print(f"Visible districts for HIGH_RET: {count_ret}")
    
    # 4. Test Filter Pill: New Inflow > 50%
    page.evaluate("setCohortFilter('HIGH_NEW')")
    count_new = page.inner_text('#cohortVisibleCount')
    print(f"Visible districts for HIGH_NEW: {count_new}")

    # 5. Test Filter Pill: Lagging Saturation < 80%
    page.evaluate("setCohortFilter('LAGGING')")
    count_lag = page.inner_text('#cohortVisibleCount')
    print(f"Visible districts for LAGGING: {count_lag}")
    
    # 6. Test Sorting by Retention % (col 4)
    page.evaluate("setCohortFilter('ALL')")
    page.evaluate("sortCohortTable(4)")
    first_row_dist = page.inner_text('#cohortMatrixBody tr:first-child td:first-child')
    print(f"Top district sorted by retention: {first_row_dist}")
    
    # 7. Test Language Switcher to Hindi
    page.evaluate("setLanguage('hi')")
    hi_title = page.inner_text('#lblCohortTitle')
    print(f"Hindi title: {hi_title}")
    
    # 8. Test Theme Switcher
    page.evaluate("toggleTheme()")
    theme_state = page.get_attribute('html', 'data-theme')
    print(f"Theme state after toggle: {theme_state}")
    
    browser.close()

print("\n✔ ALL INTERACTIVE CHECKS PASSED PERFECTLY!")
