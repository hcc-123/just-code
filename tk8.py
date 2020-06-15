from tkinter import *
root = Tk()
OPTIONS = [
    'California',
    '458',
    'FF',
    'ENZO',
    'LaFerrari'
]
'''
def callback():
    print('hi')

mb = Menubutton(root, text = 'kick me', relief = RAISED)
mb.pack()

filemenu = Menu(mb, tearoff = False)
filemenu.add_command(label = 'open', command = callback)
filemenu.add_command(label = 'save', command = callback)
filemenu.add_separator()
filemenu.add_command(label = 'quit', command = root.quit)
mb.config(menu = filemenu)
'''
variable = StringVar()
variable.set(OPTIONS[0])
w = OptionMenu(root, variable, *OPTIONS)
w.pack()


mainloop()