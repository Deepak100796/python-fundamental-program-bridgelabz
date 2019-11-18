from Week1.Utility.utility import windchill
'''

*****************************************************************************

prints the wind chill. use math.pow(a, b) to compute ab.
given the temperature t (in fahrenheit) and the wind speed v (in miles per hour)
note: the formula is not valid if t is larger than 50 in absolute value or if v is larger
than 120 or less than 3 (you may assume that the values you get are in that range).

*****************************************************************************

'''


if __name__ == '__main__':
    while True:
        try:   # try is used for catching any error

            temp = int(input("enter temp below 50 in fahrenheit : "))
            if temp >= 51 :
                print("enter between 50 and 1000")
                continue
            velocity = int(input("enter velocity in range of 3m/s and  120m/s : "))
            if velocity <= 4 or velocity >= 121:
                print("enter number between 3 and 120 ")
                continue
            windchill(temp, velocity)
            break

        except ValueError:    # if error is found then below statement will be printed
            print("check the input")
