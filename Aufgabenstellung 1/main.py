from adjacency.adjacency_list import AdjacencyList
from adjacency.adjacency_matrix import AdjacencyMatrix
from graph.utility.graph_edge_generator import GraphEdgeGenerator
from graph.graph import Graph

test = AdjacencyList(GraphEdgeGenerator(10,10))
test2 = AdjacencyMatrix(GraphEdgeGenerator(10,10))
test_graph = Graph(test)
test_graph2 = Graph(test2)
test_graph.draw_graph()
test_graph2.draw_graph()