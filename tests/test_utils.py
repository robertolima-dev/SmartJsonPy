from SmartJsonPy import utils
import json

def test_remove_duplicate_dicts():
    lst = [{"a": 1}, {"a": 1}, {"b": 2}]
    result = utils.remove_duplicate_dicts(lst)
    assert result == [{"a": 1}, {"b": 2}]

def test_remove_duplicate_items():
    lst = [1, 2, 2, 3, 1, 4]
    result = utils.remove_duplicate_items(lst)
    assert result == [1, 2, 3, 4]

def test_json_to_string():
    obj = {"nome": "João", "idade": 30}
    json_str = utils.json_to_string(obj, indent=0)
    assert json.loads(json_str) == obj

def test_string_to_json():
    json_str = '{"cidade": "São Paulo", "populacao": 12345678}'
    obj = utils.string_to_json(json_str)
    assert obj == {"cidade": "São Paulo", "populacao": 12345678}

def test_convert_list_of_dicts_to_columns():
    data = [
        {"name": "Roberto", "age": 45, "gender": "m"},
        {"name": "Joao", "age": 32, "gender": "m"},
        {"name": "Renata", "age": 39, "gender": "f"}
    ]
    expected = (
        ("name", "age", "gender"),
        ("Roberto", "Joao", "Renata"),
        (45, 32, 39),
        ("m", "m", "f")
    )
    assert utils.convert_list_of_dicts_to_columns(data) == expected
