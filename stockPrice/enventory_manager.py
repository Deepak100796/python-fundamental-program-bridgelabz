"""
Desc ­> Write a program to read in Stock Names, Number of Share, Share Price.
Print a Stock Report with total value of each Stock and the total value of Stock.
b. I/P ­> N number of Stocks, for Each Stock Read In the Share Name, Number of
Share, and Share Price
c. Logic ­> Calculate the value of each stock and the total value
d. O/P ­> Print the Stock Report.
e. Hint ­> Create Stock and Stock Portfolio Class holding the list of Stocks read
from the input file. Have functions in the Class to calculate the value of each
stock and the value of total stocks
"""
"""
    @date   : 1/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""


# @import statement
try:
    import json
    from Object_Oriented_Programs.stockPrice.stock_calculation import stock
except ImportError:
    print("import error")


# @stock update for manager
def stockUpdate():
    # object class is created
    s = stock("stock_json")

    num = int(input("how many stock you wish to add in in your portfolio :"))  # input is taken for updating the
    # portfolio

    if num == 0:     # if input is 0 then this function will return
        print(" no stocks to be added in the portfolio ")
        pass

    for i in range(num):  # for loop is used for adding or removing the data
        s.addStock()
        print("stock is added to the portfolio")

    try:  # try is used to catch the exception

        for i in range(len(s.onlyStocks())):
            print("**",s.onlyStocks()[i],end=" ")

        print(" choose from above stocks to delete ")
        user = int(input("\npress 1 for portfolio report, press 2 for removing , press 3  to exit  "))

        if user == 1:  # if input is 1 then over all report will be printed
            print("number of stocks in the portfolio are ", s.showReport()[2])
            print("total number of share to hold from all the stocks", s.showReport()[1])
            print("approx amount paid of per stock in your portfolio is ", s.showReport()[0])

        if user == 2:  # if input is 2 then stock will be deleted
            s.deleteStock()
            print("stock have been deleted")
            print(s.onlyStocks())

        if user == 3:  # if input is 3 then program will end
            print("thank you for using the service")



    except ValueError as err:  # exception is used for the same
        print("please check the input ",err)
    s.write_into_file("stock_json")





"""
main function is used for calling above function 
"""

if __name__ == '__main__':
    stockUpdate()