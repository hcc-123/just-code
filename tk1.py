from PIL import Image
from PIL import ImageTk
from tkinter import *
def callback():
    var.set('fuck you,get out of the way!')

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
var = StringVar()
var.set('what the hell?')
text1 = Label(frame1,
             textvariable = var,
              justify = LEFT,
              padx = 10)
text1.pack(side = LEFT)
photo = PhotoImage(file = '123.gif')
img = Label(frame1, image = photo)
img.pack(side = RIGHT)
button = Button(frame2, text = 'hi', command = callback)
button.pack()

frame1.pack(padx = 10, pady = 5)
frame2.pack(padx = 10, pady = 5)

mainloop()