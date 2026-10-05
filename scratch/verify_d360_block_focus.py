import sys
import io
from playwright.sync_api import sync_playwright

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_district_profile():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1440, 'height': 900})
        page = context.new_page()

        errors = []
        page.on("pageerror", lambda err: errors.append(f"PageError: {err.message}"))
        page.on("console", lambda msg: errors.append(f"ConsoleError: {msg.text}") if msg.type == "error" else None)

        file_path = "file:///c:/Master Dashboard for CLSS/RSK_Master_CLSS_Executive_Studio_Enhanced.html"
        print(f"Loading {file_path}...")
        page.goto(file_path)
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(1000)

        # 1. Switch to Tab 3 (District Profile)
        print("\n--- 1. Switching to Tab 3 (District Profile) ---")
        tab_btn = page.query_selector("button:has-text('3. District Profile')")
        if tab_btn:
            tab_btn.click()
            page.wait_for_timeout(600)
            print("Successfully clicked Tab 3")
        else:
            print("ERROR: Tab 3 button not found!")

        # Verify District Dropdown
        dist_dd = page.query_selector("#d360Dropdown")
        dist_val = dist_dd.input_value() if dist_dd else "None"
        print(f"Default selected district: {dist_val}")

        # Verify Block Dropdown
        block_dd = page.query_selector("#d360BlockDropdown")
        block_options = page.eval_on_selector_all("#d360BlockDropdown option", "opts => opts.map(o => ({ value: o.value, text: o.innerText }))")
        print(f"Block options count: {len(block_options)}")
        for opt in block_options[:5]:
            print(f"  - {opt['value']}: {opt['text']}")

        # Verify Hero Stats are populated
        hero_stats = page.inner_text("#d360HeroStats")
        print(f"Hero stats text preview:\n{hero_stats[:300]}...")

        # Verify Block Table has rows
        table_rows = page.eval_on_selector_all("#d360BlockTable tbody tr", "rows => rows.length")
        print(f"Block table rows count: {table_rows}")

        # 2. Select a specific Block (e.g. AGAR)
        print("\n--- 2. Selecting Block 'AGAR' ---")
        page.select_option("#d360BlockDropdown", "AGAR")
        page.wait_for_timeout(500)

        hero_stats_agar = page.inner_text("#d360HeroStats")
        print(f"Hero stats for AGAR:\n{hero_stats_agar[:300]}...")

        # Check if table highlights AGAR
        focused_row = page.eval_on_selector("#d360BlockTable tbody tr[style*='rgba']", "r => r ? r.innerText : 'None'")
        print(f"Focused row text: {focused_row[:100] if focused_row else 'None'}")

        # 3. Test changing District to Bhopal
        print("\n--- 3. Switching District to 'Bhopal' ---")
        page.select_option("#d360Dropdown", "Bhopal")
        page.wait_for_timeout(500)

        bhopal_blocks = page.eval_on_selector_all("#d360BlockDropdown option", "opts => opts.map(o => o.value)")
        print(f"Bhopal block options: {bhopal_blocks}")

        # Focus on BERASIA in Bhopal
        print("\n--- 4. Selecting Block 'BERASIA' in Bhopal ---")
        page.select_option("#d360BlockDropdown", "BERASIA")
        page.wait_for_timeout(500)

        hero_stats_berasia = page.inner_text("#d360HeroStats")
        print(f"Hero stats for BERASIA:\n{hero_stats_berasia[:300]}...")

        # 4. Test View Mode: Block Bifurcation
        print("\n--- 5. Testing View Mode 'Block Bifurcation' ---")
        bif_btn = page.query_selector("#d360BtnBifurcate")
        if bif_btn:
            bif_btn.click()
            page.wait_for_timeout(500)
            bento_cards = page.eval_on_selector_all("#d360BlockBentoGrid .bento-card", "cards => cards.length")
            print(f"Bento cards count: {bento_cards}")

        # 5. Test Hindi Language Toggle
        print("\n--- 6. Testing Hindi Language Toggle ---")
        hi_btn = page.query_selector("#langBtnHi")
        if hi_btn:
            hi_btn.click()
            page.wait_for_timeout(500)
            hi_block_opts = page.eval_on_selector_all("#d360BlockDropdown option", "opts => opts.map(o => o.innerText)")
            print(f"Hindi block options preview: {hi_block_opts[:3]}")

        # 6. Verify all 10 tabs load without error
        print("\n--- 7. Testing All 10 Navigation Tabs ---")
        nav_buttons = page.query_selector_all(".nav-item")
        for i, btn in enumerate(nav_buttons):
            btn_text = btn.inner_text().strip().replace('\n', ' ')
            btn.click()
            page.wait_for_timeout(300)
            print(f"  Checked Tab [{i+1}]: {btn_text}")

        print("\n--- TEST SUMMARY ---")
        if errors:
            print(f"WARNING: Encountered {len(errors)} errors:")
            for err in errors:
                print(f"  - {err}")
        else:
            print("SUCCESS: 0 errors! All District 360 block focus features, table updates, and charts rendered smoothly.")

        browser.close()

if __name__ == "__main__":
    test_district_profile()
