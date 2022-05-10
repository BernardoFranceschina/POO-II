class Imovel:
    def __init__(self, endereco, preco):
        self.__endereco = endereco
        self.__preco = preco

    def get_endereco(self):
        return self.__endereco

    def get_preco(self):
        return self.__preco

class Novo(Imovel):
    def __init__(self, endereco, preco, valorAdicional):
        super().__init__(endereco, preco)
        self.__valorAdicional = valorAdicional

    def imprimeValor(self):
        print('\nValor adicional: ', self.__valorAdicional)
        print('Valor total: ', self.get_preco() + self.__valorAdicional)

class Velho(Imovel):
    def __init__(self, endereco, preco):
        super().__init__(endereco, preco)
        self.__desconto = 0.85

    def imprimeValor(self):
        print('\nPreço inicial: ', self.get_preco())
        print('Preço final: ', self.get_preco()*self.__desconto)

novo = Novo('Floripa', 1000, 500)
novo.imprimeValor()
velho = Velho('Floripa2', 1000)
velho.imprimeValor()