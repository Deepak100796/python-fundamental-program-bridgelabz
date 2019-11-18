from Week1.Utility.utility import quad
# Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c. Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation can be found using a formula
# delta = b*b - 4*a*c
# Root 1 of x = (-b + sqrt(delta))/(2*a)
# Root 2 of x = (-b - sqrt(delta))/(2*a)


"""

main function is called where user input is taken and quad equation roots are given out

"""

if __name__ == '__main__':
    while True:
        try:    # try is used for catching any error

            num1 = int(input("enter number 1 :"))
            if num1<=0 or num1>=1000:
                print("enter between 0 and 1000")
                continue
            num2 = int(input("enter number 2 :"))
            if num2<=0 or num2>=1000:
                print("enter between 0 and 1000")
                continue
            num3 = int(input("enter number 3 :"))
            if num3<=0 or num3>=1000:
                print("enter between 0 and 1000")
                continue
            quad(num1, num2, num3)
            break

        except ValueError:
            print("check user input")