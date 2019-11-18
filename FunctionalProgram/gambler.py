from Week1.Utility.utility import Gambler
'''

*****************************************************************************

simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal.

*****************************************************************************

'''


# before calling function taking input for $$money$$

if __name__ == '__main__':
    while True:
        try:   # try is used for catching any error

            amount = int(input("amount :"))
            if amount<=0 or amount>=1000:
                print("enter the number between 0 and 1000")
                continue
            Gambler(amount)
            break

        except ValueError:
            print("check the input")