import ast


ast_tree = ast.parse(open('artifacts/test_scenarios.py').read())
print(ast_tree.body)

for units in ast.walk(ast_tree):
    if isinstance(units, ast.Call):
        # print(units.__dict__)
        # print(units.func)
        unit1 = units.func

        if isinstance(unit1, ast.Attribute):
            unit2 = unit1.value.func
            if isinstance(unit2, ast.Attribute):
                print('{0},{1}'.format(unit2.attr, unit1.attr))

            elif isinstance(unit2, ast.Name):
                print('{0},{1}'.format(unit2.id, unit1.attr))
        # print(units.func.attr)
        # print(units.func)
        # for item in units.body:
        # print(item)
        # print(ast.dump(units.func))
