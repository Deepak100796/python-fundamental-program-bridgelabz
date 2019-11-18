from algorithm.utility.utility_method import is_palindrome_integer

try:
    n=int(input("Enter the integer for palindrome: "))
    print(is_palindrome_integer(n))
except ValueError:
    print("Enter integer insted of string:  ")