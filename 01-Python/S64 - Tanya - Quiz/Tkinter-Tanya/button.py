from tkinter import *
win=Tk()
btn=Button(win,text='Row 0\nColumn 0')
btn.grid(row=0,column=0)
btn.place(x=5,y=5)

btn1=Button(win,text='Row 0\nColumn 1')
btn1.grid(row=0,column=1)
btn1.place(x=75,y=5)

btn2=Button(win,text='Row 0\nColumn 2')
btn2.grid(row=0,column=2)
btn2.place(x=145,y=5)

btn3=Button(win,text='Row 0\nColumn 3')
btn3.grid(row=0,column=3)
btn3.place(x=215,y=5)

btn4=Button(win,text='Row 1\nColumn 0')
btn4.grid(row=1,column=0)
btn4.place(x=5,y=50)

btn5=Button(win,text='Row 2\nColumn 0')
btn5.grid(row=2,column=0)
btn5.place(x=5,y=95)

btn6=Button(win,text='Row 3\nColumn 0')
btn6.grid(row=3,column=0)
btn6.place(x=5,y=140)

btn7=Button(win,text='Row 1\nColumn 1')
btn7.grid(row=1,column=1)
btn7.place(x=75,y=50)

btn8=Button(win,text='Row 1\nColumn 2')
btn8.grid(row=1,column=2)
btn8.place(x=145,y=50)

btn9=Button(win,text='Row 1\nColumn 3')
btn9.grid(row=1,column=3)
btn9.place(x=215,y=50)

btn10=Button(win,text='Row 2\nColumn 1')
btn10.grid(row=2,column=1)
btn10.place(x=75,y=95)

btn11=Button(win,text='Row 2\nColumn 2')
btn11.grid(row=2,column=2)
btn11.place(x=145,y=95)

btn12=Button(win,text='Row 2\nColumn 3')
btn12.grid(row=2,column=3)
btn12.place(x=215,y=95)

btn13=Button(win,text='Row 3\nColumn 1')
btn13.grid(row=3,column=1)
btn13.place(x=75,y=140)

btn14=Button(win,text='Row 3\nColumn 2')
btn14.grid(row=3,column=2)
btn14.place(x=145,y=140)

btn15=Button(win,text='Row 3\nColumn 3')
btn15.grid(row=3,column=3)
btn15.place(x=215,y=140)


win.mainloop()