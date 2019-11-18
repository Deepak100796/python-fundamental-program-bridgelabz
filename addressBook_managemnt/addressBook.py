"""
address book class is created where data can be added deleted or sorted as per the user
"""
try:
    import json
except ImportError:
    print("import error")


class AddressBook():  # address book class is created

    def __init__(self, filename):  # here file is initialised with file name

        with open(filename) as f:
            self.data = json.load(f)  # json file is loaded

    def addRecord(self):  # this function is used for added data to the json file

        while True:

            try:
                cities = ["mumbai", "pune", "bangalore", "delhi", "hyderabad", "surat", ]
                states = ["maharastra", "karnataka", "delhi", "telangana"]

                first_name = input("enter your first name :")
                if first_name.isalpha() is False:
                    print("enter vaild name ")
                    continue

                last_name = input("enter your last name :")
                if last_name.isalpha() is False:
                    print("length of last name should be less than 26")
                    continue

                address = input("enter your 1st and 2nd line of address :")
                if len(address) >= 60:
                    print("length of address should be less than 60")
                    continue

                for i in cities:
                    print("**", i, end=" ")
                city = input("\nenter the city name from above list :")
                while True:
                    flag = 0
                    try:
                        for i in cities:
                            if city == i:
                                print("done")
                                flag = 1
                                break
                            else:
                                return
                        if flag == 1:
                            break
                    except ValueError:
                        print("error")

                state = input("enter the state name :")

                zipcode = int(input("enter the zip code :"))
                if len(str(zipcode)) >= 7:
                    print("length of input should be less than 7")
                    continue

                phone_number = int(input("enter the full mobile number"))
                if phone_number <= 916000000000 or phone_number >= 920000000000:
                    print("enter vaild number starting from 91")
                    continue

                # dic is used for storing user input data
                dic = {"first_name": first_name,
                       "last_name": last_name,
                       "address": address,
                       "city": city,
                       "state": state,
                       "zipcode": zipcode,
                       "phone_number": phone_number}
                print("user data added successfully")

                data = self.data
                data.append(dic)  # user data is added to the file

                print(dic)  # now data and input data is called in main file
                break
            except ValueError:
                print("check user input")

    def delete(self):  # this function is used for deleting data in the json file

        # input is used for deleting data
        datadelete = input("\nname of the person you want to delete from the address book :")
        print(datadelete, "is deleted from address book ")

        name = []
        for i in range(len(self.data)):
            name.append(self.data[i]["first_name"])

        index = -1  # index is used for keeping track of the index where we have to delete the data

        for para in self.data:  # para is used for transversing through the data
            index += 1

            if datadelete == para["first_name"]:  # if condition is used for checking user input
                del self.data[index]  # here data is deleted if data  matches
                return index  # index is returned for future

        print(datadelete, " is deleted from address book ")

    def printData(self):  # this function is used for printing data in mailing format

        data = self.data

        for i in range(len(data)):  # for loop is used transversing values through data
            for j in data[i].values():
                print(j)
            print()

    def sort(self):  # sort function is used for sorting the data in json file

        array = []
        data = self.data  # data is stored in var

        for i in range(len(self.data)):  # first name is appended in array
            array.append((self.data[i]["first_name"]))
        name_sort = sorted(array)  # here only names are sorted

        sorteddata = []  # this empty array is used for storing sorted file

        for i in name_sort:  # nested loop is used for matching sorted names to file
            for j in range(len(data)):
                if i == data[j]["first_name"]:
                    sorteddata.append(data[j])  # if name matches then data is appended

        self.data = sorteddata  # now we have swapped data with sorted data
        return sorteddata  # here we have return sorted data

    def dumping(self, filename):  # this function is used for dumping edited data to the json file
        with open('address_book_json', 'w') as f:
            json.dump(self.data, f, indent=2)

    def onlyNames(self):  # this function is used for printing only names from the file
        data = self.data
        for i in range(len(data)):

             print("**", (data[i]["first_name"]), end=" ")


