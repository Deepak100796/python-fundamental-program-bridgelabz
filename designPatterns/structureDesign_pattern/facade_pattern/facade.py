"""
Facade design pattern provides a unified interface to a set of interfaces in a subsystem.
It defines a higher-level interface that any subsystem can use.

A facade class knows which subsystem is responsible for a request.
"""

"""
    @date   : 11/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""


# class _IgnitionSystem
class _IgnitionSystem(object):

    @staticmethod
    def produce_spark():
        return True


# @class engine to start
class _Engine(object):
    # @constructor
    def __init__(self):
        self.revs_per_minute = 0

    def turnon(self):
        self.revs_per_minute = 2000

    def turnoff(self):
        self.revs_per_minute = 0


# @_FuelTank
class _FuelTank(object):

    # @constructor
    def __init__(self, level=30):
        self._level = level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level


# Class _DashBoardLight
class _DashBoardLight(object):
    # @constructor

    def __init__(self, is_on=False):
        self._is_on = is_on

    # string representation
    def __str__(self):
        return self.__class__.__name__

    @property
    def is_on(self):
        return self._is_on

    @is_on.setter
    def is_on(self, status):
        self._is_on = status
    #      @check status of engine
    def status_check(self):
        if self._is_on:
            print("{}: ON".format(str(self)))
        else:
            print("{}: OFF".format(str(self)))


# @class declaration
class _HandBrakeLight(_DashBoardLight):
    pass


class _FogLampLight(_DashBoardLight):
    pass


class _Dashboard(object):
    # @constructor

    def __init__(self):
        self.lights = {"handbreak": _HandBrakeLight(), "fog": _FogLampLight()}

    # @showing states
    def show(self):
        for light in self.lights.values():
            light.status_check()


# Facade
class Car(object):

    # @constructor facade
    def __init__(self):
        # Creating object of _IgnitionSystem,_Engine,_FuelTank,_Dashboard
        self.ignition_system = _IgnitionSystem()
        self.engine = _Engine()
        self.fuel_tank = _FuelTank()
        self.dashboard = _Dashboard()

    @property
    def km_per_litre(self):
        return 17.0

    def consume_fuel(self, km):
        litres = min(self.fuel_tank.level, km / self.km_per_litre)
        self.fuel_tank.level -= litres

    # @for starting yhe engine
    def start(self):
        print("\nStarting...")
        self.dashboard.show()
        if self.ignition_system.produce_spark():
            self.engine.turnon()
        else:
            print("Can't start. Faulty ignition system")

    def has_enough_fuel(self, km, km_per_litre):
        litres_needed = km / km_per_litre
        if self.fuel_tank.level > litres_needed:
            return True
        else:
            return False

# @drive for km=100
    def drive(self, km=100):
        print("\n")
        if self.engine.revs_per_minute > 0:
            while self.has_enough_fuel(km, self.km_per_litre):
                self.consume_fuel(km)
                print("Drove {}km".format(km))
                print("{:.2f}l of fuel still left".format(self.fuel_tank.level))
        else:
            print("Can't drive. The Engine is turned off!")

    # @parking ,ethod
    def park(self):
        print("\nParking...")
        self.dashboard.lights["handbreak"].is_on = True
        self.dashboard.show()
        self.engine.turnoff()

#  @switch light
    def switch_fog_lights(self, status):
        print("\nSwitching {} fog lights...".format(status))
        boolean = True if status == "ON" else False
        self.dashboard.lights["fog"].is_on = boolean
        self.dashboard.show()

    # @tank filled using this
    def fill_up_tank(self):
        print("\nFuel tank filled up!")
        self.fuel_tank.level = 100


# @ main method
def main():
    # @creating object
    car = Car()
    car.start()
    car.drive()
    car.switch_fog_lights("ON")
    car.switch_fog_lights("OFF")
    car.park()
    car.fill_up_tank()
    car.drive()
    car.start()
    car.drive()


# @driver method
if __name__ == "__main__":
    main()
