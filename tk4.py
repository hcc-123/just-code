from tkinter import *
root = Tk()
'''
theB = Listbox(master, selectmode = EXTENDED)
theB.pack()

for item in range(11):
    theB.insert(END, item)
'''
'''
sb = Scrollbar(root)
sb.pack(side = RIGHT, fill = Y)

lb = Listbox(root, yscrollcommand = sb.set)

for i in range(1000):
    lb.insert(END, i)

lb.pack(side = LEFT, fill = BOTH)

sb.config(command = lb.yview)
'''
s1 = Scale(root, from_ = 0, to =150, tickinterval = 5, resolution = 5, length = 200)
s1.pack()

s2 = Scale(root, from_ = 0, to = 200, tickinterval = 10, orient = HORIZONTAL, length = 600)
s2.pack()

def show():
    print(s1.get(), s2.get())

Button(root, text = '获取位置', command = show).pack()

mainloop()