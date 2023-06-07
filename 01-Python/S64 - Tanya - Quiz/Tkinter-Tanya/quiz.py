from tkinter import *
from PIL import Image,ImageTk
from playsound import playsound
from pygame import mixer

win=Tk()
win.geometry('700x338')
win.resizable(False,False)

frame1=Frame(win,highlightbackground="#00b359", highlightthickness=2)
frame1.pack()

score = 0

def update_score(points) :
    global score
    score = score + points
    return score

end=Frame(win,highlightbackground="#00b359", highlightthickness=7,width=700,height=338,bg='#ccffcc')
end.pack_propagate(0)

def next():
	mixer.init()
	mixer.music.load('bgmwav.wav')
	mixer.music.play()
	frame1.forget()
	ind.pack()
	btn1.config(state=DISABLED)


def next2():
	mixer.init()
	mixer.music.load('bgmwav.wav')
	mixer.music.play()
	frame1.forget()
	chi.pack()
	btnn.config(state=DISABLED)

def next3():
	mixer.init()
	mixer.music.load('bgmwav.wav')
	mixer.music.play()
	frame1.forget()
	rus.pack()
	btnn0.config(state=DISABLED)

def next4():
	mixer.init()
	mixer.music.load('bgmwav.wav')
	mixer.music.play()
	frame1.forget()
	jap.pack()
	btnn__0.config(state=DISABLED)

def next5():
	mixer.init()
	mixer.music.load('bgmwav.wav')
	mixer.music.play()
	frame1.forget()
	aus.pack()
	btnn_1_0.config(state=DISABLED)

def india():
	ind.forget()
	ind2.pack()
	btn2.config(state=DISABLED)

def india2():
	ind2.forget()
	ind3.pack()
	btn3.config(state=DISABLED)

def india3():
	ind3.forget()
	ind4.pack()
	btn4.config(state=DISABLED)

def india4():
	ind4.forget()
	ind5.pack()
	btn5.config(state=DISABLED)

def india5():
	ind5.forget()
	end.pack()
	global score
	ans = update_score(0)
	final.config(text=f'You scored {ans}/5 correct! Hope you enjoyed the quiz:)',bg='#ccffcc',font=('kristen itc',15))

def china():
	chi.forget()
	chi2.pack()
	btnn2.config(state=DISABLED)

def china2():
	chi2.forget()
	chi3.pack()
	btnn3.config(state=DISABLED)

def china3():
	chi3.forget()
	chi4.pack()
	btnn4.config(state=DISABLED)

def china4():
	chi4.forget()
	chi5.pack()
	btnn5.config(state=DISABLED)

def china5():
	chi5.forget()
	end.pack()
	global score
	ans = update_score(0)
	final.config(text=f'You scored {ans}/5 correct! Hope you enjoyed the quiz:)',bg='#ccffcc',font=('kristen itc',15))

def russia():
	rus.forget()
	rus2.pack()
	btnn_2.config(state=DISABLED)

def russia2():
	rus2.forget()
	rus3.pack()
	btnn_3.config(state=DISABLED)

def russia3():
	rus3.forget()
	rus4.pack()
	btnn_4.config(state=DISABLED)

def russia4():
	rus4.forget()
	rus5.pack()
	btnn_5.config(state=DISABLED)

def russia5():
	rus5.forget()
	end.pack()
	global score
	ans = update_score(0)
	final.config(text=f'You scored {ans}/5 correct! Hope you enjoyed the quiz:)',bg='#ccffcc',font=('kristen itc',15))

def japan():
	jap.forget()
	jap2.pack()
	btnn__2.config(state=DISABLED)

def japan2():
	jap2.forget()
	jap3.pack()
	btnn__3.config(state=DISABLED)

def japan3():
	jap3.forget()
	jap4.pack()
	btnn__4.config(state=DISABLED)

def japan4():
	jap4.forget()
	jap5.pack()
	btnn__5.config(state=DISABLED)

def japan5():
	jap5.forget()
	end.pack()
	global score
	ans = update_score(0)
	final.config(text=f'You scored {ans}/5 correct! Hope you enjoyed the quiz:)',bg='#ccffcc',font=('kristen itc',15))

def australia():
	aus.forget()
	aus2.pack()
	btnn_1_2.config(state=DISABLED)

def australia2():
	aus2.forget()
	aus3.pack()
	btnn_1_3.config(state=DISABLED)

def australia3():
	aus3.forget()
	aus4.pack()
	btnn_1_4.config(state=DISABLED)

def australia4():
	aus4.forget()
	aus5.pack()
	btnn_1_5.config(state=DISABLED)

def australia5():
	global score
	aus5.forget()
	end.pack()
	ans = update_score(0)
	final.config(text=f'You scored {ans}/5 correct! Hope you enjoyed the quiz:)',bg='#ccffcc',font=('kristen itc',15))

def back():
	end.forget()
	frame1.pack()
	var.set("Choose a country")

def check_ind1():
	i03.config(bg='#47ff88',state=DISABLED)
	btn1.config(state=NORMAL)
	if var.get()=='Kolkata':
		i01.config(fg='red')
	elif var.get()=='Chennai':
		i02.config(fg='red')
	elif var.get()=='Bangalore':
		i04.config(fg='red')
	else:
		update_score(1)


def check_ind2():
	i12.config(bg='#47ff88',state=DISABLED)
	btn2.config(state=NORMAL)
	if var.get()=='Rahul Gandhi':
		i11.config(fg='red')
	elif var.get()=='Amit Shah':
		i13.config(fg='red')
	elif var.get()=='Draupadi Murmu':
		i14.config(fg='red')
	else:
		update_score(1)

def check_ind3():
	i23.config(bg='#47ff88',state=DISABLED)
	btn3.config(state=NORMAL)
	if var.get()=='30,5':
		i21.config(fg='red')
	elif var.get()=='31,7':
		i22.config(fg='red')
	elif var.get()=='29,8':
		i24.config(fg='red')
	else:
		update_score(1)

def check_ind4():
	i32.config(bg='#47ff88',state=DISABLED)
	btn4.config(state=NORMAL)
	if var.get()=='Sikkim':
		i31.config(fg='red')
	elif var.get()=='Karnataka':
		i33.config(fg='red')
	elif var.get()=='Gujarat':
		i34.config(fg='red')
	else:
		update_score(1)

def check_ind5():
	i41.config(bg='#47ff88',state=DISABLED)
	btn5.config(state=NORMAL)
	if var.get()=='Assam':
		i42.config(fg='red')
	elif var.get()=='Meghalaya':
		i43.config(fg='red')
	elif var.get()=='MP':
		i44.config(fg='red')
	else:
		update_score(1)

def check_chi1():
	c04.config(bg='#47ff88',state=DISABLED)
	btnn.config(state=NORMAL)
	if var.get()=='HK':
		c01.config(fg='red')
	elif var.get()=='Shanghai':
		c02.config(fg='red')
	elif var.get()=='Huairou':
		c03.config(fg='red')
	else:
		update_score(1)

def check_chi2():
	c11.config(bg='#47ff88',state=DISABLED)
	btnn2.config(state=NORMAL)
	if var.get()=='Vietnam':
		c12.config(fg='red')
	elif var.get()=='Thailand':
		c13.config(fg='red')
	elif var.get()=='Laos':
		c14.config(fg='red')
	else:
		update_score(1)

def check_chi3():
	c23.config(bg='#47ff88',state=DISABLED)
	btnn3.config(state=NORMAL)
	if var.get()=='Chongqing':
		c21.config(fg='red')
	elif var.get()=='Nanjing':
		c22.config(fg='red')
	elif var.get()=='Dalian':
		c24.config(fg='red')
	else:
		update_score(1)

def check_chi4():
	c32.config(bg='#47ff88',state=DISABLED)
	btnn4.config(state=NORMAL)
	if var.get()=='Football':
		c31.config(fg='red')
	elif var.get()=='Badminton':
		c33.config(fg='red')
	elif var.get()=='Hockey':
		c34.config(fg='red')
	else:
		update_score(1)

def check_chi5():
	c41.config(bg='#47ff88',state=DISABLED)
	btnn5.config(state=NORMAL)
	if var.get()=='Radcliffe Line':
		c42.config(fg='red')
	elif var.get()=='Siegfried Line':
		c43.config(fg='red')
	elif var.get()=='Attila Line':
		c44.config(fg='red')
	else:
		update_score(1)

def check_rus1():
	r03.config(bg='#47ff88',state=DISABLED)
	btnn0.config(state=NORMAL)
	if var.get()=='Samara':
		r01.config(fg='red')
	elif var.get()=='St. Petersburg':
		r02.config(fg='red')
	elif var.get()=='Sochi':
		r04.config(fg='red')
	else:
		update_score(1)

def check_rus2():
	r14.config(bg='#47ff88',state=DISABLED)
	btnn_2.config(state=NORMAL)
	if var.get()=='3rd':
		r11.config(fg='red')
	elif var.get()=='5th':
		r12.config(fg='red')
	elif var.get()=='9th':
		r13.config(fg='red')
	else:
		update_score(1)

def check_rus3():
	r21.config(bg='#47ff88',state=DISABLED)
	btnn_3.config(state=NORMAL)
	if var.get()=='Yen':
		r22.config(fg='red')
	elif var.get()=='Dollar':
		r23.config(fg='red')
	elif var.get()=='Euro':
		r24.config(fg='red')
	else:
		update_score(1)

def check_rus4():
	r34.config(bg='#47ff88',state=DISABLED)
	btnn_4.config(state=NORMAL)
	if var.get()=='Golden eagle':
		r31.config(fg='red')
	elif var.get()=='Snow leopard':
		r32.config(fg='red')
	elif var.get()=='Tiger':
		r33.config(fg='red')
	else:
		update_score(1)

def check_rus5():
	r42.config(bg='#47ff88',state=DISABLED)
	btnn_5.config(state=NORMAL)
	if var.get()=='19':
		r41.config(fg='red')
	elif var.get()=='9':
		r43.config(fg='red')
	elif var.get()=='15':
		r44.config(fg='red')
	else:
		update_score(1)

def check_jap1():
	j03.config(bg='#47ff88',state=DISABLED)
	btnn__0.config(state=NORMAL)
	if var.get()=='Kyoto':
		j01.config(fg='red')
	elif var.get()=='Yokohama':
		j02.config(fg='red')
	elif var.get()=='Osaka':
		j04.config(fg='red')
	else:
		update_score(1)

def check_jap2():
	j13.config(bg='#47ff88',state=DISABLED)
	btnn__2.config(state=NORMAL)
	if var.get()=='Atlantic':
		j11.config(fg='red')
	elif var.get()=='Arctic':
		j12.config(fg='red')
	elif var.get()=='Southern':
		j14.config(fg='red')
	else:
		update_score(1)

def check_jap3():
	j21.config(bg='#47ff88',state=DISABLED)
	btnn__3.config(state=NORMAL)
	if var.get()=='Tone':
		j22.config(fg='red')
	elif var.get()=='Sumida':
		j23.config(fg='red')
	elif var.get()=='Kinugawa':
		j24.config(fg='red')
	else:
		update_score(1)

def check_jap4():
	j33.config(bg='#47ff88',state=DISABLED)
	btnn__4.config(state=NORMAL)
	if var.get()=='1930':
		j31.config(fg='red')
	elif var.get()=='1978':
		j32.config(fg='red')
	elif var.get()=='1961':
		j34.config(fg='red')
	else:
		update_score(1)

def check_jap5():
	j44.config(bg='#47ff88',state=DISABLED)
	btnn__5.config(state=NORMAL)
	if var.get()=='a':
		j41.config(fg='red')
	elif var.get()=='b':
		j42.config(fg='red')
	elif var.get()=='c':
		j43.config(fg='red')
	else:
		update_score(1)

def check_aus1():
	a02.config(bg='#47ff88',state=DISABLED)
	btnn_1_0.config(state=NORMAL)
	if var.get()=='Sydney':
		a01.config(fg='red')
	elif var.get()=='Perth':
		a03.config(fg='red')
	elif var.get()=='Melbourne':
		a04.config(fg='red')
	else:
		update_score(1)

def check_aus2():
	a11.config(bg='#47ff88',state=DISABLED)
	btnn_1_2.config(state=NORMAL)
	if var.get()=='1910':
		a12.config(fg='red')
	elif var.get()=='1948':
		a13.config(fg='red')
	elif var.get()=='1956':
		a14.config(fg='red')
	else:
		update_score(1)

def check_aus3():
	a23.config(bg='#47ff88',state=DISABLED)
	btnn_1_3.config(state=NORMAL)
	if var.get()=='GDR':
		a21.config(fg='red')
	elif var.get()=='GAB':
		a22.config(fg='red')
	elif var.get()=='Australasia':
		a24.config(fg='red')
	else:
		update_score(1)

def check_aus4():
	a32.config(bg='#47ff88',state=DISABLED)
	btnn_1_4.config(state=NORMAL)
	if var.get()=='Brisbane':
		a31.config(fg='red')
	elif var.get()=='Alice Springs':
		a33.config(fg='red')
	elif var.get()=='Canberra':
		a34.config(fg='red')
	else:
		update_score(1)

def check_aus5():
	a43.config(bg='#47ff88',state=DISABLED)
	btnn_1_5.config(state=NORMAL)
	if var.get()=='7th':
		a41.config(fg='red')
	elif var.get()=='9th':
		a42.config(fg='red')
	elif var.get()=='10th':
		a44.config(fg='red')
	else:
		update_score(1)

lbl=Label(frame1,text='Countries',font=('Papyrus',30),bg='#ccffcc',width=25,height=5)
lbl.pack()

line=Label(frame1,width=96,height=4)
line.place(x=1,y=10)

tanya=Label(frame1,text='Project by: Tanya S Naik',font=('algerian'),bg='#ccffcc')
tanya.place(x=465,y=300)

choose=Label(frame1,text='Choose one country from the drop-down menu to take a quiz on the respective country!',bg='#ccffcc',font=('Times new roman',12))
choose.place(x=90,y=100)

indiaflag=Image.open('india.jpg')
resize_indiaflag = indiaflag.resize((60, 40))
flagind=ImageTk.PhotoImage(resize_indiaflag)
indflag=Label(frame1,image=flagind)
indflag.place(x=30,y=22.5)

chinaflag=Image.open('china.jpg')
resize_chinaflag = chinaflag.resize((60, 40))
flagchi=ImageTk.PhotoImage(resize_chinaflag)
chiflag=Label(frame1,image=flagchi)
chiflag.place(x=170,y=22.5)

russiaflag=Image.open('russia.jpg')
resize_russiaflag = russiaflag.resize((60, 40))
flagrus=ImageTk.PhotoImage(resize_russiaflag)
rusflag=Label(frame1,image=flagrus)
rusflag.place(x=310,y=22.5)

japanflag=Image.open('japan.jpg')
resize_japanflag = japanflag.resize((60, 40))
flagjap=ImageTk.PhotoImage(resize_japanflag)
japflag=Label(frame1,image=flagjap)
japflag.place(x=450,y=22.5)

australiaflag=Image.open('australia.jpg')
resize_australiaflag = australiaflag.resize((60, 40))
flagaus=ImageTk.PhotoImage(resize_australiaflag)
ausflag=Label(frame1,image=flagaus)
ausflag.place(x=590,y=22.5)

options = ['India','China','Russia','Japan','Australia']

var = StringVar()
var.set("Choose a country")

choice=var.get()

def quiz(choice):
	choice=var.get()
	
	if choice==options[0]:
		i=Button(frame1,text='          Take the quiz          ',font=('Times new roman',12),command=next)
		i.place(x=260,y=250)
	elif choice==options[1]:
		c=Button(frame1,text='          Take the quiz          ',font=('Times new roman',12),command=next2)
		c.place(x=260,y=250)
	elif choice==options[2]:
		r=Button(frame1,text='          Take the quiz          ',font=('Times new roman',12),command=next3)
		r.place(x=260,y=250)
	elif choice==options[3]:
		j=Button(frame1,text='          Take the quiz          ',font=('Times new roman',12),command=next4)
		j.place(x=260,y=250)
	elif choice==options[4]:
		a=Button(frame1,text='          Take the quiz          ',font=('Times new roman',12),command=next5)
		a.place(x=260,y=250)

drop = OptionMenu(frame1,var,*options,command=quiz)
drop.place(x=260,y=190)
drop.config(font=('kristen itc',10))

def play():
    playsound('bgmusic.mp3')

#INDIA

ind=Frame(win,highlightbackground="#ffb380", highlightthickness=7,width=700,height=338,bg='#ffe0cc')
ind.pack_propagate(0)

i1=Label(ind,text='What is the capital of India?',font=('Bookman Old Style',18),bg='#ffe0cc')
i1.pack(ipady=30)

i01=Radiobutton(ind,text='Kolkata',variable=var,value='Kolkata',command=check_ind1,bg='#ffe0cc',font=('Felix Titling',13))
i02=Radiobutton(ind,text='Chennai',variable=var,value='Chennai',command=check_ind1,bg='#ffe0cc',font=('Felix Titling',13))
i03=Radiobutton(ind,text='New Delhi',variable=var,value='New Delhi',command=check_ind1,bg='#ffe0cc',font=('Felix Titling',13))
i04=Radiobutton(ind,text='Bangalore',variable=var,value='Bangalore',command=check_ind1,bg='#ffe0cc',font=('Felix Titling',13))

i01.pack()
i02.pack()
i03.pack()
i04.pack()

btn1=Button(ind,text='Next>>',command=india,font=('Lucida calligraphy',12))
btn1.pack(pady=30)

ind2=Frame(win,highlightbackground="#ffb380", highlightthickness=7,width=700,height=338,bg='#ffe0cc')
ind2.pack_propagate(0)

i2=Label(ind2,text='Who is the current Prime minister of India?',font=('Bookman Old Style',18),bg='#ffe0cc')
i2.pack(ipady=30)

i11=Radiobutton(ind2,text='Rahul Gandhi',variable=var,value='Rahul Gandhi',command=check_ind2,bg='#ffe0cc',font=('Felix Titling',13))
i12=Radiobutton(ind2,text='Narendra Modi',variable=var,value='Narendra Modi',command=check_ind2,bg='#ffe0cc',font=('Felix Titling',13))
i13=Radiobutton(ind2,text='Amit Shah',variable=var,value='Amit Shah',command=check_ind2,bg='#ffe0cc',font=('Felix Titling',13))
i14=Radiobutton(ind2,text='Draupadi Murmu',variable=var,value='Draupadi Murmu',command=check_ind2,bg='#ffe0cc',font=('Felix Titling',13))

i11.pack()
i12.pack()
i13.pack()
i14.pack()

btn2=Button(ind2,text='Next>>',command=india2,font=('Lucida calligraphy',12))
btn2.pack(pady=30)

ind3=Frame(win,highlightbackground="#ffb380", highlightthickness=7,width=700,height=338,bg='#ffe0cc')
ind3.pack_propagate(0)

i3=Label(ind3,text='How many states and union territories are there in India?',font=('Bookman Old Style',18),bg='#ffe0cc')
i3.pack(ipady=30)

i21=Radiobutton(ind3,text='30 states and 5 union territories',variable=var,value='30,5',command=check_ind3,bg='#ffe0cc',font=('Felix Titling',13))
i22=Radiobutton(ind3,text='31 states and 7 union territories',variable=var,value='31,7',command=check_ind3,bg='#ffe0cc',font=('Felix Titling',13))
i23=Radiobutton(ind3,text='28 states and 8 union territories',variable=var,value='28,8',command=check_ind3,bg='#ffe0cc',font=('Felix Titling',13))
i24=Radiobutton(ind3,text='29 states and 8 union territories',variable=var,value='29,8',command=check_ind3,bg='#ffe0cc',font=('Felix Titling',13))

i21.pack()
i22.pack()
i23.pack()
i24.pack()

btn3=Button(ind3,text='Next>>',command=india3,font=('Lucida calligraphy',12))
btn3.pack(pady=30)

ind4=Frame(win,highlightbackground="#ffb380", highlightthickness=7,width=700,height=338,bg='#ffe0cc')
ind4.pack_propagate(0)

i4=Label(ind4,text='Which place in India is also known as the “Land of Rising Sun”?',font=('Bookman Old Style',18),bg='#ffe0cc')
i4.pack(ipady=30)

i31=Radiobutton(ind4,text='Sikkim',variable=var,value='Sikkim',command=check_ind4,bg='#ffe0cc',font=('Felix Titling',13))
i32=Radiobutton(ind4,text='Arunachal Pradesh',variable=var,value='AP',command=check_ind4,bg='#ffe0cc',font=('Felix Titling',13))
i33=Radiobutton(ind4,text='Karnataka',variable=var,value='Karnataka',command=check_ind4,bg='#ffe0cc',font=('Felix Titling',13))
i34=Radiobutton(ind4,text='Gujarat',variable=var,value='Gujarat',command=check_ind4,bg='#ffe0cc',font=('Felix Titling',13))

i31.pack()
i32.pack()
i33.pack()
i34.pack()

btn4=Button(ind4,text='Next>>',command=india4,font=('Lucida calligraphy',12))
btn4.pack(pady=30)

ind5=Frame(win,highlightbackground="#ffb380", highlightthickness=7,width=700,height=338,bg='#ffe0cc')
ind5.pack_propagate(0)

i5=Label(ind5,text='Which state is also known as the “Fruit Bowl” of India?',font=('Bookman Old Style',18),bg='#ffe0cc')
i5.pack(ipady=30)

i41=Radiobutton(ind5,text='Himachal Pradesh',variable=var,value='HP',command=check_ind5,bg='#ffe0cc',font=('Felix Titling',13))
i42=Radiobutton(ind5,text='Assam',variable=var,value='Assam',command=check_ind5,bg='#ffe0cc',font=('Felix Titling',13))
i43=Radiobutton(ind5,text='Meghalaya',variable=var,value='Meghalaya',command=check_ind5,bg='#ffe0cc',font=('Felix Titling',13))
i44=Radiobutton(ind5,text='Madhya Pradesh',variable=var,value='MP',command=check_ind5,bg='#ffe0cc',font=('Felix Titling',13))

i41.pack()
i42.pack()
i43.pack()
i44.pack()

btn5=Button(ind5,text='Finish!',command=india5,font=('Lucida calligraphy',12))
btn5.pack(pady=30)

#CHINA

chi=Frame(win,highlightbackground="#ffea00", highlightthickness=7,width=700,height=338,bg='#fff480')
chi.pack_propagate(0)

c1=Label(chi,text='What is the capital of China?',font=('Bookman Old Style',18),bg='#fff480')
c1.pack(ipady=30)

c01=Radiobutton(chi,text='Hong Kong',variable=var,value='HK',command=check_chi1,bg='#fff480',font=('Felix Titling',13))
c02=Radiobutton(chi,text='Shanghai',variable=var,value='Shanghai',command=check_chi1,bg='#fff480',font=('Felix Titling',13))
c03=Radiobutton(chi,text='Huairou',variable=var,value='Huairou ',command=check_chi1,bg='#fff480',font=('Felix Titling',13))
c04=Radiobutton(chi,text='Beijing',variable=var,value='Beijing',command=check_chi1,bg='#fff480',font=('Felix Titling',13))

c01.pack()
c02.pack()
c03.pack()
c04.pack()

btnn=Button(chi,text='Next>>',command=china,font=('Lucida calligraphy',12))
btnn.pack(pady=30)

chi2=Frame(win,highlightbackground="#ffea00", highlightthickness=7,width=700,height=338,bg='#fff480')
chi2.pack_propagate(0)

c2=Label(chi2,text='Which nation does not share a border with China?',font=('Bookman Old Style',18),bg='#fff480')
c2.pack(ipady=30)

c11=Radiobutton(chi2,text='North Korea',variable=var,value='North Korea',command=check_chi2,bg='#fff480',font=('Felix Titling',13))
c12=Radiobutton(chi2,text='Vietnam',variable=var,value='Vietnam',command=check_chi2,bg='#fff480',font=('Felix Titling',13))
c13=Radiobutton(chi2,text='Thailand',variable=var,value='Thailand',command=check_chi2,bg='#fff480',font=('Felix Titling',13))
c14=Radiobutton(chi2,text='Laos',variable=var,value='Laos',command=check_chi2,bg='#fff480',font=('Felix Titling',13))

c11.pack()
c12.pack()
c13.pack()
c14.pack()

btnn2=Button(chi2,text='Next>>',command=china2,font=('Lucida calligraphy',12))
btnn2.pack(pady=30)

chi3=Frame(win,highlightbackground="#ffea00", highlightthickness=7,width=700,height=338,bg='#fff480')
chi3.pack_propagate(0)

c3=Label(chi3,text='Which city in China was once called the "Forbidden City?"',font=('Bookman Old Style',18),bg='#fff480')
c3.pack(ipady=30)

c21=Radiobutton(chi3,text='Chongqing',variable=var,value='Chongqing',command=check_chi3,bg='#fff480',font=('Felix Titling',13))
c22=Radiobutton(chi3,text='Nanjing',variable=var,value='Nanjing',command=check_chi3,bg='#fff480',font=('Felix Titling',13))
c23=Radiobutton(chi3,text='Beijing',variable=var,value='Beijing',command=check_chi3,bg='#fff480',font=('Felix Titling',13))
c24=Radiobutton(chi3,text='Dalian',variable=var,value='Dalian',command=check_chi3,bg='#fff480',font=('Felix Titling',13))

c21.pack()
c22.pack()
c23.pack()
c24.pack()

btnn3=Button(chi3,text='Next>>',command=china3,font=('Lucida calligraphy',12))
btnn3.pack(pady=30)

chi4=Frame(win,highlightbackground="#ffea00", highlightthickness=7,width=700,height=338,bg='#fff480')
chi4.pack_propagate(0)

c4=Label(chi4,text='What is the national game of China?',font=('Bookman Old Style',18),bg='#fff480')
c4.pack(ipady=30)

c31=Radiobutton(chi4,text='Football',variable=var,value='Football',command=check_chi4,bg='#fff480',font=('Felix Titling',13))
c32=Radiobutton(chi4,text='Table tennis',variable=var,value='Table tennis',command=check_chi4,bg='#fff480',font=('Felix Titling',13))
c33=Radiobutton(chi4,text='Badminton',variable=var,value='Badminton',command=check_chi4,bg='#fff480',font=('Felix Titling',13))
c34=Radiobutton(chi4,text='Hockey',variable=var,value='Hockey',command=check_chi4,bg='#fff480',font=('Felix Titling',13))

c31.pack()
c32.pack()
c33.pack()
c34.pack()

btnn4=Button(chi4,text='Next>>',command=china4,font=('Lucida calligraphy',12))
btnn4.pack(pady=30)

chi5=Frame(win,highlightbackground="#ffea00", highlightthickness=7,width=700,height=338,bg='#fff480')
chi5.pack_propagate(0)

c5=Label(chi5,text='India and China’s border is called ___.',font=('Bookman Old Style',18),bg='#fff480')
c5.pack(ipady=30)

c41=Radiobutton(chi5,text='McMohan Line',variable=var,value='McMohan Line',command=check_chi5,bg='#fff480',font=('Felix Titling',13))
c42=Radiobutton(chi5,text='Radcliffe Line',variable=var,value='Radcliffe Line',command=check_chi5,bg='#fff480',font=('Felix Titling',13))
c43=Radiobutton(chi5,text='Siegfried Line',variable=var,value='Siegfried Line',command=check_chi5,bg='#fff480',font=('Felix Titling',13))
c44=Radiobutton(chi5,text='Attila Line',variable=var,value='Attila Line',command=check_chi5,bg='#fff480',font=('Felix Titling',13))

c41.pack()
c42.pack()
c43.pack()
c44.pack()

btnn5=Button(chi5,text='Finish!',command=china5,font=('Lucida calligraphy',12))
btnn5.pack(pady=30)

#RUSSIA

rus=Frame(win,highlightbackground="#6600cc", highlightthickness=7,width=700,height=338,bg='#c2c2f0')
rus.pack_propagate(0)

r1=Label(rus,text='What is the capital of Russia?',font=('Bookman Old Style',18),bg='#c2c2f0')
r1.pack(ipady=30)

r01=Radiobutton(rus,text='Samara',variable=var,value='Samara',command=check_rus1,bg='#c2c2f0',font=('Felix Titling',13))
r02=Radiobutton(rus,text='St. Petersburg',variable=var,value='St. Petersburg',command=check_rus1,bg='#c2c2f0',font=('Felix Titling',13))
r03=Radiobutton(rus,text='Moscow',variable=var,value='Moscow',command=check_rus1,bg='#c2c2f0',font=('Felix Titling',13))
r04=Radiobutton(rus,text='Sochi',variable=var,value='Sochi',command=check_rus1,bg='#c2c2f0',font=('Felix Titling',13))

r01.pack()
r02.pack()
r03.pack()
r04.pack()

btnn0=Button(rus,text='Next>>',command=russia,font=('Lucida calligraphy',12))
btnn0.pack(pady=30)

rus2=Frame(win,highlightbackground="#6600cc", highlightthickness=7,width=700,height=338,bg='#c2c2f0')
rus2.pack_propagate(0)

r2=Label(rus2,text="Russia is the world's ____ most populous country",font=('Bookman Old Style',18),bg='#c2c2f0')
r2.pack(ipady=30)

r11=Radiobutton(rus2,text='3rd',variable=var,value='3rd',command=check_rus2,bg='#c2c2f0',font=('Felix Titling',13))
r12=Radiobutton(rus2,text='5th',variable=var,value='5th',command=check_rus2,bg='#c2c2f0',font=('Felix Titling',13))
r13=Radiobutton(rus2,text='9th',variable=var,value='9th',command=check_rus2,bg='#c2c2f0',font=('Felix Titling',13))
r14=Radiobutton(rus2,text='11th',variable=var,value='11th',command=check_rus2,bg='#c2c2f0',font=('Felix Titling',13))

r11.pack()
r12.pack()
r13.pack()
r14.pack()

btnn_2=Button(rus2,text='Next>>',command=russia2,font=('Lucida calligraphy',12))
btnn_2.pack(pady=30)

rus3=Frame(win,highlightbackground="#6600cc", highlightthickness=7,width=700,height=338,bg='#c2c2f0')
rus3.pack_propagate(0)

r3=Label(rus3,text="What is Russia's currency called?",font=('Bookman Old Style',18),bg='#c2c2f0')
r3.pack(ipady=30)

r21=Radiobutton(rus3,text='Ruble',variable=var,value='Ruble',command=check_rus3,bg='#c2c2f0',font=('Felix Titling',13))
r22=Radiobutton(rus3,text='Yen',variable=var,value='Yen',command=check_rus3,bg='#c2c2f0',font=('Felix Titling',13))
r23=Radiobutton(rus3,text='Dollar',variable=var,value='Dollar',command=check_rus3,bg='#c2c2f0',font=('Felix Titling',13))
r24=Radiobutton(rus3,text='Euro',variable=var,value='Euro',command=check_rus3,bg='#c2c2f0',font=('Felix Titling',13))

r21.pack()
r22.pack()
r23.pack()
r24.pack()

btnn_3=Button(rus3,text='Next>>',command=russia3,font=('Lucida calligraphy',12))
btnn_3.pack(pady=30)

rus4=Frame(win,highlightbackground="#6600cc", highlightthickness=7,width=700,height=338,bg='#c2c2f0')
rus4.pack_propagate(0)

r4=Label(rus4,text='What is the national animal of Russia?',font=('Bookman Old Style',18),bg='#c2c2f0')
r4.pack(ipady=30)

r31=Radiobutton(rus4,text='Golden eagle',variable=var,value='Golden eagle',command=check_rus4,bg='#c2c2f0',font=('Felix Titling',13))
r32=Radiobutton(rus4,text='Snow leopard',variable=var,value='Snow leopard',command=check_rus4,bg='#c2c2f0',font=('Felix Titling',13))
r33=Radiobutton(rus4,text='Tiger',variable=var,value='Tiger',command=check_rus4,bg='#c2c2f0',font=('Felix Titling',13))
r34=Radiobutton(rus4,text='Brown bear',variable=var,value='Brown bear',command=check_rus4,bg='#c2c2f0',font=('Felix Titling',13))

r31.pack()
r32.pack()
r33.pack()
r34.pack()

btnn_4=Button(rus4,text='Next>>',command=russia4,font=('Lucida calligraphy',12))
btnn_4.pack(pady=30)

rus5=Frame(win,highlightbackground="#6600cc", highlightthickness=7,width=700,height=338,bg='#c2c2f0')
rus5.pack_propagate(0)

r5=Label(rus5,text='How many time zones does Russia have?',font=('Bookman Old Style',18),bg='#c2c2f0')
r5.pack(ipady=30)

r41=Radiobutton(rus5,text='19',variable=var,value='21',command=check_rus5,bg='#c2c2f0',font=('Felix Titling',13))
r42=Radiobutton(rus5,text='11',variable=var,value='11',command=check_rus5,bg='#c2c2f0',font=('Felix Titling',13))
r43=Radiobutton(rus5,text='9',variable=var,value='9',command=check_rus5,bg='#c2c2f0',font=('Felix Titling',13))
r44=Radiobutton(rus5,text='15',variable=var,value='15',command=check_rus5,bg='#c2c2f0',font=('Felix Titling',13))

r41.pack()
r42.pack()
r43.pack()
r44.pack()

btnn_5=Button(rus5,text='Finish!',command=russia5,font=('Lucida calligraphy',12))
btnn_5.pack(pady=30)

#JAPAN

jap=Frame(win,highlightbackground="#e60000", highlightthickness=7,width=700,height=338,bg='#ffb3b3')
jap.pack_propagate(0)

j1=Label(jap,text='What is the capital of Japan?',font=('Bookman Old Style',18),bg='#ffb3b3')
j1.pack(ipady=30)

j01=Radiobutton(jap,text='Kyoto',variable=var,value='Kyoto',command=check_jap1,bg='#ffb3b3',font=('Felix Titling',13))
j02=Radiobutton(jap,text='Yokohama',variable=var,value='Yokohama',command=check_jap1,bg='#ffb3b3',font=('Felix Titling',13))
j03=Radiobutton(jap,text='Tokyo',variable=var,value='Tokyo',command=check_jap1,bg='#ffb3b3',font=('Felix Titling',13))
j04=Radiobutton(jap,text='Osaka',variable=var,value='Osaka',command=check_jap1,bg='#ffb3b3',font=('Felix Titling',13))

j01.pack()
j02.pack()
j03.pack()
j04.pack()

btnn__0=Button(jap,text='Next>>',command=japan,font=('Lucida calligraphy',12))
btnn__0.pack(pady=30)

jap2=Frame(win,highlightbackground="#e60000", highlightthickness=7,width=700,height=338,bg='#ffb3b3')
jap2.pack_propagate(0)

j2=Label(jap2,text="Japan lies in which ocean of the world?",font=('Bookman Old Style',18),bg='#ffb3b3')
j2.pack(ipady=30)

j11=Radiobutton(jap2,text='Atlantic',variable=var,value='Atlantic',command=check_jap2,bg='#ffb3b3',font=('Felix Titling',13))
j12=Radiobutton(jap2,text='Arctic',variable=var,value='Arctic',command=check_jap2,bg='#ffb3b3',font=('Felix Titling',13))
j13=Radiobutton(jap2,text='Pacific',variable=var,value='Pacific',command=check_jap2,bg='#ffb3b3',font=('Felix Titling',13))
j14=Radiobutton(jap2,text='Southern',variable=var,value='Southern',command=check_jap2,bg='#ffb3b3',font=('Felix Titling',13))

j11.pack()
j12.pack()
j13.pack()
j14.pack()

btnn__2=Button(jap2,text='Next>>',command=japan2,font=('Lucida calligraphy',12))
btnn__2.pack(pady=30)

jap3=Frame(win,highlightbackground="#e60000", highlightthickness=7,width=700,height=338,bg='#ffb3b3')
jap3.pack_propagate(0)

j3=Label(jap3,text="Which is the longest river in Japan?",font=('Bookman Old Style',18),bg='#ffb3b3')
j3.pack(ipady=30)

j21=Radiobutton(jap3,text='Shinano river',variable=var,value='Shinano river',command=check_jap3,bg='#ffb3b3',font=('Felix Titling',13))
j22=Radiobutton(jap3,text='Tone river',variable=var,value='Tone',command=check_jap3,bg='#ffb3b3',font=('Felix Titling',13))
j23=Radiobutton(jap3,text='Sumida river',variable=var,value='Sumida',command=check_jap3,bg='#ffb3b3',font=('Felix Titling',13))
j24=Radiobutton(jap3,text='Kinugawa river',variable=var,value='Kinugawa',command=check_jap3,bg='#ffb3b3',font=('Felix Titling',13))

j21.pack()
j22.pack()
j23.pack()
j24.pack()

btnn__3=Button(jap3,text='Next>>',command=japan3,font=('Lucida calligraphy',12))
btnn__3.pack(pady=30)

jap4=Frame(win,highlightbackground="#e60000", highlightthickness=7,width=700,height=338,bg='#ffb3b3')
jap4.pack_propagate(0)

j4=Label(jap4,text='In which year was Hiroshima & Nagasaki bombed?',font=('Bookman Old Style',18),bg='#ffb3b3')
j4.pack(ipady=30)

j31=Radiobutton(jap4,text='1930',variable=var,value='1930',command=check_jap4,bg='#ffb3b3',font=('Felix Titling',13))
j32=Radiobutton(jap4,text='1978',variable=var,value='1978',command=check_jap4,bg='#ffb3b3',font=('Felix Titling',13))
j33=Radiobutton(jap4,text='1945',variable=var,value='1945',command=check_jap4,bg='#ffb3b3',font=('Felix Titling',13))
j34=Radiobutton(jap4,text='1961',variable=var,value='1961',command=check_jap4,bg='#ffb3b3',font=('Felix Titling',13))

j31.pack()
j32.pack()
j33.pack()
j34.pack()

btnn__4=Button(jap4,text='Next>>',command=japan4,font=('Lucida calligraphy',12))
btnn__4.pack(pady=30)

jap5=Frame(win,highlightbackground="#e60000", highlightthickness=7,width=700,height=338,bg='#ffb3b3')
jap5.pack_propagate(0)

j5=Label(jap5,text='How many islands does Japan have?',font=('Bookman Old Style',18),bg='#ffb3b3')
j5.pack(ipady=30)

j41=Radiobutton(jap5,text='17,131',variable=var,value='a',command=check_jap5,bg='#ffb3b3',font=('Felix Titling',13))
j42=Radiobutton(jap5,text='7,852',variable=var,value='b',command=check_jap5,bg='#ffb3b3',font=('Felix Titling',13))
j43=Radiobutton(jap5,text='11,283',variable=var,value='c',command=check_jap5,bg='#ffb3b3',font=('Felix Titling',13))
j44=Radiobutton(jap5,text='14,125',variable=var,value='d',command=check_jap5,bg='#ffb3b3',font=('Felix Titling',13))

j41.pack()
j42.pack()
j43.pack()
j44.pack()

btnn__5=Button(jap5,text='Finish!',command=japan5,font=('Lucida calligraphy',12))
btnn__5.pack(pady=30)

#AUSTRALIA

aus=Frame(win,highlightbackground="#990099", highlightthickness=7,width=700,height=338,bg='#eb99ff')
aus.pack_propagate(0)

a1=Label(aus,text='What is the capital of Australia?',font=('Bookman Old Style',18),bg='#eb99ff')
a1.pack(ipady=30)

a01=Radiobutton(aus,text='Sydney',variable=var,value='Sydney',command=check_aus1,bg='#eb99ff',font=('Felix Titling',13))
a02=Radiobutton(aus,text='Canberra',variable=var,value='Canberra',command=check_aus1,bg='#eb99ff',font=('Felix Titling',13))
a03=Radiobutton(aus,text='Perth',variable=var,value='Perth',command=check_aus1,bg='#eb99ff',font=('Felix Titling',13))
a04=Radiobutton(aus,text='Melbourne',variable=var,value='Melbourne',command=check_aus1,bg='#eb99ff',font=('Felix Titling',13))

a01.pack()
a02.pack()
a03.pack()
a04.pack()

btnn_1_0=Button(aus,text='Next>>',command=australia,font=('Lucida calligraphy',12))
btnn_1_0.pack(pady=30)

aus2=Frame(win,highlightbackground="#990099", highlightthickness=7,width=700,height=338,bg='#eb99ff')
aus2.pack_propagate(0)

a2=Label(aus2,text="In which year did Australia get independence from UK?",font=('Bookman Old Style',18),bg='#eb99ff')
a2.pack(ipady=30)

a11=Radiobutton(aus2,text='1901',variable=var,value='1901',command=check_aus2,bg='#eb99ff',font=('Felix Titling',13))
a12=Radiobutton(aus2,text='1910',variable=var,value='1910',command=check_aus2,bg='#eb99ff',font=('Felix Titling',13))
a13=Radiobutton(aus2,text='1948',variable=var,value='1948',command=check_aus2,bg='#eb99ff',font=('Felix Titling',13))
a14=Radiobutton(aus2,text='1956',variable=var,value='1956',command=check_aus2,bg='#eb99ff',font=('Felix Titling',13))

a11.pack()
a12.pack()
a13.pack()
a14.pack()

btnn_1_2=Button(aus2,text='Next>>',command=australia2,font=('Lucida calligraphy',12))
btnn_1_2.pack(pady=30)

aus3=Frame(win,highlightbackground="#990099", highlightthickness=7,width=700,height=338,bg='#eb99ff')
aus3.pack_propagate(0)

a3=Label(aus3,text="Which reef system is found in Australia?",font=('Bookman Old Style',18),bg='#eb99ff')
a3.pack(ipady=30)

a21=Radiobutton(aus3,text='Great Dividing Range',variable=var,value='GDR',command=check_aus3,bg='#eb99ff',font=('Felix Titling',13))
a22=Radiobutton(aus3,text='Great Artesian Basin',variable=var,value='GAB',command=check_aus3,bg='#eb99ff',font=('Felix Titling',13))
a23=Radiobutton(aus3,text='Great Barrier Reef',variable=var,value='GBR',command=check_aus3,bg='#eb99ff',font=('Felix Titling',13))
a24=Radiobutton(aus3,text='Australasia',variable=var,value='Australasia',command=check_aus3,bg='#eb99ff',font=('Felix Titling',13))

a21.pack()
a22.pack()
a23.pack()
a24.pack()

btnn_1_3=Button(aus3,text='Next>>',command=australia3,font=('Lucida calligraphy',12))
btnn_1_3.pack(pady=30)

aus4=Frame(win,highlightbackground="#990099", highlightthickness=7,width=700,height=338,bg='#eb99ff')
aus4.pack_propagate(0)

a4=Label(aus4,text='Which is the largest city by area in Australia?',font=('Bookman Old Style',18),bg='#eb99ff')
a4.pack(ipady=30)

a31=Radiobutton(aus4,text='Brisbane',variable=var,value='Brisbane',command=check_aus4,bg='#eb99ff',font=('Felix Titling',13))
a32=Radiobutton(aus4,text='Sydney',variable=var,value='Sydney',command=check_aus4,bg='#eb99ff',font=('Felix Titling',13))
a33=Radiobutton(aus4,text='Alice Springs',variable=var,value='Alice Springs',command=check_aus4,bg='#eb99ff',font=('Felix Titling',13))
a34=Radiobutton(aus4,text='Canberra',variable=var,value='Canberra',command=check_aus4,bg='#eb99ff',font=('Felix Titling',13))

a31.pack()
a32.pack()
a33.pack()
a34.pack()

btnn_1_4=Button(aus4,text='Next>>',command=australia4,font=('Lucida calligraphy',12))
btnn_1_4.pack(pady=30)

aus5=Frame(win,highlightbackground="#990099", highlightthickness=7,width=700,height=338,bg='#eb99ff')
aus5.pack_propagate(0)

a5=Label(aus5,text="Australia is the world's __ largest country by area.",font=('Bookman Old Style',18),bg='#eb99ff')
a5.pack(ipady=30)

a41=Radiobutton(aus5,text='7th',variable=var,value='7th',command=check_aus5,bg='#eb99ff',font=('Felix Titling',13))
a42=Radiobutton(aus5,text='9th',variable=var,value='9th',command=check_aus5,bg='#eb99ff',font=('Felix Titling',13))
a43=Radiobutton(aus5,text='6th',variable=var,value='6th',command=check_aus5,bg='#eb99ff',font=('Felix Titling',13))
a44=Radiobutton(aus5,text='10th',variable=var,value='10th',command=check_aus5,bg='#eb99ff',font=('Felix Titling',13))

a41.pack()
a42.pack()
a43.pack()
a44.pack()

btnn_1_5=Button(aus5,text='Finish!',command=australia5,font=('Lucida calligraphy',12))
btnn_1_5.pack(pady=30)

##

back=Button(end,text='Back',command=back,font=('Algerian',15))
back.pack(pady=50)

final = Label(end, font = ("Times New Roman" , 20 ))
final.pack()
print (score)

win.mainloop()