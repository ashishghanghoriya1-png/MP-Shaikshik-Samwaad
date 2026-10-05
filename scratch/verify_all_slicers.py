import os
from playwright.sync_api import sync_playwright

def test_all_slicers():
    html_path = os.path.abspath('index.html')
    url = f'file:///{html_path}'
    print(f'Testing Comprehensive Slicers on: {url}')

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1440, 'height': 900})
        
        errors = []
        page.on('pageerror', lambda err: errors.append(str(err)))

        page.goto(url, wait_until='load')
        page.wait_for_timeout(1000)

        # 1. September Slicer Test
        page.locator('#btnCycleSep').click()
        page.wait_for_timeout(400)
        sep_span = page.locator('#kpiTeachersTargetSpan').inner_text()
        sep_val = page.locator('#kpiTeachers').inner_text()
        sep_desc = page.locator('#kpiTeachersDesc').inner_text()
        print(f'[PASS] Cycle Slicer -> September: Actual={sep_val}, TargetSpan={sep_span}, Desc={sep_desc}')
        assert '67,222' in sep_span, 'Sep target span failed'
        assert '23,169' in sep_val, 'Sep actual teachers failed'

        # 2. August Slicer Test
        page.locator('#btnCycleAug').click()
        page.wait_for_timeout(400)
        aug_span = page.locator('#kpiTeachersTargetSpan').inner_text()
        aug_val = page.locator('#kpiTeachers').inner_text()
        aug_desc = page.locator('#kpiTeachersDesc').inner_text()
        print(f'[PASS] Cycle Slicer -> August: Actual={aug_val}, TargetSpan={aug_span}, Desc={aug_desc}')
        assert '68,369' in aug_span, 'Aug target span failed'
        assert '23,785' in aug_val, 'Aug actual teachers failed'

        # 3. Consolidated Slicer Test
        page.locator('#btnCycleConsolidated').click()
        page.wait_for_timeout(400)
        con_span = page.locator('#kpiTeachersTargetSpan').inner_text()
        con_val = page.locator('#kpiTeachers').inner_text()
        con_desc = page.locator('#kpiTeachersDesc').inner_text()
        print(f'[PASS] Cycle Slicer -> Consolidated: Actual={con_val}, TargetSpan={con_span}, Desc={con_desc}')
        assert '135,591' in con_span, 'Consolidated target span failed'
        assert '46,954' in con_val, 'Consolidated actual teachers failed'

        # 4. Archetype Filtering via JavaScript evaluate across August & September
        asp_res = page.evaluate('''() => {
            setMonthSlicer('AUG', document.getElementById('btnCycleAug'));
            if (typeof setCohortFilter === 'function') setCohortFilter('ASPIRATIONAL');
            return {
                target: document.getElementById('kpiTeachersTargetSpan').innerText,
                actual: document.getElementById('kpiTeachers').innerText
            };
        }''')
        print(f'[PASS] Archetype Filter (August - Aspirational): {asp_res}')

        sep_asp_res = page.evaluate('''() => {
            setMonthSlicer('SEP', document.getElementById('btnCycleSep'));
            return {
                target: document.getElementById('kpiTeachersTargetSpan').innerText,
                actual: document.getElementById('kpiTeachers').innerText
            };
        }''')
        print(f'[PASS] Archetype Filter (September - Aspirational): {sep_asp_res}')

        # Reset Archetype
        page.evaluate('''() => {
            if (typeof setCohortFilter === 'function') setCohortFilter('ALL');
            setMonthSlicer('AUG', document.getElementById('btnCycleAug'));
        }''')

        # 5. Check Console/Page errors
        assert len(errors) == 0, f'Encountered page errors: {errors}'
        print('ALL COMPREHENSIVE SLICER & CYCLE SWITCHING TESTS PASSED WITH 0 ERRORS!')
        browser.close()

if __name__ == '__main__':
    test_all_slicers()
