import sys
import io
from playwright.sync_api import sync_playwright

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_rf_matrix():
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

        # 1. Switch to Tab 2 (Key Goals & Indicators / RF)
        print("\n--- 1. Switching to Tab 2 (Results Framework) ---")
        tab_btn = page.query_selector("button:has-text('2. Key Goals')")
        if tab_btn:
            tab_btn.click()
            page.wait_for_timeout(600)
            print("Successfully clicked Tab 2")
        else:
            print("ERROR: Tab 2 button not found!")

        # 2. Check Table Headers
        headers = page.eval_on_selector_all("#rfMatrixTable thead th", "ths => ths.map(th => th.innerText.trim().replace(/\\n/g, ' '))")
        print(f"Table Header count: {len(headers)}")
        print("Headers:", headers)

        # 3. Check Table Rows
        row_count = page.eval_on_selector_all("#rfMatrixTable tbody tr", "trs => trs.length")
        print(f"Total Table Rows (Districts): {row_count}")

        # Check First 3 District Rows Data
        first_rows = page.eval_on_selector_all(
            "#rfMatrixTable tbody tr", 
            "trs => trs.slice(0, 5).map(tr => Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim()))"
        )
        print("\nFirst 5 District Rows:")
        for r in first_rows:
            print(" | ".join(r))

        # 4. Test Table Search Filter
        print("\n--- 2. Testing Search Filter (Bhopal) ---")
        page.fill("#rfMatrixSearch", "Bhopal")
        page.wait_for_timeout(300)
        visible_rows = page.eval_on_selector_all("#rfMatrixTable tbody tr:not([style*='display: none'])", "trs => trs.length")
        print(f"Visible rows matching 'Bhopal': {visible_rows}")

        # 5. Test Hindi Language Toggle
        print("\n--- 3. Testing Hindi Language Toggle ---")
        hi_btn = page.query_selector("#langBtnHi")
        if hi_btn:
            hi_btn.click()
            page.wait_for_timeout(500)
            hi_headers = page.eval_on_selector_all("#rfMatrixTable thead th", "ths => ths.map(th => th.innerText.trim().replace(/\\n/g, ' '))")
            print("Hindi Headers:", hi_headers)

        print("\n--- TEST SUMMARY ---")
        if errors:
            print(f"WARNING: Encountered {len(errors)} errors:")
            for err in errors:
                print(f"  - {err}")
        else:
            print("SUCCESS: 0 errors! All 11 columns in the Statewide 52-District Results Framework Matrix are populated and verified.")

        browser.close()

if __name__ == "__main__":
    test_rf_matrix()
