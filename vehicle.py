class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The engine of the {self.year} {self.make} {self.model} is now running."

    def display_info(self):
        return f"Vehicle: {self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        return f"Car: {self.year} {self.make} {self.model} ({self.number_of_doors} doors)"

my_vehicle = Vehicle("generic", "transport", 2018)
my_car = Car("mecedes benz", "e220d", 2018, 4)

print(" pparent class behavior ")
print(my_vehicle.display_info())
print(my_vehicle.start_engine())

print("\n Child Class Behavior (inheritance & overriding) ")
print(my_car.display_info())      
print(my_car.start_engine())        
print("\n Relationship Verification ")
is_child = issubclass(Car, Vehicle)
print(f"Is Car a subclass of Vehicle? {is_child}")