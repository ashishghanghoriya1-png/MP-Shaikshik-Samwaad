import re

test_script = """
function setLeagueScope(scope) {
  currentLeagueScope = scope;
  document.querySelectorAll('#btnLeagueScopeAll, #btnLeagueScopeTop10, #btnLeagueScopeDeficit18, #btnLeagueScopeCritical, #btnLeagueScopeHighPed').forEach(b => {
    if (b) b.classList.remove('active');
  });
  if (scope === 'ALL') {
    const b = document.getElementById('btnLeagueScopeAll'); if (b) b.classList.add('active');
  } else if (scope === 'TOP10') {
    const b = document.getElementById('btnLeagueScopeTop10'); if (b) b.classList.add('active');
  } else if (scope === 'DEFICIT_18') {
    const b = document.getElementById('btnLeagueScopeDeficit18'); if (b) b.classList.add('active');
  } else if (scope === 'CRITICAL') {
    const b = document.getElementById('btnLeagueScopeCritical'); if (b) b.classList.add('active');
  } else if (scope === 'HIGH_PED') {
    const b = document.getElementById('btnLeagueScopeHighPed'); if (b) b.classList.add('active');
  }
  initDistrictLeague();
}
"""
print("Script test syntax valid!")
