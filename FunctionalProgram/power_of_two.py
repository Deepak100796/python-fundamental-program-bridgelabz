from Week1.Utility.utility import power_of_2
# Desc -> This program takes a command-line argument N and prints a table of the powers of
# 2 that are less than or equal to 2^N.
# I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
# Logic -> repeat until i equals N.

# function is called

"""
main function is called and below function will print the power of 2
"""
if __name__ == '__main__':
    while True:
        try:    # try is used for catching any error

            userinput = int(input("enter num : "))
            if userinput<=0 or userinput>=100:
                print("enter between 0 and 100")
                continue
            power_of_2(userinput)
            break
        except ValueError:
            print("check the user input")