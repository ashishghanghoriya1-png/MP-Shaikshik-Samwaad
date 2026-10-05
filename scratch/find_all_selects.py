import io, sys, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    text = f.read()

selects = re.findall(r'<select[^>]*id=["\']([^"\']+)["\'][^>]*>', text)
print("All <select> elements in Enhanced Dashboard:")
for s in selects:
    print(f"  • #{s}")

# Let's see which select has 'block' or 'Block' in its ID or nearby labels
matches = re.finditer(r'<select[^>]*id=["\']([^"\']+)["\'].*?</select>', text, re.DOTALL)
for m in matches:
    sel_id = m.group(1)
    sel_full = m.group(0)
    options = re.findall(r'<option[^>]*value=["\']([^"\']*)["\'][^>]*>(.*?)</option>', sel_full)
    print(f"\nSelect #{sel_id}: {len(options)} initial options")
    for opt_val, opt_text in options[:5]:
        print(f"   Option: val='{opt_val}' text='{opt_text}'")
