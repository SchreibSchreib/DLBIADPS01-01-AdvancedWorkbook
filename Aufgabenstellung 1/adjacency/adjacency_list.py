class AdjacencyList:
    def __init__(self):
        self._dictionary = {}

    def add_edge(self, edge):
        edge_one, edge_two = edge

        if edge_one not in self._dictionary:
            self._dictionary[edge_one] = []

        if edge_two not in self._dictionary:
            self._dictionary[edge_two] = []

        self._dictionary[edge_one].append(edge_two)
        self._dictionary[edge_two].append(edge_one)

    def remove_edge(self, edge):
        return 0

    def exist_path(self, vertex_a, vertex_b):
        return 0
