import ast


class Py2Neko(ast.NodeVisitor):
    def generic_visit(self, node):
        print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Name(self, node):
        print('Name :', node.id)

    def visit_Num(self, node):
        print('Num :', node.__dict__['n'])

    def visit_Str(self, node):
        print("Str :", node.s)


if __name__ == '__main__':
    node = ast.parse("if a ==1: version < 3")

    # print(ast.dump(node))

    v = Py2Neko()
    v.visit(node)
