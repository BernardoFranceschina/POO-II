import random
from Cards import *

class Deck:
    def __init__(self):
        self._deck = []
        for numero in Cards.cartasNumeros:
            for naipe in Cards.cartasNaipes:
                self._deck.append(Cards(numero, naipe))

    def embaralhar(self):
        random.shuffle(self._deck)
        return self._deck