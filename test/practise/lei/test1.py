# 9-4就餐人数
# 9-6 冰淇淋小店
class Restaurant():


    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("The most famous cuisine in " + self.restaurant_name.title() + " is " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + "正在营业")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['cool', 'hot', 'nice']
    
    def read_icenum(self):
        for a in self.flavors:
            print("My favourite tastes is " + a)
        

res1 = IceCreamStand('hagengdasi', 'chocolate')
res1.read_icenum()