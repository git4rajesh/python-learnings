import ast

def extract_return(file):
    for node in ast.walk(ast.parse(open(file).read())):
        if (isinstance(node, ast.FunctionDef)):
            print('Method name', node.name)
            print('Doc string:', ast.get_docstring(node))


extract_return('data2.py')

