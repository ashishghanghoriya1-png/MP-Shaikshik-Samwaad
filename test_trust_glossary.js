const fs = require('fs');
const html = fs.readFileSync('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'utf8');
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1366, height: 900 } });
  
  const errors = [];
  page.on('pageerror', err => errors.push(err.message));
  page.on('console', msg => {
    if (msg.type() === 'error') errors.push(msg.text());
  });

  await page.setContent(html);

  const res = await page.evaluate(() => {
    const box = document.getElementById('ovTrustGlossaryBox');
    return {
      exists: !!box,
      hasContent: box?.innerHTML.length > 50,
      title: box?.querySelector('span:first-child')?.innerText,
      boxHtml: box?.innerHTML
    };
  });

  console.log('Trust Glossary Test:', { exists: res.exists, hasContent: res.hasContent, title: res.title });
  console.log('Errors:', errors);

  const el = page.locator('#panelTrustIndexBox');
  await el.screenshot({ path: 'screenshot_trust_panel_with_glossary.png' });

  await browser.close();
})();
