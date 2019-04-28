from Algorithms_Data_Structures.Graphs.graph import Graph

class GraphDbAdapter:
    def __init__(self, input_data):
        self.links_data, self.nodes_data = self.get_data_from_graphDB(input_data)

    def get_data_from_graphDB(self, input_data):
        links_data = input_data['links']
        nodes_data = input_data['nodes']
        return links_data, nodes_data


    def prepare_data_for_all_edges_of_graph(self):
        lst_edges = []
        for edge in self.links_data:
            tuple_edge = (edge['source'], edge['target'])
            lst_edges.append(tuple_edge)
        return lst_edges

    def construct_graph(self):
        lst_edges = self.prepare_data_for_all_edges_of_graph()
        graph_object = Graph()
        [graph_object.add_edge(*edge) for edge in lst_edges]

        return graph_object




