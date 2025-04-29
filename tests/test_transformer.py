"""
Testes para o módulo transformer.py
"""
import pytest
from SmartJsonPy.transformer import (
    json_to_yaml,
    json_to_xml,
    json_to_csv,
    flatten_json,
    unflatten_json
)

# Dados de teste
SAMPLE_JSON = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York"
    },
    "hobbies": ["reading", "gaming"]
}

SAMPLE_JSON_STR = '{"name": "John", "age": 30, "address": {"street": "123 Main St", "city": "New York"}, "hobbies": ["reading", "gaming"]}'

SAMPLE_LIST_JSON = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25}
]

def test_json_to_yaml():
    """Testa a conversão de JSON para YAML"""
    yaml_str = json_to_yaml(SAMPLE_JSON)
    assert "name: John" in yaml_str
    assert "age: 30" in yaml_str
    assert "address:" in yaml_str
    assert "street: 123 Main St" in yaml_str
    assert "hobbies:" in yaml_str
    assert "- reading" in yaml_str
    assert "- gaming" in yaml_str

def test_json_to_yaml_with_string():
    """Testa a conversão de string JSON para YAML"""
    yaml_str = json_to_yaml(SAMPLE_JSON_STR)
    assert "name: John" in yaml_str
    assert "age: 30" in yaml_str

def test_json_to_yaml_invalid_json():
    """Testa a conversão com JSON inválido"""
    with pytest.raises(ValueError):
        json_to_yaml('{"invalid": json}')

def test_json_to_xml():
    """Testa a conversão de JSON para XML"""
    xml_str = json_to_xml(SAMPLE_JSON)
    assert "<root>" in xml_str
    assert "<name>John</name>" in xml_str
    assert "<age>30</age>" in xml_str
    assert "<address>" in xml_str
    assert "<street>123 Main St</street>" in xml_str
    assert "<hobbies>" in xml_str
    assert "<item>reading</item>" in xml_str
    assert "<item>gaming</item>" in xml_str

def test_json_to_xml_with_custom_root():
    """Testa a conversão de JSON para XML com raiz personalizada"""
    xml_str = json_to_xml(SAMPLE_JSON, root_name="person")
    assert "<person>" in xml_str
    assert "</person>" in xml_str

def test_json_to_xml_invalid_json():
    """Testa a conversão com JSON inválido"""
    with pytest.raises(ValueError):
        json_to_xml('{"invalid": json}')

def test_json_to_csv():
    """Testa a conversão de JSON para CSV"""
    csv_str = json_to_csv(SAMPLE_LIST_JSON)
    assert "name,age" in csv_str
    assert "John,30" in csv_str
    assert "Jane,25" in csv_str

def test_json_to_csv_invalid_json():
    """Testa a conversão com JSON inválido"""
    with pytest.raises(ValueError):
        json_to_csv('{"invalid": json}')

def test_json_to_csv_not_list():
    """Testa a conversão com JSON que não é uma lista"""
    with pytest.raises(ValueError):
        json_to_csv(SAMPLE_JSON)

def test_json_to_csv_not_dict_items():
    """Testa a conversão com lista que não contém apenas dicionários"""
    with pytest.raises(ValueError):
        json_to_csv([{"name": "John"}, "not a dict"])

def test_flatten_json():
    """Testa o achatamento de JSON"""
    flat_dict = flatten_json(SAMPLE_JSON)
    assert flat_dict["name"] == "John"
    assert flat_dict["age"] == 30
    assert flat_dict["address.street"] == "123 Main St"
    assert flat_dict["address.city"] == "New York"
    assert flat_dict["hobbies.0"] == "reading"
    assert flat_dict["hobbies.1"] == "gaming"

def test_flatten_json_with_custom_separator():
    """Testa o achatamento de JSON com separador personalizado"""
    flat_dict = flatten_json(SAMPLE_JSON, separator="_")
    assert flat_dict["address_street"] == "123 Main St"
    assert flat_dict["address_city"] == "New York"

def test_flatten_json_invalid_json():
    """Testa o achatamento com JSON inválido"""
    with pytest.raises(ValueError):
        flatten_json('{"invalid": json}')

def test_unflatten_json():
    """Testa o desachatamento de JSON"""
    flat_dict = {
        "name": "John",
        "age": 30,
        "address.street": "123 Main St",
        "address.city": "New York",
        "hobbies.0": "reading",
        "hobbies.1": "gaming"
    }
    nested_dict = unflatten_json(flat_dict)
    assert nested_dict["name"] == "John"
    assert nested_dict["age"] == 30
    assert nested_dict["address"]["street"] == "123 Main St"
    assert nested_dict["address"]["city"] == "New York"
    assert nested_dict["hobbies"][0] == "reading"
    assert nested_dict["hobbies"][1] == "gaming"

def test_unflatten_json_with_custom_separator():
    """Testa o desachatamento de JSON com separador personalizado"""
    flat_dict = {
        "name": "John",
        "address_street": "123 Main St",
        "address_city": "New York"
    }
    nested_dict = unflatten_json(flat_dict, separator="_")
    assert nested_dict["name"] == "John"
    assert nested_dict["address"]["street"] == "123 Main St"
    assert nested_dict["address"]["city"] == "New York" 