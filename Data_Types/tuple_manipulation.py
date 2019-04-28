# Sample code to append a tuple.
# The point here is: List is a mutable sequence type. So you can change a given list by adding or removing elements.
# Tuple is an immutable sequence type. You can't change a tuple. So you have to create a new one.
# Tuple can only allow adding tuple to it. The best way to do it is:


t1 = (1,)
t1 += (2,)

print(t1)


# Since Python 3.5 (PEP 448) you can do unpacking within a tuple, list set, and dict:

# a = ('2',1)
# b = 'z'
# new = (*a, b)
#
# print(new)

#
# # Another example to unpack a list
#
# a = ['1', '2', '3', '4']
# b = ['5', '6']
# #function_that_needs_strings(*a, *b)