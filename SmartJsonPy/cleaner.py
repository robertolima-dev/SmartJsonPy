from typing import Any, Dict

def remove_none_values(data: dict) -> dict:
    """Remove chaves com valores None de um dicionário."""
    return {k: v for k, v in data.items() if v is not None}

def remove_empty_values(data: dict) -> dict:
    """Remove chaves com valores vazios (None, '', [], {}, etc.)."""
    return {k: v for k, v in data.items() if v not in [None, '', [], {}, ()]}

def clean_nested_dict(data: dict) -> dict:
    """Limpa recursivamente um dicionário aninhado, removendo valores vazios."""
    cleaned = {}
    for k, v in data.items():
        if isinstance(v, dict):
            nested = clean_nested_dict(v)
            if nested:
                cleaned[k] = nested
        elif isinstance(v, list):
            cleaned_list = [clean_nested_dict(i) if isinstance(i, dict) else i for i in v]
            cleaned_list = [i for i in cleaned_list if i not in [None, '', [], {}, ()]]
            if cleaned_list:
                cleaned[k] = cleaned_list
        elif v not in [None, '', [], {}, ()]:
            cleaned[k] = v
    return cleaned

def strip_whitespace_keys(data: dict) -> dict:
    """Remove espaços em branco das chaves do dicionário."""
    return {k.strip(): v for k, v in data.items() if isinstance(k, str)}
