import random

class Deck:
    cartasNumeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cartasNaipes = ['O', 'P', 'C', 'E']

    def __init__(self):
        self._deck = []
        for numero in self.cartasNumeros:
            for naipe in self.cartasNaipes:
                self._deck.append(numero+naipe)

    def embaralharDeck(self):
        random.shuffle(self._deck)
        return self._deck
