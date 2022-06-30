from Deck import *
from Jogador import *

jogadores = []
jogadorSmall = 0
jogadorBig = 1
minimalBet = 5

deck = Deck()


def play():
    deckEmbaralhado = deck.embaralharDeck()
    smallbet = int(input('Small bet'))
    bigbet = int(input('Big bet'))
    apostas = [
        {jogadores[jogadorSmall].getNumeroJogador(): smallbet},
        {jogadores[jogadorBig].getNumeroJogador(): bigbet},
    ]
    print(apostas)


def main():
    jogadoresNum = int(input('Insira o numero de jogadores 2 a 8'))
    for jogador in range(jogadoresNum):
        jogadores.append(Jogador(jogador + 1))

    play()


if __name__ == '__main__':
    main()
