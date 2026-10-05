const fs = require('fs');
const html = fs.readFileSync('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'utf8');
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1366, height: 900 } });
  await page.setContent(html);

  const colors = await page.evaluate(() => {
    const chart = charts.ovDonutStakeholder;
    return {
      labels: chart?.data?.labels,
      colors: chart?.data?.datasets?.[0]?.backgroundColor,
      data: chart?.data?.datasets?.[0]?.data
    };
  });

  console.log('Donut Chart State:', JSON.stringify(colors, null, 2));

  const el = await page.locator('#ovDonutStakeholder').locator('xpath=ancestor::div[contains(@class, "panel-box")]');
  await el.screenshot({ path: 'screenshot_stakeholder_donut.png' });

  await browser.close();
})();
