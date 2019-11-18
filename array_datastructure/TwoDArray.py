# Take a range of 0 - 1000 Numbers and find the Prime numbers in that range.
# Store the prime numbers in a 2D Array, the first dimension represents
# the range 0-100, 100-200, and so on. While the second dimension represents
# the prime numbers in that range

list1 = []
flag = 0
array = [[],[[]]]
list0 = []

for iteration_value in range(0, 10):
    min = iteration_value * 100
    max = 100*(iteration_value + 1)
    for number in range(min,max+1):
        if number > 1:
            for iterating_number in range(2, number):
                if number % iterating_number == 0:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag == 1:
                if number not in list1:
                    list1.append(number)
    # print("Prime number in range ", min, "-", max, "=", list1)
    list0.append(min)
    list0.append(max)
    array[0] = list0
    array[1][0] = list1
    print(array)
    list0.clear()
    list1.clear()

