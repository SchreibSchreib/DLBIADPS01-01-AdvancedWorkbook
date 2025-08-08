from typing import Dict, Set


class AdjacencyList:
    def __init__(self, graph_data=None):
        self.dictionary: Dict[int, Set[int]] = {}

        if graph_data:
            self._load_graph_from_file(graph_data)

    def _load_graph_from_file(self, graph_data):
        for index in range(graph_data.num_vertices):
            self.add_vertex()

        for line in graph_data.output:
            try:
                number_vertex_one, number_vertex_two = map(int, line.strip().split())
                self.add_edge(number_vertex_one, number_vertex_two)
            except ValueError:
                print(f"Skipped invalid value: {line}")

    def _vertex_exists(self, vertex_number):
        return vertex_number in self.dictionary

    def add_vertex(self):
        self.dictionary[len(self.dictionary)] = set()

    def remove_vertex(self, vertex_number):
        if not self._vertex_exists(vertex_number):
            print(f"Failed: Vertex {vertex_number} does not exist.")
            return
        
        for connected_vertex in self.dictionary[vertex_number]:
            self.dictionary[connected_vertex].discard(vertex_number)
        del self.dictionary[vertex_number]

    def add_edge(self, number_vertex_one, number_vertex_two):
        if not (self._vertex_exists(number_vertex_one)
            and self._vertex_exists(number_vertex_two)):
            print(f"Failed: One or both vertices not found: {number_vertex_one}, {number_vertex_two}")
            return

        self.dictionary[number_vertex_one].add(number_vertex_two)
        self.dictionary[number_vertex_two].add(number_vertex_one)

    def remove_edge(self, number_vertex_one, number_vertex_two):
        if not (self._vertex_exists(number_vertex_one)
            and self._vertex_exists(number_vertex_two)):
            print(f"Failed: One or both vertices not found: {number_vertex_one}, {number_vertex_two}")
            return
        
        self.dictionary[number_vertex_one].discard(number_vertex_two)
        self.dictionary[number_vertex_two].discard(number_vertex_one)

    def exist_path(self, edge):
        vertex_one, vertex_two = edge.vertices
        return vertex_two.number in self.dictionary.get(vertex_one.number, [])

    def get_adjacency_info(self):
        return self.dictionary