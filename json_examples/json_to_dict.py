import json

# Both are Str type but we can apply json.loads() to only a json with single quote outside and
# keys having double quotes

# json should have a single quote outside and then each keys should be doubly-quoted.
json_with_single_quotes =  '{ "name":"John", "age":30, "city":"New York"}'
print(type(json_with_single_quotes))

# This is a wrong representation of json and gives the below error: json.decoder.JSONDecodeError
json_with_double_quotes = "{'name': 'John', 'age':30, 'city':'New York'}"
print(type(json_with_double_quotes))



# parse json_with_single_quotes:
y = json.loads(json_with_single_quotes)
z= json.loads(json_with_double_quotes)

print('The JSON type when loaded gives a {}'.format(type(y)))

# the result is a Python dictionary:
print(y["age"])
print(repr(y))

print(z['age'])