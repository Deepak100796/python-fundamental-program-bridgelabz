"""
Define an object that encapsulates how a set of objects interact.
Mediator promotes loose coupling by keeping objects from referring to
each other explicitly, and it lets you vary their interaction
independently.

"""
"""
    @date   : 11/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""

# class MEDIATOR
class Mediator:

    # @CONSTRUCTOR
    def __init__(self):
        # @taking two object
        self._colleague_1 = Colleague1(self)
        self._colleague_2 = Colleague2(self)


# @class Colleague1
class Colleague1:

    # @CONSTRUCTOR
    def __init__(self, mediator):
        self._mediator = mediator


# @class Colleague1
class Colleague2:

    # @CONSTRUCTOR
    def __init__(self, mediator):
        self._mediator = mediator


#  Main
def main():
    mediator = Mediator()


# driver file
if __name__ == "__main__":
    main()
