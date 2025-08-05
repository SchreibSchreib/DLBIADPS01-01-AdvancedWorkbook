from graph.components.edge import Edge
from graph.components.vertex import Vertex


class AdjacencyMatrix:
    def __init__(self, filepath=None):

        if filepath is not None:
            edges, max_node = self._load_graph_from_file(filepath)
            self._matrix = self._create_matrix(edges, max_node)

    def _load_graph_from_file(self, filepath):
        edges = []
        max_node = 0

        with open(filepath, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) != 2:
                    print(f"Skipped line: {line}: invalid format")
                    continue
                vertex_one, vertex_two = map(int, parts)
                edges.append((vertex_one, vertex_two))
                max_node = max(max_node, vertex_one, vertex_two)

        return edges, max_node

    def _create_matrix(self, edges, max_node):
        matrix = []

        for y_index in range(max_node):
            row = []
            for x_index in range(max_node):
                row.append(0)
            matrix.append(row)

            for vertex_one, vertex_two in edges:
                matrix[vertex_one][vertex_two] = 1
                matrix[vertex_two][vertex_one] = 1

        return matrix

    def _vertex_exists(self, vertex):
        number_of_vertex = vertex.vertex_number

        return number_of_vertex in self._matrix

    def add_vertex(self, vertex):
        if not self._vertex_exists(vertex):
            self._matrix[vertex.vertex_number] = []
        else:
            print(f"Vertex {vertex.vertex_number} already exists.")

    def remove_vertex(self, vertex):
        if not self._vertex_exists(vertex):
            print(f"Failed: Vertex {vertex.vertex_number} does not exist.")

        else:
            for connected_vertex in self._matrix[vertex.vertex_number]:
                self._matrix[connected_vertex].remove(vertex.vertex_number)
            del self._matrix[vertex.vertex_number]

    def add_edge(self, edge):
        vertex_one, vertex_two = edge.vertices
        number_vertex_one = vertex_one.vertex_number
        number_vertex_two = vertex_two.vertex_number

        if not self._vertex_exists(vertex_one):
            print(f"Failed: Vertex {number_vertex_one} is not found.")

        elif not self._vertex_exists(vertex_two):
            print(f"Failed: Vertex {number_vertex_two} is not found.")

        else:
            self._matrix[number_vertex_one].add(number_vertex_two)
            self._matrix[number_vertex_two].add(number_vertex_one)

    def remove_edge(self, edge):
        vertex_one, vertex_two = edge.vertices
        vertex_one_number = vertex_one.vertex_number
        vertex_two_number = vertex_two.vertex_number

        if self._vertex_exists(vertex_one):
            self._matrix[vertex_one_number].remove(vertex_two_number)
            self._matrix[vertex_two_number].remove(vertex_one_number)

        else:
            print(f"Failed: No edge found between {vertex_one} and {vertex_two}")

    def exist_path(self, edge):
        vertex_one, vertex_two = edge.vertices
        return vertex_two.vertex_number in self._matrix.get(
            vertex_one.vertex_number, []
        )

    def get_adjacency_info(self):
        return self._matrix
