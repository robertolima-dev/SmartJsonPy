import json
from typing import Any

def is_valid_json_string(json_str: str) -> bool:
    """Verifica se uma string é um JSON válido."""
    try:
        json.loads(json_str)
        return True
    except (json.JSONDecodeError, TypeError):
        return False

def is_valid_json_object(obj: Any) -> bool:
    """Verifica se o objeto pode ser convertido em JSON."""
    try:
        json.dumps(obj)
        return True
    except (TypeError, OverflowError):
        return False

def has_required_keys(obj: dict, required_keys: list[str]) -> bool:
    """Verifica se todas as chaves obrigatórias estão presentes no dicionário."""
    if not isinstance(obj, dict):
        return False
    return all(key in obj for key in required_keys)

def is_json_schema_compatible(obj: dict, schema: dict) -> bool:
    """
    Verifica se o objeto segue uma estrutura básica de schema (chaves e tipos).
    Exemplo de schema: {"id": int, "nome": str}
    """
    if not isinstance(obj, dict):
        return False

    for key, expected_type in schema.items():
        if key not in obj or not isinstance(obj[key], expected_type):
            return False
    return True
