from algorithm.utility.utility_method import are_anagram

str1=input("Enter the first string: ")
str2=input("Enter the second string for checking anagram: ")
if are_anagram(str1, str2):
    print("they are anagram from each other: ")
else:
    print("no! they are not anagram: ")