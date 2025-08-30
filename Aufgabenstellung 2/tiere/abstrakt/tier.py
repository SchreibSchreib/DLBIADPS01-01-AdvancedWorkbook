from abc import ABC


class Tier(ABC):
    def __init__(self, name, alter, gewicht, mikrochip_id, geraeusch):
        self.name = name
        self.alter = alter
        self.gewicht = gewicht
        self.mikrochip_id = mikrochip_id
        self.geraeusch = geraeusch
