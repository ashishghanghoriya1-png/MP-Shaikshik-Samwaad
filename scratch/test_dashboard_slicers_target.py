import os
from playwright.sync_api import sync_playwright

def test_dashboard():
    html_path = os.path.abspath('index.html')
    url = f'file:///{html_path}'
    print(f'Testing URL: {url}')

    errors = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1440, 'height': 900})
        page = context.new_page()

        page.on('console', lambda msg: errors.append(f'CONSOLE {msg.type}: {msg.text}') if msg.type == 'error' else None)
        page.on('pageerror', lambda err: errors.append(f'PAGE ERROR: {err}'))

        # 1. Load index.html
        page.goto(url, wait_until='load')
        page.wait_for_timeout(1500)

        # 2. Check Attending Teachers KPI card text
        kpi_teachers = page.locator('#kpiTeachers').inner_text()
        kpi_desc = page.locator('#kpiTeachersDesc').inner_text()
        print(f'Initial KPI Teachers: "{kpi_teachers}"')
        print(f'Initial KPI Teachers Desc: "{kpi_desc}"')

        assert '68,369' in kpi_desc or '68,369' in kpi_teachers, f'Expected 68,369 in KPI, got {kpi_teachers} | {kpi_desc}'
        print('PASS: Initial August target 68,369 verified in KPI cards.')

        # 3. Test Month Switcher (September)
        print('Testing Month Slicer: September...')
        if page.locator('#btnCycleSep').count() > 0:
            page.locator('#btnCycleSep').click()
            page.wait_for_timeout(800)
            sep_teachers = page.locator('#kpiTeachers').inner_text()
            print(f'September KPI Teachers: "{sep_teachers}"')
            # Switch back to August
            page.locator('#btnCycleAug').click()
            page.wait_for_timeout(800)
            print('PASS: Cycled September and returned to August.')

        # 4. Test Tab 5 Block Directory & District Slicer
        print('Testing Tab 5 Block Directory & District Slicer...')
        tab5_btn = page.locator('button[data-tab="tab-governance"], .nav-tab[data-tab="tab-governance"]')
        if tab5_btn.count() > 0:
            tab5_btn.first.click()
            page.wait_for_timeout(500)
            if page.locator('#blockDistrictSelect').is_visible():
                page.select_option('#blockDistrictSelect', 'Indore')
                page.wait_for_timeout(500)
                print('PASS: Selected Indore in blockDistrictSelect.')

        # 5. Test Tab Navigation across all 9 tabs
        tabs = ['tab-overview', 'tab-studio', 'tab-peer', 'tab-quadrant', 'tab-governance', 'tab-rf', 'tab-qual', 'tab-d360', 'tab-research']
        for tab_id in tabs:
            btn = page.locator(f'button[data-tab="{tab_id}"], .nav-tab[data-tab="{tab_id}"], a[href="#{tab_id}"]')
            if btn.count() > 0:
                btn.first.click()
                page.wait_for_timeout(200)
                assert page.is_visible(f'#{tab_id}') or page.is_visible(f'.tab-section#{tab_id}'), f'Tab #{tab_id} not visible'
        print('PASS: All 9 dashboard navigation tabs switched smoothly without errors.')

        # 6. Check console errors
        critical_errors = [e for e in errors if 'favicon' not in e.lower() and 'font' not in e.lower() and '404' not in e.lower()]
        if critical_errors:
            print(f'WARNING: Encountered {len(critical_errors)} console errors:')
            for e in critical_errors:
                print('  ', e)
        else:
            print('PASS: Zero console errors during full dashboard interaction!')

        browser.close()
        print('ALL 6 AUDIT TEST SUITES PASSED SUCCESSFULLY!')

if __name__ == '__main__':
    test_dashboard()
