import networkx
import matplotlib.pyplot as pyplot
from adjacency.abstract.adjacency_object import AdjacencyObject


class Graph:
    def __init__(self, _adjacency_object: AdjacencyObject):
        self._adjacency_object = _adjacency_object

    def add_vertex(self):
        self._adjacency_object.add_vertex()

    def remove_vertex(self, vertex_number):
        return self._adjacency_object.remove_vertex(vertex_number)

    def add_edge(self, number_vertex_one, number_vertex_two):
        return self._adjacency_object.add_edge(number_vertex_one, number_vertex_two)

    def remove_edge(self, number_vertex_one, number_vertex_two):
        return self._adjacency_object.remove_edge(number_vertex_one, number_vertex_two)

    def exist_path(self, vertex_start, vertex_to_find):
        return self._adjacency_object.exist_path(vertex_start, vertex_to_find)

    def draw(self):
        graph = self._adjacency_object.create_networkx_graph()
        networkx.draw(graph, with_labels=True)
        pyplot.show(block=True)
