 1 # messagebox:消息弹框
 2 # 不断点击按钮，切换各种弹窗
 3 import tkinter as tk
 4 from tkinter import messagebox
 5 from tk_center_win import set_win_center
 6 
 7 root = tk.Tk()
 8 root.title('消息框')
 9 root.geometry('190x80+300+300')  # 设置窗口大小和位置
10 # set_win_center(root, 190, 80)  # 设置窗口大小并居中显示
11 n = 0
12 str_var = tk.StringVar()
13 str_var.set('askokcancel')
14 
15 
16 def cmd():
17     '''弹框提示'''
18     global n
19     global str_var
20     n += 1
21     if n == 1:
22         r = messagebox.askokcancel('消息框', 'askokcancel')
23         print('askokcancel:', r)
24         str_var.set('askquestion')
25     elif n == 2:
26         r = messagebox.askquestion('消息框', 'askquestion')
27         print('askquestion:', r)
28         str_var.set('askyesno')
29     elif n == 3:
30         r = messagebox.askyesno('消息框', 'askyesno')
31         print('askyesno:', r)
32         str_var.set('askretrycancel')
33     elif n == 4:
34         r = messagebox.askretrycancel('消息框', 'askretrycancel')
35         print('askretrycancel:', r)
36         str_var.set('showerror')
37     elif n == 5:
38         r = messagebox.showerror('消息框', 'showerror')
39         print('showerror:', r)
40         str_var.set('showinfo')
41     elif n == 6:
42         r = messagebox.showinfo('消息框', 'showinfo')
43         print('showinfo:', r)
44         str_var.set('showwarning')
45     else:
46         r = messagebox.showwarning('消息框', 'showwarning')
47         print('showwarning:', r)
48         str_var.set('askokcancel')
49         n = 0
50 
51 
52 label = tk.Label(root, text='不断点击按钮，切换各种弹窗', font='宋体 -14', pady=8)
53 label.grid()
54 btn = tk.Button(root, width='15', textvariable=str_var, command=cmd)
55 btn.grid()
56 
57 root.mainloop()