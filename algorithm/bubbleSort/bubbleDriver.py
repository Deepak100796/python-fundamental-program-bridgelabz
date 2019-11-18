from algorithm.utility.utility_method import bubble_sort_integer, bubble_sort_string

arr=list(map(int,input("Enter the array: space separated: ").split()))
string=list(map(str,input("Enter the array: space separated: ").split()))
bubble_sort_integer(arr)
print("sorted integer are: ")
for i in range(len(arr)):
    print(arr[i],end=" ")
print()

bubble_sort_string(string)
print("sorted string are: ")
for i in range(len(string)):
    print(string[i],end=" ")