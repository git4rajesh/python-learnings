from behave.runner import Context


def before_all(context):
    context.mylist = [1, 2, 3]
    context.mydict = {'a': 1}