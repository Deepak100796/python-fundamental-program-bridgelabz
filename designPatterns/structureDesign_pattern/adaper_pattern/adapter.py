"""
This design pattern relies on object implementation. Hence, it is called the Object Adapter Pattern.
Class Adapter Pattern

This is an alternative way to implement the adapter design pattern.
The pattern can be implemented using multiple inheritances.
"""

"""
    @date   : 11/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""


#  @class EuropeanSocketInterface
class EuropeanSocketInterface:

    # abstact method for hidding implementation
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass

    def earth(self): pass


# Adapter
class Socket(EuropeanSocketInterface):
    def voltage(self):
        return 230

        def live(self):
            return 1


def neutral(self):
    return -1


def earth(self):
    return 0


# Target interface
class USASocketInterface:
    # abstact method for hidding implementation

    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass


# The Adapter
class Adapter(USASocketInterface):
    __socket = None

    # @constructor
    def __init__(self, socket):
        self.__socket = socket

    # @voltage
    def voltage(self):
        return 110

    # @for live
    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()


# Client
class ElectricKettle:
    __power = None

    # @for constructor

    def __init__(self, power):
        self.__power = power

    def boil(self):
        if self.__power.voltage() > 110:
            print(
                "Kettle on fire!")
        else:
            if self.__power.live() == 1 and \
                    self.__power.neutral() == -1:
                print(
                    "Coffee time!")
            else:
                print("No power.")


# @main method
def main():
    # Plug in
    socket = Socket()
    adapter = Adapter(socket)
    kettle = ElectricKettle(adapter)

    # Make coffee
    kettle.boil()

    return 0


# @driver class

if __name__ == "__main__":
    main()
