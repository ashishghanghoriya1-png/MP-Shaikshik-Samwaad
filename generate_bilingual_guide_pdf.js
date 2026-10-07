/**
 * Generate Executive Bilingual User Guide PDF
 * Rajya Shiksha Kendra (RSK) MP - Shaikshik Samwaad Master Dashboard
 */

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

async function generatePDF() {
    const mdPath = path.join(__dirname, 'docs', 'RSK_Master_Dashboard_Complete_Bilingual_User_Guide.md');
    const mdContent = fs.readFileSync(mdPath, 'utf8');

    const outDirDocs = path.join(__dirname, 'docs');
    const outDirReports = path.join(__dirname, 'PDF_Reports');
    
    if (!fs.existsSync(outDirReports)) {
        fs.mkdirSync(outDirReports, { recursive: true });
    }

    const pdfTargetRoot = path.join(__dirname, 'RSK_Master_Dashboard_Complete_Bilingual_User_Guide.pdf');
    const pdfTargetDocs = path.join(outDirDocs, 'RSK_Master_Dashboard_Complete_Bilingual_User_Guide.pdf');
    const pdfTargetReports = path.join(outDirReports, 'RSK_Master_Dashboard_Complete_Bilingual_User_Guide.pdf');

    // Create styled HTML wrapper
    const htmlContent = `<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <title>RSK Master Dashboard - Bilingual User Guide</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        @page {
            size: A4 portrait;
            margin: 20mm 15mm 20mm 15mm;
            @top-center {
                content: "RAJYA SHIKSHA KENDRA (RSK) MP | BILINGUAL DASHBOARD USER GUIDE (मार्गदर्शिका)";
                font-family: 'Plus Jakarta Sans', 'Noto Sans Devanagari', sans-serif;
                font-size: 8pt;
                color: #64748b;
                border-bottom: 0.5pt solid #e2e8f0;
                padding-bottom: 4px;
            }
            @bottom-left {
                content: "RSK Shaikshik Samwaad BI Portal (CLSS & DO)";
                font-family: 'Plus Jakarta Sans', sans-serif;
                font-size: 8pt;
                color: #64748b;
            }
            @bottom-right {
                content: "Page " counter(page) " of " counter(pages);
                font-family: 'Plus Jakarta Sans', sans-serif;
                font-size: 8pt;
                font-weight: bold;
                color: #008aab;
            }
        }

        body {
            font-family: 'Plus Jakarta Sans', 'Noto Sans Devanagari', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-size: 10pt;
            line-height: 1.6;
            color: #1e293b;
            background-color: #ffffff;
            margin: 0;
            padding: 0;
        }

        .cover-header {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #004d61 100%);
            color: #ffffff;
            padding: 24px;
            border-radius: 12px;
            margin-bottom: 24px;
            border-left: 6px solid #008aab;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }

        .cover-header h1 {
            color: #38bdf8 !important;
            margin: 0 0 6px 0;
            font-size: 18pt;
            font-weight: 800;
            line-height: 1.3;
        }

        .cover-header .sub-badge {
            display: inline-block;
            background: rgba(0, 138, 171, 0.3);
            border: 1px solid #38bdf8;
            color: #f8fafc;
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 8.5pt;
            font-weight: 600;
            margin-bottom: 10px;
        }

        .cover-header p {
            margin: 4px 0 0 0;
            font-size: 9.5pt;
            color: #cbd5e1;
        }

        h1, h2, h3, h4 {
            color: #0f172a;
            font-family: 'Plus Jakarta Sans', 'Noto Sans Devanagari', sans-serif;
            page-break-after: avoid;
        }

        h1 {
            font-size: 16pt;
            font-weight: 800;
            border-bottom: 2px solid #008aab;
            padding-bottom: 6px;
            margin-top: 24px;
            margin-bottom: 14px;
            color: #008aab;
        }

        h2 {
            font-size: 13pt;
            font-weight: 700;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 4px;
            margin-top: 20px;
            margin-bottom: 10px;
            color: #0284c7;
            page-break-after: avoid;
        }

        h3 {
            font-size: 11pt;
            font-weight: 700;
            margin-top: 14px;
            margin-bottom: 6px;
            color: #334155;
            page-break-after: avoid;
        }

        h4 {
            font-size: 10pt;
            font-weight: 600;
            margin-top: 10px;
            margin-bottom: 4px;
            color: #475569;
            page-break-after: avoid;
        }

        p, li {
            font-size: 9.5pt;
            color: #334155;
            line-height: 1.55;
        }

        ul, ol {
            margin-top: 4px;
            margin-bottom: 10px;
            padding-left: 20px;
        }

        li {
            margin-bottom: 3px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 12px 0 16px 0;
            font-size: 8.5pt;
            page-break-inside: avoid;
        }

        th, td {
            border: 1px solid #cbd5e1;
            padding: 6px 10px;
            text-align: left;
            vertical-align: top;
        }

        th {
            background-color: #f1f5f9;
            color: #0f172a;
            font-weight: 700;
            border-bottom: 2px solid #94a3b8;
        }

        tr:nth-child(even) td {
            background-color: #f8fafc;
        }

        blockquote {
            background: #f0fdf4;
            border-left: 4px solid #10b981;
            margin: 10px 0;
            padding: 8px 14px;
            border-radius: 0 8px 8px 0;
            color: #065f46;
            font-size: 9pt;
            page-break-inside: avoid;
        }

        code {
            background-color: #f1f5f9;
            color: #0284c7;
            padding: 2px 5px;
            border-radius: 4px;
            font-size: 8.5pt;
            font-family: monospace;
            border: 1px solid #e2e8f0;
        }

        hr {
            border: 0;
            height: 1px;
            background: #e2e8f0;
            margin: 18px 0;
        }

        .tab-section {
            page-break-before: auto;
            margin-bottom: 20px;
        }

        .highlight-box {
            background-color: #f0f9ff;
            border: 1px solid #bae6fd;
            border-radius: 8px;
            padding: 10px 14px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div id="content"></div>
    <script>
        const markdown = ${JSON.stringify(mdContent)};
        document.getElementById('content').innerHTML = marked.parse(markdown);
    </script>
</body>
</html>`;

    console.log('[*] Launching Chromium (msedge) for bilingual PDF rendering...');
    const browser = await chromium.launch({ channel: 'msedge' });
    const page = await browser.newPage();

    // Set viewport & content
    await page.setContent(htmlContent, { waitUntil: 'networkidle' });
    
    // Wait for fonts & DOM elements to stabilize
    await page.waitForTimeout(2000);

    console.log('[*] Generating PDF with high-fidelity Devanagari typography...');
    const pdfBuffer = await page.pdf({
        format: 'A4',
        printBackground: true,
        margin: {
            top: '20mm',
            right: '15mm',
            bottom: '20mm',
            left: '15mm'
        },
        displayHeaderFooter: true,
        headerTemplate: `
            <div style="font-size: 7.5pt; font-family: 'Plus Jakarta Sans', sans-serif; color: #64748b; width: 100%; border-bottom: 0.5px solid #e2e8f0; padding: 0 15mm 4px 15mm; display: flex; justify-content: space-between;">
                <span><strong>RAJYA SHIKSHA KENDRA (RSK) MP</strong> | BILINGUAL DASHBOARD USER GUIDE</span>
                <span>Shaikshik Samwaad Master Analytics (CLSS & DO)</span>
            </div>
        `,
        footerTemplate: `
            <div style="font-size: 7.5pt; font-family: 'Plus Jakarta Sans', sans-serif; color: #64748b; width: 100%; border-top: 0.5px solid #e2e8f0; padding: 4px 15mm 0 15mm; display: flex; justify-content: space-between;">
                <span>RSK BI Portal &mdash; English & Hindi Reference</span>
                <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
            </div>
        `
    });

    fs.writeFileSync(pdfTargetRoot, pdfBuffer);
    fs.writeFileSync(pdfTargetDocs, pdfBuffer);
    fs.writeFileSync(pdfTargetReports, pdfBuffer);

    await browser.close();

    console.log(`[✓] PDF created successfully at:`);
    console.log(`    - ${pdfTargetRoot}`);
    console.log(`    - ${pdfTargetDocs}`);
    console.log(`    - ${pdfTargetReports}`);
    console.log(`    Size: ${(pdfBuffer.length / 1024).toFixed(1)} KB`);
}

generatePDF().catch(err => {
    console.error('Error generating PDF:', err);
    process.exit(1);
});
