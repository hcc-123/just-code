from tkinter import *

root = Tk()

t = Text(root, width = 30, height = 30)
t.pack()

photo = PhotoImage(file = '2020.gif')

def show():
    t.image_create(END, image = photo)

b1 = Button(t, text = '点我点我', command = show)
t.window_create(INSERT, window = b1)

mainloop()