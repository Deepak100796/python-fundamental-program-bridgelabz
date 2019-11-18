"""
Write a Program DeckOfCards.java , to initialize deck of cards having suit ("Clubs",
"Diamonds", "Hearts", "Spades") & Rank ("2", "3", "4", "5", "6", "7", "8", "9", "10",
"Jack", "Queen", "King", "Ace"). Shuffle the cards using Random method and then
distribute 9 Cards to 4 Players and Print the Cards the received by the 4 Players
using 2D Array...
"""
"""
    @date   : 1/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""

# @import statement
try:
    from random import shuffle
except ImportError:
    print("import Error")


#  @class card
class CardGame:

    # @constructors
    def __init__(self):
        # @ initialize rank and suits
        self.rank = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.suits = ["ace", "jack", "queen", "king"]
        # @taking deck list
        self.deck = []
        # deck is created using for loop
        for i in self.rank:
            self.deck.append(str(i))

        for i in self.suits:
            self.deck.append(i)

    def distribute(self):  # this function is used for distributing cards in even format

        deck = self.deck
        players = int(input("number of player playing: "))  # number of players want to play
        array = [[] for i in range(players)]  # 2d array is created to store the value

        for i in range(players):  # using random function deck is shuffled
            shuffle(deck)

            for j in range(9):  # this loop is used for distributing data to the players
                array[i].append(deck[j])

        return array  # final cards stored in array var