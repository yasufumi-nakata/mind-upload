#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd -- "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

REPO="${REPO:-yasufumi-nakata/mind-upload}" \
REPO_DIR="${REPO_DIR:-$ROOT_DIR}" \
bash "$ROOT_DIR/automation/resolve-issues.sh" "$@"
