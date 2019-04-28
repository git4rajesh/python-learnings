def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str

    return value  # Instance of str


input_str1 = 'Test1'

print(type(input_str1), to_str(input_str1))

input_bytes = b'Test1'


print(type(input_bytes), to_str(input_bytes))
