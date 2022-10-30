from tkinter import *

a=Tk()
a.geometry("700x700")
a.title("My First Application")

def clickme():
	fname.configure(bg="orangered",fg="blue",font=("times", 30))
	lname.configure(bg="orangered",fg="blue",font=("times", 30))
	fentry.configure(bg="yellow",fg="blue",font=("times", 30))
	lentry.configure(bg="yellow",fg="blue",font=("times", 30))

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


mainloop()