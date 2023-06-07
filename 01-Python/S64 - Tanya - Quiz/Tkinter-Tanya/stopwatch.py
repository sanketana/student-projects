from tkinter import *
from datetime import datetime
win=Tk()

win.title('Stopwatch')
win.geometry('500x200')

lbl=Label(win,font=('Harrington',25),text='Stopwatch')
lbl.place(x=170,y=15)

counter=66600
running=False

def count():
	global running,counter
	if running == True:
		tt=datetime.fromtimestamp(counter)
		string=tt.strftime('%H:%M:%S')
		display=string
		lbl.config(text=display)
		lbl.after(10,count)
		counter=counter+1

def start():
	global running,counter
	running=True
	count()
	start.config(state=DISABLED)
	stop.config(state=NORMAL)
	reset.config(state=NORMAL)

def stop():
	global running
	running=False
	start.config(state=NORMAL)
	stop.config(state=DISABLED)
	reset.config(state=NORMAL)

def reset():
	global running,counter
	counter=66600
	running=False
	start.config(state=NORMAL)
	reset.config(state=DISABLED)
	stop.config(state=DISABLED)
	tt=datetime.fromtimestamp(counter)
	string=tt.strftime('%H:%M:%S')
	display=string
	lbl.config(text=display)

start=Button(win,font=('Times new roman',10),text='START',command=start)
start.place(x=80,y=80)

stop=Button(win,font=('Times new roman',10),text='STOP',state=DISABLED,command=stop)
stop.place(x=225,y=80)

reset=Button(win,font=('Times new roman',10),text='RESET',state=DISABLED,command=reset)
reset.place(x=370,y=80)


win.mainloop()