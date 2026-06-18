#!/usr/bin/env bash
# Builda o wheel e instala numa venv limpa (sem deps de dev) para pegar
# dependências/entry points que só faltam fora do ambiente de desenvolvimento.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

rm -rf dist build
rm -rf ./*.egg-info 2>/dev/null || true
python -m build

VENV_DIR="$(mktemp -d)/venv"
python -m venv "$VENV_DIR"
"$VENV_DIR/bin/pip" install -q "$(ls dist/*.whl)"

"$VENV_DIR/bin/python" -c "
from SmartJsonPy.validator import is_valid_json_string
assert is_valid_json_string('{\"a\": 1}') is True
assert is_valid_json_string('not json') is False
print('IMPORT OK')
"

rm -rf "$(dirname "$VENV_DIR")"
echo "Smoke test passou."
