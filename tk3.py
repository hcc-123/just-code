from tkinter import *

master = Tk()
'''
Label(root, text = '账号：').grid(row = 0, column = 0)
Label(root, text = '密码：').grid(row = 1, column = 0)

v1 = StringVar()
v2 = StringVar()

e1 = Entry(root, textvariable = v1)
e2 = Entry(root, textvariable = v2, show = '*')
e1.grid(row = 0, column = 1, padx = 10, pady = 5)
e2.grid(row = 1, column = 1, padx = 10, pady = 5)

def show():
    print('账号：%s' % e1.get())
    print('密码：%s' % e2.get())

Button(root, text = '获取',width = 10, command = show)\
    .grid(row = 3, column = 0, sticky = W, padx = 10, pady = 5)
Button(root, text = '退出', width = 10, command = root.quit)\
    .grid(row = 3, column = 1, sticky = E, padx = 10, pady = 5)
'''
frame = Frame(master)
frame.pack(padx = 10, pady = 10)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

def test(content):
    return content.isdigit()

testCMD = master.register(test)
e1 = Entry(frame, textvariable = v1, validate = 'key', validatecommand = (testCMD, '%P'), width = 10).gird(row = 0, column = 0)
Label(frame, text = '+').gird(row = 0, column = 1)
e2 = Entry(frame, textvariable = v2, validate = 'key', validatecommand = (testCMD, '%P'), width = 10).grid(row = 0, column = 2)
Label(frame, text = '=').grid(row = 0, column = 3)
e3 = Entry(frame, textvariable = v3, state = 'readonly', width = 10).gird(row = 0, column = 4)

def calc():
    result = int(v1.get()) + int(v2.get())
    v3.get(str(result))

Button(frame, text = '计算结果', command = calc)


mainloop()