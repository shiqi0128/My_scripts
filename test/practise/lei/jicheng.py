class Car():


    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make.title() + ' ' 
        long_name += self.model.title()
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
# my_new_car = Car("aodi", "a6", 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
# my_new_car.update_odometer(20)
# my_new_car.read_odometer()
# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23600)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.ba = Battery()

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def read_battery(self):
        print("This electric has " + str(self.battery_size))

    def get_rang(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)


my_tesal = ElectricCar('beijing', 'model S', 2016)
print(my_tesal.get_descriptive_name())
my_tesal.ba.read_battery()
my_tesal.ba.get_rang()



