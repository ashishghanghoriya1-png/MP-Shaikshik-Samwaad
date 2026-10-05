import sys
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    def on_page_error(err):
        print("PAGE ERROR:", err)
        if hasattr(err, 'stack'):
            print("STACK:", err.stack)

    page.on('pageerror', on_page_error)
    page.goto('file:///c:/Master Dashboard for CLSS/index.html')
    page.wait_for_timeout(2000)
    browser.close()
