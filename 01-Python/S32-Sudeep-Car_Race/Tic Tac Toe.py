from tkinter import *
import tkinter.messagebox as msg



root=Tk()
root.title("Tic-Tac-Toe")

digits=[1,2,3,4,5,6,7,8,9]
mark=""
count=0
panels=["panel"]*10

def win(panels,sign):
    return ((panels[1] == panels[2] == panels [3] == sign)
            or (panels[1] == panels[4] == panels [7] == sign)
            or (panels[1] == panels[5] == panels [9] == sign)
            or (panels[2] == panels[5] == panels [8] == sign)
            or (panels[3] == panels[6] == panels [9] == sign)
            or (panels[3] == panels[5] == panels [7] == sign)
            or (panels[4] == panels[5] == panels [6] == sign) 
            or (panels[7] == panels[8] == panels [9] == sign))
def checker(digit):
	global count,mark,digits
	if digit==1 and digit in digits:
		digits.remove(digit)
		if count%2==0:
			mark="X"
			panels[digit]=mark
			bgn="green"
		elif count%2!=0:
			mark="O"
			panels[digit]=mark
			bgn="yellow"
		b1.config(text=mark)
		b1.config(bg=bgn)
		count=count+1
		sign=mark
		if(win(panels,sign) and sign == "X"):
			msg.showinfo("Result","Player 1 wins")
			root.destroy()

		elif(win(panels,sign) and sign == "O"):
			msg.showinfo("Result","Player 2 wins")
			root.destroy()
		

	if digit==2 and digit in digits:
		digits.remove(digit)
		if count%2==0:
			mark="X"
			panels[digit]=mark
			bgn="green"
		elif count%2!=0:
			mark="O"
			panels[digit]=mark
			bgn="yellow"
		b2.config(text=mark)
		b2.config(bg=bgn)
		count=count+1
		sign=mark
		if(win(panels,sign) and sign == "X"):
			msg.showinfo("Result","Player 1 wins")
			root.destroy()

		elif(win(panels,sign) and sign == "O"):
			msg.showinfo("Result","Player 2 wins")
			root.destroy()

	if digit==3 and digit in digits:
		digits.remove(digit)
		if count%2==0:
			mark="X"
			panels[digit]=mark
			bgn="green"
		if count%2!=0:
			mark="O"
			panels[digit]=mark
			bgn="yellow"
		b3.config(text=mark)
		b3.config(bg=bgn)
		count=count+1
		sign=mark
		if(win(panels,sign) and sign == "X"):
			msg.showinfo("Result","Player 1 wins")
			root.destroy()

		elif(win(panels,sign) and sign == "O"):
			msg.showinfo("Result","Player 2 wins")
			root.destroy()

	if digit==4 and digit in digits:
		digits.remove(digit)
		if count%2==0:
			mark="X"
			panels[digit]=mark
			bgn="green"
		elif count%2!=0:
			mark="O"
			panels[digit]=mark
			bgn="yellow"
		b4.config(text=mark)
		b4.config(bg=bgn)
		count=count+1
		sign=mark
		if(win(panels,sign) and sign == "X"):
			msg.showinfo("Result","Player 1 wins")
			root.destroy()

		elif(win(panels,sign) and sign == "O"):
			msg.showinfo("Result","Player 2 wins")
			root.destroy()

	if digit==5 and digit in digits:
		digits.remove(digit)
		if count%2==0:
			mark="X"
			panels[digit]=mark
			bgn="green"
		elif count%2!=0:
			mark="O"
			panels[digit]=mark
			bgn="yellow"
		b5.config(text=mark)
		b5.config(bg=bgn)
		count=count+1
		sign=mark
		if(win(panels,sign) and sign == "X"):
			msg.showinfo("Result","Player 1 wins")
			root.destroy()

		elif(win(panels,sign) and sign == "O"):
			msg.showinfo("Result","Player 2 wins")
			root.destroy()

	if digit==6 and digit in digits:
		digits.remove(digit)
		if count%2==0:
			mark="X"
			panels[digit]=mark
			bgn="green"
		elif count%2!=0:
			mark="O"
			panels[digit]=mark
			bgn="yellow"
		b6.config(text=mark)
		b6.config(bg=bgn)
		count=count+1
		sign=mark
		if(win(panels,sign) and sign == "X"):
			msg.showinfo("Result","Player 1 wins")
			root.destroy()

		elif(win(panels,sign) and sign == "O"):
			msg.showinfo("Result","Player 2 wins")
			root.destroy()

	if digit==7 and digit in digits:
		digits.remove(digit)
		if count%2==0:
			mark="X"
			panels[digit]=mark
			bgn="green"
		elif count%2!=0:
			mark="O"
			panels[digit]=mark
			bgn="yellow"
		b7.config(text=mark)
		b7.config(bg=bgn)
		count=count+1
		sign=mark
		if(win(panels,sign) and sign == "X"):
			msg.showinfo("Result","Player 1 wins")
			root.destroy()

		elif(win(panels,sign) and sign == "O"):
			msg.showinfo("Result","Player 2 wins")
			root.destroy()

	if digit==8 and digit in digits:
		digits.remove(digit)
		if count%2==0:
			mark="X"
			panels[digit]=mark
			bgn="green"
		elif count%2!=0:
			mark="O"
			panels[digit]=mark
			bgn="yellow"
		b8.config(text=mark)
		b8.config(bg=bgn)
		count=count+1
		sign=mark
		if(win(panels,sign) and sign == "X"):
			msg.showinfo("Result","Player 1 wins")
			root.destroy()

		elif(win(panels,sign) and sign == "O"):
			msg.showinfo("Result","Player 2 wins")
			root.destroy()

	if digit==9 and digit in digits:
		digits.remove(digit)
		if count%2==0:
			mark="X"
			panels[digit]=mark
			bgn="green"
		elif count%2!=0:
			mark="O"
			panels[digit]=mark
			bgn="yellow"
		b9.config(text=mark)
		b9.config(bg=bgn)
		count=count+1
		sign=mark
		if(win(panels,sign) and sign == "X"):
			msg.showinfo("Result","Player 1 wins")
			root.destroy()

		elif(win(panels,sign) and sign == "O"):
			msg.showinfo("Result","Player 2 wins")
			root.destroy()

	




Label(root,text="Player:X",font="times 15").grid(row=0,column=1)
Label(root,text="Player:O",font="times 15").grid(row=0,column=2)

b1=Button(root,width=15,font=("Times 16 bold"),height=7,command=lambda:checker(1))
b1.grid(row=1,column=1)

b2=Button(root,width=15,font=("Times 16 bold"),height=7,command=lambda:checker(2))
b2.grid(row=1,column=2)

b3=Button(root,width=15,font=("Times 16 bold"),height=7,command=lambda:checker(3))
b3.grid(row=1,column=3)

b4=Button(root,width=15,font=("Times 16 bold"),height=7,command=lambda:checker(4))
b4.grid(row=2,column=1)

b5=Button(root,width=15,font=("Times 16 bold"),height=7,command=lambda:checker(5))
b5.grid(row=2,column=2)

b6=Button(root,width=15,font=("Times 16 bold"),height=7,command=lambda:checker(6))
b6.grid(row=2,column=3)

b7=Button(root,width=15,font=("Times 16 bold"),height=7,command=lambda:checker(7))
b7.grid(row=3,column=1)

b8=Button(root,width=15,font=("Times 16 bold"),height=7,command=lambda:checker(8))
b8.grid(row=3,column=2)

b9=Button(root,width=15,font=("Times 16 bold"),height=7,command=lambda:checker(9))
b9.grid(row=3,column=3)






mainloop()