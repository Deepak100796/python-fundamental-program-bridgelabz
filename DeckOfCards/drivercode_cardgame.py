import json

"""
    @date   : 1/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""

# @import statement
try:
    from Object_Oriented_Programs.deckOfCards.cardCalculation import CardGame
    from dataStructureProgram.queueOperation.queue_method import queue
    from random import random,shuffle
except ImportError:
    print("import error")


def playingCard():
    cards = CardGame()  # object is created for card game

    data = cards.distribute()  # distribute function is called from card game and results will be printed in 2d array

    # print(data)   # distributed card will be printed out

    for hand in range(len(data)):  # for loop is used for adding each players cards to the linked list
        data[hand].sort()
        queue.enqueue(data[hand])  # hands are updated to the queue via linked list
    print()
    print()
    print(queue.get_queue())  # same distributed cards are printed out in linked list format in queue


"""
main function is called
"""
if __name__ == '__main__':
    playingCard()