from Deck import *
from Jogador import *

jogadores = []
jogadorSmall = 1
jogadorBig = 2
smallBet = 5
minimalBet = 10

deck = Deck()
deckEmbaralhado = deck.embaralhar()
cartasMesa = []


def menu(jogador, rodada):
    opcaoLim = 5
    opcaoStr =

    opcao = 0
    while opcao < 1 or opcao > opcaoLim:
        opcao = int(input(opcaoStr))

    return opcao

def bet():
    for rodada in range(1, 4):
        for jogador in jogadores:
            print('Rodada ', rodada, '- Vez do jogador numero', jogador.getNumeroJogador())
            opcao = menu(jogador.getNumeroJogador(), rodada)

        cartasMesa.append(deckEmbaralhado.pop())
        print(cartasMesa)


def validaJogadoresComFicha():
    for jogador in jogadores:
        if jogador.getFichas() < minimalBet:
            print('Jogador ', jogador.getNumeroJogador(), 'não possui fichas suficientes para continuar jogando!')
            # jogadores[jogador.getNumeroJogador()-1] = None


def play():
    validaJogadoresComFicha()
    distribuiCartas()
    bet()


def distribuiCartas():
    global deckEmbaralhado
    for jogador in jogadores:
        cartasDoJogador = deckEmbaralhado[:2]
        deckEmbaralhado = deckEmbaralhado[2:]
        jogador.setCartas(cartasDoJogador)


def main():
    jogadoresNum = 0
    while jogadoresNum < 2 or jogadoresNum > 8:
        jogadoresNum = int(input('Insira o numero de jogadores 2 a 8\n'))
    for jogador in range(jogadoresNum):
        jogadores.append(Jogador(jogador + 1))

    play()


if __name__ == '__main__':
    main()
