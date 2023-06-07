from tkinter import *
win=Tk()

lb1=Label(win,text=' ')
lb1.grid(row=1,column=0)

def click():
	#lb1.config(text='Button has been clicked')
	x='Welcome to '+txt.get()
	txt.delete(0,END)
	lb1.config(text=x)

btn=Button(win,text='Enter',bg='#FF0498',command=click)
btn.grid(row=0,column=0)

txt=Entry(win,width=10,state=DISABLED)
txt.grid(row=1,column=1)
txt.get()

win.mainloop()