from tkinter import *
win=Tk()
btn=Button(win,text='red',width=15)
btn.grid(row=0,column=0)

btn1=Button(win,text='green',width=15)
btn1.grid(row=1,column=0)

btn2=Button(win,text='orange',width=15)
btn2.grid(row=2,column=0)

btn3=Button(win,text='white',width=15)
btn3.grid(row=3,column=0)

btn4=Button(win,text='yellow',width=15)
btn4.grid(row=4,column=0)

btn5=Button(win,text='blue',width=15)
btn5.grid(row=5,column=0)

btn6=Button(win,bg='red',width=15)
btn6.grid(row=0,column=1)

btn7=Button(win,bg='green',width=15)
btn7.grid(row=1,column=1)

btn8=Button(win,bg='orange',width=15)
btn8.grid(row=2,column=1)

btn9=Button(win,bg='white',width=15)
btn9.grid(row=3,column=1)

btn10=Button(win,bg='yellow',width=15)
btn10.grid(row=4,column=1)

btn11=Button(win,bg='blue',width=15)
btn11.grid(row=5,column=1)

win.mainloop()
