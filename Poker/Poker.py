import more_itertools as mit


def checkio(data):
    for index in range(len(data) - 1, -1, -1):
        if data.count(data[index]) == 1:
            del data[index]
    return data


class Poker:
    def ganhador(self, hand, table, jogador):
        cards = hand + table

        for i in range(len(cards)):
            cards[i] = int(cards[i].getNumero())

        # print(cards, 'todas as cardas ')
        # print(list(dict.fromkeys(cards)), 'unicos', len(list(dict.fromkeys(cards))))
        # print(checkio(cards), 'dupes', len(checkio(cards)))
        # print(list(dict.fromkeys(checkio(cards))), 'pares', len(list(dict.fromkeys(checkio(cards)))))
        combo = 'High Card'
        pontos = self.highCard(hand)
        if self.royalFlush(cards, (hand + table)):
            combo = 'Royal Flush'
            pontos = pontos + 900
        elif self.straightFlush(cards, (hand + table)):
            combo = 'Straight Flush'
            pontos = pontos + 800
        elif self.fourOfAKind(cards.copy()):
            combo = 'Four of a Kind'
            pontos = pontos + 700
        elif self.fullHouse(cards.copy()):
            combo = 'Full House'
            pontos = pontos + 600
        elif self.flush((hand + table)):
            combo = 'Flush'
            pontos = pontos + 500
        elif self.straight(cards.copy()):
            combo = 'Straight'
            pontos = pontos + 400
        elif self.threeOfAKind(cards.copy()):
            combo = 'Three of a Kind'
            pontos = pontos + 300
        elif self.twoPair(cards.copy()):
            combo = 'Two Pair'
            pontos = pontos + 200
        elif self.onePair(cards.copy()):
            combo = 'One Pair'
            pontos = pontos + 100

        print(f'Jogador {jogador}: {combo}')
        return pontos

    def highCard(self, hand, second=False):
        if second:
            pontos = 0
            for i in hand:
                pontos = pontos + int(i.getNumero())
            return pontos
        else:
            pontos = []
            for i in hand:
                pontos.append(int(i.getNumero()))
            return max(pontos)

    def onePair(self, cards):
        if len(list(dict.fromkeys(checkio(cards)))) == 1:
            return True
        return False

    def twoPair(self, cards):
        if len(list(dict.fromkeys(checkio(cards)))) >= 2:
            return True
        return False

    def threeOfAKind(self, cards):
        three = {}
        for i in checkio(cards):
            three[i] = checkio(cards).count(i)
        for i in three:
            if three[i] == 3:
                return True
        return False

    def straight(self, cards, royal=False):
        for i in [list(group) for group in mit.consecutive_groups(sorted(cards))]:
            if royal:
                if len(i) >= 5 and min(i) == 10 and max(i) == 14:
                    return True
            else:
                if len(i) >= 5:
                    return True
        return False

    def flush(self, cards):
        for i in range(len(cards)):
            cards[i] = cards[i].getNaipe()
        flush = {}
        for i in checkio(cards):
            flush[i] = checkio(cards).count(i)
        for i in flush:
            if flush[i] == 5:
                return True
        return False

    def fullHouse(self, cards):
        if self.threeOfAKind(cards) and self.twoPair(cards):
            return True
        return False

    def fourOfAKind(self, cards):
        four = {}
        for i in checkio(cards):
            four[i] = checkio(cards).count(i)
        for i in four:
            if four[i] == 4:
                return True
        return False

    def straightFlush(self, cards, flushCards):
        if self.straight(cards, True) and self.flush(flushCards):
            return True
        return False

    def royalFlush(self, cards, flushCards):
        if self.straight(cards, True) and self.flush(flushCards):
            return True
        return False
