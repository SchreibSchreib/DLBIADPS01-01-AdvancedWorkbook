from abc import ABC, abstractmethod


class AdjacencyObject(ABC):
    @abstractmethod
    def add_vertex(self) -> None:
        pass

    @abstractmethod
    def remove_vertex(self, vertex_number):
        pass

    @abstractmethod
    def add_edge(self, number_vertex_one, number_vertex_two):
        pass

    @abstractmethod
    def remove_edge(self, number_vertex_one, number_vertex_two):
        pass

    @abstractmethod
    def exist_path(self, vertex_start, vertex_to_find, visited_vertices):
        pass

    @abstractmethod
    def create_networkx_graph(self):
        pass
