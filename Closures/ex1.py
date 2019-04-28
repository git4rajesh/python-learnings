def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested inner function
        print(msg)

    printer()  # this is called now


# We execute the function
# Output: Hello
print_msg("Hello")
