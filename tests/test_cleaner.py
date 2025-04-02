from SmartJsonPy import cleaner

def test_remove_none_values():
    data = {"a": 1, "b": None, "c": 3}
    assert cleaner.remove_none_values(data) == {"a": 1, "c": 3}

def test_remove_empty_values():
    data = {"a": 0, "b": "", "c": [], "d": {}, "e": None, "f": "ok"}
    assert cleaner.remove_empty_values(data) == {"a": 0, "f": "ok"}

def test_clean_nested_dict():
    data = {
        "a": 1,
        "b": None,
        "c": {
            "x": "",
            "y": {"z": None, "w": 2},
            "k": []
        },
        "d": [
            {"m": None},
            {"n": "valid"},
            "text",
            {}
        ]
    }
    expected = {
        "a": 1,
        "c": {"y": {"w": 2}},
        "d": [{"n": "valid"}, "text"]
    }
    assert cleaner.clean_nested_dict(data) == expected

def test_strip_whitespace_keys():
    data = {"  nome ": "Ana", " idade": 30, "email ": "ana@email.com"}
    assert cleaner.strip_whitespace_keys(data) == {"nome": "Ana", "idade": 30, "email": "ana@email.com"}
