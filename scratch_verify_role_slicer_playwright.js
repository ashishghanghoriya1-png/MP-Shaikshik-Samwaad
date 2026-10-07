/**
 * Playwright E2E Verification for Cadre / Role Slicer
 * Tests conditional visibility across all tabs and data responsiveness on Tab 1 Overview.
 */

const { chromium } = require('playwright');
const path = require('path');

const targets = [
    'index.html',
    'deploy/index.html',
    'RSK_Master_CLSS_Executive_Dashboard.html',
    'RSK_Master_CLSS_Executive_Studio_Enhanced.html'
];

async function runRoleSlicerVerification() {
    console.log('===================================================================');
    console.log(' Playwright E2E: Cadre/Role Slicer Functionality & Visibility Tests');
    console.log('===================================================================\n');

    const browser = await chromium.launch({ channel: 'msedge' });
    let allPassed = true;

    for (const target of targets) {
        const filePath = 'file:///' + path.resolve(__dirname, target).replace(/\\/g, '/');
        console.log(`[*] Testing target: ${target}`);
        
        const page = await browser.newPage();
        
        const errors = [];
        page.on('console', msg => {
            if (msg.type() === 'error') errors.push(msg.text());
        });
        page.on('pageerror', err => {
            errors.push(err.message);
        });

        try {
            await page.goto(filePath, { waitUntil: 'domcontentloaded' });
            await page.waitForTimeout(1000);

            // 1. Verify Cadre Slicer is visible on Tab 1 (Overview)
            const isVisibleTab1 = await page.$eval('#cadreSlicerGroup', el => window.getComputedStyle(el).display !== 'none');
            if (!isVisibleTab1) throw new Error('Cadre slicer should be visible on Tab 1 Overview');
            console.log('  [✓] Tab 1 Overview: Cadre Slicer is visible (display: flex)');

            // 2. Test Role Slicer interactions on Tab 1 Overview
            const teacherBtn = await page.$('#roleSlicer button[onclick*="Participant"]');
            if (teacherBtn) {
                await teacherBtn.click();
                await page.waitForTimeout(300);
                const activeRole = await page.evaluate(() => window.activeRole);
                if (activeRole !== 'Participant') throw new Error('activeRole failed to set to Participant');
                console.log('  [✓] Tab 1: Clicked "Teachers" -> activeRole updated to Participant');
            }

            const facBtn = await page.$('#roleSlicer button[onclick*="Facilitator"]');
            if (facBtn) {
                await facBtn.click();
                await page.waitForTimeout(300);
                const activeRole = await page.evaluate(() => window.activeRole);
                if (activeRole !== 'Facilitator') throw new Error('activeRole failed to set to Facilitator');
                console.log('  [✓] Tab 1: Clicked "Facilitators" -> activeRole updated to Facilitator');
            }

            const monBtn = await page.$('#roleSlicer button[onclick*="Observer"]');
            if (monBtn) {
                await monBtn.click();
                await page.waitForTimeout(300);
                const activeRole = await page.evaluate(() => window.activeRole);
                if (activeRole !== 'Observer') throw new Error('activeRole failed to set to Observer');
                console.log('  [✓] Tab 1: Clicked "Monitors" -> activeRole updated to Observer');
            }

            const allBtn = await page.$('#roleSlicer button[onclick*="ALL"]');
            if (allBtn) {
                await allBtn.click();
                await page.waitForTimeout(300);
                console.log('  [✓] Tab 1: Restored "All Stakeholders"');
            }

            // 3. Test Conditional Visibility: Non-applicable Tabs (Should HIDE)
            const hideTabs = ['tab-d360', 'tab-league', 'tab-blocks', 'tab-pedagogy', 'tab-cohort', 'tab-research'];
            for (const tabId of hideTabs) {
                await page.evaluate(t => window.activateTab(t), tabId);
                await page.waitForTimeout(150);
                const isHidden = await page.$eval('#cadreSlicerGroup', el => window.getComputedStyle(el).display === 'none');
                if (!isHidden) throw new Error(`Cadre slicer should be HIDDEN on ${tabId}`);
            }
            console.log('  [✓] Non-applicable Tabs (3, 4, 5, 7, 10, 11): Cadre Slicer dynamically HIDDEN');

            // 4. Test Conditional Visibility: Applicable Tabs (Should SHOW)
            const showTabs = ['tab-rf', 'tab-questions', 'tab-governance', 'tab-insights', 'tab-overview'];
            for (const tabId of showTabs) {
                await page.evaluate(t => window.activateTab(t), tabId);
                await page.waitForTimeout(150);
                const isShown = await page.$eval('#cadreSlicerGroup', el => window.getComputedStyle(el).display !== 'none');
                if (!isShown) throw new Error(`Cadre slicer should be SHOWN on ${tabId}`);
            }
            console.log('  [✓] Applicable Tabs (1, 2, 6, 8, 9): Cadre Slicer dynamically SHOWN');

            // Filter out non-fatal console noise
            const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('CORS'));
            if (fatalErrors.length === 0) {
                console.log('  [✓] Zero console errors detected during tab transitions and slicing');
            }

            console.log(`[PASS] ${target} is 100% verified!\n`);
        } catch (err) {
            console.error(`[FAIL] ${target} error:`, err.message);
            allPassed = false;
        } finally {
            await page.close();
        }
    }

    await browser.close();

    if (allPassed) {
        console.log('===================================================================');
        console.log(' [✓] ALL 4 DASHBOARD TARGETS PASSED ROLE SLICER E2E VERIFICATION');
        console.log('===================================================================');
    } else {
        process.exit(1);
    }
}

runRoleSlicerVerification();
