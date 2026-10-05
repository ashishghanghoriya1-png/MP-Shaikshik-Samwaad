import asyncio
from playwright.async_api import async_playwright
import os

async def inspect_d360_live():
    file_path = os.path.abspath("RSK_Master_CLSS_Executive_Studio_Enhanced.html")
    file_url = f"file:///{file_path.replace(os.sep, '/')}"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(file_url, wait_until="networkidle")
        await page.wait_for_timeout(1000)
        
        # Navigate to Tab 3
        btn_d360 = page.locator("button:has-text('3. District Profile')")
        await btn_d360.click()
        await page.wait_for_timeout(500)
        
        print("=== TAB 3 LIVE DOM STATE ===")
        # Check #d360BlockTable rows
        table_rows = await page.locator("#d360BlockTable tbody tr").count()
        print(f"#d360BlockTable tbody rows count: {table_rows}")
        
        # Check #d360HeroStats
        hero_teachers = await page.locator("#d360ValTeachers").inner_text()
        print(f"Hero card d360ValTeachers: '{hero_teachers}'")
        
        # Check charts visibility
        canvas_ids = ['d360PedChart', 'd360GenderChart', 'd360BlockCompChart', 'sameBlockPeerChart']
        for cid in canvas_ids:
            c = page.locator(f"#{cid}")
            vis = await c.is_visible()
            box = await c.bounding_box()
            print(f"Canvas #{cid} -> Visible: {vis}, Box: {box}")
            
        # Now change block focus to 'AGAR'
        print("\n--- Selecting block 'AGAR' ---")
        await page.select_option("#d360BlockDropdown", value="AGAR")
        await page.evaluate("onD360BlockChange()")
        await page.wait_for_timeout(500)
        
        hero_teachers_after = await page.locator("#d360ValTeachers").inner_text()
        print(f"After selecting AGAR: d360ValTeachers: '{hero_teachers_after}'")
        
        table_rows_after = await page.locator("#d360BlockTable tbody tr").count()
        print(f"After selecting AGAR: #d360BlockTable tbody rows count: {table_rows_after}")
        
        bento_cards_count = await page.locator("#d360BlockBentoGrid .bento-card").count()
        print(f"After selecting AGAR: #d360BlockBentoGrid cards count: {bento_cards_count}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(inspect_d360_live())
