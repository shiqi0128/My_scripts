# 第一次打印
# with open(r"F:\test\practise\ten\learning_python.txt") as file_object:
#     contents = file_object.read()
#     print(contents)


# 第二次打印
with open(r"F:\test\practise\ten\learning_python.txt") as file_object:
    for line in file_object:
        print(line.replace('Python', 'C').rstrip())

# 第三次打印
# with open(r"F:\test\practise\ten\learning_python.txt") as file_object:
#     lines = file_object.readlines()
# print(lines)



