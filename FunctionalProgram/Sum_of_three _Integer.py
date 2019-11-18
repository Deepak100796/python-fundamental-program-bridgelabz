

"""

sum of integer is program where all the three input will be checked
and sum will be printed

"""


if __name__ == '__main__':
    while True:
        try:   # try is used for catching any error

            num1 = int(input("enter number 1 :"))
            if num1 <= 0 or num1 >= 1000:
                print("enter between 0 and 1000")
                continue
            num2 = int(input("enter number 2 :"))
            if num2 <= 0 or num2 >= 1000:
                print("enter between 0 and 1000")
                continue
            num3 = int(input("enter number 3 :"))
            if num3 <= 0 or num3 >= 1000:
                print("enter between 0 and 1000")
                continue

            sum(num1, num2, num3)
            break
        except ValueError:     # if error is found in input then below statement will be printed
            print("check the input")