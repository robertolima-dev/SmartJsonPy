"""
Módulo para transformação de dados JSON em diferentes formatos.
"""
import json
import yaml
import xmltodict
import pandas as pd
from typing import Any, Dict, List, Union

def json_to_yaml(json_data: Union[str, Dict, List]) -> str:
    """
    Converte dados JSON para formato YAML.
    
    Args:
        json_data: Dados JSON em formato string, dicionário ou lista
        
    Returns:
        str: Dados em formato YAML
        
    Raises:
        ValueError: Se os dados JSON forem inválidos
    """
    if isinstance(json_data, str):
        try:
            json_data = json.loads(json_data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Dados JSON inválidos: {str(e)}")
    
    return yaml.dump(json_data, allow_unicode=True, sort_keys=False)

def json_to_xml(json_data: Union[str, Dict, List], root_name: str = "root") -> str:
    """
    Converte dados JSON para formato XML.
    
    Args:
        json_data: Dados JSON em formato string, dicionário ou lista
        root_name: Nome do elemento raiz do XML
        
    Returns:
        str: Dados em formato XML
        
    Raises:
        ValueError: Se os dados JSON forem inválidos
    """
    if isinstance(json_data, str):
        try:
            json_data = json.loads(json_data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Dados JSON inválidos: {str(e)}")
    
    def _convert_to_xml(data: Any) -> Any:
        if isinstance(data, list):
            return {"item": data}
        elif isinstance(data, dict):
            return {k: _convert_to_xml(v) for k, v in data.items()}
        return data
    
    converted_data = _convert_to_xml(json_data)
    return xmltodict.unparse({root_name: converted_data}, pretty=True)

def json_to_csv(json_data: Union[str, Dict, List], output_file: str = None) -> Union[str, None]:
    """
    Converte dados JSON para formato CSV.
    
    Args:
        json_data: Dados JSON em formato string, dicionário ou lista
        output_file: Caminho do arquivo de saída (opcional)
        
    Returns:
        str: Dados em formato CSV se output_file não for especificado
        None: Se output_file for especificado
        
    Raises:
        ValueError: Se os dados JSON forem inválidos ou não forem uma lista de dicionários
    """
    if isinstance(json_data, str):
        try:
            json_data = json.loads(json_data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Dados JSON inválidos: {str(e)}")
    
    if not isinstance(json_data, list):
        raise ValueError("Os dados JSON devem ser uma lista de dicionários")
    
    if not all(isinstance(item, dict) for item in json_data):
        raise ValueError("Todos os itens da lista devem ser dicionários")
    
    df = pd.DataFrame(json_data)
    
    if output_file:
        df.to_csv(output_file, index=False)
        return None
    
    return df.to_csv(index=False)

def flatten_json(json_data: Union[str, Dict, List], separator: str = ".") -> Dict:
    """
    Converte um JSON aninhado em um dicionário plano.
    
    Args:
        json_data: Dados JSON em formato string, dicionário ou lista
        separator: Separador para as chaves aninhadas
        
    Returns:
        Dict: Dicionário com chaves planas
        
    Raises:
        ValueError: Se os dados JSON forem inválidos
    """
    if isinstance(json_data, str):
        try:
            json_data = json.loads(json_data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Dados JSON inválidos: {str(e)}")
    
    def _flatten(d: Any, parent_key: str = "", sep: str = separator) -> Dict:
        items = []
        
        if isinstance(d, dict):
            for k, v in d.items():
                new_key = f"{parent_key}{sep}{k}" if parent_key else k
                items.extend(_flatten(v, new_key, sep=sep).items())
        elif isinstance(d, list):
            for i, v in enumerate(d):
                new_key = f"{parent_key}{sep}{i}" if parent_key else str(i)
                items.extend(_flatten(v, new_key, sep=sep).items())
        else:
            items.append((parent_key, d))
            
        return dict(items)
    
    return _flatten(json_data)

def unflatten_json(flat_dict: Dict, separator: str = ".") -> Dict:
    """
    Converte um dicionário plano em um JSON aninhado.
    
    Args:
        flat_dict: Dicionário com chaves planas
        separator: Separador usado nas chaves planas
        
    Returns:
        Dict: Dicionário aninhado
    """
    result = {}
    
    for key, value in flat_dict.items():
        parts = key.split(separator)
        current = result
        
        for i, part in enumerate(parts[:-1]):
            next_part = parts[i + 1]
            next_is_digit = next_part.isdigit()
            
            if part not in current:
                current[part] = [] if next_is_digit else {}
            current = current[part]
        
        last_part = parts[-1]
        if last_part.isdigit():
            last_part = int(last_part)
            if isinstance(current, list):
                while len(current) <= last_part:
                    current.append(None)
                current[last_part] = value
            else:
                current[last_part] = value
        else:
            current[last_part] = value
    
    return result 