from Cards import *

class Poker:
    def highCard(self, hand):
        pontos = []
        for i in hand:
            pontos.append(Cards.cartasNumeros.index(i.getNumero()))
        return max(pontos)

    def onePair(self, hand, table):
        cards = hand + table
        print(cards)

    def twoPair(self):
        # 2 pares
        return 3

    def threeOfAKind(self):
        # 3 cartas iguais
        return 4

    def straight(self):
        # 5 cartas em sequencia
        return 5

    def flush(self):
        # 5 cartas com a msm naipe
        return 6

    def fullHouse(self):
        # 3 cartas iguais + 1 par
        return 7

    def fourOfAKind(self):
        # 4 cartas iguais
        return 8

    def straightFlush(self):
        # 5 cartas em sequencia da msm naipe
        return 9

    def royalFlush(self):
        # A-K-Q-J-10 da msm naipe
        return 10
