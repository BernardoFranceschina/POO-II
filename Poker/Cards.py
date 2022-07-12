class Cards:
    cartasNumeros = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    cartasNaipes = ['O', 'P', 'C', 'E']

    def __init__(self, numero, naipe):
        self._naipe = naipe
        self._numero = numero

    def getNaipe(self):
        return self._naipe

    def getNumero(self):
        if self._numero == 'J':
            return '11'
        if self._numero == 'Q':
            return '12'
        if self._numero == 'K':
            return '13'
        if self._numero == 'A':
            return '14'
        return self._numero

    def getCartas(self):
        return self._numero + self._naipe
