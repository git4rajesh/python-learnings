import ast
import os
import sys


def load_test_cases(artifact):
    base_path = os.path.join(os.path.dirname(__file__), 'artifacts')
    units_lst = []
    fullpath = os.path.join(base_path, artifact)
    data = open(fullpath).read()
    tree = ast.parse(data, fullpath)
    return tree


def filter_tree(tree):
    for index, node in enumerate(tree.body[:]):
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            function_defs_lst = node.body
            atoms_lst = filter_functions(function_defs_lst)
            return class_name.lower(), atoms_lst


def filter_functions(function_defs):
    # valid_nodes = filter(lambda node: node.name[0] != '_', function_defs)
    valid_node_names_lst = []
    for node in function_defs:
        if node.name[0] != '_':
            valid_node_names_lst.append(node.name)
    return valid_node_names_lst


if __name__ == "__main__":
    artifact_files = sys.argv[1:]
    # artifact_files = ['task', 'timesheet']
    print('strict digraph tree {')
    for artifact_name in artifact_files:
        artifact_file_name = ''.join([artifact_name, '.py'])
        tree = load_test_cases(artifact_file_name)
        artifact, atoms = filter_tree(tree)
        # print(artifact, atoms)
        for atom in atoms:
            print('    {0} -> {1};'.format(artifact, atom))

    print('}')
