class Vertex:
    def __init__(self, vertex_number):
        self._vertex_number = vertex_number

    @property
    def vertex_number(self):
        return self._vertex_number