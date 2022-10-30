from tkinter import *

#CAPSTONE PROJECT ... CALCULATOR

a=Tk()
a.geometry("400x800")
a.resizable(0, 0)
a.title("CALCULATOR")

buttoncolor='skyblue'
windowcolor='darkblue'
textboxcolor='darkblue'


a.config(bg=windowcolor)



textin=StringVar()
operator=""



def clickbut(number):
	global operator
	operator=operator+str(number)
	textin.set(operator)

def equlbut():
	global operator
	eq=eval(operator)
	textin.set(eq)
	operator=''


def clrbut():
	global operator 
	textin.set('')
	operator=''
	entry1.insert(0,"0")

def backspace():
	length=len(entry1.get())
	entry1.delete(first=length-1,last=length)
	if length==1:
		global operator
		textin.set('')
		operator=''
		entry1.insert(0,"0")





entry1=Entry(a,font=("Courier New",16,'bold'),textvar=textin,width=29,bg=textboxcolor,justify=RIGHT)
entry1.place(x=10,y=60)

entry1.focus()




#b is button

b1=Button(a,padx=16,pady=7,bg=buttoncolor,command=lambda:clickbut(1),text="1",font=("Courier New",16 , 'bold'))
b1.place(x=10,y=100)

b2=Button(a,padx=16,pady=7,bg=buttoncolor,command=lambda:clickbut(2),text="2",font=("Courier New",16 , 'bold'))
b2.place(x=80,y=100)


b3=Button(a,padx=16,pady=7,bg=buttoncolor,command=lambda:clickbut(3),text="3",font=("Courier New",16 , 'bold'))
b3.place(x=150,y=100)


b4=Button(a,padx=16,pady=7,bg=buttoncolor,command=lambda:clickbut(4),text="4",font=("Courier New",16 , 'bold'))
b4.place(x=10,y=170)


b5=Button(a,padx=16,pady=7,bg=buttoncolor,command=lambda:clickbut(5),text="5",font=("Courier New",16 , 'bold'))
b5.place(x=80,y=170)


b6=Button(a,padx=16,pady=7,bg=buttoncolor,command=lambda:clickbut(6),text="6",font=("Courier New",16 , 'bold'))
b6.place(x=150,y=170)


b7=Button(a,padx=16,pady=7,bg=buttoncolor,command=lambda:clickbut(7),text="7",font=("Courier New",16 , 'bold'))
b7.place(x=10,y=240)


b8=Button(a,padx=16,pady=7,bg=buttoncolor,command=lambda:clickbut(8),text="8",font=("Courier New",16 , 'bold'))
b8.place(x=80,y=240)

b9=Button(a,padx=16,pady=7,bg=buttoncolor,command=lambda:clickbut(9),text="9",font=("Courier New",16 , 'bold'))
b9.place(x=150,y=240)


b10=Button(a,padx=16,pady=7,bg=buttoncolor,command=lambda:clickbut("00"),text="00",font=("Courier New",16 , 'bold'))
b10.place(x=10,y=310)

b11=Button(a,padx=14,pady=7,bg=buttoncolor,command=lambda:clickbut(0),text="0",font=("Courier New",16 , 'bold'))
b11.place(x=95,y=310)

b12=Button(a,padx=16,pady=7,bg=buttoncolor,command=backspace,text="⌫",font=("Courier New",16 , 'bold'))
b12.place(x=230,y=100)

b13=Button(a,padx=10,pady=7,bg=buttoncolor,command=lambda:clickbut("."),text=".",font=("Courier New",16 , 'bold'))
b13.place(x=160,y=310)

b14=Button(a,padx=16,pady=42,bg=buttoncolor,command=clrbut,text="CE",font=("Courier New",16 , 'bold'))
b14.place(x=230,y=170)

b15=Button(a,padx=22,pady=7,bg=buttoncolor,command=equlbut,text="=",font=("Courier New",16 , 'bold'))
b15.place(x=230,y=310)

b16=Button(a,padx=10,pady=7,bg=buttoncolor,command=lambda:clickbut("+"),text="+",font=("Courier New",16 , 'bold'))
b16.place(x=325,y=100)

b17=Button(a,padx=10,pady=7,bg=buttoncolor,command=lambda:clickbut("-"),text="-",font=("Courier New",16 , 'bold'))
b17.place(x=325,y=170)

b18=Button(a,padx=10,pady=7,bg=buttoncolor,command=lambda:clickbut("*"),text="×",font=("Courier New",16 , 'bold'))
b18.place(x=325,y=240)

b19=Button(a,padx=10,pady=7,bg=buttoncolor,command=lambda:clickbut("/"),text="÷",font=("Courier New",16 , 'bold'))
b19.place(x=325,y=310)



mainloop()
