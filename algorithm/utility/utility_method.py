import calendar
import math
"""
this function is for checking if two string are anagram or not.
"""


def are_anagram(str1,str2):
    #find the length if both string
    n1=len(str1)
    n2=len(str2)
    # if length of both string is not equal then it is not anagram#
    if(n1!=n2):
        return False

    #sort the both string
    str1=sorted(str1)
    str2=sorted(str2)

    # Compare sorted strings
    for i in range(0,n1):
        if(str1[i] != str2[i]):
            return False
    return True


"""
this function is for palindrome string checking
"""


def is_palindrome_string(str1):
    # Using for loop find the reverse
    s1=""
    for i in str1:
        s1=i+s1
    if(s1==str1):
        return True
    return False

"""
this function is for palindrome integer checking
"""
def is_palindrome_integer(n):
    reverse=0
    original_no=n
    while(n>0):
        remainder=n%10
        reverse= (reverse*10)+ remainder
        n=n//10
    print(reverse)
    if(original_no==reverse):
        return True
    return False

"""
this function is for cheching if number is prime or not
"""
def is_prime(n):
    if(n<1):
        return False
    for i in range(2,n):
        if(n%i == 0):
            return False
    return True
"""
this function is for printing the prime number
"""
def print_prime(n):
    for i in range(2,n):
        if(is_prime(i)):
            print(i,end=" ")
"""
this method is for binary search integer
"""
def binary_search_integer(arr,l,r,element):
    if(l<=r):
        mid = int((l+r)/2)
    # If element is present at the middle itself
        if(arr[mid]==element):
            return mid
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif(arr[mid]>element):
            return binary_search_integer(arr,l,mid-1,element)
        else:
            return binary_search_integer(arr,mid+1,r,element)
    return -1

"""
this method is for binary search string
"""
def binary_search_string(arr,x):
    l = 0
    r = len(arr)
    while (l <= r):
        m = l + ((r - l) // 2)

        res = (x == arr[m])

        # Check if x is present at mid
        if (res == 0):
            return m - 1

        # If x greater, ignore left half
        if (res > 0):
            l = m + 1

        # If x is smaller, ignore right half
        else:
            r = m - 1

    return -1


"""
this method is for inserton sort integer
"""
def insertion_sort_integer(arr):
    n=len(arr)
    for i in range(1,n):

        key=arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

"""
this method is for insertion sort string
"""
def insertion_sort_string(string):
    n=len(string)
    for i in range(1,n):
        key=string[i]
        j=i-1
        while(j>=0 and (string[j]>key)):
            string[j+1]=string[j]
            j=j-1
        string[j+1]=key
    return string
"""
this method is for bubble sort integer
"""
def bubble_sort_integer(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

"""
this method is for bubble sort string
"""
def bubble_sort_string(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1] , arr[j]




"""
merge sort for integers
"""


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code

"""
this method is for find day of week
"""

def day_of_week(date):
    day, month, year = (int(i) for i in date.split(' '))
    dayNumber = calendar.weekday(year, month, day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]
    return (days[dayNumber])

"""
this method is for change celsious to fahrehnheit 
"""
def celcious_fahrehnheit(n):
    # Used the formula
    return (n * 1.8) + 32


"""
this method is for change  fahrehnheit celsious  
"""
def fahrehnheit_celcious(n):
    return(n - 32.0) * 5.0 / 9.0

"""
this method is for monthly payment
"""
def monthly_payment(p,y,r):
    n=12*y
    r1=r/(12*100);
    payment = p * r1 / (1 - math.pow((1 + r1), -n));
    return payment;

"this method is for sqrt"
def find_sqrt(c):
    t=c
    epsilon = 1e-15;
    while (abs(t - c / t) > epsilon * t):
        t = (c / t + t) / 2
    return t


"""
this methos is for binary to decimal conversion
"""

def tobinary(num):
    if (num==0):
        k=[0]
        return k
    else:
        s = []
        while(num):
            s.append(num%2)
            num=num//2
    return s[::-1]
"""
this method is for binary to decimal
"""

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

def swapNibbles(binary):
    j=len(binary)-4
    for i in range(4):
        binary[i],binary[j] = binary[j], binary[i]
        j=j+1
    return binary


# Python3 Program to print all palindromic
# primes smaller than or equal to n.

# A function that reurns true only if
# num contains one digit
def oneDigit(num):
    # comparison operation is faster than
    # division operation. So using following
    # instead of "return num / 10 == 0;"
    return (num >= 0 and num < 10);


# A recursive function to find out whether
# num is palindrome or not. Initially, dupNum
# contains address of a copy of num.
def isPalUtil(num, dupNum):
    # Base case (needed for recursion termination):
    # This statement/ mainly compares the first
    # digit with the last digit
    if (oneDigit(num)):
        return (num == (dupNum) % 10);

        # This is the key line in this method. Note
    # that all recursive/ calls have a separate
    # copy of num, but they all share same copy
    # of dupNum. We divide num while moving up
    # the recursion tree
    if (not isPalUtil(int(num / 10), dupNum)):
        return False;

        # The following statements are executed
    # when we move up the recursion call tree
    dupNum = int(dupNum / 10);

    # At this point, if num%10 contains ith
    # digit from beginning, then (dupNum)%10
    # contains ith digit from end
    return (num % 10 == (dupNum) % 10);


# The main function that uses recursive
# function isPalUtil() to find out whether
# num is palindrome or not
def isPal(num):
    # If num is negative, make it positive
    if (num < 0):
        num = -num;

        # Create a separate copy of num, so that
    # modifications made to address dupNum
    # don't change the input number.
    dupNum = num;  # dupNum = num

    return isPalUtil(num, dupNum);


# Function to generate all primes and checking
# whether number is palindromic or not
def printPalPrimesLessThanN(n):
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True] * (n + 1);
    p = 2;
    while (p * p <= n):

        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p]):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False;
        p += 1;

        # Print all palindromic prime numbers
    for p in range(2, n + 1):

        # checking whether the given number
        # is prime palindromic or not
        if (prime[p] and isPal(p)):
            print(p, end=" ");  # Python3 Program to print all palindromic
# primes smaller than or equal to n.

# A function that reurns true only if
# num contains one digit
def oneDigit(num):

    # comparison operation is faster than
    # division operation. So using following
    # instead of "return num / 10 == 0;"
    return (num >= 0 and num < 10);

# A recursive function to find out whether
# num is palindrome or not. Initially, dupNum
# contains address of a copy of num.
def isPalUtil(num, dupNum):

    # Base case (needed for recursion termination):
    # This statement/ mainly compares the first
    # digit with the last digit
    if (oneDigit(num)):
        return (num == (dupNum) % 10);

    # This is the key line in this method. Note
    # that all recursive/ calls have a separate
    # copy of num, but they all share same copy
    # of dupNum. We divide num while moving up
    # the recursion tree
    if (not isPalUtil(int(num / 10), dupNum)):
        return False;

    # The following statements are executed
    # when we move up the recursion call tree
    dupNum =int(dupNum/10);

    # At this point, if num%10 contains ith
    # digit from beginning, then (dupNum)%10
    # contains ith digit from end
    return (num % 10 == (dupNum) % 10);

# The main function that uses recursive
# function isPalUtil() to find out whether
# num is palindrome or not
def isPal(num):

    # If num is negative, make it positive
    if (num < 0):
        num = -num;

    # Create a separate copy of num, so that
    # modifications made to address dupNum
    # don't change the input number.
    dupNum = num; # dupNum = num

    return isPalUtil(num, dupNum);

# Function to generate all primes and checking
# whether number is palindromic or not
def printPalPrimesLessThanN(n):

    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True] * (n + 1);
    p = 2;
    while (p * p <= n):

        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p]):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False;
        p += 1;

    # Print all palindromic prime numbers
    for p in range(2, n + 1):

        # checking whether the given number
        # is prime palindromic or not
        if (prime[p] and isPal(p)):
            print(p, end = " ");  # Python3 Program to print all palindromic
# primes smaller than or equal to n.

# A function that reurns true only if
# num contains one digit
def oneDigit(num):

    # comparison operation is faster than
    # division operation. So using following
    # instead of "return num / 10 == 0;"
    return (num >= 0 and num < 10);

# A recursive function to find out whether
# num is palindrome or not. Initially, dupNum
# contains address of a copy of num.
def isPalUtil(num, dupNum):

    # Base case (needed for recursion termination):
    # This statement/ mainly compares the first
    # digit with the last digit
    if (oneDigit(num)):
        return (num == (dupNum) % 10);

    # This is the key line in this method. Note
    # that all recursive/ calls have a separate
    # copy of num, but they all share same copy
    # of dupNum. We divide num while moving up
    # the recursion tree
    if (not isPalUtil(int(num / 10), dupNum)):
        return False;

    # The following statements are executed
    # when we move up the recursion call tree
    dupNum =int(dupNum/10);

    # At this point, if num%10 contains ith
    # digit from beginning, then (dupNum)%10
    # contains ith digit from end
    return (num % 10 == (dupNum) % 10);

# The main function that uses recursive
# function isPalUtil() to find out whether
# num is palindrome or not
def isPal(num):

    # If num is negative, make it positive
    if (num < 0):
        num = -num;

    # Create a separate copy of num, so that
    # modifications made to address dupNum
    # don't change the input number.
    dupNum = num; # dupNum = num

    return isPalUtil(num, dupNum);

# Function to generate all primes and checking
# whether number is palindromic or not
def printPalPrimesLessThanN(n):

    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True] * (n + 1);
    p = 2;
    while (p * p <= n):

        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p]):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False;
        p += 1;

    # Print all palindromic prime numbers
    for p in range(2, n + 1):

        # checking whether the given number
        # is prime palindromic or not
        if (prime[p] and isPal(p)):
            print(p, end = " ");  # Python3 Program to print all palindromic
# primes smaller than or equal to n.

# A function that reurns true only if
# num contains one digit
def oneDigit(num):

    # comparison operation is faster than
    # division operation. So using following
    # instead of "return num / 10 == 0;"
    return (num >= 0 and num < 10);

# A recursive function to find out whether
# num is palindrome or not. Initially, dupNum
# contains address of a copy of num.
def isPalUtil(num, dupNum):

    # Base case (needed for recursion termination):
    # This statement/ mainly compares the first
    # digit with the last digit
    if (oneDigit(num)):
        return (num == (dupNum) % 10);

    # This is the key line in this method. Note
    # that all recursive/ calls have a separate
    # copy of num, but they all share same copy
    # of dupNum. We divide num while moving up
    # the recursion tree
    if (not isPalUtil(int(num / 10), dupNum)):
        return False;

    # The following statements are executed
    # when we move up the recursion call tree
    dupNum =int(dupNum/10);

    # At this point, if num%10 contains ith
    # digit from beginning, then (dupNum)%10
    # contains ith digit from end
    return (num % 10 == (dupNum) % 10);

# The main function that uses recursive
# function isPalUtil() to find out whether
# num is palindrome or not
def isPal(num):

    # If num is negative, make it positive
    if (num < 0):
        num = -num;

    # Create a separate copy of num, so that
    # modifications made to address dupNum
    # don't change the input number.
    dupNum = num; # dupNum = num

    return isPalUtil(num, dupNum);

# Function to generate all primes and checking
# whether number is palindromic or not
def printPalPrimesLessThanN(n):

    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True] * (n + 1);
    p = 2;
    while (p * p <= n):

        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p]):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False;
        p += 1;

    # Print all palindromic prime numbers
    for p in range(2, n + 1):

        # checking whether the given number
        # is prime palindromic or not
        if (prime[p] and isPal(p)):
            print(p, end = " ");  # Python3 Program to print all palindromic
# primes smaller than or equal to n.

# A function that reurns true only if
# num contains one digit
def oneDigit(num):

    # comparison operation is faster than
    # division operation. So using following
    # instead of "return num / 10 == 0;"
    return (num >= 0 and num < 10);

# A recursive function to find out whether
# num is palindrome or not. Initially, dupNum
# contains address of a copy of num.
def isPalUtil(num, dupNum):

    # Base case (needed for recursion termination):
    # This statement/ mainly compares the first
    # digit with the last digit
    if (oneDigit(num)):
        return (num == (dupNum) % 10);

    # This is the key line in this method. Note
    # that all recursive/ calls have a separate
    # copy of num, but they all share same copy
    # of dupNum. We divide num while moving up
    # the recursion tree
    if (not isPalUtil(int(num / 10), dupNum)):
        return False;

    # The following statements are executed
    # when we move up the recursion call tree
    dupNum =int(dupNum/10);

    # At this point, if num%10 contains ith
    # digit from beginning, then (dupNum)%10
    # contains ith digit from end
    return (num % 10 == (dupNum) % 10);

# The main function that uses recursive
# function isPalUtil() to find out whether
# num is palindrome or not
def isPal(num):

    # If num is negative, make it positive
    if (num < 0):
        num = -num;

    # Create a separate copy of num, so that
    # modifications made to address dupNum
    # don't change the input number.
    dupNum = num; # dupNum = num

    return isPalUtil(num, dupNum);

# Function to generate all primes and checking
# whether number is palindromic or not
def printPalPrimesLessThanN(n):

    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True] * (n + 1);
    p = 2;
    while (p * p <= n):

        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p]):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False;
        p += 1;

    # Print all palindromic prime numbers
    for p in range(2, n + 1):

        # checking whether the given number
        # is prime palindromic or not
        if (prime[p] and isPal(p)):
            print(p, end = " ");  # Python3 Program to print all palindromic
# primes smaller than or equal to n.

# A function that reurns true only if
# num contains one digit
def oneDigit(num):

    # comparison operation is faster than
    # division operation. So using following
    # instead of "return num / 10 == 0;"
    return (num >= 0 and num < 10);

# A recursive function to find out whether
# num is palindrome or not. Initially, dupNum
# contains address of a copy of num.
def isPalUtil(num, dupNum):

    # Base case (needed for recursion termination):
    # This statement/ mainly compares the first
    # digit with the last digit
    if (oneDigit(num)):
        return (num == (dupNum) % 10);

    # This is the key line in this method. Note
    # that all recursive/ calls have a separate
    # copy of num, but they all share same copy
    # of dupNum. We divide num while moving up
    # the recursion tree
    if (not isPalUtil(int(num / 10), dupNum)):
        return False;

    # The following statements are executed
    # when we move up the recursion call tree
    dupNum =int(dupNum/10);

    # At this point, if num%10 contains ith
    # digit from beginning, then (dupNum)%10
    # contains ith digit from end
    return (num % 10 == (dupNum) % 10);

# The main function that uses recursive
# function isPalUtil() to find out whether
# num is palindrome or not
def isPal(num):

    # If num is negative, make it positive
    if (num < 0):
        num = -num;

    # Create a separate copy of num, so that
    # modifications made to address dupNum
    # don't change the input number.
    dupNum = num; # dupNum = num

    return isPalUtil(num, dupNum);

# Function to generate all primes and checking
# whether number is palindromic or not
def printPalPrimesLessThanN(n):

    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True] * (n + 1);
    p = 2;
    while (p * p <= n):

        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p]):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False;
        p += 1;

    # Print all palindromic prime numbers
    for p in range(2, n + 1):

        # checking whether the given number
        # is prime palindromic or not
        if (prime[p] and isPal(p)):
            print(p, end = " ");


"""
this function is for number guesser 
"""
def number_guesser():
    arr=[]
    l = 0

    n=int(input("Enter the maximum number: "))
    h = n
    for i in range(n):
        arr.append(i)
    print("Take a number in your mind between 1 to range :)\nI am telling you,I will guess it within 7 times .Haha you can't beat me\n\n")
    # print("\nPress any key to start game , Then I will tell you the Answer.");
    # ch = input()
    while(l<=h):
        mid = (l + h) // 2;
        print("I think " , arr[mid]  ,"is your number ?  If agree Press 'y' , If less than this Press 'L'  "
                                            "If greater Press 'G' ")
        ans = input("Enter the choice Y or L or G")
        if (ans == 'Y' or ans == 'y'):
            {
                print("\n\nYou said I got it u had taken (Answer : " , arr[mid] )
            }
        elif (ans == 'l' or ans == 'L'):
            h = mid - 1;
        elif (ans == 'g' or ans == 'G'):
            l = mid + 1;
    return

"""
this function is for vending machine notes counts
"""
def countCurrencyAmount(amount):
    notes=[1000, 500, 200, 100, 50, 20, 10, 5,2, 1]
    n=len(notes)
    note_counter=[0] *n
    for i, j in zip(notes, note_counter):
        if amount >= i:
            j = amount // i

            amount = amount - j * i
            # print(amount)
            print(i, " : ", j)





