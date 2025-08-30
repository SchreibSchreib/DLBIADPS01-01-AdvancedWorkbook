from tiere.abstrakt.tier import Tier


class Hund(Tier):
    def __init__(self, name, alter, gewicht, mikrochip_id, geraeusch, gassi_gehen_zeit):
        super().__init__(name, alter, gewicht, mikrochip_id, geraeusch)
        self._gassi_gehen_zeit = gassi_gehen_zeit
    
    def bellen(self):
        print(f"{self.name} bellt: {self.geraeusch}!")

    def gassi_gehen(self):
        print(f"{self.name} muss spätestens um {self._gassi_gehen_zeit} Gassi gehen.")

    