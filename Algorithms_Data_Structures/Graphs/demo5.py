from collections import OrderedDict

links_data = [
    {'target': "project", 'source': "fluent", 'strength': 0.7},
    {'target': "timesheet", 'source': "fluent", 'strength': 0.7},
    {'target': "task", 'source': "project", 'strength': 0.7},
    {'target': "set_title(project)", 'source': "project", 'strength': 0.7},
    {'target': "set_description(project)", 'source': "project", 'strength': 0.7},
    {'target': "log", 'source': "timesheet", 'strength': 0.7},
    {'target': "submit", 'source': "log", 'strength': 0.7},
    {'target': "approve", 'source': "submit", 'strength': 0.7},
    {'target': "verify", 'source': "approve", 'strength': 0.1},
    {'target': "verify", 'source': "set_title(project)", 'strength': 0.1},
    {'target': "verify", 'source': "set_description(project)", 'strength': 0.1},
    {'target': "asset", 'source': "fluent", 'strength': 0.1}
]

nodes_data = [
	  { 'id': "fluent", 'group': 0, 'label': "Fluent", 'type': "Entity" },
	  { 'id': "project"   , 'group': 0, 'label': "Project"   , 'type': "Entity" },
	  { 'id': "timesheet"   , 'group': 0, 'label': "Timesheet"   , 'type': "Entity" },
	  { 'id': "task"   , 'group': 0, 'label': "Task"  , 'type': "Entity" },
	  { 'id': "log"   , 'group': 0, 'label': "Log"    , 'type': "Atom" },
	  { 'id': "submit", 'group': 1, 'label': "Submit", 'type': "Atom" },
	  { 'id': "approve"   , 'group': 1, 'label': "Approve"   , 'type': "Atom" },
	  { 'id': "verify"   , 'group': 1, 'label': "Verify"   , 'type': "Atom" },
	  { 'id': "asset"  , 'group': 2, 'label': "Asset"   , 'type': "Entity" },
	  { 'id': "set_title(project)"  , 'group': 2, 'label': "set_title"   , 'type': "Atom" },
	  { 'id': "set_description(project)"  , 'group': 2, 'label': "set_decription"  , 'type': "Atom" }
]

def extract_start_end_weight(links_data):
    lst_edges = []
    for edge in links_data:
        tuple_edge = (edge['source'], edge['target'], edge['strength'])
        lst_edges.append(tuple_edge)
    return lst_edges


class Node:
    def __init__(self, node_name, num):
        self.name = node_name
        self.id = num
        self.children_nodes = {}

    def __str__(self):
        return str(self.name) + ' children: ' + str([x.name for x in self.children_nodes])

    def add_child(self, child_node, weight=0):
        self.children_nodes[child_node] = weight

    def get_child_connections(self):
        return self.children_nodes.keys()

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        if neighbor in self.children_nodes:
            return self.children_nodes[neighbor]


class Graph:
    def __init__(self):
        self.dct_nodes = {}
        self.num_nodes = 0

    def add_node(self, node_name):
        self.num_nodes = self.num_nodes + 1
        if node_name not in self.dct_nodes:
            new_node = Node(node_name, self.num_nodes)
            self.dct_nodes[node_name] = new_node
            return new_node
        else:
            print('Node already present in Graph')

    def get_node(self, node_name):
        if node_name in self.dct_nodes:
            return self.dct_nodes[node_name]
        else:
            return None

    def get_total_nodes(self):
        return self.num_nodes

    def add_edge(self, start, end, weight=1):
        if start not in self.dct_nodes:
            self.add_node(start)
        if end not in self.dct_nodes:
            self.add_node(end)
        self.dct_nodes[start].add_child(self.dct_nodes[end], weight)

    def get_all_start_nodes(self):
        # All the nodes in the Graph
        set_of_node_names = set(self.dct_nodes)

        # Iterating over the Graph and getting the Connection Node names
        for node_name in self.dct_nodes:
            connected_node_names = self.get_all_child_connections(node_name)
            set_connected_node_names = set(connected_node_names)

            # Getting the final set of nodes which doesnt appear in connected nodes
            set_of_node_names -= set_connected_node_names
            # This gives the list of start nodes in the graph as they dont appear in connected nodes
        self.start_nodes = list(set_of_node_names)
        return self.start_nodes

    def get_all_end_nodes(self):
        lst_end_nodes = []
        for node_name in self.dct_nodes:
            if not self.dct_nodes[node_name].get_child_connections():
                lst_end_nodes.append(node_name)
        self.end_nodes = lst_end_nodes
        return self.end_nodes

    def get_weight(self, node1_name, node2_name):
        node1 = self.get_node(node1_name)
        node2 = self.get_node(node2_name)
        weight = node1.get_weight(node2)
        return weight if weight else 0

    def get_all_child_connections(self, node_name):
        node = self.get_node(node_name)
        connected_node_names = []
        for connected_node in node.get_child_connections():
            connected_node_names.append(connected_node.get_name())
        return connected_node_names

    def find_paths_between_nodes(self, start, end, loop_count=1, path=[]):
        paths = []
        if start not in self.dct_nodes or end not in self.dct_nodes:
            return paths

        path = path + [start]

        if start == end:
            return [path]

        for node in self.get_all_child_connections(start):
            # if node not in path:
            if path.count(node) < loop_count:
                newpaths = self.find_paths_between_nodes(node, end, loop_count, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.dct_nodes:
            return None
        shortest = None
        for node in self.get_all_child_connections(start):
            if node not in path:
                newpath = self.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def find_all_paths(self):
        lst_all_paths = []
        start_nodes = self.get_all_start_nodes()
        end_nodes = self.get_all_end_nodes()
        for start_node in start_nodes:
            for end_node in end_nodes:
                path = self.find_paths_between_nodes(start_node, end_node)
                lst_all_paths.extend(path)
        return lst_all_paths

    def get_valid_coverage(self, lst_invalid_paths):
        lst_all_paths = self.find_all_paths()
        set_all_paths = set(tuple(path) for path in lst_all_paths)
        set_invalid_paths = set(tuple(path) for path in lst_invalid_paths)
        valid_paths = set_all_paths - set_invalid_paths

        valid_paths = list(list(path) for path in valid_paths)
        return valid_paths

    def clone(self, src_node_name, target_node_name):
        src_node = Node(src_node_name, self.num_nodes + 1)
        self.dct_nodes[src_node_name] = src_node
        target_node = self.get_node(target_node_name)

        # Assign the children of 'target'_node to the src_node along the weights
        src_node.children_nodes = target_node.children_nodes.copy()

        # Assign the parents of 'target'_node to the src_node along with the weights
        parent_node_names = self.get_parent_node_names(target_node_name)
        for parent_name in parent_node_names:
            # weight = self.get_weight(parent_name, target_node_name)
            self.add_edge(parent_name, src_node_name, 0)

        return src_node

    def get_parent_node_names(self, child_node_name):
        lst_parent_nodes_names = []
        for node_name in self.dct_nodes:
            if child_node_name in self.get_all_child_connections(node_name):
                lst_parent_nodes_names.append(node_name)
        return lst_parent_nodes_names

    def get_node_id_from_name(self, node_name):
        node = self.get_node(node_name)
        return node.get_id()

    def construct_mapping_dcts_ids_names(self):
        self.dct_name_id = {}
        self.dct_id_name = {}
        for name in self.dct_nodes:
            node = self.get_node(name)
            id = node.get_id()
            self.dct_name_id[name] = id
            self.dct_id_name[id] = name
        return self

    def get_all_node_names(self):
        return list(self.dct_nodes.keys())

    def convert_lst_d3_json(self, lst_valid_paths):
        dct_master_cases = {}
        index = 0
        for lpath in lst_valid_paths:
            dct_data = {}
            new_links_data = self.populate_links_data(lpath)
            dct_data['links_data'] = new_links_data
            new_nodes_data = self.populate_nodes_data(lpath)
            dct_data['nodes_data'] = new_nodes_data
            index = index + 1
            key_name = 'G' + str(index)
            dct_master_cases[key_name] = dct_data
        return dct_master_cases

    def get_master_graph(self, lst_valid_paths):
        test_graphs = self.convert_lst_d3_json(lst_valid_paths)
        pass

    def get_lst_nodes_links(self, test_graphs):
        lst_nodes_data = []
        lst_links_data = []
        for test in test_graphs:
            node_data = test_graphs[test]['nodes_data']
            link_data = test_graphs[test]['links_data']
            lst_nodes_data.extend(node_data)
            lst_links_data.extend(link_data)
        return lst_links_data, lst_nodes_data

    def get_set_nodes_links(self, lst_links_data, lst_nodes_data):
        import json
        set_nodes_data = set()
        set_links_data = set()
        for item in lst_nodes_data:
            set_nodes_data.add(json.dumps(item, sort_keys=True))
        for item in lst_links_data:
            set_links_data.add(json.dumps(item, sort_keys=True))
        return set_links_data, set_nodes_data


    def convert_str_dict(self,set_links_data, set_nodes_data):
        import ast
        lst_nodes_data = list(set_nodes_data)
        lst_links_data = list(set_links_data)
        lst_link = []
        lst_nodes = []
        for item in lst_links_data:
            lst_link.append(ast.literal_eval(item))
        for item in lst_nodes_data:
            lst_nodes.append(ast.literal_eval(item))

        return  lst_link, lst_nodes

    def construct_master_graph(self, lst_link, lst_nodes):
        dct_master_graph = {}
        dct_data = {}
        dct_data['nodes_data'] = lst_nodes
        dct_data['links_data'] = lst_link
        dct_master_graph['graph_data'] = dct_data
        print(dct_master_graph)

    def populate_nodes_data(self, testcase):
        new_nodes_data = []
        for atom in testcase:
            for node in nodes_data:
                if atom == node['id']:
                    new_nodes_data.append(node)
                    break
        return new_nodes_data

    def populate_links_data(self, lpath):
        lst_d3_json = []
        for index, value in enumerate(lpath):
            if index <= len(lpath) - 2:
                d3_json = {}
                d3_json['source'] = value
                d3_json['target'] = lpath[index + 1]
                d3_json['strength'] = 1
                lst_d3_json.append(d3_json)
        return lst_d3_json


if __name__ == '__main__':
    cyle_count = 2
    g = Graph()
    input_datas = extract_start_end_weight(links_data)

    for data in input_datas:
        g.add_edge(*data)

    # print(g.get_all_start_nodes())
    # print(g.get_all_end_nodes())
    #
    # print(g.get_weight('a', 'b'))
    # print(g.get_all_child_connections('b'))
    #
    # #
    #
    # print('>' * 100)
    # print(g.find_paths_between_nodes('a', 'f'))
    # print('>' * 100)
    #
    # from functools import partial
    #
    # print('Path with One loop >>>>>>')
    # find_paths_between_nodes_with_no_loop = partial(g.find_paths_between_nodes, loop_count=1, path=[])
    # print(find_paths_between_nodes_with_no_loop('a', 'f'))
    # print('>' * 100)
    #
    # print('Path with Two loops >>>>>>')
    # find_paths_between_nodes_with_one_loop = partial(g.find_paths_between_nodes, loop_count=2, path= [])
    # print(find_paths_between_nodes_with_one_loop('a', 'f'))
    # print('>' * 100)
    # print(g.find_shortest_path('a', 'f'))

    print('\nGetting all the paths\n')
    print(g.find_all_paths())

    print('\nGetting only the Valid paths\n')
    invalid_paths = [('fluent', 'project', 'task')]
    lst_valid_paths = g.get_valid_coverage(invalid_paths)
    print(lst_valid_paths)

    print('\nGetting valid paths in d3 json format\n')
    print(g.convert_lst_d3_json(lst_valid_paths))

    # print('\n>>> Cloning Node portfolio as project  >>>>\n')
    # g.clone('portfolio', 'project')
    # print(g.find_paths_between_nodes('fluent', 'verify'))
    # g.construct_mapping_dcts_ids_names()
    #
    # print(g.get_node_id_from_name('verify'))
    # print(g.get_node_id_from_name('portfolio'))
    #
    # print(g.dct_id_name)
    # print(g.dct_name_id)
    # print(g.get_node('project'))