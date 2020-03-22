from car import Car

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

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.ba = Battery()

