#!/usr/bin/env bash
# resolve-issues.sh - automatically resolve GitHub Issues with an AI CLI tool
#
# Usage:
#   ./resolve-issues.sh           # normal run
#   ./resolve-issues.sh --dry-run # dry run (no changes)
#
# Requirements:
#   - gh (GitHub CLI) installed and authenticated
#   - jq installed
#   - a CLI/script configured for AI_CMD

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_REPO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Load .env if present.
ENV_FILE="${ENV_FILE:-${SCRIPT_DIR}/.env}"
if [[ -f "$ENV_FILE" ]]; then
    set -a
    # shellcheck disable=SC1090
    . "$ENV_FILE"
    set +a
fi

# Configurable settings (can be overridden in .env).
REPO="${REPO:-yasufumi-nakata/mind-upload}"
REPO_DIR="${REPO_DIR:-$DEFAULT_REPO_DIR}"
AUTOMATION_DIR="${AUTOMATION_DIR:-$SCRIPT_DIR}"
LOG_DIR="${LOG_DIR:-${AUTOMATION_DIR}/logs}"
LOG_FILE="${LOG_FILE:-${LOG_DIR}/resolve-issues-$(date +%Y%m%d-%H%M%S).log}"
TARGET_BRANCH="${TARGET_BRANCH:-main}"
ISSUE_LIMIT="${ISSUE_LIMIT:-${issue_limit:-50}}"
AI_CMD="${AI_CMD:-codex exec --full-auto -}"
AI_TIMEOUT_SECONDS="${AI_TIMEOUT_SECONDS:-300}"
AI_WORKDIR="${AI_WORKDIR:-$REPO_DIR}"
CO_AUTHOR="${CO_AUTHOR:-}"
ALLOW_DIRTY="${ALLOW_DIRTY:-false}"
AUTO_STASH_DIRTY="${AUTO_STASH_DIRTY:-false}"
DRY_RUN=false

AUTO_STASH_DONE=false
DIRTY_STASH_REF=""

# Argument handling.
if [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN=true
    echo "Dry-run mode: no changes will be made."
fi

# Logging helper.
log() {
    local msg="[$(date '+%Y-%m-%d %H:%M:%S')] $1"
    echo "$msg"
    echo "$msg" >> "$LOG_FILE"
}

# Error handling.
error_exit() {
    log "ERROR: $1"
    exit 1
}

require_cmd() {
    local cmd="$1"
    command -v "$cmd" >/dev/null 2>&1 || error_exit "Required command not found: $cmd"
}

append_markdown_path_list() {
    local paths="$1"
    local out_file="$2"
    if [[ -z "$paths" ]]; then
        echo "- (No changed files)" >> "$out_file"
        return
    fi
    while IFS= read -r path; do
        [[ -z "$path" ]] && continue
        printf -- '- `%s`\n' "$path" >> "$out_file"
    done <<< "$paths"
}

append_markdown_numstat_list() {
    local numstat="$1"
    local out_file="$2"
    if [[ -z "$numstat" ]]; then
        echo "- (No diff statistics)" >> "$out_file"
        return
    fi
    while IFS=$'\t' read -r added deleted path; do
        [[ -z "$path" ]] && continue
        printf -- '- `%s` (+%s / -%s)\n' "$path" "$added" "$deleted" >> "$out_file"
    done <<< "$numstat"
}

build_issue_resolution_comment() {
    local issue_num="$1"
    local issue_title="$2"
    local commit_sha="$3"
    local changed_files="$4"
    local diff_numstat="$5"
    local out_file="$6"

    cat > "$out_file" <<EOF
Automated handling has completed.

### Resolution Summary
- To satisfy the requirements of Issue #${issue_num} (“${issue_title}”), the relevant areas were reviewed and updated with a minimal-change approach.
- The applied changes and diff statistics are recorded below.

### Applied Changes
- Commit: \`${commit_sha}\`
- Changed files:
EOF

    append_markdown_path_list "$changed_files" "$out_file"

    cat >> "$out_file" <<'EOF'

### Diff Statistics
EOF

    append_markdown_numstat_list "$diff_numstat" "$out_file"

    cat >> "$out_file" <<'EOF'

No execution-environment details are included in this Issue.
EOF
}

run_with_timeout() {
    local seconds="$1"
    shift
    if command -v gtimeout >/dev/null 2>&1; then
        gtimeout "$seconds" "$@"
        return $?
    elif command -v timeout >/dev/null 2>&1; then
        timeout "$seconds" "$@"
        return $?
    else
        "$@" &
        local cmd_pid=$!
        local watcher_pid
        (
            sleep "$seconds"
            if kill -0 "$cmd_pid" 2>/dev/null; then
                kill -TERM "$cmd_pid" 2>/dev/null || true
                sleep 5
                kill -KILL "$cmd_pid" 2>/dev/null || true
            fi
        ) &
        watcher_pid=$!

        local had_errexit=0
        if [[ $- == *e* ]]; then
            had_errexit=1
        fi
        set +e
        wait "$cmd_pid"
        local exit_code=$?
        if [[ $had_errexit -eq 1 ]]; then
            set -e
        fi

        kill -TERM "$watcher_pid" 2>/dev/null || true
        wait "$watcher_pid" 2>/dev/null || true
        return "$exit_code"
    fi
}

run_ai() {
    if [[ -z "$AI_CMD" ]]; then
        log "ERROR: AI_CMD is not set. Please configure it in .env."
        return 1
    fi
    if [[ ! -d "$AI_WORKDIR" ]]; then
        log "ERROR: AI_WORKDIR does not exist: $AI_WORKDIR"
        return 1
    fi
    export AI_PROMPT_FILE="$PROMPT_FILE"
    (cd "$AI_WORKDIR" && run_with_timeout "$AI_TIMEOUT_SECONDS" sh -c "$AI_CMD")
}

stash_dirty_worktree() {
    local status
    status=$(git -C "$REPO_DIR" status --porcelain)
    if [[ -z "$status" ]]; then
        return 0
    fi
    local stash_msg
    stash_msg="automation-auto-stash $(date '+%Y%m%d-%H%M%S')"
    log "Worktree is dirty; stashing changes temporarily: ${stash_msg}"
    if ! git -C "$REPO_DIR" stash push -u -m "$stash_msg" >/dev/null; then
        error_exit "Failed to create stash. Check for another Git process, permissions, or disk space."
    fi
    DIRTY_STASH_REF=$(git -C "$REPO_DIR" stash list | grep -m 1 "$stash_msg" | cut -d: -f1 || true)
    if [[ -z "$DIRTY_STASH_REF" ]]; then
        log "WARN: Could not identify the temporary stash entry."
    fi
}

stash_failed_issue() {
    local issue_num="$1"
    local status
    status=$(git -C "$REPO_DIR" status --porcelain)
    if [[ -z "$status" ]]; then
        return 0
    fi
    local stash_msg
    stash_msg="automation-failed-issue-${issue_num} $(date '+%Y%m%d-%H%M%S')"
    log "WARN: Stashing Issue #${issue_num} changes temporarily: ${stash_msg}"
    if ! git -C "$REPO_DIR" stash push -u -m "$stash_msg" >/dev/null; then
        error_exit "Failed to stash changes for Issue #${issue_num}. Check the worktree."
    fi
}

restore_stash() {
    if [[ -z "$DIRTY_STASH_REF" ]]; then
        return 0
    fi
    log "Restoring temporarily stashed changes: ${DIRTY_STASH_REF}"
    if git -C "$REPO_DIR" stash show -p "$DIRTY_STASH_REF" | git -C "$REPO_DIR" apply --check --index >/dev/null 2>&1; then
        if git -C "$REPO_DIR" stash apply --index "$DIRTY_STASH_REF" >/dev/null; then
            git -C "$REPO_DIR" stash drop "$DIRTY_STASH_REF" >/dev/null || log "WARN: Failed to drop stash: ${DIRTY_STASH_REF}"
            log "Stash restored."
        else
            log "WARN: Failed to apply stash. Please inspect it manually: ${DIRTY_STASH_REF}"
        fi
    else
        log "WARN: Kept stash because conflicts are likely: ${DIRTY_STASH_REF}"
    fi
    DIRTY_STASH_REF=""
}

ensure_clean_tracked() {
    if [[ "$ALLOW_DIRTY" == "true" ]]; then
        return
    fi
    if git -C "$REPO_DIR" diff --quiet && git -C "$REPO_DIR" diff --staged --quiet; then
        if [[ "$AUTO_STASH_DONE" == "false" ]]; then
            AUTO_STASH_DONE=true
        fi
        return
    fi
    if [[ "$AUTO_STASH_DIRTY" == "true" && "$AUTO_STASH_DONE" == "false" ]]; then
        stash_dirty_worktree
        AUTO_STASH_DONE=true
        return
    fi
    error_exit "The worktree has uncommitted changes. You can continue with ALLOW_DIRTY=true."
}

checkout_target_branch() {
    local current_branch
    current_branch=$(git -C "$REPO_DIR" rev-parse --abbrev-ref HEAD)
    if [[ "$current_branch" == "$TARGET_BRANCH" ]]; then
        return
    fi
    log "Switching to target branch: ${TARGET_BRANCH}"
    if git -C "$REPO_DIR" show-ref --verify --quiet "refs/heads/${TARGET_BRANCH}"; then
        git -C "$REPO_DIR" checkout "$TARGET_BRANCH"
        return
    fi
    if git -C "$REPO_DIR" show-ref --verify --quiet "refs/remotes/origin/${TARGET_BRANCH}"; then
        git -C "$REPO_DIR" checkout -b "$TARGET_BRANCH" "origin/${TARGET_BRANCH}"
        return
    fi
    error_exit "Target branch not found: ${TARGET_BRANCH}"
}

cleanup_prompt() {
    if [[ -n "${PROMPT_FILE:-}" && -f "$PROMPT_FILE" ]]; then
        rm -f "$PROMPT_FILE"
    fi
    PROMPT_FILE=""
}

cleanup_all() {
    cleanup_prompt
    restore_stash
}

trap cleanup_all EXIT INT TERM

# Initialization.
mkdir -p "$LOG_DIR"
log "=== Issue auto-resolution script started ==="

require_cmd git
require_cmd gh
require_cmd jq

if [[ ! -d "$REPO_DIR/.git" ]]; then
    error_exit "REPO_DIR is not a Git repository: $REPO_DIR"
fi

if [[ "$DRY_RUN" == false ]]; then
    AI_CMD_BIN=$(printf '%s\n' "$AI_CMD" | awk '{print $1}')
    if [[ -z "$AI_CMD_BIN" ]]; then
        error_exit "AI_CMD is empty. Please configure it in .env."
    fi
    require_cmd "$AI_CMD_BIN"
fi

# Fetch the latest code.
log "Updating repository..."
if [[ "$DRY_RUN" == false ]]; then
    ensure_clean_tracked
    checkout_target_branch
    git -C "$REPO_DIR" pull origin "$TARGET_BRANCH" 2>&1 | tee -a "$LOG_FILE" || log "WARN: git pull failed (continuing)."
fi

# Fetch open Issues.
log "Fetching open Issues..."
ISSUES=$(gh issue list --repo "$REPO" --state open --json number,title,body --limit "$ISSUE_LIMIT" 2>>"$LOG_FILE") || error_exit "Failed to fetch Issues."

ISSUE_COUNT=$(echo "$ISSUES" | jq 'length')
log "Open Issue count: $ISSUE_COUNT"

if [[ "$ISSUE_COUNT" -eq 0 ]]; then
    log "There are no Issues to process. Exiting."
    exit 0
fi

# Process each Issue.
echo "$ISSUES" | jq -c '.[]' | while read -r issue; do
    ISSUE_NUM=$(echo "$issue" | jq -r '.number')
    ISSUE_TITLE=$(echo "$issue" | jq -r '.title')
    ISSUE_BODY=$(echo "$issue" | jq -r '.body // ""')
    
    log "--- Processing Issue #${ISSUE_NUM}: ${ISSUE_TITLE} ---"

    if [[ "$DRY_RUN" == false ]]; then
        ensure_clean_tracked
    fi

    UNTRACKED_BEFORE=""
    if [[ "$DRY_RUN" == false ]]; then
        UNTRACKED_BEFORE=$(git -C "$REPO_DIR" ls-files --others --exclude-standard)
    fi
    
    # Build the prompt for the AI tool.
    PROMPT="You are a developer working on the mind-upload project. Please resolve the GitHub Issue below.

## Issue #${ISSUE_NUM}: ${ISSUE_TITLE}

${ISSUE_BODY}

---

Inspect the repository structure and modify the appropriate files.
After the fix is complete, report a summary of the changes and the verification steps you ran.
Do not write execution-environment details to GitHub, including OS information, usernames, absolute paths, or secrets."

    if [[ "$DRY_RUN" == true ]]; then
        log "[DRY-RUN] Generated prompt for Issue #${ISSUE_NUM}"
        log "[DRY-RUN] Prompt length: ${#PROMPT}"
        continue
    fi
    
    # Save the prompt to a temporary file and delete it after execution.
    PROMPT_FILE=$(mktemp "${TMPDIR:-/tmp}/mind_upload_prompt_${ISSUE_NUM}_XXXXXX.txt")
    printf '%s' "$PROMPT" > "$PROMPT_FILE"
    
    log "Resolving Issue #${ISSUE_NUM}..."
    if ! run_ai < "$PROMPT_FILE" >>"$LOG_FILE" 2>&1; then
        log "ERROR: Failed to resolve Issue #${ISSUE_NUM}"
        stash_failed_issue "$ISSUE_NUM"
        rm -f "$PROMPT_FILE"
        PROMPT_FILE=""
        continue
    fi
    rm -f "$PROMPT_FILE"
    PROMPT_FILE=""
    
    log "AI processing complete"
    
    # Detect whether any changes were made.
    if git -C "$REPO_DIR" diff --quiet && git -C "$REPO_DIR" diff --staged --quiet; then
        log "Issue #${ISSUE_NUM}: no file changes were made"
        continue
    fi
    
    # Commit the changes.
    log "Committing changes..."
    git -C "$REPO_DIR" add -A
    if [[ -n "$UNTRACKED_BEFORE" ]]; then
        while IFS= read -r path; do
            [[ -z "$path" ]] && continue
            git -C "$REPO_DIR" reset -q -- "$path"
        done <<< "$UNTRACKED_BEFORE"
    fi
    STAGED_FILES=$(git -C "$REPO_DIR" diff --cached --name-only)
    STAGED_NUMSTAT=$(git -C "$REPO_DIR" diff --cached --numstat)
    if [[ -z "$STAGED_FILES" ]]; then
        log "Issue #${ISSUE_NUM}: there were no staged changes to commit"
        git -C "$REPO_DIR" reset -q
        continue
    fi
    COMMIT_MSG="Fixes #${ISSUE_NUM}: ${ISSUE_TITLE}

Automated fix
"
    if [[ -n "$CO_AUTHOR" ]]; then
        COMMIT_MSG="${COMMIT_MSG}"$'\n\n'"Co-authored-by: ${CO_AUTHOR}"
    fi
    git -C "$REPO_DIR" commit -m "$COMMIT_MSG"
    COMMIT_SHA=$(git -C "$REPO_DIR" rev-parse --short HEAD)
    
    # Push the changes.
    log "Pushing changes..."
    git -C "$REPO_DIR" push origin "$TARGET_BRANCH"
    
    # Close the Issue.
    log "Closing Issue #${ISSUE_NUM}..."
    CLOSE_COMMENT_FILE=$(mktemp "${TMPDIR:-/tmp}/issue_close_${ISSUE_NUM}_XXXXXX.md")
    build_issue_resolution_comment "$ISSUE_NUM" "$ISSUE_TITLE" "$COMMIT_SHA" "$STAGED_FILES" "$STAGED_NUMSTAT" "$CLOSE_COMMENT_FILE"
    if gh issue comment "$ISSUE_NUM" --repo "$REPO" --body-file "$CLOSE_COMMENT_FILE" >>"$LOG_FILE" 2>&1; then
        gh issue close "$ISSUE_NUM" --repo "$REPO" >>"$LOG_FILE" 2>&1 || log "WARN: Failed to close the Issue"
    else
        log "ERROR: Failed to post the resolution comment for Issue #${ISSUE_NUM}, so closing was skipped"
    fi
    rm -f "$CLOSE_COMMENT_FILE"
    
    log "Issue #${ISSUE_NUM} processing completed"
done

log "=== Issue auto-resolution script finished ==="
