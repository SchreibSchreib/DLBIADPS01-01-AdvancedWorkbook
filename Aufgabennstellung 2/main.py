from tiere.hund import Hund
from tiere.katze import Katze
from tiere.vogel import Vogel

hund = Hund("Bello", 5, "12 kg", "ABC123", "Wuff Wuff", "8:00")
katze = Katze("Tinka", 7, "5 kg", "DEF456", "Miau", "Spielzeugmaus")
vogel = Vogel("Fridolin", 2, "32 g", "GHI789", "Chirp Chirp", 25)
tierliste = [hund, katze, vogel]
print()

for tier in tierliste:
    tier.geraeusch_machen()
    tier.aktivität()
    print()