__author__ = "Zodis"
__version__ = "0.1"

values = {
    "A": 0,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10}


def calculateHand(player):
    player.scores = []
    player.blackjack = False
    if isinstance(player.hand[0], list):
        for group in player.hand:
            _calculateHand(player, group)
    else:
        if not checkBlackjack(player):
            _calculateHand(player, player.hand)
    player.score = list(map(lambda s: max(s) if max(s) <= 21 else min(s), player.scores))[0]


def _calculateHand(player, handList):
    value1 = value2 = 0
    aceFound = False
    for card in handList:
        if card.rank != "A":
            value1 += values[card.rank]
            value2 += values[card.rank]
        else:
            if not aceFound:
                value1 += 1
                value2 += 11
                aceFound = True
            else:
                value3 = value2
                value1 += 1
                value2 += 1
                value3 += 11
                value2 = value3 if value3 <= 21 else value2

    if value1 == value2:
        player.scores.append([value1])
    else:
        player.scores.append([value1, value2])


def checkBlackjack(player):
    if (((player.hand[0].rank == "A" and values[player.hand[1].rank] == 10) or (
            player.hand[1].rank == "A" and values[player.hand[0].rank] == 10)) and len(player.hand) == 2):
        player.blackjack = True
        return True


def checkScore(player):
    player.score = calculateHand(player)[0]
    return (player.score < 21)


'''
def score_hand(a):
    n = sum(11 if x == "A" else 10 if x in "JQK" else int(x) for x in a)
    for _ in range(a.count("A")):
        if n > 21:
            n -= 10
    return n
'''