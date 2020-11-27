from time import sleep

from Dealer import Dealer
from Deck import Card, Deck
from Player import Player
from Score import *


__author__ = "Zodis"
__version__ = "0.1"


def checkHands(dealer):
    if not dealer.blackjack:
        for player in dealer.listOfPlayers:
            if player.betted:
                if player.blackjack:
                    # print(f"\n{player.name} ha fatto blackjack")
                    player.wallet += (5 / 2) * player.bet
                elif player.score <= 21:
                    if dealer.score > 21 or player.score > dealer.score:
                        print(f"\n{player.name} ha vinto")
                        player.wallet += 2 * player.bet
                    elif player.score == dealer.score:
                        print(f"\n{player.name} ha pareggiato")
                        player.wallet += player.bet
                    else:
                        print(f"\n{player.name} ha perso")
                elif player.score > 21:
                    print(f"\n{player.name} ha sballato")
    else:
        print("\nil mazziere ha fatto blackjack")


def askInt(quest):
    done = False
    while not done:
        n = input(quest)
        try:
            n = int(n)
            done = True
        except:
            print(f"\n{n} non è un numero")
    return n


def main():
    finished = False
    numberOfDecks = 6

    numberOfPlayers = askInt("\nNumero di giocatori: ")
    
    listOfPlayers = []
    for _ in range(numberOfPlayers):
        name = input("\nNome giocatore: ")
        wallet = askInt("\nQuanto ha?: ")
        listOfPlayers.append(Player(name, wallet))

    minimumBet = askInt("\nPuntata minima: ")

    deck = Deck(numberOfDecks)

    dealer = Dealer(deck, listOfPlayers)
    dealer.deck.shuffleDeck()

    while not finished:
        action = input("\nCosa fare? ([G]iocare) - ([U]scire): ")
        if action.upper() == "U":
            finished = True
        elif action.upper() == "G":
            if (len(dealer.deck.deck) < dealer.deck.numberOfDecks * 26):
                print("\nrimescolamento del mazzo")
                dealer.deck.renew()

            for player in dealer.listOfPlayers:
                if player.wallet < minimumBet:
                    dealer.listOfPlayers.remove(player)
                    print(f"\n{player.name} si ritira per mancanza di fondi")
                    del player
                else:
                    player.gamble(minimumBet)

            if len(dealer.listOfPlayers) and dealer.playersBet():
                dealer.distribute()
                print(f"\nmano mazziere: {dealer.hand[0]}, carta coperta")
                if not dealer.blackjack:
                    for player in dealer.listOfPlayers:
                        if player.betted and not player.blackjack:
                            dealer.selectAction(player)
                            score = str(player.score)
                            print(f"\nPunteggio: {score}, mano: {player.hand}")
                        else:
                            print(f"\n{player} ha fatto blackjack")
                    dealer.selfDeal()
                checkHands(dealer)
            elif not len(dealer.listOfPlayers):
                print("\nnon ci sono più giocatori, il gioco finisce")
                finished = True


if __name__ == "__main__":
    main()
    print("\nfine del gioco")
    sleep(1)