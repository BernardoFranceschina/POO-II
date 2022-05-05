class Ingresso:
    def __init__(self, valor):
        self.__valor = valor

    def get_valor(self):
        return self.__valor

    def imprimeValor(self):
        print('\nValor ingresso: ', self.__valor)


class Vip(Ingresso):
    def __init__(self, valor, valorAdicional):
        super().__init__(valor)
        self.__valorAdicional = valorAdicional

    def get_valor_adicional(self):
        return self.__valorAdicional

    def imprimeValor(self):
        print('\nValor VIP: ', self.get_valor() + self.get_valor_adicional())


class Normal(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def imprimeValor(self):
        print('\nValor ingresso normal - ', self.get_valor())


class CamaroteInferior(Vip):
    def __init__(self, valor, valorAdicional, localizacao):
        super().__init__(valor, valorAdicional)
        self.__localizacao = localizacao

    def imprimeLocalizacao(self):
        print('\nLocalização: ', self.__localizacao)


class CamaroteSuperior(Vip):
    def __init__(self, valor, valorAdicional, valorAdicionalCamarote):
        super().__init__(valor, valorAdicional)
        self.__valorAdicionalCamarote = valorAdicionalCamarote

    def imprimeValor(self):
        print('\nValor camarote: ', self.get_valor() + self.get_valor_adicional() + self.__valorAdicionalCamarote)


ingresso = Ingresso(20)
ingresso.imprimeValor()
vip = Vip(20, 5)
vip.imprimeValor()
normal = Normal(20)
normal.imprimeValor()
camaroteInferior = CamaroteInferior(20, 30, 'H3')
camaroteInferior.imprimeLocalizacao()
camaroteSuperior = CamaroteSuperior(20, 5, 5)
camaroteSuperior.imprimeValor()