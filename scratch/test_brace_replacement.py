import re

with open(r"C:\My Files Work\CLSS RF BI\RSK_Executive_BI_ProMax.html", "r", encoding="utf-8", errors="ignore") as f:
    template_html = f.read()

def replace_js_function(src, func_name, new_code):
    # Match function body by counting braces
    pattern = r'function\s+' + func_name + r'\s*\([^)]*\)\s*\{'
    m = re.search(pattern, src)
    if not m:
        raise ValueError(f"Could not find function {func_name}")
    start = m.start()
    brace_count = 0
    end = start
    for i in range(m.end() - 1, len(src)):
        if src[i] == '{':
            brace_count += 1
        elif src[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                end = i + 1
                break
    return src[:start] + new_code + src[end:]

html = template_html
print('Before replacement functions count:', len(re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', html)))

# Test replacing updateKPIs
html = replace_js_function(html, 'updateKPIs', 'function updateKPIs() { console.log("NEW updateKPIs"); }')
html = replace_js_function(html, 'initOverviewCharts', 'function initOverviewCharts() { console.log("NEW initOverviewCharts"); }')
html = replace_js_function(html, 'initPedagogyRadar', 'function initPedagogyRadar() { console.log("NEW initPedagogyRadar"); }')

funcs = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', html)
print('After replacement functions count:', len(funcs))
print('activateTab present:', 'activateTab' in funcs)
print('updateBlockView present:', 'updateBlockView' in funcs)
print('animateValue present:', 'animateValue' in funcs)
print('getChartTheme present:', 'getChartTheme' in funcs)
