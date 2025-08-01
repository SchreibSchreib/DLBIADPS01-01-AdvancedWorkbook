class Edge:
    def __init__(self, vertex_a, vertex_b):
        self._vertices = (vertex_a, vertex_b)

    @property
    def vertices(self):
        return self._vertices