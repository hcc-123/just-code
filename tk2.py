from tkinter import *

root = Tk()
'''
girls = ['西施', '貂蝉', '王昭君', '杨贵妃']

v = []
for girl in girls:
    v.append(IntVar())
    b = Checkbutton(root, text = girl, variable = [-1])
    b.pack(anchor = W)
'''
group = LabelFrame(root, text = '最好的脚本语言是？', padx = 5, pady = 5)
group.pack(padx = 10, pady = 10)

LANGS = [
    ('python, 1'),
     ('ruby', 2),
    ('ruby', 3),
    ('lua', 4)]

v = IntVar()

for key, num in LANGS:
    b = Radiobutton(group, text = key, vairable = v, value = num)
    b.pack(anchor = W)

mainloop()
