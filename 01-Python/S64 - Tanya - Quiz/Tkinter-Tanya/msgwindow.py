from tkinter import *
from tkinter import messagebox

win=Tk()

def click():
	messagebox.showinfo('Title info','Hello tkinter')

btn=Button(win,text='Click me',command=click)
btn.grid(row=0,column=0)

win.mainloop()