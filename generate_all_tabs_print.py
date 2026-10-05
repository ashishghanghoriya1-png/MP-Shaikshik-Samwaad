import os
import sys
import io
import time
from PIL import Image
from playwright.sync_api import sync_playwright

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

tabs_info = [
    {
        "id": "tab-overview",
        "name": "01_Executive_Overview_and_KPI_Studio",
        "title": "Tab 1: Executive Overview & Statewide Macro Telemetry"
    },
    {
        "id": "tab-rf",
        "name": "02_Results_Framework_7_Pillars",
        "title": "Tab 2: Results Framework (7-Pillar Health Scorecard)"
    },
    {
        "id": "tab-d360",
        "name": "03_District_360_Deep_Dive",
        "title": "Tab 3: District 360° Deep-Dive & Comparative Benchmarking"
    },
    {
        "id": "tab-league",
        "name": "04_52_District_Strategic_League",
        "title": "Tab 4: 52-District Strategic Performance League & Quadrants"
    },
    {
        "id": "tab-blocks",
        "name": "05_Block_Level_Micro_Directory",
        "title": "Tab 5: 322-Block Granular Cadre Directory & Micro-Performance"
    },
    {
        "id": "tab-questions",
        "name": "06_Question_Bank_Item_Diagnostics",
        "title": "Tab 6: Question Bank Item-Level Diagnostic Analysis"
    },
    {
        "id": "tab-pedagogy",
        "name": "07_Pedagogical_Transformation_Studio",
        "title": "Tab 7: Pedagogical Transformation Studio & Misconception Matrices"
    },
    {
        "id": "tab-governance",
        "name": "08_Multi_Tier_Governance_Telemetry",
        "title": "Tab 8: Multi-Tier Operational Governance & Monitoring Telemetry"
    },
    {
        "id": "tab-cohort",
        "name": "09_Same_Block_Peer_Cohort_Benchmarks",
        "title": "Tab 9: Same-Block Longitudinal Peer Cohort Benchmarking"
    },
    {
        "id": "tab-insights",
        "name": "10_Thematic_Topology_Field_Voices",
        "title": "Tab 10: Thematic Topology of Field Voices (30,000+ Teacher Submissions)"
    },
    {
        "id": "tab-research",
        "name": "11_Academic_Research_Monograph",
        "title": "Tab 11: Academic Research Monograph & Policy Briefing"
    }
]

os.makedirs('dashboard_prints', exist_ok=True)
index_path = os.path.abspath('index.html')

image_paths = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    # Set high-DPI viewport (1600x1200 @ 2x device_scale_factor) for crisp print quality
    context = browser.new_context(
        viewport={'width': 1600, 'height': 1100},
        device_scale_factor=2
    )
    page = context.new_page()
    page.goto('file:///' + index_path.replace('\\', '/'), wait_until='networkidle')
    page.wait_for_timeout(2000)

    for idx, tab in enumerate(tabs_info, start=1):
        tab_id = tab["id"]
        print(f"Rendering {tab['title']} ({tab_id})...")
        
        # Click the tab button or invoke activateTab in browser context
        page.evaluate(f"activateTab('{tab_id}')")
        page.wait_for_timeout(1500)
        
        # Trigger chart resize and re-render if needed
        page.evaluate("""
            window.dispatchEvent(new Event('resize'));
            if (window.Chart) {
                Object.values(Chart.instances || {}).forEach(chart => {
                    chart.resize();
                    chart.update();
                });
            }
        """)
        page.wait_for_timeout(800)

        # In case of district 360, let's make sure sample district or comparison is loaded
        if tab_id == 'tab-d360':
            page.evaluate("""
                const distSel = document.getElementById('d360DistrictSelect');
                if (distSel && distSel.value === '') {
                    distSel.selectedIndex = 1;
                    distSel.dispatchEvent(new Event('change'));
                }
            """)
            page.wait_for_timeout(1000)
        
        # In case of peer cohort, ensure comparison render
        if tab_id == 'tab-cohort':
            page.evaluate("""
                if (typeof renderPeerCohortChart === 'function') {
                    renderPeerCohortChart();
                }
            """)
            page.wait_for_timeout(1000)

        # Take full tab screenshot
        tab_element = page.locator(f"#{tab_id}")
        if tab_element.count() > 0:
            img_file = os.path.join('dashboard_prints', f"{tab['name']}.png")
            page.screenshot(path=img_file, full_page=True)
            image_paths.append(img_file)
            print(f"  -> Captured {img_file} ({os.path.getsize(img_file):,} bytes)")
        else:
            print(f"  -> Warning: #{tab_id} not found!")

    browser.close()

print(f"\nAll {len(image_paths)} tabs captured as high-resolution images in 'dashboard_prints/'.")

# Convert the captured high-resolution images into a single master PDF visual album
print("\nCompiling Master Visual Album PDF...")
pdf_path = os.path.abspath('RSK_Master_CLSS_Complete_Dashboard_Visual_Print.pdf')

pil_images = []
for img_p in image_paths:
    im = Image.open(img_p)
    if im.mode == 'RGBA':
        im = im.convert('RGB')
    pil_images.append(im)

if pil_images:
    pil_images[0].save(
        pdf_path,
        "PDF",
        resolution=150.0,
        save_all=True,
        append_images=pil_images[1:]
    )
    print(f"SUCCESS: Generated Master Visual Print PDF: {pdf_path} ({os.path.getsize(pdf_path):,} bytes)")
