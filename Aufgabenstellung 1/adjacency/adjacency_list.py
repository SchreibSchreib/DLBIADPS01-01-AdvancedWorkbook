from typing import Dict, Set
from adjacency.abstract.adjacency_object import AdjacencyObject
from memory_profiler import profile
import networkx


class AdjacencyList(AdjacencyObject):
    def __init__(self, graph_data=None):
        self.dictionary: Dict[int, Set[int]] = {}

        if graph_data:
            self._load_graph_from_file(graph_data)

    @profile
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
    
    @profile
    def add_vertex(self):
        new_id = 0
        while new_id in self.dictionary:
            new_id += 1
        self.dictionary[new_id] = set()
    
    @profile
    def remove_vertex(self, vertex_number):
        if not self._vertex_exists(vertex_number):
            return False
        
        for connected_vertex in self.dictionary[vertex_number]:
            self.dictionary[connected_vertex].discard(vertex_number)
        del self.dictionary[vertex_number]
        return True
    
    @profile
    def add_edge(self, number_vertex_one, number_vertex_two):
        if not (self._vertex_exists(number_vertex_one)
            and self._vertex_exists(number_vertex_two)):
            print(f"Failed: One or both vertices not found: {number_vertex_one}, {number_vertex_two}")
            return False

        self.dictionary[number_vertex_one].add(number_vertex_two)
        self.dictionary[number_vertex_two].add(number_vertex_one)
        return True
    
    @profile
    def remove_edge(self, number_vertex_one, number_vertex_two):
        if not (self._vertex_exists(number_vertex_one)
            and self._vertex_exists(number_vertex_two)):
            print(f"Failed: One or both vertices not found: {number_vertex_one}, {number_vertex_two}")
            return False
        
        self.dictionary[number_vertex_one].discard(number_vertex_two)
        self.dictionary[number_vertex_two].discard(number_vertex_one)
        return True
    
    @profile
    def exist_path(self, vertex_start, vertex_to_find, visited_vertices=None):
        if visited_vertices is None:
            visited_vertices = set()

        if vertex_start == vertex_to_find:
            return True
        
        visited_vertices.add(vertex_start)

        for neighbor in self.dictionary[vertex_start]:
            if neighbor not in visited_vertices:
                if self.exist_path(neighbor, vertex_to_find, visited_vertices):
                    return True
        return False

    def create_networkx_graph(self):
        graph = networkx.Graph()

        for index, items in self.dictionary.items():
            graph.add_node(index)
            for item in items:
                if index < item:
                    graph.add_edge(index, item)

        return graph