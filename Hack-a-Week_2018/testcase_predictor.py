from Algorithms_Data_Structures.Graphs.graphDBAdapter import GraphDbAdapter
from Algorithms_Data_Structures.Graphs.input.latest_input import input_data
from Algorithms_Data_Structures.Graphs.d3_json_formatter import D3JsonFormatter



class TestCasePredictor:
    def __init__(self):
        self.adapter_object = GraphDbAdapter(input_data)
        self.nodes_data = self.adapter_object.nodes_data
        self.graph = self.adapter_object.construct_graph()


    def run(self):
        lst_valid_paths = self.graph.run_prediction()
        d3_obj = D3JsonFormatter(lst_valid_paths, self.nodes_data)
        test_graph= d3_obj.convert_to_d3_json_format()
        master_graph = d3_obj.get_master_graph()
        return test_graph, master_graph



if __name__ == '__main__':
    testgen_obj = TestCasePredictor()
    testgen_obj.run()
