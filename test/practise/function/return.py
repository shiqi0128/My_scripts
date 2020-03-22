def name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + middle_name + last_name
    else:
        full_name = first_name + last_name
    return full_name.title()


a = name('jimi ', 'yoyo ', 'haha ')
print(a)    
a = name('jimi ', 'haha ')
print(a)

def name(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


a = name("jimi", "haha")
print(a)

def name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break
    

    a = name(f_name, l_name)
    print("\nHello, " + a + "!")

  8-6城市名
def city_country(name, country):
    c = name + ',' + country
    return c.title()

a = city_country("beijing", "China")
print(a)
a = city_country("new york", "america")
print(a)

8-7专辑
def make_album(singer_name, type_name, count=""):
    a = {'singer_name': singer_name, 'type_name': type_name}
    if count:
        a['count'] = count   # 添加字典中的键—值对
    return a

b = make_album(singer_name="张杰", type_name="逆战", count=10)
print(b)


8-8 用户的专辑
def make_album(singer_name, type_name):
    a = {'singer_name': singer_name, 'type_name': type_name}
    return a
while True:
    print("\n请输入歌手姓名： ")
    print("(enter 'q' at any time to quit)")
    print("\n请输入专辑名称： ")
    print("(enter 'q' at any time to quit)")

    s_name = input("singer_name: ")
    if s_name == 'q':
        break

    t_name = input("type_name: ")
    if t_name == 'q':
        break   
    b = make_album(s_name, t_name)
    print(b)