"""
Palindrome­Checker
a. Desc ­> A palindrome is a string that reads the same forward and backward, for
example, radar, toot, and madam. We would like to construct an algorithm to
input a string of characters and check whether it is a palindrome.
b. I/P ­> Take a String as an Input
c. Logic ­> The solution to this problem will use a deque to store the characters of
the string. We will process the string from left to right and add each character to
the rear of the deque.
d. O/P ­> True or False to Show if the String is Palindrome or not.
"""

"""
    

    @date   : 2/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""

"""
"""

 # @ taling user input
user_string = list(input("Enter a string: "))
# @ put into the queue
original_queue = list(user_string)
check_queue = []
# @ iterating into string
for iterating_number in range(len(user_string)):
    # Pop the elements from the list into another list
    value = user_string.pop()
    check_queue.append(value)

print("1--", original_queue)
print("2--", check_queue)
# Check if poped list and original list are same or not
if check_queue == original_queue:
    print("It is a palindrome")
else:
    print("It is not a palindrome")