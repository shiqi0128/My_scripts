# 10-03访客
# filename = (r"F:\test\practise\ten\guest.txt")
# with open(filename, 'w') as file_object:
#     file_object.write(input("请输入用户名: "))

# 10-04访客名单
# filename = (r"F:\test\practise\ten\guest_book.txt")

# while True:
#     message = input("请输入用户名: ")
#     if message == 'quit':
#         break
#     else:
#         with open(filename, 'a') as file_object:
#             file_object.write(message + '\n')
#         print("Hello," + message + '!')

# 10-05关于编程的调查
filename = (r"F:\test\practise\ten\reason.txt")

while True:
    message = input("Why you like creat games? ")
    if message == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(message + '\n')
  
   