from random import shuffle
from PIL import Image

__author__ = "Zodis"
__version__ = "0.1"

clubs = "\u2663"
diamonds = "\u2666"
hearts = "\u2665"
spades = "\u2660"
suitsSymbols = {
    "clubs": clubs,
    "diamonds": diamonds,
    "hearts": hearts,
    "spades": spades
}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.image = Image.open(f"./images/{rank}{suit}.png")

    def __repr__(self):
        return f"{self.rank} di {suitsSymbols[self.suit]}"

    @classmethod
    def from_tuple(cls, card):
        (suit, rank) = card
        return cls(suit, rank)


class Deck:
    def __init__(self, numberOfDecks):
        self.numberOfDecks = numberOfDecks

        self.suits = ["clubs", "diamonds", "hearts", "spades"]

        self.ranks = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K"]
        self.deck = list(map(Card.from_tuple, ([
                         (suit, rank) for suit in self.suits for rank in self.ranks] * self.numberOfDecks)))

    def __repr__(self):
        return f"{self.deck}"

    def shuffleDeck(self):
        shuffle(self.deck)

    def drawCard(self):
        return self.deck.pop(0)

    def renew(self):
        print("\nmescolando il mazzo")
        del self.deck
        self.deck = list(map(Card.from_tuple, ([
                         (suit, rank) for suit in self.suits for rank in self.ranks] * self.numberOfDecks)))
        self.shuffleDeck()
