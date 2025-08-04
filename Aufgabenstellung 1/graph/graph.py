import networkx
import matplotlib.pyplot as pyplot


class Graph:
    def __init__(self, adjacency_info=None):
        if adjacency_info is not None:
            self._adjacency_info = adjacency_info.get_adjacency_info()
            self._update_graph()

    def _update_graph(self):
        self.graph = networkx.Graph()

        for index, items in self._adjacency_info.items():
            self.graph.add_node(index)
            for item in items:
                if index <= item:
                    self.graph.add_edge(index, item)

    def draw_graph(self):
        networkx.draw(self.graph, with_labels=True)
        pyplot.show(block=True)
