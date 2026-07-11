#!/usr/bin/env bash
# Phase 1 scripted gates — Python stdlib server
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
PORT="${VCOS_MC_PORT:-8765}"
HOST="127.0.0.1"
BASE="http://${HOST}:${PORT}"
LOG="$ROOT/data/outbox/test-phase1.log"
mkdir -p "$ROOT/data/outbox"
: >"$LOG"
pass=0
fail=0

log() { echo "$@" | tee -a "$LOG"; }
ok() { log "PASS: $*"; pass=$((pass + 1)); }
bad() { log "FAIL: $*"; fail=$((fail + 1)); }

log "=== P1-16 static safety scan ==="
SCAN_FAIL=0

if grep -RIn --exclude-dir=data --exclude='*.log' --exclude='WAVE0*' --exclude='test-phase1.sh' \
  -E '0\.0\.0\.0' . 2>/dev/null | grep -v 'not.*0\.0\.0\.0' | grep -v 'Never' | head -20 | tee -a "$LOG" | grep -q .; then
  SCAN_FAIL=1
fi

# hardcoded secret-like tokens (not env var names)
if grep -RIn --exclude-dir=data --exclude='*.log' --exclude='test-phase1.sh' \
  -E 'sk-[a-zA-Z0-9]{20,}|xai-[a-zA-Z0-9]{20,}' . 2>/dev/null | head -5 | tee -a "$LOG" | grep -q .; then
  SCAN_FAIL=1
fi

# Affirmative forbidden whole-words in UI (exclude "Sentinel", honest negatives)
while IFS= read -r line; do
  if echo "$line" | grep -qiE 'not (sent|synced|approved|published|connected|delivered)'; then
    continue
  fi
  if echo "$line" | grep -q 'Sentinel'; then
    continue
  fi
  log "forbidden affirmative UI: $line"
  SCAN_FAIL=1
done < <(grep -nE '\b(Sent|Synced|Approved|Published|Connected|Delivered)\b' app.js 2>/dev/null || true)

# /approval done must not mutate status to done
if grep -n "status.*=.*['\"]done['\"]" server.py | grep -i approval | tee -a "$LOG" | grep -q .; then
  SCAN_FAIL=1
fi
if ! grep -q 'approval clear' server.py; then
  log "missing /approval clear"
  SCAN_FAIL=1
fi
if ! grep -q 'startswith("/approval done' server.py && ! grep -q "startswith('/approval done" server.py; then
  # allow startswith("/approval done
  if ! grep -q 'approval done' server.py; then
    log "missing legacy /approval done help redirect"
    SCAN_FAIL=1
  fi
fi

if [[ $SCAN_FAIL -eq 0 ]]; then ok "P1-16 static scan clean"; else bad "P1-16 static scan"; fi

if grep -q '127.0.0.1' server.py && grep -q 'ThreadingHTTPServer' server.py; then
  ok "P1-14 source binds localhost"
else
  bad "P1-14 source bind"
fi

log "=== P1-01 / P1-06 no-key startup ==="
if ! curl -sf "$BASE/api/health" >/dev/null 2>&1; then
  unset XAI_API_KEY GROK_API_KEY || true
  python3 server.py >>"$LOG" 2>&1 &
  echo $! > data/outbox/server.pid
  for _ in $(seq 1 15); do
    curl -sf "$BASE/api/health" >/dev/null 2>&1 && break
    sleep 0.2
  done
fi

if curl -sf "$BASE/api/health" | tee -a "$LOG" | grep -q '"ok"'; then
  ok "P1-01 health"
else
  bad "P1-01 health"
fi

HJSON=$(curl -sf "$BASE/api/health")
if echo "$HJSON" | grep -q '"llm": false'; then
  ok "P1-06 no-key llm false"
elif echo "$HJSON" | grep -q '"llm": true'; then
  log "NOTE: llm true (server may have been started with a key) — health still ok"
  ok "P1-06 health ok with llm true note"
else
  bad "P1-06 health parse"
fi

log "=== schema ==="
if python3 - <<'PY' | tee -a "$LOG"
import json, sys, urllib.request
s = json.loads(urllib.request.urlopen("http://127.0.0.1:8765/api/state").read())
required = ["version","updated_at","data_freshness","north_star","active_priority_order",
            "parked","tonight_chunk","l1","l2","ships","approvals_queue","obsidian","jarvis"]
missing = [k for k in required if k not in s]
if missing:
    print("MISSING", missing)
    sys.exit(1)
for k in ("lane","task","done_means"):
    assert k in s.get("tonight_chunk",{}), k
for k in ("vault_path","home_note","fast_path"):
    assert k in s.get("obsidian",{}), k
for k in ("agents","gateway_note","source","last_checked"):
    assert k in s.get("jarvis",{}), k
print("schema ok")
PY
then ok "schema validation"; else bad "schema validation"; fi

log "=== slash smoke ==="
R1=$(curl -sf -X POST "$BASE/api/chat/send" -H 'Content-Type: application/json' \
  -d '{"channel":"l1","content":"/approval done ap-001"}')
echo "$R1" | tee -a "$LOG" | grep -qiE 'clear|retired|not supported|sounds like' \
  && ok "legacy /approval done redirect" || bad "legacy /approval done"

R2=$(curl -sf -X POST "$BASE/api/chat/send" -H 'Content-Type: application/json' \
  -d '{"channel":"l2","content":"phase1-script-probe"}')
echo "$R2" | tee -a "$LOG" | grep -qi 'not sent' \
  && ok "L2 queued not sent label" || bad "L2 label"

grep -q 'phase1-script-probe' data/outbox/l2-telegram-queue.md && ok "L2 outbox file" || bad "L2 outbox file"

# malformed tonight
R3=$(curl -sf -X POST "$BASE/api/chat/send" -H 'Content-Type: application/json' \
  -d '{"channel":"l1","content":"/tonight onlyone"}')
echo "$R3" | tee -a "$LOG" | grep -qi 'Format' && ok "malformed /tonight help" || bad "malformed /tonight"

log "=== SUMMARY pass=$pass fail=$fail ==="
echo "pass=$pass fail=$fail" >>"$LOG"
if [[ $fail -gt 0 ]]; then exit 1; fi
exit 0
