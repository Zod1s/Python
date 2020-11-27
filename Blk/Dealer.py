from Deck import *
from Score import *

__author__ = "Zodis"
__version__ = "0.1"


class Dealer:
    def __init__(self, deck, listOfPlayers):
        self.deck = deck
        self.listOfPlayers = listOfPlayers
        self.hand = []
        self.scores = []
        self.blackjack = False
        self.score = 0

    def __repr__(self):
        return f"mano mazziere: {self.hand}"

    def distribute(self):
        self.hand = []
        self.blackjack = False
        self.score = 0
        for player in self.listOfPlayers:
            player.hand = []
            player.score = 0
            player.blackjack = False
        for _ in range(2):
            for player in self.listOfPlayers:
                if player.betted:
                    player.hand.append(self.deck.drawCard())
            self.hand.append(self.deck.drawCard())
        for player in self.listOfPlayers:
            print(player)
            checkBlackjack(player)
        if self.hand[0].rank == "A":
            checkBlackjack(self)

    def selectAction(self, player):
        done = False
        while not done:
            action = input(f"\n{player}, cosa fare? ([C]arta) - ([S]tare): ")
            if action.lower() == "c":
                player.hand.append(self.deck.drawCard())
                done = not checkScore(player)
            elif action.lower() == "s":
                calculateHand(player)
                done = True

    def selfDeal(self):
        print(f"mano mazziere: {self.hand}")
        while not self.blackjack and self._checkScore():
            self.hand.append(self.deck.drawCard())
            print(f"mano mazziere: {self.hand}")
        calculateHand(self)
        print(f"punteggio mazziere: {self.score}")

    def _checkScore(self):
        self.scores = []
        calculateHand(self)
        return (self.score < 17)

    def playersBet(self):
        bet = False
        for player in self.listOfPlayers:
            if player.betted:
                bet = True

        return bet
