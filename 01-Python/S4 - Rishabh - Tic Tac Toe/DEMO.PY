from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe')
root.geometry("1366x768")
root.configure(background ='Cadet Blue')

#frames

Tops = Frame(root, bg = 'Cadet Blue', pady =2, width =1350, height=100, relief =RIDGE)
Tops.grid(row=0, column=0)

MainFrame = Frame(root, bg = 'Powder Blue', pady =2, width =1350, height=100,)
MainFrame.grid(row=0, column=0)

LeftFrame = Frame(MainFrame ,bd=10, width =750, height=500, pady=2,padx=10,bg = 'Cadet Blue' ,relief=RIDGE)
LeftFrame.pack(side=LEFT)


RightFrame = Frame(MainFrame ,bd=10, width =750, height=500, pady=10,padx=2,bg = 'Cadet Blue' ,relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame ,bd=10, width =560, height=200, padx=10,pady=2,bg = 'Cadet Blue' ,relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame ,bd=10, width =560, height=200, padx=10,pady=2,bg = 'Cadet Blue' ,relief=RIDGE)
RightFrame2.grid(row=1, column=0)

#player x and player y

PlayerX=IntVar()
PlayerO=IntVar()


PlayerX.set=(0)
PlayerO.set=(0)

buttons = StringVar()
click = True


def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()



def scorekeeper():
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        button1.configure(background="powder blue") 
        button2.configure(background="powder blue") 
        button3.configure(background="powder blue") 
        n = float(PlayerX.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner X",
         "You have just won the game")

    if(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        button4.configure(background="Red") 
        button5.configure(background="Red") 
        button6.configure(background="Red") 
        n = float(PlayerX.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won the game")


    if(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        button7.configure(background="Green") 
        button8.configure(background="Green") 
        button9.configure(background="Green") 
        n = float(PlayerX.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won the game")


    if(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        button3.configure(background="Grey") 
        button5.configure(background="Grey") 
        button7.configure(background="Grey") 
        n = float(PlayerX.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won the game")


    if(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        button1.configure(background="Grey") 
        button5.configure(background="Grey") 
        button9.configure(background="Grey") 
        n = float(PlayerX.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won the game")

    if(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        button1.configure(background="Powder Blue") 
        button4.configure(background="Powder Blue") 
        button7.configure(background="Powder Blue") 
        n = float(PlayerX.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won the game")



    if(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        button2.configure(background="Powder Blue") 
        button5.configure(background="Powder Blue") 
        button8.configure(background="Powder Blue") 
        n = float(PlayerX.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won the game")


    if(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        button3.configure(background="Powder Blue") 
        button6.configure(background="Powder Blue") 
        button9.configure(background="Powder Blue") 
        n = float(PlayerX.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won the game")   







    if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        button1.configure(background="Orange") 
        button2.configure(background="Orange") 
        button3.configure(background="Orange") 
        n = float(PlayerO.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner O", "You have just won the game")

    if(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
        button4.configure(background="blue") 
        button5.configure(background="blue") 
        button6.configure(background="blue") 
        n = float(PlayerO.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner O", "You have just won the game")


    if(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
        button7.configure(background="Green") 
        button8.configure(background="Green") 
        button9.configure(background="Green") 
        n = float(PlayerO.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner O", "You have just won the game")

    if(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        button1.configure(background="Red") 
        button4.configure(background="Red") 
        button7.configure(background="Red") 
        n = float(PlayerO.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner O", "You have just won the game")




    if(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        button3.configure(background="Cadet Blue") 
        button5.configure(background="Cadet Blue") 
        button7.configure(background="Cadet Blue") 
        n = float(PlayerO.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner O", "You have just won the game")


    if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        button1.configure(background="Orange") 
        button5.configure(background="Orange") 
        button9.configure(background="Orange") 
        n = float(PlayerO.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner O", "You have just won the game")

    if(button1["text"]=="O" and button4["text"]=="X" and button7["text"]=="O"):
        button1.configure(background="Powder Blue") 
        button4.configure(background="Powder Blue") 
        button7.configure(background="Powder Blue") 
        n = float(PlayerO.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner O", "You have just won the game")



    if(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
        button2.configure(background="Cadet Blue") 
        button5.configure(background="Cadet Blue") 
        button8.configure(background="Cadet Blue") 
        n = float(PlayerO.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner O", "You have just won the game")


    if(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        button3.configure(background="Red") 
        button6.configure(background="Red") 
        button9.configure(background="Red") 
        n = float(PlayerO.get())
        score = (n + 1)
        #PlayerX.set(score)
        messagebox.showinfo("Winner O", "You have just won the game")   






def reset():
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" "

    button1.configure(background="gainsboro") 
    button2.configure(background="gainsboro") 
    button3.configure(background="gainsboro") 
    button4.configure(background="gainsboro") 
    button5.configure(background="gainsboro") 
    button6.configure(background="gainsboro") 
    button7.configure(background="gainsboro") 
    button8.configure(background="gainsboro") 
    button9.configure(background="gainsboro") 

def NewGame():
    reset()
    PlayerX.set=(0)
    PlayerO.set=(0)


lblPlayerX =Label (RightFrame1, font=('arial', 40, 'bold'), text="Player X :",padx=2,pady=2, bg="CadetBlue")
lblPlayerX.grid(row=0, column=0,sticky=W)
txtPlayerX=Entry (RightFrame1,font=('arial', 40, 'bold'),bd=2,fg="black",textvariable= PlayerX, width=14,
justify=LEFT).grid(row=0, column=1)


lblPlayerO =Label (RightFrame1, font=('arial', 40, 'bold'), text="Player O :",padx=2,pady=2, bg="CadetBlue")
lblPlayerO.grid(row=1, column=0,sticky=W)
txtPlayerO=Entry (RightFrame1,font=('arial', 40, 'bold'),bd=2,fg="black",textvariable= PlayerO, width=14,
justify=LEFT).grid(row=1, column=1)



#Buttons



btnReset = Button(RightFrame2, text="Reset", font=('Times 26 bold'), height = 3, width=25, command =reset)
btnReset.grid(row=0, column=0)

btnNewgame = Button(RightFrame2, text="NewGame", font=('Times 26 bold'), height = 3, width=25, command =NewGame)
btnNewgame.grid(row=1, column=0,)


button1 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(button1))
button1.grid(row=1, column=0,)

button2 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(button2))
button2.grid(row=1, column=1,)

button3 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(button3))
button3.grid(row=1, column=2,)

button4 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(button4))
button4.grid(row=2, column=0,)

button5 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(button5))
button5.grid(row=2, column=1,)

button6 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(button6))
button6.grid(row=2, column=2,)

button7 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(button7))
button7.grid(row=3, column=0,)

button8 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(button8))
button8.grid(row=3, column=1,)

button9 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(button9))
button9.grid(row=3, column=2,)



root.mainloop() 