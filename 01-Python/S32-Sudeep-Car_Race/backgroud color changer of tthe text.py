from tkinter import *
from tkinter import ttk

#Create an instance of tkinter frame
win= Tk()

#Define the geometry of the window
win.geometry("750x250")

#Define a function to Change the color of the label widget
def change_color():
   label.config(bg= "gray51", fg= "white")

#Create a label
label= Label(win, text= "Hey There! How are you?")
label.pack(pady=30)

#Create a Button
ttk.Button(win, text="Change Color", command=change_color).pack(pady=20)
win.mainloop()
