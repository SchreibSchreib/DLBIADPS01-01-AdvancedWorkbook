from tkinter import N
from graph.utility.graph_edge_generator import GraphEdgeGenerator
from adjacency.adjacency_matrix import AdjacencyMatrix
from adjacency.adjacency_list import AdjacencyList
from controller.graph_controller import GraphController


print("Willkommen zum Graph-Programm!")
print("==============================")

while True:
    start_option = input("Möchten Sie einen zufälligen Graphen erstellen? (j/n): ").strip().lower()
    if start_option in ("j", "n"):
        break
    print("Bitte 'j' oder 'n' eingeben.")

if start_option == "j":
    while True:
        try:
            num_vertices = int(input("Anzahl der Knoten: "))
            num_edges = int(input("Anzahl der Kanten (Maximum = Knoten * (Knoten - 1) / 2): "))
            if num_vertices or num_edges > 0:
                break
            else:
                print("Bitte eine positive Zahl eingeben.")
        except ValueError:
            print("Ungültige Eingabe.")

    random_graph_data = GraphEdgeGenerator(num_vertices, num_edges)
    print(f"Zufälliger Graph mit {num_vertices} Knoten und {num_edges} Kanten erstellt.")

    while True:
        adjacency_option = input("Möchten Sie den Graphen mittels einer Adjazensmatrix oder einer Adjezenzliste verarbeiten? (M)atrix/(L)iste").strip().lower()
        if adjacency_option == "m":
            adjacency_object = AdjacencyMatrix(random_graph_data)
            break
        elif adjacency_option == "l":
            adjacency_object = AdjacencyList(random_graph_data)
            break
        else:
            print("Ungültige Eingabe.")
else:
    while True:
        adjacency_option = input("Möchten Sie den Graphen mittels einer Adjazensmatrix oder einer Adjezenzliste verarbeiten? (M)atrix/(L)iste").strip().lower()
        if adjacency_option == "m":
            adjacency_object = AdjacencyMatrix()
            break
        elif adjacency_option == "l":
            adjacency_object = AdjacencyList()
            break
        else:
            print("Ungültige Eingabe.")

GraphController(adjacency_object).run()
        

    

    
