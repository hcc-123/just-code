from tkinter import *
import math as m
root = Tk()

w = Canvas(root, width = 200, height = 100)
w.pack()
centre_x = 100
centre_y = 50
r = 50
points = [
    centre_x - int(r * m.sin(2 * m.pi / 5)),
    centre_y - int(r * m.cos(2 * m.pi / 5)),
    centre_x + int(r * m.sin(2 * m.pi / 5)),
    centre_y - int(r * m.cos(2 * m.pi / 5)),
    centre_x - int(r * m.sin(m.pi / 5)),
    centre_y + int(r * m.cos(m.pi / 5)),
    centre_x,
    centre_y - r,
    centre_x + int(r * m.sin(m.pi / 5)),
    centre_y + int(r * m.cos(m.pi / 5))

]
w.create_polygon(points, outline = '', fill = 'pink')

mainloop()