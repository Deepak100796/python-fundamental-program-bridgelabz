"""
singleton------>: This pattern restricts the instantiation of a class to one object.
 It is a type of creations pattern and involves only one class to create methods and specified objects.
"""

"""
The following program demonstrates the implementation 
of singleton class where it prints the instances created multiple times.
"""

"""
    @date   : 11/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""

class Singleton:
    # @ class level variable
    __instance = None

    @staticmethod

   # """ Static access method. """
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

s = Singleton()
print(s)

s = Singleton.getInstance()
print (s)
s = Singleton.getInstance()
print (s)

