from car import Car


my_tesal = ElectricCar('beijing', 'model S', 2016)
print(my_tesal.get_descriptive_name())
my_tesal.ba.read_battery()
my_tesal.ba.get_rang()