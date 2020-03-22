 def power(x):
    return x * x

print(power(10))


def display_message():
    # 函数章节
    print("函数章节")


display_message()


def favourite_book(title):
    print("One of my favourite：" + title.title())


favourite_book('dfhgfj小王子')


def describe_pet(pet_name, animal_type='dog'):
    # 显示宠物的信息
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='harry')
describe_pet(pet_name="Tom")
describe_pet(pet_name="fanfan")
