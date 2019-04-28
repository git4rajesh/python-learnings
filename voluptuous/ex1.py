from voluptuous import Schema, Required


s = Schema({
    'q': str,
    'per_page': int,
    'page': int,
 })

s({"q": "hello"})