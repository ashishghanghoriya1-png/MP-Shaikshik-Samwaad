with open(r'c:\Master Dashboard for CLSS\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('function filterCohortTable')
print("Position of filterCohortTable:", pos)
if pos != -1:
    print("Snippet around filterCohortTable:\n", html[pos-200:pos+300])

# Also let's check if there is an earlier unclosed function or syntax error in index.html
# Let's write the whole script to a .js file and run node --check or syntax check!
script_start = html.find('<script', 1000) # main script
script_end = html.rfind('</script>')
script_content = html[html.find('>', script_start)+1:script_end]

with open(r'c:\Master Dashboard for CLSS\scratch\main_script.js', 'w', encoding='utf-8') as f:
    f.write(script_content)

print(f"Extracted main script ({len(script_content):,} chars) to scratch/main_script.js")
