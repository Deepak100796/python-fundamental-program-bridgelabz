# Python program to handle simple runtime error

arr = [1,2,3]

try:
    print(arr[1])
    print(arr[4])

except IndexError:
    print("An Error occurred:")