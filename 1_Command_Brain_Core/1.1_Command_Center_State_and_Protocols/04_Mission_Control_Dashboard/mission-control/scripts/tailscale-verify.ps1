# tailscale-verify.ps1 — L2 Windows preflight for dual-laptop flywheel
# Usage: .\tailscale-verify.ps1 [-L1Target "mac-sentinel-tailscale-name"]
param(
    [string]$L1Target = ""
)

$Pass = 0
$Fail = 0
$Warn = 0

function Ok($msg)   { Write-Host "  [OK] $msg" -ForegroundColor Green;  $script:Pass++ }
function Bad($msg)  { Write-Host "  [FAIL] $msg" -ForegroundColor Red;    $script:Fail++ }
function Warn($msg) { Write-Host "  [WARN] $msg" -ForegroundColor Yellow; $script:Warn++ }

Write-Host "━━━ Tailscale Dual-Laptop Preflight (L2 Windows) ━━━"
Write-Host "Host: $env:COMPUTERNAME | $(Get-Date -Format o)"
Write-Host ""

# 1. Tailscale
if (Get-Command tailscale -ErrorAction SilentlyContinue) {
    Ok "tailscale CLI found"
    try {
        tailscale status | Select-Object -First 20
        Ok "tailscale status reachable"
    } catch {
        Bad "tailscale status failed — daemon not running or not logged in"
    }
    try {
        $tsIp = tailscale ip -4 2>$null
        if ($tsIp) { Ok "local Tailscale IPv4: $tsIp" } else { Warn "no Tailscale IPv4" }
    } catch { Warn "could not read tailscale ip" }
} else {
    Bad "tailscale CLI not found — install from https://tailscale.com/download"
}

# 2. Git / GitHub
Write-Host ""
Write-Host "--- Git / GitHub transport ---"
$repoPath = "C:\Users\92324\VCOS-Coordination\vcos-hq"
if (Test-Path $repoPath) {
    Push-Location $repoPath
    Ok "vcos-hq repo found: $repoPath"
    try {
        $origin = git remote get-url origin 2>$null
        Write-Host "  origin: $origin"
        git fetch origin 2>&1 | Out-Null
        Ok "git fetch origin succeeded"
        $head = git rev-parse --short HEAD
        $subj = git log -1 --format=%s
        Write-Host "  HEAD: $head @ $subj"
    } catch {
        Bad "git fetch failed — check credentials"
    }
    Pop-Location
} else {
    Bad "repo not found at $repoPath"
}

# 3. Optional L1 ping
Write-Host ""
Write-Host "--- L1 peer check ---"
if ([string]::IsNullOrEmpty($L1Target)) {
    Warn "no L1 target — usage: .\tailscale-verify.ps1 -L1Target <mac-tailscale-name>"
} else {
    if (Test-Connection -ComputerName $L1Target -Count 2 -Quiet) {
        Ok "ping $L1Target succeeded"
    } else {
        Bad "ping $L1Target failed"
    }
}

# 4. Secret scan
Write-Host ""
Write-Host "--- Repo secret scan (quick) ---"
if (Test-Path $repoPath) {
    Push-Location $repoPath
    $tracked = git ls-files 2>$null | Select-String -Pattern '\.env$|\.pem$|id_rsa|credentials\.json|\.hermes/' | Where-Object { $_ -notmatch 'secret-handling|\.md$' }
    if (-not $tracked) {
        Ok "no obvious secret filenames in git index"
    } else {
        Bad "potential secret files tracked: $tracked"
    }
    $staged = git diff --cached --name-only 2>$null | Select-String -Pattern '\.env|hermes'
    if ($staged) {
        Bad "staged files match secret patterns — unstage before commit"
    } else {
        Ok "no .env/hermes patterns in staged files"
    }
    Pop-Location
}

Write-Host ""
Write-Host "━━━ Summary: $Pass pass | $Warn warn | $Fail fail ━━━"
if ($Fail -gt 0) {
    Write-Host "VERDICT: BLOCKED — fix failures before VCOS-STAB-03 SHIP"
    exit 1
}
Write-Host "VERDICT: READY — safe to execute VCOS-STAB-03"
exit 0