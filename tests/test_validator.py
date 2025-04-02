import pytest
from SmartJsonPy import validator

def test_is_valid_json_string():
    assert validator.is_valid_json_string('{"nome": "João"}') is True
    assert validator.is_valid_json_string("{nome: 'João'}") is False
    assert validator.is_valid_json_string(12345) is False

def test_is_valid_json_object():
    assert validator.is_valid_json_object({"id": 1, "ativo": True}) is True
    assert validator.is_valid_json_object(set([1, 2, 3])) is False

def test_has_required_keys():
    d = {"id": 1, "nome": "Maria"}
    assert validator.has_required_keys(d, ["id", "nome"]) is True
    assert validator.has_required_keys(d, ["id", "email"]) is False
    assert validator.has_required_keys("string", ["id"]) is False

def test_is_json_schema_compatible():
    schema = {"id": int, "nome": str}
    valid_obj = {"id": 10, "nome": "Pedro"}
    invalid_obj = {"id": "dez", "nome": "Pedro"}
    assert validator.is_json_schema_compatible(valid_obj, schema) is True
    assert validator.is_json_schema_compatible(invalid_obj, schema) is False
    assert validator.is_json_schema_compatible("string", schema) is False
