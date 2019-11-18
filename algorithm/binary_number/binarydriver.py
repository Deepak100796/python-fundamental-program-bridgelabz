from algorithm.utility.utility_method import tobinary, binaryToDecimal, swapNibbles

decimal=int(input("Enter the decimal for converting binary "))
binary=int(input("Enter the binary number: "))

print(tobinary(decimal))
# result=swapNibbles(binary)
print(binaryToDecimal(binary))