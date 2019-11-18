from Week1.Utility.utility import leap_year
'''

*****************************************************************************

determine if it is a leap year.print the year is a leap year or not.

*****************************************************************************

'''


# leap-year function is created

# function is called

if __name__ == '__main__':
    while True:

        try:      # try is used for catching any error
            year = int(input("enter year in yyyy format  : "))
            if year<=1000 or year>=10000:
                print("enter year again" )
                continue
            leap_year(year)
            break
        except ValueError:      # value error
            print("check the input")


