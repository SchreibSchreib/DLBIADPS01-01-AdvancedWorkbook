from time_measure.timer import timer
from adjacency.abstract.adjacency_object import AdjacencyObject
from memory_profiler import profile
import networkx


class AdjacencyMatrix(AdjacencyObject):
    def __init__(self, graph_data=None):
        self.matrix = []
        self._existing_nodes = set()

        if graph_data:
            self._existing_nodes = set(range(graph_data.num_vertices))
            self.matrix = [
                [0] * graph_data.num_vertices for i in range(graph_data.num_vertices)
            ]
            self._create_matrix(graph_data)
    
    @timer
    @profile
    def _create_matrix(self, graph_data):
        for line in graph_data.output:
            try:
                number_vertex_one, number_vertex_two = map(int, line.split())
                self._add_edge_no_logging(number_vertex_one, number_vertex_two)
            except ValueError:
                print(f"Skipped invalid value: {line}")

    def _add_edge_no_logging(self, number_vertex_one, number_vertex_two):
        if self._vertex_exists(number_vertex_one) and self._vertex_exists(
            number_vertex_two
        ):
            self.matrix[number_vertex_one][number_vertex_two] = 1
            self.matrix[number_vertex_two][number_vertex_one] = 1
            return True
        return False

    def _vertex_exists(self, vertex_number):
        return vertex_number in self._existing_nodes

    def _expand_matrix(self):
        for row in self.matrix:
            row.append(0)

        self.matrix.append([0] * (len(self.matrix) + 1))

    def _reduce_matrix(self, index):
        if len(self.matrix) == 0:
            return False

        self.matrix.pop(index)
        for row in self.matrix:
            row.pop(index)
        print("Matrix neu durchnummeriert")
        return True
    
    @timer
    @profile
    def add_vertex(self):
        self._existing_nodes.add(len(self._existing_nodes))
        self._expand_matrix()
    
    @timer
    @profile
    def remove_vertex(self, index):
        self._existing_nodes.remove(len(self._existing_nodes) - 1)
        return self._reduce_matrix(index)
    
    @timer
    @profile
    def add_edge(self, number_vertex_one, number_vertex_two):
        if self._vertex_exists(number_vertex_one) and self._vertex_exists(
            number_vertex_two
        ):
            self.matrix[number_vertex_one][number_vertex_two] = 1
            self.matrix[number_vertex_two][number_vertex_one] = 1
            return True
        return False
    
    @timer
    @profile
    def remove_edge(self, number_vertex_one, number_vertex_two):
        if self._vertex_exists(number_vertex_one) and self._vertex_exists(
            number_vertex_two
        ):
            self.matrix[number_vertex_one][number_vertex_two] = 0
            self.matrix[number_vertex_two][number_vertex_one] = 0
            return True
        return False
    
    @timer
    def exist_path(self, vertex_start, vertex_to_find, visited_vertices=None):
        if visited_vertices is None:
            visited_vertices = set()

        if vertex_start == vertex_to_find:
            return True

        visited_vertices.add(vertex_start)

        for neighbor, list_value in enumerate(self.matrix[vertex_start]):
            if list_value == 1 and neighbor not in visited_vertices:
                if self.exist_path(neighbor, vertex_to_find, visited_vertices):
                    return True
        return False

    def create_networkx_graph(self):
        graph = networkx.Graph()

        for y_index in range(0, len(self.matrix)):
            graph.add_node(y_index)
            for x_index in range(y_index + 1, len(self.matrix)):
                if self.matrix[y_index][x_index] == 1:
                    graph.add_edge(x_index, y_index)
        
        return graph