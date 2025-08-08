from tiere.abstrakt.tier import Tier


class Katze(Tier):
    def __init__(self, name, alter, gewicht, mikrochip_id, geraeusch, lieblingsspielzeug):
        super().__init__(name, alter, gewicht, mikrochip_id, geraeusch)
        self.lieblingsspielzeug = lieblingsspielzeug
    
    def geraeusch_machen(self):
        print(f"{self.name} miaut: {self.geraeusch}!")

    def aktivität(self):
        print(f"{self.name} klettert zu ihrem Lieblingsspielzeug ({self.lieblingsspielzeug}).")