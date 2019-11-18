from algorithm.utility.utility_method import mergeSort, printList

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]

    print ("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)