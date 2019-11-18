"""
Desc ­> Take an Arithmetic Expression such as
(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) where parentheses are used to order the
performance of operations. Ensure parentheses must appear in a balanced
fashion.
b. I/P ­> read in Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)
c. Logic ­> Write a Stack Class to push open parenthesis “(“ and pop closed
parenthesis “)”. At the End of the Expression if the Stack is Empty then the
Arithmetic Expression is Balanced. Stack Class Methods are Stack(), push(),
pop(), peak(), isEmpty(), size()
d. O/P ­> True or False to Show Arithmetic Expression is balanced or not.
"""

"""


    @date   : 1/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""

# @taling paranthesis for checking balance
open_list = ["[", "{", "(", "("]
close_list = ["]", "}", ")", ")"]


# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if (len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"


# driver code
# @ taling input as parathesis
try:
    string = list(map(str, input("Enter the paranthesis for balance: : ")))
except IOError:
    print("Enter the correct input: ")
# Driver code
# string = "{[]{()}}"
print(string, "-", check(string))
