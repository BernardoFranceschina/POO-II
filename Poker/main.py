from Deck import *
from Jogador import *
from Poker import *

jogadores = []
minimalBet = 10

deck = Deck()
poker = Poker()
deckEmbaralhado = deck.embaralhar()
cartasMesa = []


def rodadas():
    for rodada in range(1, 5):
        for jogador in jogadores:
            print('\n\nRodada ', rodada, '- Vez do jogador numero', jogador.getNumeroJogador())
            print('Cartas:', jogador.printCartas())
            if rodada >= 4:
                print(poker.onePair(jogador.getCartas(), cartasMesa))

        if rodada < 4:
            cartasMesa.append(deckEmbaralhado.pop())
        print('\n'*8)
        print('Cartas da mesa:')
        for i in cartasMesa:
            print(i.getCartas(), end=' ')

    print('\n\nFim das rodadas')

    print('Vencedor:')

def validaJogadoresComFicha():
    for jogador in jogadores:
        if jogador.getFichas() < minimalBet:
            print('Jogador ', jogador.getNumeroJogador(), 'não possui fichas suficientes para continuar jogando!')
            # jogadores[jogador.getNumeroJogador()-1] = None


def iniciaJogo():
    validaJogadoresComFicha()
    distribuiCartas()
    rodadas()


def distribuiCartas():
    cartasMesa = []
    deckEmbaralhado = deck.embaralhar()
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

    iniciaJogo()


if __name__ == '__main__':
    main()