from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('file:///c:/Master Dashboard for CLSS/RSK_Master_CLSS_Executive_Dashboard.html')
    page.wait_for_timeout(1000)

    # Go to Tab 3
    page.click("button[onclick*='tab-d360']")
    page.wait_for_timeout(500)

    chart_labels = page.evaluate("Chart.getChart('d360BlockCompChart').data.datasets.map(d => d.label)")
    print('Chart.getChart labels:', chart_labels)
    chart_data = page.evaluate("Chart.getChart('d360BlockCompChart').data.datasets.map(d => ({ label: d.label, data: d.data }))")
    print('Chart.getChart data:', chart_data)

    browser.close()
