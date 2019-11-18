from Week1.Utility.utility import harmonic_value
'''

*****************************************************************************

prints the nth harmonic number: 1/1 + 1/2 + ... + 1/n

*****************************************************************************

'''

# input is given and function is called

if __name__ == '__main__':
    while True:

        try:  # try is used for catching any error

            number = int(input("enter the number to find its harmonic value : "))
            if number<=0 or number>=1000:
                print("enter between 0 and 1000")
                continue
            harmonic_value(number)
            break

        except ValueError:
            print("check the input")