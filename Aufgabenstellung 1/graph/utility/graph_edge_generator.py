import random


class GraphEdgeGenerator:
    def __init__(self, num_vertices, num_edges):
        self.num_vertices = num_vertices
        self._num_edges = num_edges
        self.output = self.generate_random_edges()

    def generate_random_edges(self):
        output_strings = []

        while len(output_strings) < self._num_edges:
            vertex_one = random.randint(0, self.num_vertices - 1)
            vertex_two = random.randint(0, self.num_vertices - 1)

            output_strings.append(f"{min(vertex_one, vertex_two)} {max(vertex_one, vertex_two)}")
        
        return output_strings
