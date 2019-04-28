class Node:
    def __init__(self, node_name):
        self.name = node_name
        self.adjacent_nodes = {}

    def __str__(self):
        return str(self.name) + ' adjacent: ' + str([x.name for x in self.adjacent_nodes])

    def add_neighbor(self, neighbor_node, weight=0):
        self.adjacent_nodes[neighbor_node] = weight

    def get_connections(self):
        return self.adjacent_nodes.keys()

    def get_name(self):
        return self.name

    def get_weight(self, neighbor):
        if neighbor in self.adjacent_nodes:
            return self.adjacent_nodes[neighbor]

    # def clone_node(self, src_node_name):
    #     new_node = Node(src_node_name)
    #     new_node.adjacent_nodes = self.adjacent_nodes.copy()
    #     return new_node


class Graph:
    def __init__(self):
        self.dct_nodes = {}
        self.num_nodes = 0

    def __iter__(self):
        return iter(self.dct_nodes.values())

    def add_node(self, node_name):
        if node_name not in self.dct_nodes:
            new_node = Node(node_name)
            self.dct_nodes[node_name] = new_node
            self.num_nodes = self.num_nodes + 1
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
            connected_node_names = self.get_all_connections(node_name)
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

    def get_weights(self, node1_name, node2_name):
        node1 = self.get_node(node1_name)
        node2 = self.get_node(node2_name)
        weight = node1.get_weight(node2)
        return weight if weight else 0

    def get_all_connections(self, node_name):
        node = self.get_node(node_name)
        connected_node_names = []
        for connected_node in node.get_connections():
            connected_node_names.append(connected_node.get_name())
        return connected_node_names

    def find_paths_between_nodes(self, start, end, path=[]):
        paths = []
        if start not in self.dct_nodes:
            return paths
        path = path + [start]
        if start == end:
            return [path]

        for node in self.get_all_connections(start):
            if node not in path:
                newpaths = self.find_paths_between_nodes(node, end, path)
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
        for node in self.get_all_connections(start):
            if node not in path:
                newpath = self.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def find_all_paths(self):
        lst_all_paths = []
        for start_node in self.start_nodes:
            for end_node in self.end_nodes:
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
        src_node = Node(src_node_name)
        target_node = self.get_node(target_node_name)

        # Assign the children to the src_node
        src_node.adjacent_nodes = target_node.adjacent_nodes.copy()

        # Assign the parents to the src_node
        parent_node_names = self.get_parent_node_names(target_node_name)
        for parent_name in parent_node_names:
            weight = self.get_weights(parent_name, target_node_name)
            self.add_edge(parent_name, src_node_name, weight)

        # Populate in the Graph
        self.dct_nodes[src_node_name] = src_node
        return src_node

    def get_parent_node_names(self, child_node_name):
        lst_parent_nodes_names = []
        for node_name in self.dct_nodes:
            if child_node_name in self.get_all_connections(node_name):
                lst_parent_nodes_names.append(node_name)
        return lst_parent_nodes_names


if __name__ == '__main__':
    g = Graph()

    # g.add_node('a')
    # g.add_node('b')
    # g.add_node('c')
    # g.add_node('d')
    # g.add_node('e')
    # g.add_node('f')
    # g.add_node('a')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)
    g.add_edge('a', 'x')
    g.add_edge('x', 'y')
    # g.add_edge('x', 'x', 1)

    print(g.get_all_start_nodes())
    print(g.get_all_end_nodes())
    #
    # print(g.get_weights('a', 'b'))
    # print(g.get_all_connections('b'))
    #
    # print(g.find_paths_between_nodes('a', 'f'))
    # print(g.find_shortest_path('a', 'f'))
    # print(g.find_paths_between_nodes('a', 'y'))
    #
    # print(g.find_all_paths())
    #
    # invalid_paths = [['a', 'b', 'd', 'e', 'f'], ['a', 'c', 'd', 'e', 'f']]
    # print(g.get_valid_coverage(invalid_paths))
    #
    # print(g.get_parent_node_names('c'))
    #
    # g.clone('w', 'c')
    # print(g.get_all_connections('w'))
    # print(g.get_parent_node_names('w'))
    #
    # print(g.find_paths_between_nodes('a', 'w'))
    # print(g.find_paths_between_nodes('a', 'c'))
    #
