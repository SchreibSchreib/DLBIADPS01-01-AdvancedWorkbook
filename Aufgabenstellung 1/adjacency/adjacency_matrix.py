class AdjacencyMatrix:
    def __init__(self, graph_data=None):
        self.matrix = []
        self._existing_nodes = set()

        if graph_data:
            self._existing_nodes = set(range(graph_data.num_vertices))
            self.matrix = [
                [0] * graph_data.num_vertices for i in range(graph_data.num_vertices)
            ]
            self._create_matrix(graph_data)

    def _create_matrix(self, graph_data):
        for line in graph_data.output:
            try:
                number_vertex_one, number_vertex_two = map(int, line.split())
                self.add_edge(number_vertex_one, number_vertex_two)
            except ValueError:
                print(f"Skipped invalid value: {line}")

    def _vertex_exists(self, vertex_number):
        return vertex_number in self._existing_nodes

    def _expand_matrix(self):
        for row in self.matrix:
            row.append(0)

        self.matrix.append([0] * (len(self.matrix) + 1))

    def _reduce_matrix(self, index):
        if len(self.matrix) == 0:
            return

        self.matrix.pop(index)
        for row in self.matrix:
            row.pop(index)

    def add_vertex(self):
        self._existing_nodes.add(len(self._existing_nodes))
        self._expand_matrix()

    def remove_vertex(self, index):
        self._existing_nodes.remove(len(self._existing_nodes) - 1)
        self._reduce_matrix(index)

    def add_edge(self, number_vertex_one, number_vertex_two):
        if self._vertex_exists(number_vertex_one) and self._vertex_exists(
            number_vertex_two
        ):
            self.matrix[number_vertex_one][number_vertex_two] = 1
            self.matrix[number_vertex_two][number_vertex_one] = 1

    def remove_edge(self, number_vertex_one, number_vertex_two):
        if self._vertex_exists(number_vertex_one) and self._vertex_exists(
            number_vertex_two
        ):
            self.matrix[number_vertex_one][number_vertex_two] = 0
            self.matrix[number_vertex_two][number_vertex_one] = 0

    def exist_path(self, number_vertex_one, number_vertex_two, visited_vertices=None):
        if visited_vertices is None:
            visited_vertices = set()

        if number_vertex_one == number_vertex_two:
            return True
        
        visited_vertices.add(number_vertex_one)

        for neighbour, list_value in enumerate(self.matrix[number_vertex_one]):
            if list_value == 1 and neighbour not in visited_vertices:
                if self.exist_path(neighbour, number_vertex_two, visited_vertices):
                    return True
        return False

    def get_adjacency_info(self):
        return self.matrix
