# Background Auto-Sync Watcher for MP Shaikshik Samwaad
$workspace = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "Watching folder: $workspace for changes..." -ForegroundColor Cyan

$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $workspace
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true
$watcher.Filter = "*.*"

$debounceTimer = $null

$action = {
    $path = $Event.SourceEventArgs.FullPath
    if ($path -match "\.git") { return }
    Write-Host "Change detected: $path" -ForegroundColor Yellow
    
    # Sync after 3 seconds of quiet
    Start-Sleep -Seconds 3
    
    if (Test-Path "$workspace\RSK_Executive_BI_ProMax.html") {
        Copy-Item "$workspace\RSK_Executive_BI_ProMax.html" -Destination "$workspace\index.html" -Force
        Copy-Item "$workspace\RSK_Executive_BI_ProMax.html" -Destination "$workspace\deploy\index.html" -Force
    }
    
    cd "$workspace"
    git add .
    $time = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    git commit -m "Auto-synced changes on $time"
    git push origin main
    Write-Host "Pushed updates to GitHub Pages!" -ForegroundColor Green
}

Register-ObjectEvent $watcher 'Changed' -Action $action
Register-ObjectEvent $watcher 'Created' -Action $action

Write-Host "Auto-sync watcher is active! Press Ctrl+C to stop." -ForegroundColor Green
while ($true) { Start-Sleep -Seconds 5 }
