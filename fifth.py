# Create a SpaceX class.
# it should take 1 parameter in its constructor: the stored fuel
#
# it should have 4 methods:
#
# addRocket(rocket)
# it should add a new rocket to SpaceX that is given in its first parameter
# use the rockets from the fourth exercise.
#
# refill_all()
# it should refill all of its rockets with fuel and substract the needed fuel from the storage
#
# launch_all()
# it should launch all the rockets
#
# buy_fuel(amount)
# it should increase stored fuel by amount
#
# getStats()
# it should return its stats as a sting like: "rockets: 3, fuel: 100, launches: 1"

from fourth import Rocket

class SpaceX:

    def __init__(self, stored_fuel):
        self.stored_fuel = stored_fuel
        self.fleet = []
        self.launches = 0
        self.rocket = Rocket()

    def addRocket(self, rocket_type):
        self.fleet.append(Rocket(rocket_type))

    def refill_all(self):
        for _ in self.fleet:
            self.stored_fuel -= self.rocket.refill()

    def launch_all(self):
        for _ in self.fleet:
            self.rocket.launch()
            self.launches += 1

    def buy_fuel(self, amount):
        self.stored_fuel += amount

    def getStats(self):
        return "rockets: {}, fuel: {}, launches: {}".format(len(self.fleet), self.stored_fuel, self.launches)


################################################

# The following code should work with the class:

# class implementation goes here

space_x = SpaceX(100)
falcon1 = Rocket('falcon1', 0, 0)
falcon9 = Rocket('falcon9', 0, 0)
returned_falcon9 = Rocket('falcon9', 11, 1)

print(returned_falcon9.getStats()) # name: falcon9, fuel: 11

space_x.addRocket(falcon1)
space_x.addRocket(falcon9)
space_x.addRocket(returned_falcon9)

print(space_x.getStats()) # rockets: 3, fuel: 100, launches: 1
space_x.refill_all()
print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 1
space_x.launch_all()
print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 4
space_x.buy_fuel(50)
print(space_x.getStats()) # rockets: 3, fuel: 116, launches: 4
