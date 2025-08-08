from tiere.abstrakt.tier import Tier


class Vogel(Tier):
    def __init__(self, name, alter, gewicht, mikrochip_id, geraeusch, flügelspannweite):
        super().__init__(name, alter, gewicht, mikrochip_id, geraeusch)
        self.flügelspannweite = flügelspannweite
    
    def geraeusch_machen(self):
        print(f"{self.name} zwitschert: {self.geraeusch}!")

    def aktivität(self):
        print(f"{self.name} fliegt. Seine Flügelspannweite beträgt {self.flügelspannweite}cm.")