function getDistrictSurveyVal(prog, role, sheet, col, district) {
      const s = dataPackage.surveys.find(x => 
        x.program === prog && 
        x.role === role && 
        (x.sheet === sheet || x.sheet.split(',').map(k => k.trim()).includes(sheet) || x.sheet.includes(sheet))
      );
      if (!s) return 0;
      const row = s.districtData.find(d => d.district === district);
      return row ? (row[col] || 0) : 0;
    }

    // 3. District League
    function initDistrictLeague() {
      const table = document.getElementById('leagueGrid');
      const heading = document.getElementById('leagueTableHeading');
      const isHi = (currentLang === 'hi');
      
      let headerHtml = '';
      let rowsHtml = '';

      if (activeProgram === 'DO') {
        heading.innerText = isHi ? '🗺️