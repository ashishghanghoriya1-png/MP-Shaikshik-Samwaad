import sys
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding='utf-8')

errors = []
console_logs = []

def handle_console(msg):
    console_logs.append(f"[{msg.type}] {msg.text}")
    if msg.type == 'error':
        errors.append(msg.text)

def handle_pageerror(err):
    errors.append(str(err))

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.on('console', handle_console)
    page.on('pageerror', handle_pageerror)
    
    print("Opening file:///c:/Master Dashboard for CLSS/index.html...")
    page.goto('file:///c:/Master Dashboard for CLSS/index.html')
    page.wait_for_timeout(2000)
    
    # Check all tabs
    tabs = [
        'tab-overview', 'tab-rf', 'tab-d360', 'tab-league', 'tab-blocks',
        'tab-questions', 'tab-pedagogy', 'tab-governance', 'tab-insights',
        'tab-research', 'tab-cohort'
    ]
    
    tab_reports = {}
    for t_id in tabs:
        print(f"\n--- Testing Tab: {t_id} ---")
        page.evaluate(f"activateTab('{t_id}')")
        page.wait_for_timeout(500)
        
        # Check for visible elements, empty divs, NaN or undefined in text
        content = page.inner_text(f'#{t_id}')
        nan_count = content.count('NaN')
        undef_count = content.count('undefined')
        null_count = content.count('null')
        
        # Check tables
        tables = page.locator(f'#{t_id} table').count()
        rows = page.locator(f'#{t_id} tr').count()
        
        print(f"Tab {t_id}: Length={len(content):,}, Tables={tables}, Rows={rows}, NaN={nan_count}, Undefined={undef_count}")
        if nan_count > 0 or undef_count > 0:
            print(f"  WARNING: Found {nan_count} NaNs or {undef_count} Undefineds in {t_id}!")
            
    browser.close()

print("\n" + "="*50)
print(f"TOTAL CONSOLE ERRORS: {len(errors)}")
for e in errors:
    print("ERROR:", e)
