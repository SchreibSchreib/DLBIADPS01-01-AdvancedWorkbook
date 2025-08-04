from graph.components.edge import Edge
from graph.components.vertex import Vertex
from typing import Dict, List


class AdjacencyList:
    def __init__(self, filepath=None):
        self._dictionary: Dict[int, List[int]] = {}

        if filepath is not None:
            self._load_graph_from_file(filepath)

    def _load_graph_from_file(self, filepath):
        with open(filepath, "r") as file:
            for line in file:
                parts = line.strip().split()
                vertex_one, vertex_two = map(int, parts)
                self.add_vertex(Vertex(vertex_one))
                self.add_vertex(Vertex(vertex_two))
                self.add_edge(Edge(Vertex(vertex_one), Vertex(vertex_two)))

    def _vertex_exists(self, vertex):
        number_of_vertex = vertex.vertex_number

        return number_of_vertex in self._dictionary

    def add_vertex(self, vertex):
        if not self._vertex_exists(vertex):
            self._dictionary[vertex.vertex_number] = []
        else:
            print(f"Vertex {vertex.vertex_number} already exists.")

    def remove_vertex(self, vertex):
        if not self._vertex_exists(vertex):
            print(f"Failed: Vertex {vertex.vertex_number} does not exist.")

        else:
            for connected_vertex in self._dictionary[vertex.vertex_number]:
                self._dictionary[connected_vertex].remove(vertex.vertex_number)
            del self._dictionary[vertex.vertex_number]

    def add_edge(self, edge):
        vertex_one, vertex_two = edge.vertices
        number_vertex_one = vertex_one.vertex_number
        number_vertex_two = vertex_two.vertex_number

        if not self._vertex_exists(vertex_one):
            print(f"Failed: Vertex {number_vertex_one} is not found.")

        elif not self._vertex_exists(vertex_two):
            print(f"Failed: Vertex {number_vertex_two} is not found.")

        else:
            self._dictionary[number_vertex_one].append(number_vertex_two)
            self._dictionary[number_vertex_two].append(number_vertex_one)

    def remove_edge(self, edge):
        vertex_one, vertex_two = edge.vertices
        vertex_one_number = vertex_one.vertex_number
        vertex_two_number = vertex_two.vertex_number

        if self._vertex_exists(vertex_one):
            self._dictionary[vertex_one_number].remove(vertex_two_number)
            self._dictionary[vertex_two_number].remove(vertex_one_number)

        else:
            print(f"Failed: No edge found between {vertex_one} and {vertex_two}")

    def exist_path(self, edge):
        vertex_one, vertex_two = edge.vertices
        return vertex_two.vertex_number in self._dictionary.get(
            vertex_one.vertex_number, []
        )
