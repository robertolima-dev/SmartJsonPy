from SmartJsonPy import extractor

def test_extract_keys():
    data = {
        "a": 1,
        "b": {"c": 2, "d": {"e": 3}},
        "f": [
            {"g": 4},
            {"h": 5}
        ]
    }
    keys = extractor.extract_keys(data)
    for k in ["a", "b", "c", "d", "e", "f", "g", "h"]:
        assert k in keys
    assert len(keys) == 8

def test_extract_values_by_key():
    data = {
        "a": 1,
        "b": {"a": 2, "d": {"a": 3}},
        "e": [
            {"a": 4},
            {"f": 5}
        ]
    }
    values = extractor.extract_values_by_key(data, "a")
    assert sorted(values) == [1, 2, 3, 4]
