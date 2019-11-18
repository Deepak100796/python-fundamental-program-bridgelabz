"""
JSON Inventory Data Management of Rice, Pulses and Wheats
a. Desc ­> Create a JSON file having Inventory Details for Rice, Pulses and Wheats
with properties name, weight, price per kg.
b. Use Library : Java JSON Library , For IOS JSON Library use
NSJSONSerialization for parsing the JSON .
c. I/P ­> read in JSON File
d. Logic ­> Get JSON Object in Java or NSDictionary in iOS. Create Inventory
Object from JSON. Calculate the value for every Inventory.
e. O/P ­> Create the JSON from Inventory Object and output the JSON String
"""

"""
    @date   : 2/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""
# @import error
try:
    import json
except ImportError:
    print("import error")

"""
json function is created where data is loaded and inventory value are calculated and 
it file is dumped back as a json str
"""


def json_inventory():
    with open("JSON", "r") as f:  # json file is loaded in dict format
        data = json.load(f)

    riceinvent = 0
    wheatinvent = 0
    pulseinvent = 0

    try:  # try exception is used id data is not present in the inventory

        # to file data in each inventory
        for i in data["Rice"]:
            for price in i:
                riceinvent += i["price per kg"]  # data is incremented

        for i in data["wheat"]:
            for price in i:
                wheatinvent += i["price per kg"]  # data is incremented

        for i in data["pulses"]:
            for price in i:
                pulseinvent += i["price per kg"]  # data is incremented


    except TypeError:
        print(" there is type error ")

    print( """total value for rice in inventory is {},
total value for wheat in inventory is {},
total value for pulse in inventory is {}""".format(riceinvent, wheatinvent, pulseinvent))

    dump=json.dumps("JSON")
    # print(type(dump))  # then data is dumped in str format


"""
main function is created to call json function 
"""
if __name__ == '__main__':

    json_inventory()