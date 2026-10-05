import asyncio
from playwright.async_api import async_playwright
import os

async def check_all_dropdowns():
    file_path = os.path.abspath("RSK_Master_CLSS_Executive_Studio_Enhanced.html")
    file_url = f"file:///{file_path.replace(os.sep, '/')}"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(file_url, wait_until="networkidle")
        await page.wait_for_timeout(1000)
        
        select_ids = [
            'd360Dropdown',
            'd360BlockDropdown',
            'compDistA',
            'compDistB',
            'blockDistrictSelect',
            'qbSheetSelect',
            'qbDistrictSelect',
            'pedMisconDistSelect'
        ]
        
        print("=== INITIAL DROPDOWN OPTIONS AUDIT ===")
        for sid in select_ids:
            sel = page.locator(f"#{sid}")
            count = await sel.count()
            if count > 0:
                opt_count = await page.evaluate(f"document.getElementById('{sid}') ? document.getElementById('{sid}').options.length : 0")
                first_opt = await page.evaluate(f"document.getElementById('{sid}') && document.getElementById('{sid}').options.length > 0 ? document.getElementById('{sid}').options[0].text : 'N/A'")
                second_opt = await page.evaluate(f"document.getElementById('{sid}') && document.getElementById('{sid}').options.length > 1 ? document.getElementById('{sid}').options[1].text : 'N/A'")
                print(f"#{sid} -> Options: {opt_count} | 1st: '{first_opt}' | 2nd: '{second_opt}'")
            else:
                print(f"#{sid} -> NOT FOUND IN DOM")
                
        await browser.close()

if __name__ == "__main__":
    asyncio.run(check_all_dropdowns())
