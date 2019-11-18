from Week1.Utility.utility import Coupons
'''

*****************************************************************************
given n distinct coupon numbers, how many random numbers do you need to generate distinct coupon number?
this program simulates this random process.
*****************************************************************************

'''


# coupons functions used to generate random numbers


if __name__ == '__main__':
    while True:
        try:  # try is used for catching the errors
            number = int(input("please enter number to generate coupons : "))
            if number <= 1 or number >= 1000:
                print("please enter the number between 0 and 1000")
                continue
            Coupons(number)
            break
        except ValueError:  # errors are caught and below statement is printed
            print("check the input")