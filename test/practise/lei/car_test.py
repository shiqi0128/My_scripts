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
        self.odometer_reading = mileage
        # if mileage >= self.odometer_reading:
        #     self.odometer_reading = mileage
        # else:
        #     print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
# my_new_car = Car("aodi", "a6", 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
# my_new_car.update_odometer(20)
# my_new_car.read_odometer()
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23600)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# 9-4就餐人数
class Restaurant():


    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("The most famous cuisine in " + self.restaurant_name.title() + " is " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + "正在营业")

    def read_number(self):
        print("There are " + str(self.number_served) + " had been in " + self.restaurant_name)


res1 = Restaurant('小南国', 'sweet')
res2 = Restaurant('点都德', 'well')
res3 = Restaurant('海底捞', 'hot')

print("The restaurant's name is " + res1.restaurant_name.title()) 
print("The delicious food is " + res1.cuisine_type.title())
res1.describe_restaurant()
res1.open_restaurant()

print("The restaurant's name is " + res2.restaurant_name.title()) 
print("The delicious food is " + res2.cuisine_type.title())
res2.describe_restaurant()
res2.open_restaurant()

print("The restaurant's name is " + res3.restaurant_name.title()) 
print("The delicious food is " + res3.cuisine_type.title())
res3.describe_restaurant()
res3.open_restaurant()
res3.number_served = 500
res3.read_number()