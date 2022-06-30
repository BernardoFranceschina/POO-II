class Jogador:
    def __init__(self, numeroJogador):
        self._numeroJogador = numeroJogador
        self._deck = []
        self._carteira = 5000

    def setValor(self, carteira):
        self._carteira = carteira

    def setCartas(self, deck):
        self._deck = deck

    def getCartas(self):
        return self._deck

    def getNumeroJogador(self):
        return self._numeroJogador
