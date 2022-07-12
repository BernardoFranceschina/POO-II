from Deck import *
from Jogador import *
from Poker import *

jogadores = []
minimalBet = 10
deck = Deck()
poker = Poker()
deckEmbaralhado = deck.embaralhar()
apostaDaRodada = []


def ganhador(pot, cartasMesa):
    pontos = []
    for jogador in jogadores:
        if jogador.getFichas() >= minimalBet:
            pontos.append(poker.ganhador(jogador.getCartas(), cartasMesa, jogador.getNumeroJogador()))
        else:
            pontos.append(-1)

    maiorPonto = max(pontos)
    disclaimer = checkio(pontos.copy())
    if maiorPonto in disclaimer:
        print('Conflito de pontos na vitória:', maiorPonto)
    print('\nVencedor:')
    print('Jogador', pontos.index(maiorPonto) + 1)
    for jogador in jogadores:
        if jogador.getNumeroJogador() == pontos.index(maiorPonto) + 1:
            jogador.setFichas(jogador.getFichas() + pot)
        jogador.setQntApostada(0)

    opcao = int(input('\n1) Ver pontuação\n2) Continuar jogo\n3) Parar de jogar'))
    if opcao == 1:
        pontuacao()
        iniciaJogo()
    elif opcao == 2:
        iniciaJogo()
    else:
        exit(1)


def pontuacao():
    for jogador in jogadores:
        print('\nJogador', jogador.getNumeroJogador(), jogador.getFichas())

def rodadas():
    pot = 0
    cartasMesa = []
    for rodada in range(1, 5):
        for jogador in jogadores:
            if jogador.getFichas() >= minimalBet:
                print('\n\nRodada ', rodada, '- Vez do jogador numero', jogador.getNumeroJogador())
                print('Cartas:',' '.join(jogador.printCartas()))
                aposta = int(input('\nFaça sua aposta\n'))
                apostaDaRodada.append(aposta)
                jogador.setQntApostada(aposta)
                pot = pot + aposta
                print('\n' * 10)
                print(f'Pot {pot}')

        if rodada == 1:
            for i in range(3):
                cartasMesa.append(deckEmbaralhado.pop())
        elif rodada < 4:
            cartasMesa.append(deckEmbaralhado.pop())
        print('\nCartas da mesa:')
        for i in cartasMesa:
            print(i.getCartas(), end=' ')

    print('\n\nFim das rodadas')

    ganhador(pot, cartasMesa)


def validaJogadoresComFicha():
    for jogador in jogadores:
        if jogador.getFichas() < minimalBet:
            print('Jogador ', jogador.getNumeroJogador(), 'não possui fichas suficientes para continuar jogando!')


def iniciaJogo():
    validaJogadoresComFicha()
    distribuiCartas()
    rodadas()


def distribuiCartas():
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
