import math


class Quadrado:
    def __init__(self, lado):
        self.__lado = lado

    def getLado(self):
        return self.__lado


class Retangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def getBase(self):
        return self.__base

    def getAltura(self):
        return self.__altura


class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    def getRaio(self):
        return self.__raio


# class Quadrilatero:
#     def __init__(self):

def main():
    formas = []
    qntFormas = int(input('Quantas formas deseja criar?'))
    for i in range(qntFormas):
        print('\nRestam criar', qntFormas - i, 'formas geométricas\n')
        forma = int(input('Qual forma deseja criar?\n1 - Quadrado\n2 - Retângulo\n3 - Círculo'))
        if (forma == 1):
            lado = float(input('Informe o tamanho do lado do quadrado'))
            formas.append(Quadrado(lado))
        elif (forma == 2):
            base = float(input('Informe o tamanho da base do retangulo'))
            altura = float(input('Informe o tamanho da altura do retangulo'))
            formas.append(Retangulo(base, altura))
        elif (forma == 3):
            raio = float(input('Informe o raio do circulo'))
            formas.append(Circulo(raio))
        else:
            print('Forma inválida')

    for forma in formas:
        if(hasattr(forma, '_Quadrado__lado')):
            print('\nLados do quadrado:', forma.getLado(), '\nPerimetro:', forma.getLado()*4, '\nArea:', forma.getLado()*forma.getLado())
        elif(hasattr(forma, '_Circulo__raio')):
            print('\nRaio do circulo:', forma.getRaio(), '\nPerimetro:', forma.getRaio() * (math.pi * 2), '\nArea:', math.pi * (forma.getRaio()*forma.getRaio()))
        else:
            print('\nBase:', forma.getBase(), '\nAltura:',  forma.getAltura(), '\nPerimetro:', 2*(forma.getBase()+forma.getAltura()), '\nArea:', forma.getBase()*forma.getAltura())




main()