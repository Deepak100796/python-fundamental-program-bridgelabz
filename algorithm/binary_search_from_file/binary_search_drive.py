import pandas as pd
from algorithm.utility.utility_method import insertion_sort_string, binary_search_string, bubble_sort_string

#
# with open('binary_search_file.txt', 'r') as r:
#     for line in sorted(r):
#         print(line, end='')
file1 = open("myfile.txt","w+")
file1.writelines("hi this from deepak mishra from assam")
print(file1.readline())
# for i in file1: