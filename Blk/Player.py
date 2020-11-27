__author__ = "Zodis"
__version__ = "0.1"


class Player:
    def __init__(self, name, wallet):
        self.hand = []
        self.scores = []
        self.score = 0
        self.bet = 0
        self.wallet = wallet
        self.name = name
        self.betted = False
        self.blackjack = False

    def __repr__(self):
        return f"{self.name} (portafoglio: {self.wallet}, mano: {self.hand})"

    def gamble(self, minimumBet):
        self.bet = 0
        self.betted = False
        while not self.betted:
            self.bet = int(input(
                f"\n{self.name}, portafoglio: {self.wallet}, puntata minima: {minimumBet}, puntata: "))
            if self.bet == -1:
                return
            elif self.bet >= minimumBet:
                if self.bet <= self.wallet:
                    self.wallet -= self.bet
                    print("\npuntata accolta")
                    self.betted = True
                else:
                    print("\npuntata troppo alta")
                    self.bet = 0
            else:
                print("puntata troppo bassa")
