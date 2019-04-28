def swap_case(s):
    new_str = list (map(convert_case, s))
    new_str = ''.join(new_str)
    return new_str

def convert_case(c):
    if c.isupper():
        return c.lower()
    else:
        return c.upper()