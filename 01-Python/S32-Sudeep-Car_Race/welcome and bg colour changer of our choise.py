from tkinter import *
from tkinter.ttk import *

a=Tk()
a.geometry("700x700")
a.title("My First Application")



def clickme2():
	y=combo.get()
	a.configure(bg=y)
	fname.config(bg=y)
	lname.config(bg=y)
	
def clickme():
	x="Welcome " + fentry.get() 
	extlabel.configure(text=x)



btn=Button(a, text="Click Me",command=clickme)
btn.grid(row=3,column=2)

fname = Label(a, text="First Name: " )
fname.grid(row=1 , column=1)

fentry = Entry(a)
fentry.grid(row=1 , column=2)

lname = Label(a, text="Last Name: ")
lname.grid(row=2,column=1)

lentry = Entry(a)
lentry.grid(row=2,column=2)

extlabel=Label(a)
extlabel.grid(row=4,column=1)

comboname = Label(a, text="Favorite color: ")
comboname.grid(row=5,column=1)

combo=Combobox()
combo['values']=('red','orange','yellow','green','blue','indigo','violet','skyblue','lightgreen','navy','purple','cyan','brown','pink','darkblue',)
combo.grid(row=5,column=2)

btn2=Button(a, text="Click Me",command=clickme2)
btn2.grid(row=6,column=2)


mainloop()