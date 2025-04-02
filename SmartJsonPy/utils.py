import json
from typing import Any, List

def remove_duplicate_dicts(lst: List[dict]) -> List[dict]:
    """Remove dicionários duplicados de uma lista."""
    seen = set()
    result = []
    for d in lst:
        t = tuple(sorted(d.items()))
        if t not in seen:
            seen.add(t)
            result.append(d)
    return result

def remove_duplicate_items(lst: List[Any]) -> List[Any]:
    """Remove itens duplicados de uma lista comum, mantendo a ordem."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def json_to_string(obj: Any, indent: int = 2) -> str:
    """Converte um objeto JSON (dict/list) para string formatada."""
    return json.dumps(obj, ensure_ascii=False, indent=indent)

def string_to_json(text: str) -> Any:
    """Converte uma string JSON em dict ou list."""
    return json.loads(text)

def convert_list_of_dicts_to_columns(data: List[dict]) -> tuple:
    """Converte uma lista de dicionários em colunas para geração de planilha."""
    if not data:
        return ()

    headers = tuple(data[0].keys())
    columns = tuple(tuple(d.get(key) for d in data) for key in headers)
    return (headers,) + columns
