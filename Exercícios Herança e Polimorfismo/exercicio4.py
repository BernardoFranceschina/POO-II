from exercicio1 import Administrativo, Tecnico
from exercicio2 import *
from exercicio3 import *

def criaIngresso():
    tipoIngresso = input('\n\nQual ingresso deseja comprar?\n1 - Normal\n2 - VIP\n')
    if (tipoIngresso == '1'):
        ingressoNormal = Normal(20)
        ingressoNormal.imprimeValor()
    elif (tipoIngresso == '2'):
        camarote = input('\n1 - Camarote superior\n2 - Camarote inferior\n')
        if (camarote == '1'):
            camarotecuperior = CamaroteSuperior(20, 10, 10)
            camarotecuperior.imprimeValor()
        elif (camarote == '2'):
            camaroteinferior = CamaroteInferior(20, 10, 'Floripa')
            camaroteinferior.imprimeValor()

def criaImovel():
    tipoImovel = input('Qual tipo de imovel deseja comprar?\n1 - Novo\n2 - Velho')
    if (tipoImovel == '1'):
        novo = Novo('Floripa', 1000, 500)
        novo.imprimeValor()
    elif (tipoImovel == '2'):
        velho = Velho('Floripa2', 1000)
        velho.imprimeValor()

class Teste:
    def main():
        tecnico = Tecnico('Bruno', 1300, 20178080, 500)
        print('Nome:', tecnico.get_nome(), 'Matricula:', tecnico.get_matricula())
        administrativo = Administrativo('Gabriela', 4000, 508080, 'Dia')
        print('Nome:', administrativo.get_nome(), 'Matricula:', administrativo.get_matricula())

        criaIngresso()

        criaImovel()

Teste.main()