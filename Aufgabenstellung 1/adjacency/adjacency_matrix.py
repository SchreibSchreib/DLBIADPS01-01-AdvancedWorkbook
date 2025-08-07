from graph.components.edge import Edge
from graph.components.vertex import Vertex


class AdjacencyMatrix:
    def __init__(self, data=None):

        if data is not None:
            edges, max_node, self._existing_nodes = self._load_graph_from_file(data)
            self._matrix = self._create_matrix(
                edges, max_node + 1
            )

    def _load_graph_from_file(self, data):
        edges = []
        max_node = 0
        existing_nodes = set()

        for index in range(data.num_vertices):
            existing_nodes.add(index)

        for line in data.output:
            parts = line.strip().split()
            if len(parts) != 2:
                print(f"Skipped line: {line}: invalid format")
                continue
            vertex_one, vertex_two = map(int, parts)
            edges.append((vertex_one, vertex_two))
            max_node = max(max_node, vertex_one, vertex_two)

        return edges, max_node, existing_nodes

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
        return vertex.vertex_number() in self._existing_nodes

    def add_vertex(self, vertex):
        if not self._vertex_exists(vertex):
            self._existing_nodes.add(vertex.vertex_number)
        else:
            print(f"Vertex {vertex.vertex_number} already exists.")

    def remove_vertex(self, vertex):
        if not self._vertex_exists(vertex):
            print(f"Failed: Vertex {vertex.vertex_number} does not exist.")
        else:
            self._existing_nodes.remove(vertex.vertex_number)
            for entry in self._matrix[vertex.vertex_number]:
                entry = 0

    def add_edge(self, edge):
        vertex_one, vertex_two = edge.vertices
        number_vertex_one = vertex_one.vertex_number
        number_vertex_two = vertex_two.vertex_number

        if not self._vertex_exists(vertex_one):
            print(f"Failed: Vertex {number_vertex_one} is not found.")

        elif not self._vertex_exists(vertex_two):
            print(f"Failed: Vertex {number_vertex_two} is not found.")

        else:
            self._matrix[number_vertex_one][number_vertex_two] = 1
            self._matrix[number_vertex_two][number_vertex_one] = 1

    def remove_edge(self, edge):
        vertex_one, vertex_two = edge.vertices
        vertex_one_number = vertex_one.vertex_number
        vertex_two_number = vertex_two.vertex_number

        if self._vertex_exists(vertex_one):
            self._matrix[vertex_one_number][vertex_two_number] = 0
            self._matrix[vertex_two_number][vertex_one_number] = 0

        else:
            print(f"Failed: No edge found between {vertex_one} and {vertex_two}")

    def exist_path(self, edge):
        vertex_one, vertex_two = edge.vertices
        return self._matrix[vertex_two.vertex_number][vertex_one.vertex_number] == 1

    def get_adjacency_info(self):
        return self._matrix
    
    def vertex_exist(self, vertex_number):
        return vertex_number in self._existing_nodes
