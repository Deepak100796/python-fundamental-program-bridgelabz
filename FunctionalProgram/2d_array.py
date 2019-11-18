from Week1.Utility.utility import Array2d
'''

*****************************************************************************
created 2 dimensional array in memory to read in m rows and n cols
by importing numpy for generating random numbers in array
*****************************************************************************

'''

# array function is used to complete the task
if __name__ == '__main__':
    while True:
        try:
            row = int(input("number of rows : "))   # user input is taken
            if row <= 0 or row >= 1000:
                print("check the input for row")
                continue
            col = int(input("number of cols : "))
            if col <= 0 or col >= 1000:
                print("check the input for row")
                continue
            # array function is called to do the need full
            Array2d(row, col)
            break
        except ValueError:
            print("check the input")
