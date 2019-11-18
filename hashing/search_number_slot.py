"""
Hashing Function to search a Number in a slot
a. Desc ­> Create a Slot of 10 to store Chain of Numbers that belong to each Slot to
efficiently search a number from a given set of number
b. I/P ­> read a set of numbers from a file and take user input to search a number
c. Logic ­> Firstly store the numbers in the Slot. Since there are 10 Numbers divide
each number by 11 and the reminder put in the appropriate slot. Create a Chain
for each Slot to avoid Collision. If a number searched is found then pop it or else
push it. Use Map of Slot Numbers and Ordered LinkedList to solve the problem.
In the Figure Below, you can see number 77/11 reminder is 0 hence sits in the 0
slot while 26/11 remainder is 4 hence sits in slot 4
d. O/P ­> Save the numbers in a file
Page 11 of 167. Number of Binary Search Tree
Solve the Problem in the following link

"""
try:
    # @ creating array input
    input_list = [99, 11, 22, 3, 4, 5, 6, 7, 44, 66, 77, 88, 110, 8888]
except:
    print("enter correct input")
list1 = [1]
hash_table = {}
for i in range(len(input_list)):
    list1.clear()
    key_v = input_list[i] % 11
    # Divide the number by total number of slots + 1
    # Get the key
    # if input_list[i] not in hash_table.values():

    # print(key_v)
    for j in range(len(input_list)):
            if key_v == input_list[j]%11:
                # See if any other value matches with the key
                if input_list[i] not in list1:
                    # Add it to corresponding slot
                    list1.append(input_list[j])
            else:
                break

    hash_table[key_v] = list1
    # print(hash_table)
    # print(list)
print(hash_table)
