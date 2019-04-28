1. In Python 3, bytes and str instances are never equivalent—not even the empty string. Refer ex1.py

2. Things to Remember
    ✦ In Python 3, bytes contains sequences of 8-bit values, str contains sequences of Unicode characters.
bytes and str instances can’t be used together with operators (like > or +).

    ✦ In Python 2, str contains sequences of 8-bit values, unicode contains sequences of Unicode characters. str and unicode can be used
    together with operators if the str only contains 7-bit ASCII characters.

    ✦ Use helper functions to ensure that the inputs you operate on are the type of character sequence you expect (8-bit values, UTF-8
    encoded characters, Unicode characters, etc.).

    ✦ If you want to read or write binary data to/from a file, always open the file using a binary mode (like 'rb' or 'wb').

