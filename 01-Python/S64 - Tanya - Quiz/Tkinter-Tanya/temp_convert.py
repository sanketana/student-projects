from tkinter import *
win=Tk()
win.geometry('400x130')

title=Label(win,text='Temperature converter',font='algerian')
title.pack(fill=X,padx=100)

c=Label(win,text='Celsius',font=('kristen itc',10))
c.place(x=70,y=30)

f=Label(win,text='Fahrenheit',font=('kristen itc',10))
f.place(x=285,y=30)

box=Entry(win,width=15)
box.place(x=45,y=55)

box1=Entry(win,width=15)
box1.place(x=275,y=55)

def convert():
	celsius=box.get()
	fahrenheit=(float(celsius)*(9/5))+32
	box1.insert(0,fahrenheit)


btn=Button(win,text='Convert',font='harrington',command=convert)
btn.pack(fill=X,padx=150,pady=25)

win.mainloop()