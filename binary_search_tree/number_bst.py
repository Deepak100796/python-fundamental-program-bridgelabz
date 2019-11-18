# Find Number of Binary Search Trees possible with given number of nodes

class BST:
    def factorial(self,number):
        factorial = 1
        # Find the factorial of a number
        for i in range(1,number+1):
            factorial = factorial * i
        # print(factorial)
        return factorial


bst = BST()
number = int(input("Enter a number : "))
# bst.factorial(number)
val1 = bst.factorial(2*number)
val2 = bst.factorial(number+1)
val3 = bst.factorial(number)
# This is formula to find number of BSTs
bst_number = val1/(val2*val3)
print("Number of BSTs are : ", bst_number)