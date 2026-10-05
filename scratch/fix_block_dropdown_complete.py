import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Starting fix for #d360BlockDropdown in build_enhanced_studio.py...")

with open('build_enhanced_studio.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update initDistrict360 to always call populateD360BlockDropdown()
old_init_d360 = """function initDistrict360() {
      const dd = document.getElementById('d360Dropdown');
      if (!dd) return;
      dd.innerHTML = '';
      const isHi = (typeof currentLang !== 'undefined' && currentLang === 'hi');
      ((typeof getActiveCycleSummary === "function") ? getActiveCycleSummary() : (dataPackage.districtSummary || [])).forEach(d => {
        const opt = document.createElement('option');
        opt.value = d.district;
        opt.innerText = isHi ? getDistName(d.district) : d.district;
        dd.appendChild(opt);
      });
      if (dd.options.length > 0) {
        dd.selectedIndex = 0;
        updateDistrict360View();
      }
    }"""

new_init_d360 = """function initDistrict360() {
      const dd = document.getElementById('d360Dropdown');
      if (!dd) return;
      const currentVal = dd.value;
      dd.innerHTML = '';
      const isHi = (typeof currentLang !== 'undefined' && currentLang === 'hi');
      ((typeof getActiveCycleSummary === "function") ? getActiveCycleSummary() : (dataPackage.districtSummary || [])).forEach(d => {
        const opt = document.createElement('option');
        opt.value = d.district;
        opt.innerText = isHi ? getDistName(d.district) : d.district;
        dd.appendChild(opt);
      });
      if (currentVal && [...dd.options].some(o => o.value === currentVal)) {
        dd.value = currentVal;
      } else if (dd.options.length > 0) {
        dd.selectedIndex = 0;
      }
      populateD360BlockDropdown();
      updateDistrict360View();
    }"""

# 2. Update populateD360BlockDropdown to be robust and case-insensitive
old_pop_block = """function populateD360BlockDropdown() {
      const dSel = document.getElementById('d360Dropdown');
      const bSel = document.getElementById('d360BlockDropdown');
      if (!dSel || !bSel) return;
      const distName = dSel.value;
      bSel.innerHTML = '<option value="ALL">All Blocks (District Aggregation)</option>';
      const isHi = (typeof currentLang !== 'undefined' && currentLang === 'hi');
      
      const blkList = (typeof getActiveCycleBlockSummary === "function") ? getActiveCycleBlockSummary() : (dataPackage.blockSummary || []);
      const distBlocks = blkList.filter(b => b.district === distName);
      distBlocks.forEach(b => {
        const opt = document.createElement('option');
        opt.value = b.block;
        opt.innerText = isHi ? `${b.block} (${b.participants.toLocaleString()} शिक्षक)` : `${b.block} (${b.participants.toLocaleString()} Teachers)`;
        bSel.appendChild(opt);
      });
    }"""

new_pop_block = """function populateD360BlockDropdown() {
      const dSel = document.getElementById('d360Dropdown');
      const bSel = document.getElementById('d360BlockDropdown');
      if (!dSel || !bSel) return;
      const distName = dSel.value || 'Agar Malwa';
      const currentBlockVal = bSel.value;
      const isHi = (typeof currentLang !== 'undefined' && currentLang === 'hi');
      
      bSel.innerHTML = `<option value="ALL">${isHi ? 'सभी ब्लॉक (जिला एकत्रीकरण)' : 'All Blocks (District Aggregation)'}</option>`;
      
      const blkList = (typeof getActiveCycleBlockSummary === "function") ? getActiveCycleBlockSummary() : (dataPackage.blockSummary || []);
      const distBlocks = blkList.filter(b => String(b.district).trim().toLowerCase() === String(distName).trim().toLowerCase());
      distBlocks.forEach(b => {
        const opt = document.createElement('option');
        opt.value = b.block;
        const count = b.participants || b.actualAttendees || b.total || 0;
        opt.innerText = isHi ? `${b.block} (${count.toLocaleString()} शिक्षक)` : `${b.block} (${count.toLocaleString()} Teachers)`;
        bSel.appendChild(opt);
      });
      
      if (currentBlockVal && [...bSel.options].some(o => o.value === currentBlockVal)) {
        bSel.value = currentBlockVal;
      } else {
        bSel.value = 'ALL';
      }
    }"""

# 3. Update updateDistrict360View to auto-populate block dropdown if empty
old_upd_d360 = """function updateDistrict360View() {
      const dd = document.getElementById('d360Dropdown');
      if (!dd || !dd.value) return;
      const dname = dd.value;"""

new_upd_d360 = """function updateDistrict360View() {
      const dd = document.getElementById('d360Dropdown');
      if (!dd || !dd.value) return;
      const bSel = document.getElementById('d360BlockDropdown');
      if (bSel && bSel.options.length <= 1) {
        populateD360BlockDropdown();
      }
      const dname = dd.value;"""

# 4. Update activateTab for tab-d360
old_act_d360 = """      } else if (tabId === 'tab-d360') {
        updateDistrict360View();
        updateDistrictComparison();"""

new_act_d360 = """      } else if (tabId === 'tab-d360') {
        if (typeof populateD360BlockDropdown === 'function') populateD360BlockDropdown();
        updateDistrict360View();
        updateDistrictComparison();"""

# 5. Update setLanguage to re-populate block dropdown with translated text
old_setlang_d360 = """        const d360BlockLbl = document.querySelector('label[for="d360BlockDropdown"]');
        if (d360BlockLbl) d360BlockLbl.innerText = t.d360LblBlock;"""

new_setlang_d360 = """        const d360BlockLbl = document.querySelector('label[for="d360BlockDropdown"]');
        if (d360BlockLbl) d360BlockLbl.innerText = t.d360LblBlock;
        if (typeof populateD360BlockDropdown === 'function') populateD360BlockDropdown();"""

# Apply replacements in build_enhanced_studio.py
if "initDistrict360_replace" not in code:
    code = code.replace(
        "enhanced_js = motion_fallback_code + orig_js",
        f"enhanced_js = motion_fallback_code + orig_js.replace('''{old_init_d360}''', '''{new_init_d360}''').replace('''{old_pop_block}''', '''{new_pop_block}''').replace('''{old_upd_d360}''', '''{new_upd_d360}''').replace('''{old_act_d360}''', '''{new_act_d360}''').replace('''{old_setlang_d360}''', '''{new_setlang_d360}''')"
    )

with open('build_enhanced_studio.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_enhanced_studio.py updated with Block dropdown fixes.")
