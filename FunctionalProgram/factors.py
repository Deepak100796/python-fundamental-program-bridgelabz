from Week1.Utility.utility import primefactors
'''

*****************************************************************************
computes the prime factorization of n ,number to find the prime factors
               print the prime factors of number n

*****************************************************************************

'''

# python program to print prime factors

# function is called and end results will be prime factors of the input

if __name__ == '__main__':
    while True:
        try:   # try is used to catch any error

            prime = int(input("please enter number for finding factors :  "))
            if prime<=0 or prime>=1000:
                print("enter the number between 0 and 1000")
                continue
            primefactors(prime)
            break


        except ValueError:
            print("check the input")