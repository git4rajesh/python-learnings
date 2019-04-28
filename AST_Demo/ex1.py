import ast
import inspect

field_type = 'Brand-X'
Version = [1,2,3]
v = ast.parse("if field_type =='Brand-X': Version = 2")
for item in v.body:
    print(ast.dump(item))


# def foo():
#     p = 2
#     p += 2
#     return p
#
#
# meth_var = ast.parse(inspect.getsource(foo))
# print(ast.dump(meth_var))
