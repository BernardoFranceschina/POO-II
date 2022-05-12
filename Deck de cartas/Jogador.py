class Jogador:
    def __init__(self, deck, numeroJogador):
        self.__deck = deck
        self.__numeroJogador = numeroJogador

    def getCartas(self):
        return self.__deck

    def getNumeroJogador(self):
        return self.__numeroJogador
