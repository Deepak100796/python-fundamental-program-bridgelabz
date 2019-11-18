"""
stock calculation
"""
"""
    @date   : 1/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""
# import json
try:
    import json
    import numpy as np
except ImportError:
    print("import error")


# class stock
class stock():

    # constructor for file handling
    def __init__(self, filename):  # here file is initialised with file name
        try:
            with open(filename) as f:
                self.data = json.load(f)  # data is loaded in this function
                # print(self.data)
        except FileNotFoundError:
            print("file not found")
    # @add stock
    def addStock(self):
        try:  # try is used to catch user input error

            stock = input("name the stock you want to add : ")
            total_share = int(input("number of share you want to buy : "))
            share_price = np.random.randint(100, 200)

        except ValueError:  # here below statement will be printed out
            print("check the input data")

        # @add data to the dictionary
        dict1 = {"stock": stock, "total_share": total_share, "share_price": share_price}

        # initialize to json data
        z = self.data
        z.append(dict1)
        return  z, dict1

    # @ for printing data
    def showReport(self):
        # @variable
        share_price = 0
        total_share = 0
        share = 0
        # @for loop is used for traversing the dict
        for stocks in range(len(self.data)):
            share += 1
            share_price = share_price + self.data[stocks]["share_price"]
            total_share = total_share + self.data[stocks]["total_share"]

        return share_price, total_share, share

    def deleteStock(self):  # this function is used for deleting the stock

        user = input("stock name to delete from the portfolio :")
        g = -1

        for i in self.data:
            g += 1
            # print(i['stock'])

            if i['stock'] == user:
                del self.data[g]  # data is deleted from the json file
                return g  # here we have a return value of the index

    # file is saved and write back to the original file
    def write_into_file(self,filename):
        with open("stock_json",'w') as f:
            json.dump(self.data,f,indent=2)


    def onlyStocks(self):  # this function is used for displaying only stocks
        stocks = []

        for i in range(len(self.data)):
            stocks.append(self.data[i]["stock"])

        return stocks  # stocks val is returned an displayed in the main file