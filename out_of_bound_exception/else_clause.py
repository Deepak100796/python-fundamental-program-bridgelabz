# Program to depict else clause with try-except

# Function which returns a/b


def fun(a,b):
    try:
        c = ((a+b) / (a-b))

    except ZeroDivisionError:
        print("a/b result in 0: ")
    else:
        print(c)


# Driver program to test above function
fun(2.0, 3.0)
fun(3.0, 3.0)
