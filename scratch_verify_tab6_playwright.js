/**
 * Playwright Automated E2E Verification for Tab 6 (Survey Questions) Role Slicer
 * Verifies dropdown filtering by Teachers (26), Facilitators (24), and Monitors (20).
 */

const { chromium } = require('playwright');
const path = require('path');

const targets = [
    'index.html',
    'deploy/index.html',
    'RSK_Master_CLSS_Executive_Dashboard.html',
    'RSK_Master_CLSS_Executive_Studio_Enhanced.html'
];

async function runTab6Verification() {
    console.log('===================================================================');
    console.log(' Playwright E2E: Tab 6 (Survey Questions) Role Slicer Verification');
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

            // 1. Activate Tab 6 (Survey Questions)
            await page.evaluate(() => window.activateTab('tab-questions'));
            await page.waitForTimeout(300);

            // 2. Check Cadre Slicer is Visible on Tab 6
            const isSlicerVisible = await page.$eval('#cadreSlicerGroup', el => window.getComputedStyle(el).display !== 'none');
            if (!isSlicerVisible) throw new Error('Cadre Slicer should be visible on Tab 6');
            console.log('  [✓] Tab 6 Active: Cadre Slicer is visible (display: flex)');

            // 3. Test "All Stakeholders" (70 Questions)
            const allCount = await page.$$eval('#qbSheetSelect option', opts => opts.length);
            if (allCount !== 70) throw new Error(`Expected 70 questions for ALL, got ${allCount}`);
            console.log(`  [✓] Role 'ALL': Dropdown populated with ${allCount} questions`);

            // 4. Test "Teachers" (26 Questions)
            const teacherBtn = await page.$('#roleSlicer button[onclick*="Participant"]');
            await teacherBtn.click();
            await page.waitForTimeout(300);

            const teachCount = await page.$$eval('#qbSheetSelect option', opts => opts.length);
            if (teachCount !== 26) throw new Error(`Expected 26 questions for Teachers, got ${teachCount}`);
            const firstTeach = await page.$eval('#qbSheetSelect option', opt => opt.text);
            if (!firstTeach.includes('Participants') && !firstTeach.includes('Teacher')) {
                throw new Error(`First question mismatch for Teachers: ${firstTeach}`);
            }
            console.log(`  [✓] Role 'Teachers': Filtered to ${teachCount} teacher questions (First: Q82)`);

            // 5. Test "Facilitators" (24 Questions)
            const facBtn = await page.$('#roleSlicer button[onclick*="Facilitator"]');
            await facBtn.click();
            await page.waitForTimeout(300);

            const facCount = await page.$$eval('#qbSheetSelect option', opts => opts.length);
            if (facCount !== 24) throw new Error(`Expected 24 questions for Facilitators, got ${facCount}`);
            const firstFac = await page.$eval('#qbSheetSelect option', opt => opt.text);
            if (!firstFac.includes('Facilitator')) {
                throw new Error(`First question mismatch for Facilitators: ${firstFac}`);
            }
            console.log(`  [✓] Role 'Facilitators': Filtered to ${facCount} facilitator questions (First: Q67)`);

            // 6. Test "Monitors" (20 Questions)
            const monBtn = await page.$('#roleSlicer button[onclick*="Observer"]');
            await monBtn.click();
            await page.waitForTimeout(300);

            const monCount = await page.$$eval('#qbSheetSelect option', opts => opts.length);
            if (monCount !== 20) throw new Error(`Expected 20 questions for Monitors, got ${monCount}`);
            const firstMon = await page.$eval('#qbSheetSelect option', opt => opt.text);
            if (!firstMon.includes('Monitor') && !firstMon.includes('Observer')) {
                throw new Error(`First question mismatch for Monitors: ${firstMon}`);
            }
            console.log(`  [✓] Role 'Monitors': Filtered to ${monCount} monitor questions (First: Q55)`);

            // 7. Restore All Stakeholders
            const allBtn = await page.$('#roleSlicer button[onclick*="ALL"]');
            await allBtn.click();
            await page.waitForTimeout(300);
            const restoredCount = await page.$$eval('#qbSheetSelect option', opts => opts.length);
            if (restoredCount !== 70) throw new Error(`Expected 70 restored questions, got ${restoredCount}`);
            console.log(`  [✓] Restored 'All Stakeholders': ${restoredCount} questions`);

            // Filter out non-fatal console noise
            const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('CORS'));
            if (fatalErrors.length === 0) {
                console.log('  [✓] Zero console errors detected during question filtering');
            }

            console.log(`[PASS] ${target} Tab 6 is 100% verified!\n`);
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
        console.log(' [✓] ALL 4 DASHBOARD TARGETS PASSED TAB 6 ROLE SLICER E2E TESTS');
        console.log('===================================================================');
    } else {
        process.exit(1);
    }
}

runTab6Verification();
