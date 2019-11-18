import json

"""
    @date   : 1/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""
#   @import statement
try:
    from Object_Oriented_Programs.stockPrice.stock_calculation import stock
except ImportError:
    print("import Error")


# @stock report fuction
def stock_report():
    s = stock("stock_json")  # object is created for the class

    print("number of stocks in the portfolio are ", s.showReport()[2])
    print("total number of share to hold from all the stocks", s.showReport()[1])
    print("approx amount paid of per stock in your portfolio is ", s.showReport()[0])
    print(s.addStock())
    # print(s.deleteStock())
    s.write_into_file("stock_json")
    print(s.showReport())


if __name__ == '__main__':
    stock_report()