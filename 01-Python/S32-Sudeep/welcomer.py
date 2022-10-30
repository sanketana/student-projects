from tkinter import *
from tkinter.ttk import *

a=Tk()
a.geometry("700x700")
a.title("My First Application")

def clickme():
	x="Welcome " + fentry.get() 
	extlabel.configure(text=x)

fname = Label(a, text="First Name: " )
fname.grid(row=1 , column=1)

fentry = Entry(a)
fentry.grid(row=1 , column=2)

lname = Label(a, text="Last Name: ")
lname.grid(row=2,column=1)

lentry = Entry(a)
lentry.grid(row=2,column=2)

btn=Button(a, text="Click Me",command=clickme)
btn.grid(row=3,column=2)

extlabel=Label(a)
extlabel.grid(row=4,column=1)



mainloop()