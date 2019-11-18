# A python program to create user-defined exception

# class MyError is derived from super class Exception


class MyError(Exception):

    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return repr(self.value)

"""
driver code for MyErrror class
"""
try:
    raise MyError(2 * 3)

except MyError as error:
    print("a new exception occurred: ", error.value)
