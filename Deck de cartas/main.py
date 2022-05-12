import random
from Jogador import Jogador

def main():
    cartasNumeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cartasNaipes = ['O', 'P', 'C', 'E']

    # Junta os arrays com naipes e numero para formas as cartas
    cartas = []
    for numero in cartasNumeros:
        for naipe in cartasNaipes:
            cartas.append(numero + naipe)

    # Embaralha o deck de cartas
    random.shuffle(cartas)
    cartasEmbaralhadas = cartas
    qntCartas = len(cartasEmbaralhadas)

    jogadoresNum = int(input('Insira o numero de jogadores'))
    cartasPorJogador = int((qntCartas / jogadoresNum))
    cartasQueSobraram = qntCartas - (int(cartasPorJogador) * jogadoresNum)

    # Cria os jogadores
    jogadores = []
    for jogador in range(jogadoresNum):
        cartasDoJogador = cartasEmbaralhadas[:cartasPorJogador]
        cartasEmbaralhadas = cartasEmbaralhadas[cartasPorJogador:]
        jogadores.append(Jogador(cartasDoJogador, jogador+1))

    for jogador in jogadores:
        print('Jogador', jogador.getNumeroJogador(), 'possui as cartas:', jogador.getCartas())

    print('Cartas que sobraram:', cartasQueSobraram, cartasEmbaralhadas)

main()