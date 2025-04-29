# 📦 SmartJsonPy

**SmartJsonPy** é um pacote Python leve e poderoso para manipulação de JSON. Ele oferece funções para validação, limpeza, extração, deduplicamento e conversão de dados JSON. Ideal para preparação de dados, integrações com APIs e exportação para planilhas.


---

## 🧪 Testes
Execute os testes com `pytest`:
```bash
pytest tests/
```

---

## 🚀 Instalação
```bash
pip install SmartJsonPy
```

> Requer: Python >= 3.7

---

## ✨ Funcionalidades

### ✅ Validação de JSON
```python
from SmartJsonPy import validator

validator.is_valid_json_string('{"nome": "João"}')  # True
validator.is_valid_json_object({"id": 1})              # True
validator.has_required_keys({"id": 1}, ["id"])        # True
validator.is_json_schema_compatible({"id": 1}, {"id": int})  # True
```

### 🧹 Limpeza de dados
```python
from SmartJsonPy import cleaner

data = {"a": 1, "b": None, "c": "", "d": []}
cleaner.remove_none_values(data)       # {"a": 1, "c": "", "d": []}
cleaner.remove_empty_values(data)      # {"a": 1}
cleaner.strip_whitespace_keys({" nome ": "Ana"})  # {"nome": "Ana"}

nested = {"x": {"y": {"z": None}}, "a": ["ok", {}]}
cleaner.clean_nested_dict(nested)  # {"a": ["ok"]}
```

### 🔍 Extração de dados
```python
from SmartJsonPy import extractor

data = {"a": 1, "b": {"a": 2}, "c": [{"a": 3}, {"x": 9}]}
extractor.extract_keys(data)           # ['a', 'b', 'c', 'x']
extractor.extract_values_by_key(data, "a")  # [1, 2, 3]
```

### 🔁 Deduplicar dados
```python
from SmartJsonPy import utils

# Dicionários duplicados
lst = [{"a": 1}, {"a": 1}, {"b": 2}]
utils.remove_duplicate_dicts(lst)  # [{"a": 1}, {"b": 2}]

# Itens duplicados
nums = [1, 2, 2, 3, 1]
utils.remove_duplicate_items(nums)  # [1, 2, 3]
```

### 🔄 Conversões entre string e JSON
```python
from SmartJsonPy import utils

# JSON para string
d = {"nome": "João"}
utils.json_to_string(d)  # '{"nome": "João"}'

# String para JSON
s = '{"nome": "Maria"}'
utils.string_to_json(s)  # {'nome': 'Maria'}
```

### 🔄 Transformação de Dados
```python
from SmartJsonPy import transformer

# JSON para YAML
data = {"nome": "João", "idade": 30}
yaml_str = transformer.json_to_yaml(data)
# name: João
# age: 30

# JSON para XML
xml_str = transformer.json_to_xml(data, root_name="pessoa")
# <?xml version="1.0" encoding="utf-8"?>
# <pessoa>
#   <nome>João</nome>
#   <idade>30</idade>
# </pessoa>

# JSON para CSV
lista = [
    {"nome": "João", "idade": 30},
    {"nome": "Maria", "idade": 25}
]
csv_str = transformer.json_to_csv(lista)
# nome,idade
# João,30
# Maria,25

# Achatamento de JSON
nested = {"a": {"b": {"c": 1}}}
flat = transformer.flatten_json(nested)
# {"a.b.c": 1}

# Desachatamento de JSON
nested = transformer.unflatten_json({"a.b.c": 1})
# {"a": {"b": {"c": 1}}}
```

### 📊 Conversão para formato de colunas (planilhas)
```