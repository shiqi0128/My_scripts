# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nfirst_number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nsecond_number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by zero!")
#     else:
#         print(answer)

# filename = 'alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = "Sorry, the file " + filename + " does not exist."
#     print(msg)


def count_words(filename):
    # 计算一个文件包含多少个单词
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = [r'F:\test\practise\ten\alice.txt', r'F:\test\practise\ten\siddhartha.txt', r'F:\test\practise\ten\guest.txt']
for filename in filenames:
    count_words(filename)
