"""   

   陪人聊天，每字1元，标点符号半价收费，千字八折！！！
   先付款，后聊天，款到即聊。网络虚假，若受伤、受骗、不承担任何责任！！！
   ID:   32622967
   NAME：匚匸
                           2020年03月27日 19时35分"""
'''一题.if循环的格式：
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
'''
'''二题：
break 语句可以跳出 for 和 while 的循环体。任何对应的循环 else 块将不执行
continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
'''
# 三题
a = int(input('请输入一个整数：'))
b = int(input('请输入一个整数：'))
c = int(input('请输入一个整数：'))
if a >= b and a >= c:
    print(a)
elif c >= b and c >= a:
    print(c)
else:
    print(b)
# 四题：判断是否为闰年
a = int(input("请输入有效的年份："))
if a % 4 == 0 and a % 100 != 0:
    print('{}年是闰年'.format(a))
else:
    print('{}年不是闰年'.format(a))
# 五题
list_day = ['周一', '周二', '周三', '周四', '周五', '周末', '周末']
while True:
    a = int(input('请输入一个整数：'))
    if 1 <= a <= 5:
        print('今天是{}'.format(list_day[a - 1]))
    elif 6 <= a <= 7:
        print('今天是{}'.format(list_day[a - 1]))
    elif a == 0:
        print('退出循环')
        break
    else:
        print('输出有误，请重新输入！！！')
# 六题。有道云：http://note.youdao.com/noteshare?id=2094367cbfacbab1d9be5b3c3c468270
# 选做。
i = 1
while i <= 9:
    j = 1
    while j < i + 1:
        print('{}*{}={}'.format(j, i, i * j), end=' ')
        j += 1
    print()
    i += 1
