from abc import ABC, abstractmethod


class Tier(ABC):
    def __init__(self, name, alter, gewicht, mikrochip_id, geraeusch):
        self.name = name
        self.alter = alter
        self.gewicht = gewicht
        self.mikrochip_id = mikrochip_id
        self.geraeusch = geraeusch

    @abstractmethod
    def geraeusch_machen(self):
        pass

    @abstractmethod
    def aktivität(self):
        pass