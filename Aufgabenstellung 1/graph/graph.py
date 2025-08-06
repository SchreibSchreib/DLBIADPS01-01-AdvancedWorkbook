from ast import Dict
import networkx
import matplotlib.pyplot as pyplot


class Graph:
    def __init__(self, adjacency_object=None):
        if adjacency_object is not None:
            self._adjacency_object = adjacency_object
            self._adjacency_info = adjacency_object.get_adjacency_info()
            if isinstance(self._adjacency_info, dict):
                self._update_graph_from_list()
            else:
                self._update_graph_from_matrix()

    def _update_graph_from_list(self):
        self.graph = networkx.Graph()

        for index, items in self._adjacency_info.items():
            self.graph.add_node(index)
            for item in items:
                if index < item:
                    self.graph.add_edge(index, item)

    def _update_graph_from_matrix(self):
        self.graph = networkx.Graph()

        for y_index in range(0, len(self._adjacency_info)):
            if self._adjacency_object.vertex_exist(y_index):
                self.graph.add_node(y_index)
            for x_index in range(y_index + 1, len(self._adjacency_info)):
                if self._adjacency_info[y_index][x_index] == 1:
                    self.graph.add_edge(x_index, y_index)

    def draw_graph(self):
        networkx.draw(self.graph, with_labels=True)
        pyplot.show(block=True)
