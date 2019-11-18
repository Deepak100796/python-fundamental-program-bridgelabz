
"""
UnOrdered List:
a. Desc ­> Read the Text from a file, split it into words and arrange it as Linked List.
Take a user input to search a Word in the List. If the Word is not found then add it
to the list, and if it found then remove the word from the List. In the end save the
list into a file
b. I/P ­> Read from file the list of Words and take user input to search a Text
c. Logic ­> Create a Unordered Linked List. The Basic Building Block is the Node
Object. Each node object must hold at least two pieces of information. One ref to
the data field and second the ref to the next node object.
d. O/P ­> The List of Words to a File.
"""
"""
    This is stack class. it include all the stack operation like push data , pop data get the size etc.

    @date   : 2/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""



# @import statements
from dataStructureProgram.unordered_linkedlist.unorderedList import UnOrderedLinklist

# @creating object of Unordredlist
unordered = UnOrderedLinklist()

# @open file from list
with open("list.txt","r") as file:
    read_file = file.read()

# This will print every line one by one in the file
# for each in read_file:

# print(read_file,">>>>>>>")
word = read_file.split()
file.close()
print (word)
try:
    input = input("Enter the word what you want to check: ")
except IOError:
    print("Enter the correct input: ")
j=0

# @ putting word into the linklist
for i in word:
    unordered.add(i)

# @ checking if input is in the list or not
if input == unordered.search(input):
        j=1
s=""
# @ if yes then remove the input file from list and file
if j == 1:
    unordered.remove(input)
    word.remove(input)

    for i in word:
        s = s+i+" "
    with open("list.txt", "w") as file:
        file.write(s)

    print("found and deleted")

else:
    # @adding to linklist
    unordered.add(input)
    print("added to the list")
    # @ write the result into another file
    with open("list1.txt", "w+") as file1:
        file1.write(s+input)








