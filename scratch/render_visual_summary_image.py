import os
from playwright.sync_api import sync_playwright

def render_poster_images():
    html_path = os.path.abspath('scratch/visual_summary_poster.html')
    url = f'file:///{html_path}'
    jpg_path = os.path.abspath('RSK_Shaikshik_Samwaad_One_Page_Visual_Summary.jpg')
    png_path = os.path.abspath('RSK_Shaikshik_Samwaad_One_Page_Visual_Summary.png')
    
    print(f'Rendering poster from: {url}')

    with sync_playwright() as p:
        # Launch browser with high device_scale_factor for ultra-crisp typography
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'width': 1280, 'height': 1100},
            device_scale_factor=2
        )
        page = context.new_page()
        page.goto(url, wait_until='networkidle')
        page.wait_for_timeout(1000)

        # Ensure web fonts are completely loaded
        page.evaluate('document.fonts.ready')

        # Take full-page screenshots
        page.screenshot(path=png_path, full_page=True)
        print(f'Successfully rendered PNG: {png_path}')

        page.screenshot(path=jpg_path, type='jpeg', quality=95, full_page=True)
        print(f'Successfully rendered JPG: {jpg_path}')

        browser.close()

if __name__ == '__main__':
    render_poster_images()
