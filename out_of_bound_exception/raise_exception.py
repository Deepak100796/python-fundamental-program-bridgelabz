# Program to depict Raising Exception


try:
    raise NameError("hi there: ")

except NameError:
    print("exception")
    raise   # To determine whether the exception was raised or not

