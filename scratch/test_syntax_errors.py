import sys
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding='utf-8')

errors = []
console_logs = []

def handle_console(msg):
    console_logs.append(f"[{msg.type}] {msg.text}")
    if msg.type == 'error':
        errors.append(f"Console error: {msg.text} (Location: {msg.location})")

def handle_pageerror(err):
    errors.append(f"Page error: {err}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.on('console', handle_console)
    page.on('pageerror', handle_pageerror)
    
    print("Opening file:///c:/Master Dashboard for CLSS/index.html...")
    page.goto('file:///c:/Master Dashboard for CLSS/index.html')
    page.wait_for_timeout(3000)
    browser.close()

print("\n" + "="*50)
print(f"TOTAL ERRORS FOUND: {len(errors)}")
for e in errors:
    print(e)

print(f"\nALL CONSOLE LOGS ({len(console_logs)}):")
for l in console_logs[:30]:
    print(l)
