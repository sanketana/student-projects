from tkinter import *
win=Tk()

win.geometry('320x500')
win.configure(bg='#e6ffee')


field_text=''

def clearr():
	global field_text
	field_text=''
	box.delete(0,END)

def button_click(num):
	global field_text
	field_text=field_text+str(num)
	box.delete(0,END)
	box.insert(0,field_text)

def equalto():
	global field_text
	result=str(eval(field_text))
	box.delete(0,END)
	box.insert(0,result)

''''''''''''''

lb=Label(win,text='CALCULATOR',font=('papyrus',(20)),bg='#e6ffee')
lb.place(x=30,y=25)

box=Entry(win,width=16,font=('papyrus', 24))
box.place(x=13,y=150)



btn1=Button(win,text='1',font=(10),width=7,height=2,command=lambda:button_click(1))
btn2=Button(win,text='2',font=(10),width=7,height=2,command=lambda:button_click(2))
btn3=Button(win,text='3',font=(10),width=7,height=2,command=lambda:button_click(3))
btn4=Button(win,text='4',font=(10),width=7,height=2,command=lambda:button_click(4))
btn5=Button(win,text='5',font=(10),width=7,height=2,command=lambda:button_click(5))
btn6=Button(win,text='6',font=(10),width=7,height=2,command=lambda:button_click(6))
btn7=Button(win,text='7',font=(10),width=7,height=2,command=lambda:button_click(7))
btn8=Button(win,text='8',font=(10),width=7,height=2,command=lambda:button_click(8))
btn9=Button(win,text='9',font=(10),width=7,height=2,command=lambda:button_click(9))
btn0=Button(win,text='0',font=(10),width=23,height=2,command=lambda:button_click(0))
add=Button(win,text='+',font=(10),width=7,height=2,bg='#b3ffcb',command=lambda:button_click('+'))
sub=Button(win,text='-',font=(10),width=7,height=2,bg='#b3ffcb',command=lambda:button_click('-'))
mult=Button(win,text='x',font=(10),width=7,height=2,bg='#b3ffcb',command=lambda:button_click('*'))
div=Button(win,text='÷',font=(10),width=7,height=2,bg='#b3ffcb',command=lambda:button_click('/'))
equal=Button(win,text='=',font=(10),width=7,height=2,bg='#80ffa8',command=lambda:equalto())
clear=Button(win,text='AC',font=(10),width=23,height=2,command=lambda:clearr())


btn1.place(x=15,y=380)
btn2.place(x=90,y=380)
btn3.place(x=165,y=380)
btn4.place(x=15,y=325)
btn5.place(x=90,y=325)
btn6.place(x=165,y=325)
btn7.place(x=15,y=270)
btn8.place(x=90,y=270)
btn9.place(x=165,y=270)
btn0.place(x=18,y=435)
add.place(x=240,y=270)
sub.place(x=240,y=325)
mult.place(x=240,y=380)
div.place(x=240,y=435)
equal.place(x=240,y=215)
clear.place(x=18,y=215)




win.mainloop()