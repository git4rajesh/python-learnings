from functools import partial

# def partial(func, *part_args):
#     def wrapper(*extra_args):
#         args = list(part_args)
#         args.extend(extra_args)
#         return func(*args)
#
#     return wrapper


# So, by calling partial(sum2, 4) you create a new function
# (a callable, to be precise) that behaves like sum2, but has one positional argument less.
# That missing argument is always substituted by 4, so that partial(sum2, 4)(2) == sum2(4, 2)

def sum2(num1, num2):
    return num1 + num2

method_add_4 = partial(sum2, num2=4)
output = method_add_4(5)

print('The sum is : %s' % str(output))


# ReadMe1:
# 1. Partial function application is a fancy sounding name for a simple concept:
#                      pre-filling a couple of arguments before they're called in a function

# 2. They don't convey why you'd want to do it or where it can be applied.
#   And until you wrap your head around functions as a composition tool


def create_url(*args, **kwargs):
    complete_create_url = 'base_url/account/projects'
    return complete_create_url


