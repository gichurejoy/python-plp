class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self.strength_level = strength_level

    def introduce(self):
        print(f"I am {self.name}, and my power is {self.power}!")

    def fight(self):
        print(f"{self.name} fights using {self.power} with a strength level of {self.strength_level}.")

class Villain(Superhero):
    def __init__(self, name, power, strength_level, evil_plan):
        super().__init__(name, power, strength_level)
        self.evil_plan = evil_plan

    def fight(self):
        print(f"{self.name} uses {self.power} to execute their evil plan: {self.evil_plan}!")

class Vehicle:
    def move(self):
        print("The vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("🚗 Car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ Plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚤 Boat is sailing on the water.")

def vehicle_test(vehicle):
    vehicle.move()

if __name__ == "__main__":
    print("Superhero")
    hero = Superhero("Photon Girl", "Light Beams", 85)
    villain = Villain("Dark Lord", "Shadow Control", 90, "Block out the sun")

    hero.introduce()
    hero.fight()

    villain.introduce()
    villain.fight()

    print("Vehicle")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        vehicle_test(v)
