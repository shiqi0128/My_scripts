name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
prompt += "\nWhat's your first name: "
name = input(prompt)
print("\nHello, " + name + "!")

height = input("How tall are you,in inches?")
height = int(height)

if height >= 36:
  print("\nYou're tall enough to ride!")
else:
  print("\nYou'll be able to ride when you're a little older.")


number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
   print("\nThe number " + str(number) + " is even.")
else:
   print("\nThe number " + str(number) + " is odd.")

汽车租赁
message = input("What kind of car would you like to rent: ")
print("Let me see if I can find you a " + message + ".")
餐位定位
people = input("How many people,please: ")
people = int(people)

if people > 8:
   print("\nno seats")
else:
   print("\nhave seats")
10的整数倍
number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + "是10的倍数.")
else:
    print(str(number) + "不是10的倍数.")