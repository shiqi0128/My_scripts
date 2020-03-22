a = "\nPlease enter the name of a city you have visited: "
a += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(a)

    if city == 'quit':
        break
    else:
            print("I'd love to go to " + city.title() + "!")