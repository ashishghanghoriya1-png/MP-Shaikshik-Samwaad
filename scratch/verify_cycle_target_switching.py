import os
from playwright.sync_api import sync_playwright

def test_cycle_target_switching():
    html_path = os.path.abspath('index.html')
    url = f'file:///{html_path}'
    print(f'Testing URL: {url}')

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1440, 'height': 900})
        page = context.new_page()

        page.goto(url, wait_until='load')
        page.wait_for_timeout(1500)

        # 1. August Initial State
        aug_val = page.locator('#kpiTeachers').inner_text()
        aug_span = page.locator('#kpiTeachersTargetSpan').inner_text()
        aug_desc = page.locator('#kpiTeachersDesc').inner_text()
        print(f'[AUGUST] Actual: {aug_val} | Target Span: {aug_span} | Desc: {aug_desc}')
        assert '68,369' in aug_span, f'Expected / 68,369 in August span, got {aug_span}'
        assert '68,369' in aug_desc, f'Expected 68,369 in August desc, got {aug_desc}'
        print('PASS: August shows 68,369 target!')

        # 2. Switch to September
        print('Clicking September cycle button...')
        page.locator('#btnCycleSep').click()
        page.wait_for_timeout(1000)

        sep_val = page.locator('#kpiTeachers').inner_text()
        sep_span = page.locator('#kpiTeachersTargetSpan').inner_text()
        sep_desc = page.locator('#kpiTeachersDesc').inner_text()
        print(f'[SEPTEMBER] Actual: {sep_val} | Target Span: {sep_span} | Desc: {sep_desc}')
        assert '67,222' in sep_span, f'Expected / 67,222 in September span, got {sep_span}'
        assert '67,222' in sep_desc, f'Expected 67,222 in September desc, got {sep_desc}'
        print('PASS: September shows 67,222 target!')

        # 3. Switch to Consolidated
        print('Clicking Consolidated cycle button...')
        if page.locator('#btnCycleConsolidated').count() > 0:
            page.locator('#btnCycleConsolidated').click()
            page.wait_for_timeout(1000)
            con_val = page.locator('#kpiTeachers').inner_text()
            con_span = page.locator('#kpiTeachersTargetSpan').inner_text()
            con_desc = page.locator('#kpiTeachersDesc').inner_text()
            print(f'[CONSOLIDATED] Actual: {con_val} | Target Span: {con_span} | Desc: {con_desc}')
            assert '135,591' in con_span or '135,591' in con_desc, f'Expected 135,591 in Consolidated, got {con_span} | {con_desc}'
            print('PASS: Consolidated shows 135,591 combined target!')

        # 4. Switch back to August
        page.locator('#btnCycleAug').click()
        page.wait_for_timeout(1000)
        aug_span2 = page.locator('#kpiTeachersTargetSpan').inner_text()
        assert '68,369' in aug_span2
        print('PASS: Returned to August successfully with 68,369 target restored!')

        browser.close()
        print('ALL CYCLE TARGET SWITCHING TESTS PASSED PERFECTLY!')

if __name__ == '__main__':
    test_cycle_target_switching()
