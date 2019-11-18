from algorithm.utility.utility_method import binary_search_integer, insertion_sort_integer

arr = list(map(int, input("enter the space separated integer value: ").split()))
element = int(input("Enter the element what you want to search: "))
sort_ineger=insertion_sort_integer(arr)
print(sort_ineger)
print(binary_search_integer(arr, 0, len(arr)-1, element))