# class Dog():
#     """一次模拟小狗的简单尝试"""
#     def __init__
# 9-1 餐馆   # 9-2 三家餐馆
# class Restaurant():


#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
    
#     def describe_restaurant(self):
#         print("The most famous cuisine in " + self.restaurant_name.title() + " is " + self.cuisine_type.title())

#     def open_restaurant(self):
#         print(self.restaurant_name.title() + "正在营业")


# res1 = Restaurant('小南国', 'sweet')
# res2 = Restaurant('点都德', 'well')
# res3 = Restaurant('海底捞', 'hot')

# print("The restaurant's name is " + res1.restaurant_name.title()) 
# print("The delicious food is " + res1.cuisine_type.title())
# res1.describe_restaurant()
# res1.open_restaurant()

# print("The restaurant's name is " + res2.restaurant_name.title()) 
# print("The delicious food is " + res2.cuisine_type.title())
# res2.describe_restaurant()
# res2.open_restaurant()

# print("The restaurant's name is " + res3.restaurant_name.title()) 
# print("The delicious food is " + res3.cuisine_type.title())
# res3.describe_restaurant()
# res3.open_restaurant()

# 9-3 用户
class User():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def describe_user(self):
        print("I'm " + self.first_name + self.last_name + ',')
        print("I'm " + " a " + self.sex)
        print("I'm " + str(self.age))

    def greet_user(self):
        print("Hello" + "," + " pretty girl " + self.first_name + self.last_name)

user1 = User("王", "若若", "girl", 18)
user2 = User("王", "一一", "girl", 28)
user3 = User("王", "大大", "girl", 38)

print("\nMy name is " + user1.first_name + user1.last_name + "," + "I'm a " + str(user1.age) + " pretty " + user1.sex)
user1.describe_user()
user1.greet_user()

print("\nMy name is " + user2.first_name + user2.last_name + "," + "I'm a " + str(user2.age) + " pretty " + user2.sex)
user2.describe_user()
user2.greet_user()

print("\nMy name is " + user3.first_name + user3.last_name + "," + "I'm a " + str(user3.age) + " pretty " + user3.sex)
user3.describe_user()
user3.greet_user()
