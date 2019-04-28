import ast
import os
import shutil
from pandas import DataFrame
from py2neo import Graph

DIRECTORY = 'autobots/entities'
ENTITIES = ['asset', 'dataimport', 'issue', 'portfolio', 'project', 'resource', 'rollups', 'schedule', 'task',
            'timeadmin', 'timesheet', 'user']


def load_test_cases(artifact):
    artifact_file_name = ''.join([artifact, '.py'])
    base_path = os.path.join(os.path.dirname(__file__), DIRECTORY + '/' + artifact)
    fullpath = os.path.join(base_path, artifact_file_name)
    data = open(fullpath).read()
    tree = ast.parse(data, fullpath)
    return tree


def filter_tree(tree, artifact_files):
    for index, node in enumerate(tree.body[:]):
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            class_def = '{}()'.format(class_name)
            decorator_lst = node.decorator_list
            class_node = {'label': class_name, 'id': class_name.lower(), 'definition': class_def,
                          'decorators': decorator_lst, 'type': 'artifact'}
            atom_nodes_lst = filter_nodes(node.body)  # Filter only atom nodes
            atom_nodes_metadata_lst_dct = get_metadata_all_atom_nodes(
                atom_nodes_lst, class_name, artifact_files)  # Get the list of dict having details of each node
            return class_node, atom_nodes_metadata_lst_dct


def get_metadata_all_atom_nodes(nodes_lst, class_name, artifact_files):
    node_metadata_lst_dct = []
    for node in nodes_lst:
        node_metadata = get_metadata_dict(node, class_name, artifact_files)
        node_metadata_lst_dct.append(node_metadata)

    return node_metadata_lst_dct


def get_metadata_dict(node, class_name, artifact_files):
    function_name = node.name
    if function_name.lower() in artifact_files:
        relation = '{}()'.format(function_name)
        type = 'entity'

    else:
        function_name = '{0}({1})'.format(function_name, class_name)
        relation = '.'
        type = 'atom'
    function_def = '{0}()'.format(function_name)
    node = {'label': function_name, 'id': function_name.lower(), 'definition': function_def,
            'decorators': node.decorator_list, 'type': type, 'relation': relation}
    return node


def filter_nodes(function_defs_lst):
    valid_node_lst = []
    for node in function_defs_lst:
        if node.name[0] != '_':
            valid_node_lst.append(node)
    return valid_node_lst


def write_to_csv(node_lst_dct, filename):
    data_frame = DataFrame(node_lst_dct)
    data_frame.to_csv(path_or_buf='{0}.csv'.format(filename), index=False)


def execute_import_queries(filename_atom, filename_entity):
    query_atom = "LOAD CSV WITH HEADERS FROM 'file:///{}.csv' AS line" \
                 " MERGE (u1:Entity{{id:line.artifact_id}}) SET u1.name=line.artifact_id,u1.code_definition=line.artifact_definition" \
                 " MERGE (u2:Atom{{id:line.atom_id}}) SET u2.name=line.atom_id,u2.code_definition=line.atom_definition" \
                 " MERGE (u1)-[c:belongs{{name:line.relation}}]->(u2) RETURN u1, u2, c".format(filename_atom)
    query_entity = "LOAD CSV WITH HEADERS FROM 'file:///{}.csv' AS line" \
                   " MERGE (u1:Entity{{id:line.artifact_id}}) SET u1.name=line.artifact_id,u1.code_definition=line.artifact_definition" \
                   " MERGE (u2:Entity{{id:line.atom_id}}) SET u2.name=line.atom_id,u2.code_definition=line.atom_definition" \
                   " MERGE (u1)-[c:connects{{name:line.relation}}]->(u2) RETURN u1, u2, c".format(filename_entity)

    graph = Graph('automation@bolt://localhost:7687', auth=('neo4j', 'Graph123'))
    graph.run(query_atom)
    graph.run(query_entity)


def copy_to_neo(filename):
    src_path = os.path.abspath('{0}.csv'.format(filename))
    dest_path = r'/Users/skrishnan/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-5c3376b4-3f70-4352-9523-b5d3705b2a82/installation-3.4.6/import'
    shutil.copy2(src_path, dest_path)


def get_parsed():
    atom_relation_df_lst_dct = []
    entity_relation_df_lst_dct = []
    for artifact_name in ENTITIES:
        tree = load_test_cases(artifact_name)
        class_node, atom_nodes_metadata_lst_dct = filter_tree(tree, ENTITIES)
        for atom_node in atom_nodes_metadata_lst_dct:

            node_dct = {'artifact_label': class_node['label'], 'artifact_id': class_node['id'],
                        'artifact_definition': class_node['definition'], 'atom_label': atom_node['label'],
                        'atom_id': atom_node['id'], 'atom_definition': atom_node['definition'],
                        'relation': atom_node['relation']}
            if atom_node['type'] == 'atom':
                atom_relation_df_lst_dct.append(node_dct)
            else:
                entity_relation_df_lst_dct.append(node_dct)
    return atom_relation_df_lst_dct, entity_relation_df_lst_dct


if __name__ == "__main__":
    # artifact_files = sys.argv[1:]

    print('Step 1 : AST parsing & analyzing atoms-entity relations')
    atom_relation_df_lst_dct, entity_relation_df_lst_dct = get_parsed()
    print('Done')

    print('Step 2 : Write the relations and metadata to csv')
    filename_atom = 'atom'
    filename_entity = 'entity'
    write_to_csv(atom_relation_df_lst_dct, filename=filename_atom)
    write_to_csv(entity_relation_df_lst_dct, filename=filename_entity)
    print('Done')

    print('Step 3 : Copy the csv to Neo4j Graph DB Import folder')
    copy_to_neo(filename_atom)
    copy_to_neo(filename_entity)
    print('Done')

    print('Step 4 : Execute queries to import csv into Neo4j Graph DB')
    execute_import_queries(filename_atom, filename_entity)
    print('Done')
