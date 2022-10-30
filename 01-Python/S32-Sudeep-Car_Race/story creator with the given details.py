from tkinter import *

a=Tk()
a.geometry("1500x500")
a.title("My First Application")

def clickme():
	x="once apon a time there was a boy ... his name is " + fentry.get() + "\nthe date today was " + dateentry.get() + "\nand guess what ... its his birthday \ntoday! his parents got him a " + emailentry.get() + "\nin his favirote color " + phonenumberentry.get() + "\nhe was very exited to go to the school today...he bought chocolates to distribute in school and by the way his school name was " + schoolentry.get() +	"he was in "+	gradeentry.get() + "\nth grade ... after the enjoying hours in school he came home and he was surprised thet \ntherir parents aranged a party for him .... he celebrated the party very very happily and he slept happily. " 
	extlabel.configure(text=x,font=("Arabic",15) , fg="red")

fname = Label(a, text="First Name: " )
fname.grid(row=1 , column=1)

fentry = Entry(a)
fentry.grid(row=1 , column=2)

lname = Label(a, text="Last Name: ")
lname.grid(row=2,column=1)

lentry = Entry(a)
lentry.grid(row=2,column=2)

emailname = Label(a, text="Favorite pet: ")
emailname.grid(row=3,column=1)

emailentry = Entry(a)
emailentry.grid(row=3,column=2)

schoolname = Label(a, text="School Name: ")
schoolname.grid(row=4,column=1)

schoolentry = Entry(a)
schoolentry.grid(row=4,column=2)

gradenumber = Label(a, text="Grade: ")
gradenumber.grid(row=5,column=1)

gradeentry = Entry(a)
gradeentry.grid(row=5,column=2)

phonenumbernumber = Label(a, text="Favorite Color: ")
phonenumbernumber.grid(row=6,column=1)

phonenumberentry = Entry(a)
phonenumberentry.grid(row=6,column=2)

birthdate = Label(a, text="Birthdate")

birthdate.grid(row=7,column=1)

datenumber = Label(a, text="Date: ")
datenumber.grid(row=8,column=1)

dateentry = Entry(a)
dateentry.grid(row=8,column=2)

btn=Button(a, text="Click Me",command= clickme)
btn.grid(row=9,column=2)

extlabel=Label(a)
extlabel.grid(row=10,column=2)



mainloop() 