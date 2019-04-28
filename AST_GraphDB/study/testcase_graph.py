import ast
import os
from pathlib import Path
import shutil
from pandas import DataFrame
from py2neo import Graph
#
# DIRECTORY = 'autobots/tests/scenario'
# ENTITIES = ['asset', 'dataimport', 'issue', 'portfolio', 'project', 'resource', 'rollups',
#             'schedule', 'task',
#             'timeadmin', 'timesheet', 'user','data_import']

DIRECTORY = 'jedi/fluent_ml/tests'
ENTITIES = ['project', 'card', 'verifyproject', 'verifycard',
   'prm', 'leankit', 'goto_prm', 'goto_lk', 'run_integration', 'goto_prm_to_verify_project']


def load_test_cases(artifact_path):
    artifact_file_name = os.path.basename(str(artifact_path))
    base_path = os.path.join(os.path.dirname(__file__), str(artifact_path))
    # fullpath = os.path.join(base_path, artifact_file_name)
    data = open(base_path).read()
    tree = ast.parse(data, base_path)
    return tree


def filter_tree(tree, artifact_files, file_path, atom_atom_relation_df, atom_entity_relation_df,
                entity_atom_relation_df, entity_entity_relation_df):

    unit_body = tree.body
    # Fetching all the testcases inside a Test Module
    unit_function_def_lst = filter(lambda unit: isinstance(unit, ast.FunctionDef), unit_body)
    i = 0

    for unit_function_def in unit_function_def_lst:
        # Each Function_def is a testcase
        testcase_name = unit_function_def.name
        # TODO : ZID can be num obj also
        zid = get_zid(unit_function_def)
        zid = zid + ' : ' + file_path + '/' + testcase_name

        # All units in function definition body is expression objects.
        # So, filter only those expression objects whos value has a Call object
        # This will remove such expression objects like docstring
        unit_expression_lst = filter(lambda unit: isinstance(unit.value, ast.Call),
                                     unit_function_def.body)

        # Traversing thru the function calls inside a testcase
        for unit in unit_expression_lst:
            atoms = ast.walk(unit)
            atoms = reversed(list(atoms))
            classname = None
            for atom in atoms:
                is_include = False
                node1 = None
                node2 = None
                if isinstance(atom, ast.Attribute):
                    if not hasattr(atom.value, 'func'):
                        continue
                    prev_atom = atom.value.func
                    if isinstance(prev_atom, ast.Attribute):
                        node1 = prev_atom.attr
                        node2 = atom.attr
                        if node1.lower() in ENTITIES:
                            classname = node1
                            node1_call = '{0}()'.format(node1)
                        else:
                            node1_call = '{0}({1})'.format(node1, classname)
                        if node2.lower() in ENTITIES:
                            classname = node2
                            node2_call = '{0}()'.format(node2)
                        else:
                            node2_call = '{0}({1})'.format(node2, classname)

                        new_node_dct = {'node1': node1_call, 'node2': node2_call, 'zids': [zid]}
                        node_dct = get_node_dct(node1_call, node2_call, atom_atom_relation_df,
                                                atom_entity_relation_df, entity_atom_relation_df,
                                                entity_entity_relation_df)
                        if node_dct:
                            if node_dct['zids']:
                                a = set(node_dct['zids'])
                                a.add(zid)
                                node_dct['zids'] = list(a)
                            else:
                                node_dct.update(new_node_dct)

                            node_dct['weight'] = len(node_dct['zids'])
                        else:
                            node_dct = new_node_dct
                            node_dct['weight'] = len(node_dct['zids'])
                            is_include = True
                        # print('{0},{1}'.format(unit2.attr, unit1.attr))
                    elif isinstance(prev_atom, ast.Name):
                        node1 = prev_atom.id
                        node2 = atom.attr
                        if node1.lower() in ENTITIES:
                            classname = node1
                            node1_call = '{0}()'.format(node1)
                        else:
                            node1_call = '{0}({1})'.format(node1, classname)
                        if node2.lower() in ENTITIES:
                            classname = node2
                            node2_call = '{0}()'.format(node2)
                        else:
                            node2_call = '{0}({1})'.format(node2, classname)

                        new_node_dct = {'node1': node1_call, 'node2': node2_call, 'zids': [zid]}
                        node_dct = get_node_dct(node1_call, node2_call, atom_atom_relation_df,
                                                atom_entity_relation_df, entity_atom_relation_df,
                                                entity_entity_relation_df)
                        if node_dct:
                            if node_dct['zids']:
                                a = set(node_dct['zids'])
                                a.add(zid)
                                node_dct['zids'] = list(a)
                            else:
                                node_dct.update(new_node_dct)
                            node_dct['weight'] = len(node_dct['zids'])
                        else:
                            node_dct = new_node_dct
                            node_dct['weight'] = len(node_dct['zids'])
                            is_include = True
                    if is_include:
                        if node1.lower() in ENTITIES and node2.lower() in ENTITIES:
                            entity_entity_relation_df.append(node_dct)
                        elif node1.lower() in ENTITIES and node2.lower() not in ENTITIES:
                            entity_atom_relation_df.append(node_dct)
                        elif node1.lower() not in ENTITIES and node2.lower() in ENTITIES:
                            atom_entity_relation_df.append(node_dct)
                        else:
                            atom_atom_relation_df.append(node_dct)
                        # print('{0},{1}'.format(unit2.id, unit1.attr))

    return atom_atom_relation_df, atom_entity_relation_df, entity_atom_relation_df, entity_entity_relation_df


def get_node_dct(node1, node2, atom_atom_relation_df, atom_entity_relation_df,
                 entity_atom_relation_df, entity_entity_relation_df):
    node_dct = None
    node_dct = next((node_dct for node_dct in atom_atom_relation_df if
                     node_dct['node1'] == node1 and node_dct[
                         'node2'] == node2), None)
    if not node_dct:
        node_dct = next((node_dct for node_dct in atom_entity_relation_df if
                         node_dct['node1'] == node1 and node_dct[
                             'node2'] == node2), None)
    if not node_dct:
        node_dct = next((node_dct for node_dct in entity_atom_relation_df if
                         node_dct['node1'] == node1 and node_dct[
                             'node2'] == node2), None)
    if not node_dct:
        node_dct = next((node_dct for node_dct in entity_entity_relation_df if
                         node_dct['node1'] == node1 and node_dct[
                             'node2'] == node2), None)
    return node_dct


def get_zid(unit_function_def):
    zid = ''
    if (unit_function_def.decorator_list) and isinstance(unit_function_def.decorator_list[0],
                                                         ast.Call):
        decorator_list = unit_function_def.decorator_list
        for decorator in decorator_list:
            if hasattr(decorator.func, 'id') and decorator.func.id == 'zid':
                zid = decorator.args[0].s
    return zid


def write_to_csv(node_lst_dct, filename):
    data_frame = DataFrame(node_lst_dct)
    data_frame.to_csv(path_or_buf='{0}.csv'.format(filename), index=False)




def execute_import_queries(atom_atom_testcase, atom_entity_testcase, entity_atom_testcase,
                           entity_entity_testcase):
    graph = Graph('automation@bolt://localhost:7687', auth=('neo4j', 'Graph123'))
    query_atom = "LOAD CSV WITH HEADERS FROM 'file:///{}.csv' AS line" \
                 " MERGE (u1:Atom{{name:line.node1}}) " \
                 " MERGE (u2:Atom{{name:line.node2}}) " \
                 " MERGE (u1)-[c:chains]->(u2   ) SET c.weight=line.weight, c.testcases=line.zids RETURN u1, u2, c".format(
        atom_atom_testcase)
    graph.run(query_atom)

    query_atom = "LOAD CSV WITH HEADERS FROM 'file:///{}.csv' AS line" \
                 " MERGE (u1:Atom{{name:line.node1}}) " \
                 " MERGE (u2:Entity{{name:line.node2}}) " \
                 " MERGE (u1)-[c:chains]->(u2) SET c.weight=line.weight, c.testcases=line.zids RETURN u1, u2, c".format(
        atom_entity_testcase)
    graph.run(query_atom)

    query_atom = "LOAD CSV WITH HEADERS FROM 'file:///{}.csv' AS line" \
                 " MERGE (u1:Entity{{name:line.node1}}) " \
                 " MERGE (u2:Atom{{name:line.node2}}) " \
                 " MERGE (u1)-[c:chains]->(u2) SET c.weight=line.weight, c.testcases=line.zids RETURN u1, u2, c".format(
        entity_atom_testcase)
    graph.run(query_atom)

    query_atom = "LOAD CSV WITH HEADERS FROM 'file:///{}.csv' AS line" \
                 " MERGE (u1:Entity{{name:line.node1}}) " \
                 " MERGE (u2:Entity{{name:line.node2}}) " \
                 " MERGE (u1)-[c:chains]->(u2) SET c.weight=line.weight, c.testcases=line.zids RETURN u1, u2, c".format(
        entity_entity_testcase)
    graph.run(query_atom)


def copy_to_neo(filename):
    src_path = os.path.abspath('{0}.csv'.format(filename))
    dest_path = r'/Users/skrishnan/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-5c3376b4-3f70-4352-9523-b5d3705b2a82/installation-3.4.6/import'
    shutil.copy2(src_path, dest_path)


def get_parsed(entities):
    atom_atom_relation_df = []
    atom_entity_relation_df = []
    entity_atom_relation_df = []
    entity_entity_relation_df = []

    for artifact_path in entities:
        tree = load_test_cases(artifact_path)
        file_path = os.path.basename(os.path.dirname(str(artifact_path))) + '/' + os.path.basename(
            (str(artifact_path)))
        atom_atom_relation_df, atom_entity_relation_df, entity_atom_relation_df, entity_entity_relation_df = filter_tree(
            tree, ENTITIES, file_path, atom_atom_relation_df, atom_entity_relation_df,
            entity_atom_relation_df, entity_entity_relation_df)

    return atom_atom_relation_df, atom_entity_relation_df, entity_atom_relation_df, entity_entity_relation_df


if __name__ == "__main__":
    path = Path(DIRECTORY)
    entities = list(path.rglob("*_test.py"))
    temp = list(path.rglob("test_*.py"))
    entities = entities + temp

    print('Step 1 : AST parsing & create dictionary list of atoms relations in testcases')
    atom_atom_relation_df, atom_entity_relation_df, entity_atom_relation_df, entity_entity_relation_df = get_parsed(
        entities)
    print('Done')

    print('Step 2 : Write the testcases relations to csv')
    atom_atom_testcases = 'atom_atom_testcase'
    atom_entity_testcases = 'atom_entity_testcase'
    entity_atom_testcases = 'entity_atom_testcase'
    entity_entity_testcases = 'entity_entity_testcase'
    write_to_csv(atom_atom_relation_df, filename='atom_atom_testcase')
    write_to_csv(atom_entity_relation_df, filename='atom_entity_testcase')
    write_to_csv(entity_atom_relation_df, filename='entity_atom_testcase')
    write_to_csv(entity_entity_relation_df, filename='entity_entity_testcase')

    print('Done')

    # print('Step 3 : Copy the csv to Neo4j Graph DB Import folder')
    # copy_to_neo(atom_atom_testcases)
    # copy_to_neo(atom_entity_testcases)
    # copy_to_neo(entity_atom_testcases)
    # copy_to_neo(entity_entity_testcases)
    # print('Done')

    # print('Step 4 : Execute queries to import csv into Neo4j Graph DB')
    # execute_import_queries(atom_atom_testcases, atom_entity_testcases, entity_atom_testcases,
    #                        entity_entity_testcases)
    # print('Done')
