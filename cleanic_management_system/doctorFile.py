# @import Error
try:
    import calendar
    import json
    import datetime
except ImportError:
    print("import Error")

"""
    @date   : 1/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""


# @doctor class
class Doctor(object):
    # @class level private variable
    __dId = None
    __dName = None
    __aval = None
    __spec = None

    def __init__(self, filename):
        with open(filename) as f:
            self.data = json.load(f)

    # @getter and setter method for doctor id
    def getDId(self):
        return self.__dId

    def setDId(self, dId):
        self.__dId = dId

    # @getter and setter for doctor name
    def getDName(self):
        return self.__dName

    def setDname(self, dName):
        self.__dName = dName

    # @getter and setter method for checking availability
    def getAvalable(self):
        return self.__aval

    def setAvalable(self, aval):
        self.__aval = aval

    # @getter and setter method for specification
    def getSpecialist(self):
        return self.__spec

    def setSpecialist(self, spec):
        self.__spec = spec

    def toString(self):
        jsonData = {"Id": self.getDId(), "name": self.getDName(), "avail": self.getAvalable(),
                    "spec": self.getSpecialist(),
                    "pCount": 0}
        return jsonData

    def write_into_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=2)

    """
    #@ this function is for add doctor
    """

    def addDoctor(self):
        print("Enter Your Details ...")
        self.dName = input("Enter the name:-------> ")
        self.setDname(self.dName)

        print()
        # print(self.dName)
        self.dId = input("Enter Id:------> ")
        self.setDId(self.dId)
        # print(self.dId)

        self.spec = input("Enter Specialization:-------> ")
        self.setSpecialist(self.spec)

        self.aval = input("Enter Availability (1:AM   2:PM  3:Both)")
        self.setAvalable(self.aval)

        z = self.data
        z.append(self.toString())
        self.write_into_file('doctors.json')



# @creating object of doctor class
doctor = Doctor('doctors.json')
