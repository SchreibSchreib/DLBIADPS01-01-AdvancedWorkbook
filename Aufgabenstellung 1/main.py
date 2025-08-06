from adjacency.adjacency_list import AdjacencyList
from adjacency.adjacency_matrix import AdjacencyMatrix
from graph.utility.graph_edge_generator import GraphEdgeGenerator
from graph.graph import Graph

test = AdjacencyList(GraphEdgeGenerator(10,100).output)
test2 = AdjacencyMatrix(GraphEdgeGenerator(100,10).output)
test_graph = Graph(test)
test_graph2 = Graph(test2)
test_graph.draw_graph()
test_graph2.draw_graph()