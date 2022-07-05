from Deck import *
from Jogador import *

jogadores = []
jogadorSmall = 1
jogadorBig = 2
smallBet = 5
minimalBet = (smallBet * 2)
# rodada = 1

deck = Deck()
apostas = []


def bet():
    for rodada in range(1, 3):
        for jogador in jogadores:
            while 
            print('Rodada ', rodada, '- Vez do jogador numero', jogador.getNumeroJogador())
            opcaoStr = ''
            if rodada == 1:
                if jogador.getNumeroJogador() == jogadorSmall:
                    opcaoStr = '1) Fazer SMALL BET'
                if jogador.getNumeroJogador() == jogadorBig:
                    opcaoStr = '1) Fazer BIG BET'
            opcao = int(input(opcaoStr))

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
    deckEmbaralhado = deck.embaralhar()
    for jogador in jogadores:
        cartasDoJogador = deckEmbaralhado[:2]
        deckEmbaralhado = deckEmbaralhado[2:]
        jogador.setCartas(cartasDoJogador)


def main():
    jogadoresNum = int(input('Insira o numero de jogadores 2 a 8'))
    for jogador in range(jogadoresNum):
        jogadores.append(Jogador(jogador + 1))

    play()


if __name__ == '__main__':
    main()
