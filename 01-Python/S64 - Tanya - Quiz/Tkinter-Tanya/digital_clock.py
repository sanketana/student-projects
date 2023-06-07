from tkinter import *
from datetime import datetime
win=Tk()
win.title('Digital clock')

def update():
	now=datetime.now()
	current=now.strftime('%H:%M:%S')
	lbl.config(text=current)
	lbl.after(1000,update)

lbl=Label(win,font=('Times new roman',50,'bold'))
lbl.pack()

update()

win.mainloop()