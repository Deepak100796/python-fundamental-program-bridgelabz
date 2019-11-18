from algorithm.utility.utility_method import binary_search_string, insertion_sort_string

string=list(map(str,input("Enter the space seperated string ").split()))

element= input("enter the element what you want to search")


# sort_string = insertion_sort_string(string)
# print(sort_string)

result = binary_search_string(string,element)
if(result!=-1):
    print(result)
else:
    print("not faund: ")
