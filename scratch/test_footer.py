from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    file_path = 'file:///' + os.path.abspath('C:/My Files Work/CLSS RF BI/index.html').replace('\\', '/')
    page.goto(file_path)
    page.wait_for_timeout(1000)
    page.evaluate("activateTab('tab-d360')")
    page.wait_for_timeout(500)
    foot_text = page.locator('#d360BlockTableFoot').inner_text()
    print('FOOTER RESULT:')
    print(foot_text)
    browser.close()
