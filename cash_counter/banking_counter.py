"""
Simulate Banking Cash Counter
a. Desc ­> Create a Program which creates Banking Cash Counter where people
come in to deposit Cash and withdraw Cash. Have an input panel to add people
to Queue to either deposit or withdraw money and dequeue the people. Maintain
the Cash Balance.
b. I/P ­> Panel to add People to Queue to Deposit or Withdraw Money and dequeue
c. Logic ­> Write a Queue Class to enqueue and dequeue people to either deposit
or withdraw money and maintain the cash balance
d. O/P ­> True or False to Show Arithmetic Expression is balanced or not.
"""

# @import statement for dqueue
from collections import deque


class CountCash:

    # Ask a person whether he wants to deposit or withdraw thw money and save them in queue
    def sorting_people(self, f_people_count):
        f_people_queue = deque([])
        for iterating_element in range(f_people_count):
            f_choice = int(input("Enter your choice : "))
            if f_choice == 1:
                f_people_queue.append(1)
            elif f_choice == 2:
                f_people_queue.append(2)
            else:
                print("Invalid Choice")
        return f_people_queue

    def bank_operations(self, g_people_queue, people_count):
        f_people_queue = deque(g_people_queue)
        # print(f_people_queue)
        g_total_cash = 10000000
        # print(f_people_queue)
        # print(people_count)

        for iterating_element in range(len(f_people_queue)):
            if f_people_queue != None:
                if f_people_queue[iterating_element] == 1:
                    # If peron chooses to withdraw money
                    # then deduct the amount and pop him
                    f_amount = int(input("Enter your amount to withdraw : "))
                    g_total_cash = g_total_cash - f_amount
                    print("Remaining = ", g_total_cash)
                    f_people_queue.popleft()
                    print(f_people_queue)

                elif f_people_queue[iterating_element] == 2:
                    # If person chooses to deposit money
                    # then add the amount and pop him

                    f_amount = int(input("Enter your amount to deposit: "))
                    g_total_cash = g_total_cash + f_amount
                    print("Remaining = ", g_total_cash)
                    f_people_queue.popleft()
                    print(f_people_queue)


# g_people_queue = deque([])

# driver program
try:
    print("Options : " "1--Withdraw" "2--Deposit")
except IOError:
    print("Enter the write option")

g_people_count = int(input("Enter number of people available :"))
cc = CountCash()
g_people_queue = deque(cc.sorting_people(g_people_count))
cc.bank_operations(g_people_queue, g_people_count)
