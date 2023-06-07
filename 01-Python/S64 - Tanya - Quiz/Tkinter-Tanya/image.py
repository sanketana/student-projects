from tkinter import *
from PIL import Image,ImageTk

win=Tk()
win.geometry('500x500')

image=Image.open('rose.jpg')
img=ImageTk.PhotoImage(image)
lbl=Label(image=img)
lbl.pack()

win.mainloop()