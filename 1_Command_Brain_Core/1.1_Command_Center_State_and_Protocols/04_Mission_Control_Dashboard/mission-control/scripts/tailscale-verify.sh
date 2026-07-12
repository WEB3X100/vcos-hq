#!/usr/bin/env bash
# tailscale-verify.sh — L1/L2 preflight for dual-laptop flywheel
# Usage: ./tailscale-verify.sh [L2_TAILSCALE_HOSTNAME_OR_IP]
# Example: ./tailscale-verify.sh l2-windows
set -euo pipefail

L2_TARGET="${1:-}"
PASS=0
FAIL=0
WARN=0

ok()   { echo "  ✓ $1"; PASS=$((PASS + 1)); }
bad()  { echo "  ✗ $1"; FAIL=$((FAIL + 1)); }
warn() { echo "  ! $1"; WARN=$((WARN + 1)); }

echo "━━━ Tailscale Dual-Laptop Preflight ━━━"
echo "Host: $(hostname) | $(date -Iseconds 2>/dev/null || date)"
echo

# 1. Tailscale installed and running
if command -v tailscale >/dev/null 2>&1; then
  ok "tailscale CLI found"
else
  bad "tailscale CLI not found — install from https://tailscale.com/download"
fi

if tailscale status >/dev/null 2>&1; then
  ok "tailscale status reachable"
  echo
  echo "--- tailscale status (peers) ---"
  tailscale status | head -20
  echo "---"
else
  bad "tailscale status failed — daemon not running or not logged in"
fi

# 2. This machine's Tailscale IP
if command -v tailscale >/dev/null 2>&1; then
  TS_IP=$(tailscale ip -4 2>/dev/null || true)
  if [[ -n "${TS_IP}" ]]; then
    ok "local Tailscale IPv4: ${TS_IP}"
  else
    warn "no Tailscale IPv4 assigned"
  fi
fi

# 3. GitHub transport (coordination bus — independent of Tailscale)
echo
echo "--- Git / GitHub transport ---"
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  ok "inside git worktree: $(git rev-parse --show-toplevel)"
  REMOTE=$(git remote get-url origin 2>/dev/null || echo "none")
  echo "  origin: ${REMOTE}"
  if git fetch origin --dry-run 2>/dev/null; then
    ok "git fetch origin (dry-run) OK"
  else
    warn "git fetch dry-run failed — check credentials/network"
  fi
  echo "  HEAD: $(git rev-parse --short HEAD) @ $(git log -1 --format='%s')"
else
  warn "not inside a git repo — cd to vcos-hq first"
fi

# 4. Optional L2 peer ping
echo
echo "--- L2 peer check ---"
if [[ -z "${L2_TARGET}" ]]; then
  warn "no L2 target passed — usage: $0 <l2-tailscale-name-or-ip>"
  echo "  Peers from tailscale status above — pass one as argument to ping."
else
  if ping -c 2 -W 3 "${L2_TARGET}" >/dev/null 2>&1; then
    ok "ping ${L2_TARGET} succeeded"
  else
    bad "ping ${L2_TARGET} failed"
  fi
  # SSH optional — only if L2 has OpenSSH and Tailscale SSH enabled
  if command -v ssh >/dev/null 2>&1; then
    if ssh -o BatchMode=yes -o ConnectTimeout=5 "${L2_TARGET}" "hostname" 2>/dev/null; then
      ok "ssh ${L2_TARGET} hostname OK"
    else
      warn "ssh to ${L2_TARGET} not available (optional)"
    fi
  fi
fi

# 5. Secret leak quick scan (repo only)
echo
echo "--- Repo secret scan (quick) ---"
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  LEAK=$(git ls-files | grep -E '\.env$|\.pem$|id_rsa|credentials\.json|\.hermes/' | grep -v -E 'secret-handling|\.md$' || true)
  if [[ -z "${LEAK}" ]]; then
    ok "no obvious secret filenames tracked in git index"
  else
    bad "potential secret files tracked: ${LEAK}"
  fi
  if git diff --cached --name-only | grep -E '\.env|hermes' >/dev/null 2>&1; then
    bad "staged files match secret patterns — unstage before commit"
  else
    ok "no .env/hermes patterns in staged files"
  fi
fi

echo
echo "━━━ Summary: ${PASS} pass | ${WARN} warn | ${FAIL} fail ━━━"
if [[ "${FAIL}" -gt 0 ]]; then
  echo "VERDICT: BLOCKED — fix failures before VCOS-STAB-03 SHIP"
  exit 1
fi
echo "VERDICT: READY — safe to trigger L2 mission (Tailscale + git preflight)"
exit 0