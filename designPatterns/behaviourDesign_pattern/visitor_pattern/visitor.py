"""
visitor pattern used for where group of element is there
"""
"""
    @date   : 11/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""

# @import statement
try:
    import abc
except ImportError:
    print("import error: ")


# @base class
class ItemElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept(self):
        pass


class ShoppingCartVisitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visit(self, item):
        pass


# @ class book inherit itemElement
class Book(ItemElement):
    def __init__(self, cost, isbn):
        self.price = cost
        self.isbn = isbn

    def get_price(self):
        return self.price

    def get_isbn(self):
        return self.isbn

    def accept(self, visitor):
        return visitor.visit(self)


#   @class fruits
class Fruit(ItemElement):
    def __init__(self, price, wt, nm):
        self.price = price
        self.weight = wt
        self.name = nm

    def get_price(self):
        return self.price

    def get_weight(self):
        return self.weight

    def get_name(self):
        return self.name

    def accept(self, visitor):
        return visitor.visit(self)


# @inherit the class for reducibility
class ShoppingCartVisitorImpl(ShoppingCartVisitor):
    def visit(self, item):
        if isinstance(item, Book):
            cost = 0
            # apply 5$ discount if book price is greater than 50
            if item.get_price() > 50:
                cost = item.get_price() - 5
            else:
                cost = item.get_price()
            print("Book ISBN:: {} cost = {}".format(item.get_isbn(), cost))
            return cost
        elif isinstance(item, Fruit):
            cost = item.get_price() * item.get_weight()
            print("{} cost = {}".format(item.get_name(), cost))
            return cost


# calculate function
def calculate_price(items):
    # calling ShoppingCartVisitorImpl
    visitor = ShoppingCartVisitorImpl()
    sum = 0
    # @iterating through items
    for item in items:
        sum = sum + item.accept(visitor)

    return sum


# @driver program
if __name__ == '__main__':
    items = [
        Book(20, "1234"),
        Book(100, "5678"),
        Fruit(10, 2, "Banana"),
        Fruit(5, 5, "Apple")
    ]

    # @calling the method using object
    total = calculate_price(items)
    print("Total Cost = {}".format(total))
