class Jogador:
    def __init__(self, numeroJogador):
        self._numeroJogador = numeroJogador
        self._deck = []
        self._fichas = 1000
        self._qntApostada = 0

    def setQntApostada(self, qntApostada):
        self._qntApostada = qntApostada

    def getQntApostada(self):
        return self._qntApostada

    def setFichas(self, fichas):
        self._fichas = fichas

    def getFichas(self):
        return self._fichas

    def setCartas(self, deck):
        self._deck = deck

    def getCartas(self):
        return self._deck

    def getNumeroJogador(self):
        return self._numeroJogador
