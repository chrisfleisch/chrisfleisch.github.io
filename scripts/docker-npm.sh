#!/usr/bin/env bash
set -euo pipefail

service="${1:?Usage: scripts/docker-npm.sh <tools|fe> <npm-args...>}"
shift

publish_flag=""
if [[ "${1:-}" == "run" && "${2:-}" == "dev" ]]; then
  publish_flag="--service-ports"
fi

exec docker compose run --rm $publish_flag "$service" npm "$@"
