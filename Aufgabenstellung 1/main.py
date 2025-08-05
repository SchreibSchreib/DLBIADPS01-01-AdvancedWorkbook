from adjacency.adjacency_list import AdjacencyList
from adjacency.adjacency_matrix import AdjacencyMatrix
from graph.graph import Graph

test = AdjacencyList(filepath="Aufgabenstellung 1\graph_data.txt")
test2 = AdjacencyMatrix(filepath="Aufgabenstellung 1\graph_data.txt")
test_graph = Graph(test)
test_graph.draw_graph()