def add(num1,num2):
    return num1+num2


def subtract(num1,num2):
    return num1+num2


def multiply(num1,num2):
    return num1*num2


def divide(num1,num2):
    return num1/num2


print("Please select operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n")
select=input("select operation 1 ,or 2, or  3 ,or  4")
a = int(input("Enter the num1 value: "))
b = int(input("Enter the num2 value: "))
if select == '1':
    print(a, "+" ,b , "=" , add(a, b))
elif select=='2':
    print(a, "*", b, "=", multiply(a, b))

elif select=='3':
    print(a, "-", b, "=", subtract(a, b))
elif select=='4':
    print(a, "/", b, "=", divide(a, b))
else:
    print(" Envalid ")