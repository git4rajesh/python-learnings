def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # this got changed


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()



# The print_msg() function was called with the string "Hello" and the returned function was bound to the name another.
# On calling another(), the message was still remembered although we had already finished executing the print_msg() function.
# This technique by which some data ("Hello") gets attached to the code is called closure in Python.
