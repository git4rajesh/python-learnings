import ast


def foo(i):
    print('>>>>', i)


def parse_stmt():
    a = ast.parse('foo(1 + 1)')

    # b = compile('foo(1 + 1)', '<unknown>', 'exec', ast.PyCF_ONLY_AST)
    code = ast.dump(a, annotate_fields=False)
    eval(code)


parse_stmt()
