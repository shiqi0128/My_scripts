# 10-06加法运算
# print("Please write down two numbers, we'll add them.") 
# print("Please enter 'q' to quit!")

# while True:
#     try:
#         first_number = int(input("First number: "))
#     except ValueError:
#         pass
#     else:
#         if first_number == 'q':
#             break
#     try:
#         second_number = int(input("Second number: "))
#     except ValueError:
#         pass
#     else:
#         if second_number == 'q':
#             break
#         answer = int(first_number) + int(second_number)
#         print(answer)

# 10-08猫和狗
# filename1 = 'F:\test\practise\ten\cats.txt'
# filename2 = 'F:\test\practise\ten\dogs.txt'
# while True:
#         open_filename = input("Please input a file to open it.\nEnter \'q\' to quit.")
#         if open_filename == 'q':
#             break
#         try:
#             with open(open_filename) as file_object:
#                 contents = file_object.read()
#         except FileNotFoundError:
#             print("Sorry, I can't find your file")
#         else:
#             print(contents)
# 10-09沉默的猫和狗
# while True:
#         open_filename = input("Please input a file to open it.\nEnter \'q\' to quit.")
#         if open_filename == 'q':
#             break
#         try:
#             with open(open_filename) as file_object:
#                 contents = file_object.read()
#         except FileNotFoundError:
#             pass
#         else:
#             print(contents)

# 10-10 常见单词
filename = r"F:\test\practise\ten\row.txt"
with open(filename) as file_object:
    contents = file_object.read()

print('r"F:\test\practise\ten\row.txt" use \'row\' for ' + str(contents.count('row')) + " times.")


