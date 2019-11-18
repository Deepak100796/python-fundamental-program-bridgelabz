# this class represent the model structure ihn MVC


try:
    import json
except ImportError:
    print("import error please check your import statement:  ")


# @Person class
class Person(object):

    # @constructor for object initialization
    def __init__(self, firstName=None, lastName=None):
        # @object initialization
        self.firstName = firstName
        self.lastName = lastName

    # @returns Person name, ex: John Doe
    def name(self):
        return "%s %s" % (self.firstName, self.lastName)

    @classmethod
    # returns all people inside db.txt as list of Person objects

    def getAll(cls):
        # @open json file from file system
        with open("name.json") as f:
            json_list = json.load(f)
        result = []
        # @load the data
        # json_list = json.loads(dataBase.read())
        # @iterating to the json file
        for name in json_list:

            person = Person(name['firstName'], name['lastName'])
            result.append(person)
        return result
