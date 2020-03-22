import json

def greet_user():
    filename = r'F:\test\practise\ten\username.json'
    try:
        with open(filename) as f_obj:
            print(f_obj)
            username = json.load(f_obj)
            print(type(username))
    except OSError as f:
        username = input("What's your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
        print(f)
    else:
        print("Welcome back, " + username)
        

greet_user()