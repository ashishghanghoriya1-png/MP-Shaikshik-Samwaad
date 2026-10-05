import re, sys
sys.stdout.reconfigure(encoding='utf-8')

files_to_update = [
    r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html',
    r'c:\Master Dashboard for CLSS\index.html'
]

replacements = [
    ("0 Teachers Treated TLM Merely as Craft Activity", "7,414 Teachers Treated TLM Merely as Craft Activity"),
    ("0 शिक्षकों ने टीएलएम को केवल सामग्री निर्माण गतिविधि माना", "7,414 शिक्षकों ने टीएलएम को केवल सामग्री निर्माण गतिविधि माना"),
    ("0.0% Crafting Focus", "32.0% Crafting Focus"),
    (
        "In Q177, 42.5% of teachers (18,493) recognized the full experiential cycle (Experiencing → Reflective Questioning → Consolidation). However, 32.0% (0 teachers) reduced TLM solely to hands-on craft making without cognitive reflection.",
        "In Q177, 42.5% of teachers (9,851) recognized the full experiential cycle (Experiencing → Reflective Questioning → Consolidation). However, 32.0% (7,414 teachers) reduced TLM solely to hands-on craft making without cognitive reflection."
    ),
    (
        "Q177 में, 42.5% शिक्षकों (18,493) ने टीएलएम की पूर्ण चक्रीय प्रक्रिया (अनुभव → चिंतन/प्रश्न → समेकन) को समझा। 32.0% शिक्षकों (0) ने इसे केवल सामग्री निर्माण गतिविधि तक सीमित रखा।",
        "Q177 में, 42.5% शिक्षकों (9,851) ने टीएलएम की पूर्ण चक्रीय प्रक्रिया (अनुभव → चिंतन/प्रश्न → समेकन) को समझा। 32.0% शिक्षकों (7,414) ने इसे केवल सामग्री निर्माण गतिविधि तक सीमित रखा।"
    )
]

for fpath in files_to_update:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for old_str, new_str in replacements:
        if old_str in content:
            count = content.count(old_str)
            content = content.replace(old_str, new_str)
            print(f"[{fpath}] Replaced {count} instances.")
            modified = True
            
    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[+] Saved updated file: {fpath}")
    else:
        print(f"[!] No replacements needed in: {fpath}")
