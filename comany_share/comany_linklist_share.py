"""
Maintain the List of CompanyShares in a Linked List So new CompanyShares can
be added or removed easily. Do not use any Collection Library to implement Linked
List.
"""

"""
    @date   : 3/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""

# @import statement
try:
    from Object_Oriented_Programs.stockPrice.stock_calculation import stock
    # from dataStructureProgram.ordered_linkedlist.linklist import OrderedList
    import json

    from dataStructureProgram.unordered_linkedlist.unorderedList import UnOrderedLinklist
except ImportError:
    print("import error")

# @comany share function
def companyshares():
    st = stock("stock_json")  # object is created for stock and linked list
    llist = UnOrderedLinklist()

    # @open a json file
    try:
        with open("stock_json") as f:  # json file is loaded
            data = json.load(f)
    except FileNotFoundError:
        print("find not found: ")
    for items in data:  # json file is converted in linked list
        llist.add(items)

    # input is taken from the user

    try:  # try is used for the finding exception

        for i in range(len(st.onlyStocks())):    # will display all the stocks in the portfolio
            print("**",st.onlyStocks()[i],end=" ")

        print("\nchoose from above stocks to delete stocks ")
        user = int(input("enter 1 to add or enter 2 to delete or enter 3 to exit :"))

        if user == 1:

            llist.add(st.addStock()[1])  # if user is given 1 we will ad the stock to the linked list

        elif user == 2:

            g = st.deleteStock()  # if user is given 2 we will call stock class to delete the data
            llist.remove(data[g])  # here data is removed

        else:
            print("bye bye")  # program will end here

        st.write_into_file("stock_json")

    except ValueError:
        print(" please check the Value Error ")


"""
main  function is created and function is called 
"""

if __name__ == '__main__':
    companyshares()
