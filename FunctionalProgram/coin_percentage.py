from Week1.Utility.utility import CoinToss
'''

*****************************************************************************
use random function to get value between 0 and 1. if < 0.5 then tails or head
the number of times to flip coin. ensure it is positive integer
by importing numpy for generating random numbers in array
*****************************************************************************

'''

# program is called from the main function
if __name__ == '__main__':
    while True:
        try:
            toss = int(input("number of flips: "))
            if toss <= 1 or toss >= 100:
                print("please enter the number between 0 and 100 ")
                continue
            CoinToss(toss)
            break
        except ValueError:
            print(" check the input")