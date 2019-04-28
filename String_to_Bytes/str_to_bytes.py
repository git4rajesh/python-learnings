def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes


input_str1 = 'Test1'

print(type(input_str1), to_bytes(input_str1))

input_bytes = b'Test1'


print(type(input_bytes), to_bytes(input_bytes))
