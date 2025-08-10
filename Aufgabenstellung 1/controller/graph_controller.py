from graph.graph import Graph

class GraphController:
    def __init__(self, graph):
        self._graph = Graph(graph)
        self._running = True
        self._actions = {
            "1": self.add_vertex,
            "2": self.remove_vertex,
            "3": self.add_edge,
            "4": self.remove_edge,
            "5": self.check_path,
            "6": self.draw_graph,
            "0": self.exit_program,
        }

    def run(self):
        while self._running:
            self.print_menu()
            choice = input("Ihre Wahl: ").strip()
            action = self._actions.get(choice)
            if action:
                action()
            else:
                print("Ungültige Auswahl. Bitte erneut versuchen.")

    def print_menu(self):
        print("\n--- Menü ---")
        print("1: Knoten hinzufügen")
        print("2: Knoten entfernen")
        print("3: Kante hinzufügen")
        print("4: Kante entfernen")
        print("5: Pfadprüfung")
        print("6: Graph anzeigen")
        print("0: Beenden")

    def read_int(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Ungültige Eingabe. Bitte eine Zahl eingeben.")

    def add_vertex(self):
        self._graph.add_vertex()
        print(f"Neuer Knoten wurde hinzugefügt.")

    def remove_vertex(self):
        vertex_number = self.read_int("Knotennummer: ")
        if self._graph.remove_vertex(vertex_number):
            print(f"Knoten {vertex_number} entfernt.")
        else:
            print("Fehlgeschlagen: Knoten existiert nicht")

    def add_edge(self):
        number_vertex_one = self.read_int("Von Knoten: ")
        number_vertex_two = self.read_int("Zu Knoten: ")
        if self._graph.add_edge(number_vertex_one, number_vertex_two):
            print(f"Kante {number_vertex_one} - {number_vertex_two} hinzugefügt.")
        else:
            print("Fehlgeschlagen: Knoten nicht gefunden.")

    def remove_edge(self):
        number_vertex_one = self.read_int("Von Knoten: ")
        number_vertex_two = self.read_int("Zu Knoten: ")
        if self._graph.remove_edge(number_vertex_one, number_vertex_two):
            print(f"Kante {number_vertex_one} - {number_vertex_two} entfernt.")
        else:
            print("Fehlgeschlagen: Knoten nicht gefunden")

    def check_path(self):
        vertex_start = self.read_int("Startknoten: ")
        vertex_to_find = self.read_int("Zielknoten: ")
        if self._graph.exist_path(vertex_start, vertex_to_find):
            print(f"Es gibt einen Pfad von {vertex_start} nach {vertex_to_find}.")
        else:
            print(f"Kein Pfad von {vertex_start} nach {vertex_to_find} gefunden.")

    def draw_graph(self):
        print("Aktueller Graph:")
        self._graph.draw()

    def exit_program(self):
        print("Programm beendet.")
        self._running = False
