class Restaurant():


    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("The most famous cuisine in " + self.restaurant_name.upper() + " is " + self.cuisine_type.title())

    def open_restaurant(self):
        print(" It's open now!")


# my_restaurant = Restaurant('KFC', 'Fast food')
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()