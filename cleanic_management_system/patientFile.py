import json

"""
    @date   : 1/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""


# class patient
class Patient(object):
    # @class level variable
    __pid = None
    __pName = None
    __age = None
    __mobile = None

    def __init__(self, filename):
        with open(filename) as f:
            self.data = json.load(f)

    # @getter and setter for Patient Id
    def getPId(self):
        return self.__pid

    def setPId(self, name):
        self.__pid = name

    # @getter and setter method for Patient name
    def getPName(self):
        return self.__pName

    def setPName(self, name):
        self.__pName = name

    # @getter and setter for age
    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    # @getter and setter for mobile no
    def getMobile(self):
        return self.__mobile

    def setMobile(self, mobile):
        self.__mobile = mobile

    # for printing
    def toString(self):
        jsonData = {"Id": self.getPId(), "name": self.getPName(), "age": self.getAge(), "mobile": self.getMobile(),
                    "DoctorId": ""}
        return jsonData

    def write_into_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=2)

    """
    this method is for add patient details
    """

    def addPatient(self):
        print("Enter Your Details ...")
        self.pName = input("Enter Name:------> ")
        self.setPName(self.pName)
        self.pid = input("Enter Id:----------> ")
        self.age = input("Enter Age:-----> ")
        self.setAge(self.age)
        self.setPId(self.pid)
        self.mobile = input("Enter Mobile:-----> ")
        self.setMobile(self.mobile)
        z = self.data
        z.append(self.toString())
        self.write_into_file('patients.json')


patient = Patient('patients.json')
