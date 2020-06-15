from tkinter import *
import hashlib
root = Tk()

text = Text(root, width = 30, height = 5, undo = True, autpseparators = False)
text.pack()
text.insert(INSERT, 'I love FishC.com!')
'''
text.insert(INSERT, 'I love FishC.com!')
contents = text.get('1.0', END)


def getSig(contents):
    m = hashlib.md5(contents.encode())
    return m.digest()

sig = getSig(contents)

def check():
    contents = text.get('1.0', END)
    if sig != getSig(contents):
        print('fuck off!')
    else:
        print('nothing changes')

Button(root, text = '检查', command = check).pack()
'''
text.bind('<Key>', callback)
def callback(event):
    text.edit_separator()

def show():
    text.edit_undo()
Button(root, text = '撤销', command = show).pack()
mainloop()