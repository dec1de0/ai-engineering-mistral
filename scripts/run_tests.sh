#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [[ -z "${DEPLOYED_API_URL:-}" && -z "${API_BASE_URL:-}" ]]; then
  echo "DEPLOYED_API_URL is not set. Deploy your backend and export the URL." >&2
  echo "Example: export DEPLOYED_API_URL=https://your-host" >&2
  exit 1
fi

pytest -q
