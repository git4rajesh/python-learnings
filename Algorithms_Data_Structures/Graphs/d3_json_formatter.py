import json
import ast

class D3JsonFormatter:
    def __init__(self, lst_paths, nodes_data):
        self.lst_valid_paths = self.remove_condition_nodes(lst_paths)
        self.nodes_data = nodes_data

    def remove_condition_nodes(self, lst_paths):
        lst_valid_paths = []
        for testcase in lst_paths:
            new_testcase = list(filter(lambda atom: not atom.startswith('cond'), testcase))
            lst_valid_paths.append(new_testcase)
        return lst_valid_paths

    def get_labels_from_ids_in_node(self, id):
        for node in self.nodes_data:
            if id == node['id']:
                return node['label']

    def convert_to_d3_json_format(self):
        test_case_d3_json_graph = {}
        index = 0
        for testcase in self.lst_valid_paths:
            dct_data = {}
            new_links_data = self.populate_links_data(testcase)
            dct_data['links'] = new_links_data
            new_nodes_data = self.populate_nodes_data(testcase)
            dct_data['nodes'] = new_nodes_data
            index = index + 1
            key_name = 'G' + str(index)
            test_case_d3_json_graph[key_name] = dct_data
        tests_d3_graph = self.convert_single_to_double_quotes(test_case_d3_json_graph)
        self.write_to_file('prediction.json', tests_d3_graph)
        return tests_d3_graph

    def get_master_graph(self):
        test_graphs = self.convert_to_d3_json_format()
        lst_links_data, lst_nodes_data = self.get_lst_nodes_links(test_graphs)
        set_links_data, set_nodes_data = self.get_unique_nodes_links(lst_links_data, lst_nodes_data)
        lst_link, lst_nodes = self.convert_json_dumps_to_dict(set_links_data, set_nodes_data)
        dct_temp_master_graph = self.construct_master_graph(lst_link, lst_nodes)
        dct_master_graph = self.convert_single_to_double_quotes(dct_temp_master_graph)
        return dct_master_graph

    def populate_nodes_data(self, testcase):
        new_nodes_data = []
        for atom in testcase:
            for node in self.nodes_data:
                if atom == node['id']:
                    new_nodes_data.append(node)
                    break
        return new_nodes_data

    def populate_links_data(self, testcase):
        lst_d3_json = []
        for index, value in enumerate(testcase):
            if index <= len(testcase) - 2:
                d3_json = {}
                d3_json['source'] = self.get_labels_from_ids_in_node(value)
                d3_json['target'] = self.get_labels_from_ids_in_node(testcase[index + 1])
                lst_d3_json.append(d3_json)
        return lst_d3_json

    def get_lst_nodes_links(self, test_graphs):
        lst_nodes_data = []
        lst_links_data = []
        for test in test_graphs:
            node_data = test_graphs[test]['nodes']
            link_data = test_graphs[test]['links']
            lst_nodes_data.extend(node_data)
            lst_links_data.extend(link_data)
        return lst_links_data, lst_nodes_data

    def get_unique_nodes_links(self, lst_links_data, lst_nodes_data):
        set_nodes_data = set()
        set_links_data = set()
        for item in lst_nodes_data:
            set_nodes_data.add(json.dumps(item, sort_keys=True))
        for item in lst_links_data:
            set_links_data.add(json.dumps(item, sort_keys=True))
        return set_links_data, set_nodes_data

    def convert_json_dumps_to_dict(self, set_links_data, set_nodes_data):
        lst_nodes_data = list(set_nodes_data)
        lst_links_data = list(set_links_data)
        lst_link = []
        lst_nodes = []
        for item in lst_links_data:
            lst_link.append(ast.literal_eval(item))
        for item in lst_nodes_data:
            lst_nodes.append(ast.literal_eval(item))

        return lst_link, lst_nodes

    def construct_master_graph(self, lst_link, lst_nodes):
        dct_master_graph = {}
        dct_master_graph['nodes_data'] = lst_nodes
        dct_master_graph['links_data'] = lst_link
        self.write_to_file('master.json', dct_master_graph)
        return dct_master_graph

    def write_to_file(self, file_name, tests_d3_graph):
        with open(file_name, 'w') as file:
            file.write(json.dumps(tests_d3_graph))

    def convert_single_to_double_quotes(self, dict_single_quote):
        class mydict(dict):
            def __str__(self):
                return json.dumps(self)

        dict_double_quotes = mydict(dict_single_quote)
        return dict_double_quotes

    # def remove_condition_nodes_old(self):
    #     for testcase in self.lst_valid_paths:
    #         new_testcase = testcase.copy()
    #         for atom in new_testcase:
    #             if atom.startswith('cond'):
    #                 testcase.remove(atom)
