from typing import Any, List, Union

def extract_keys(data: Union[dict, list]) -> List[str]:
    """Extrai todas as chaves (únicas) de um JSON, incluindo estruturas aninhadas."""
    keys = set()

    if isinstance(data, dict):
        for k, v in data.items():
            keys.add(k)
            keys.update(extract_keys(v))
    elif isinstance(data, list):
        for item in data:
            keys.update(extract_keys(item))

    return list(keys)

def extract_values_by_key(data: Union[dict, list], key: str) -> List[Any]:
    """Extrai todos os valores associados a uma chave específica, mesmo aninhada."""
    values = []

    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                values.append(v)
            values.extend(extract_values_by_key(v, key))
    elif isinstance(data, list):
        for item in data:
            values.extend(extract_values_by_key(item, key))

    return values
