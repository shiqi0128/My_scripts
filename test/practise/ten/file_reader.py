# with open('reason.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# filename = 'F:/test/practise/ten/pi.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())


# filename = 'F:/test/practise/ten/pi.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))

# filename = 'F:/test/practise/ten/pi_million_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# birthay = input("Enter your birthday, in the form mmddyy: ")  
# if birthay in pi_string:
#     print("Your birthday appears in the first million digits of pi!")  
# else:
#     print("Your birth does not appear in the first million digits of pi.")

# print(pi_string[:52] + "...")
# print(len(pi_string))
#
# import os
#
# print(os.getcwd())
import os

# a = os.path.split(r'F:\test\practise\ten\dogs.txt')
# print(a)
# b = os.path.join(r'f:\\', 'test', r'practise\ten\dogs.txt')
# print(b)

with open('reason.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
        print(line.strip())

