from tkinter import *
win=Tk()
win.geometry("200x200")
win.title('Geometry')

#external padding = padx, pady
lb1=Label(win,text='Welcome to tkinter',bg='#FF9999')
lb1.pack(fill=X,padx=40,pady=8)

#internal padding=ipadx,ipady
lb2=Label(win,text='Welcome to Python',bg='#09FF90')
lb2.pack(ipadx=50,ipady=17)


lb3=Label(win,text='Hello',bg='#FF2089')
lb3.pack(side=LEFT,padx=5,pady=5)

lb4=Label(win,text='Good morning',bg='#FF8977')
lb4.place(x=60,y=100)



win.mainloop()