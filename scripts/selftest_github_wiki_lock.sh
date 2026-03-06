#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOCK_SCRIPT="$ROOT/scripts/with_github_wiki_lock.sh"
LOCK_DIR="$ROOT/ignore/github-wiki-toolchain.lock"
SELFTEST_LOCK_DIR="$ROOT/ignore/github-wiki-lock-selftest.lock"
WAIT_SECONDS="${GITHUB_WIKI_LOCK_WAIT_SECONDS:-180}"
TEST_ROOT="$ROOT/ignore/github-wiki-lock-selftest-$PPID-$$"
SELFTEST_LOCK_HELD=0

log() {
  echo "[github-wiki-lock-selftest] $1"
}

fail() {
  echo "[github-wiki-lock-selftest] $1" >&2
  exit 1
}

cleanup() {
  rm -rf "$TEST_ROOT"
  if [[ "$SELFTEST_LOCK_HELD" == "1" ]]; then
    rm -rf "$SELFTEST_LOCK_DIR"
  fi
}
trap cleanup EXIT

wait_for_file() {
  local path="$1"
  local label="$2"
  local start_time
  local now

  start_time="$(date +%s)"

  while true; do
    if [[ -f "$path" ]]; then
      return 0
    fi

    now="$(date +%s)"
    if (( now - start_time >= WAIT_SECONDS )); then
      break
    fi
    sleep 0.1
  done

  fail "Timed out waiting for $label: $path"
}

wait_for_pattern() {
  local path="$1"
  local pattern="$2"
  local label="$3"
  local start_time
  local now

  start_time="$(date +%s)"

  while true; do
    if [[ -f "$path" ]] && grep -Eq "$pattern" "$path"; then
      return 0
    fi

    now="$(date +%s)"
    if (( now - start_time >= WAIT_SECONDS )); then
      break
    fi
    sleep 0.1
  done

  fail "Timed out waiting for $label: $pattern"
}

reset_state() {
  rm -rf "$LOCK_DIR" "$TEST_ROOT"
  mkdir -p "$ROOT/ignore" "$TEST_ROOT"
}

acquire_selftest_lock() {
  local start_time
  local now

  start_time="$(date +%s)"
  mkdir -p "$ROOT/ignore"

  while ! mkdir "$SELFTEST_LOCK_DIR" 2>/dev/null; do
    now="$(date +%s)"
    if (( now - start_time >= WAIT_SECONDS )); then
      fail "Timed out waiting for lock self-test guard: $SELFTEST_LOCK_DIR"
    fi
    sleep 1
  done

  SELFTEST_LOCK_HELD=1
}

wait_for_toolchain_lock_idle() {
  local start_time
  local now
  local lock_pid

  start_time="$(date +%s)"

  while [[ -d "$LOCK_DIR" ]]; do
    if [[ -f "$LOCK_DIR/pid" ]]; then
      lock_pid="$(cat "$LOCK_DIR/pid" 2>/dev/null || true)"
      if [[ -n "$lock_pid" ]] && ! kill -0 "$lock_pid" 2>/dev/null; then
        rm -rf "$LOCK_DIR"
        break
      fi
    fi

    now="$(date +%s)"
    if (( now - start_time >= WAIT_SECONDS )); then
      fail "Timed out waiting for the GitHub Wiki toolchain lock to become idle."
    fi
    sleep 1
  done
}

run_stale_lock_recovery() {
  local output

  log "stale-lock-recovery"
  reset_state
  mkdir -p "$LOCK_DIR"
  printf '99999999\n' > "$LOCK_DIR/pid"

  output="$("$LOCK_SCRIPT" bash -lc 'echo STALE_LOCK_CLEARED')"
  [[ "$output" == *"STALE_LOCK_CLEARED"* ]] || fail "Stale lock recovery did not complete."
  [[ ! -d "$LOCK_DIR" ]] || fail "Lock directory remained after stale lock recovery."
}

run_serialization() {
  local event_log="$TEST_ROOT/serialization.log"
  local expected
  local actual
  local first_pid
  local second_pid

  log "serialization"
  reset_state
  : > "$event_log"

  "$LOCK_SCRIPT" bash -lc "printf 'first-start\n' >> '$event_log'; sleep 2; printf 'first-end\n' >> '$event_log'" &
  first_pid=$!
  wait_for_pattern "$event_log" '^first-start$' "first lock holder start"

  "$LOCK_SCRIPT" bash -lc "printf 'second-start\n' >> '$event_log'; printf 'second-end\n' >> '$event_log'" &
  second_pid=$!

  wait "$first_pid"
  wait "$second_pid"

  expected=$'first-start\nfirst-end\nsecond-start\nsecond-end'
  actual="$(cat "$event_log")"
  [[ "$actual" == "$expected" ]] || fail "Unexpected serialization order: $actual"
}

run_timeout() {
  local timeout_log="$TEST_ROOT/timeout.log"
  local holder_pid

  log "timeout"
  reset_state

  "$LOCK_SCRIPT" bash -lc 'sleep 3' &
  holder_pid=$!
  wait_for_file "$LOCK_DIR/pid" "lock pid file"

  if GITHUB_WIKI_LOCK_WAIT_SECONDS=1 "$LOCK_SCRIPT" true >"$timeout_log" 2>&1; then
    fail "Second lock attempt unexpectedly succeeded during timeout test."
  fi

  grep -q "Timed out waiting for GitHub Wiki toolchain lock" "$timeout_log" || fail "Timeout message was not emitted."
  wait "$holder_pid"
}

run_failure_cleanup() {
  local failure_log="$TEST_ROOT/failure.log"
  local status=0

  log "failure-cleanup"
  reset_state

  if "$LOCK_SCRIPT" bash -lc 'exit 23' >"$failure_log" 2>&1; then
    fail "Wrapped failing command unexpectedly succeeded."
  else
    status=$?
  fi

  [[ "$status" -eq 23 ]] || fail "Wrapped failure exit code was not preserved: $status"
  [[ ! -d "$LOCK_DIR" ]] || fail "Lock directory remained after wrapped command failure."
}

acquire_selftest_lock
wait_for_toolchain_lock_idle
run_stale_lock_recovery
run_serialization
run_timeout
run_failure_cleanup

log "ok"
