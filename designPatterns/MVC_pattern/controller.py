"""
Model View Controller is the most commonly used design pattern. Developers find it easy to implement this design pattern.

"""
"""
    @date   : 11/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""

# import view
try:
    from pythonProgram_bridgelabz.oops.designPatterns.MVC_pattern import view
    from pythonProgram_bridgelabz.oops.designPatterns.MVC_pattern.model import Person
except ImportError:
    print("module not found: ")


# @show all data
def showAll():
    # gets list of all Person objects
    people_in_db = Person.getAll()

    # calls view
    return view.showAllView(people_in_db)


# @start method for starting
def start():
    view.startView()
    inputs = input()
    if inputs == 'y':
        return showAll()
    else:
        return view.endView()


# @driver programs
if __name__ == "__main__":
    # running controller function
    start()
