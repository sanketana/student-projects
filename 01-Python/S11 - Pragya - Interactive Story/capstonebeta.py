from tkinter import *
wind=Tk()
wind.geometry('1000x2000')

f1=Frame(wind)

f2=Frame(wind)

f3= Frame(wind)

f4= Frame(wind)

f5= Frame(wind)

f6= Frame(wind)

f7= Frame(wind)

f8= Frame(wind)

f9= Frame(wind)

Intro1= Label(f1, text= "WELCOME TO THE HORROR ESCAPE GAME!", font= ("Castellar", 15))
Intro1.pack()

Intro= Label(f1, text="For maximum immersion, it is recommended that you choose a name of your desire.", font=("Helvetica",10))
Intro.pack()

def cont():
	f1.destroy()
	f2.pack()

def clickedno():
	Narrator2= Label(f1,text= "That... is a terrible name anyways. Your name is just Max from here on out")
	Narrator2.pack()
	Continue= Button(f1, text ="Continue", command=cont)
	Continue.pack(pady = 10)


def clicked():
	name= FakeName.get()
	MyLabel= Label(f1,text= f'{name}? Is this your desired choice?')
	MyLabel.pack()
	btn1= Button(f1, text='Yes', command= clicked2)
	btn1.pack()
	btn2= Button(f1, text= 'No', command= clickedno)
	btn2.pack()


def clicked2():
	Narrator1= Label(f1,text= "That... is a terrible name. Your name is just Max from here on out")
	Narrator1.pack()
	Continue= Button(f1, text ="Continue", command=cont)
	Continue.pack(pady = 10)

#make a no button

Intro1= Label(f1)
Intro1.pack()
	
FakeName=Entry(f1, width=20,font=("Helvetica",17))
FakeName.pack()

Intro1= Label(f1)
Intro1.pack()
btn = Button(f1, text = 'Submit', command = clicked)
btn.pack()

f1.pack()

#secondpart

ALARM = PhotoImage(file= "alarmclock1.png")
AlarmButton= Button(f2, image= ALARM )
AlarmButton.pack()


Intro1= Label(f1)
Intro1.pack()
Line0= Label(f2, text= "YOU ARE PLAYING AS: MAX")
Line0.pack()
Line1= Label(f2, text= "I wake up to an unfamiliar ceiling as an annoying screeching sound rings through my ears")
Line1.pack()
Line2= Label(f2,text= "This...isnt my bed. It smells like rotting animals and the blanket is wet with some weird fluid.")
Line2.pack()
Line3= Label(f2, text= "The alarm clock is getting worse. I can't even think properly.")
Line3.pack()
Line4= Label(f2, text= "Should I smash the alarm clock?")
Line4.pack()

def cont1():
	f2.destroy()
	f3.pack()




def ButtonY_clicked():
	global ButtonMidway
	Answer= Label(f2, text= "The alarm clock is promptly knocked over by my sheer fury.")
	Answer.pack()
	End1= Label(f2, text= "I see something horrifying standing at the corner of the room.")
	ButtonMidway=Button(f2, text= "Gasp dramatically", command= Startend)
	ButtonMidway.pack()

def Startend():
	global ButtonMidway
	global COW

	COW= PhotoImage(file= 'perfectcow.png')
	ButtonMidway.config(image= COW)


	End2=Label(f2,text= "A cow is standing at the corner of the room.")
	End2.pack()
	ButtonSpeak= Button(f2,text= "Scream Loudly",command= JokeEnding)
	ButtonSpeak.pack()


def JokeEnding():
	End3= Label(f2, text= "'Yes. I was responsible for it all. I am one with the Universe, I am the new King of the Hospital.'")
	End3.pack()
	End4= Label(f2,text= "I scream in horror. This was truly a nightmare. The Cow did it. It was responsible for it all")
	End4.pack()
	End5 =Label(f2,text= "you got the JOKE ENDING, (you might wanna pick another option)", font= ("Castellar", 15))
	End5.pack()


	



def ButtonN_clicked():
	Answer1= Label(f2, text= "I just stop the alarm clock by pressing the button on its right side.")
	Answer1.pack()
	Continue= Button(f2, text= "Continue", command= cont1)
	Continue.pack()

ButtonY= Button(f2,text="Yes", command= ButtonY_clicked)
ButtonY.pack()


ButtonN= Button(f2,text= "No", command= ButtonN_clicked)
ButtonN.pack()



#thirdpart

JOHN= PhotoImage(file= "john.png")
John= Button(f3, image= JOHN )
John.pack()

Line5= Label(f3, text= "A sudden sound knocks me out of my painful reverie.")
Line5.pack()
Line6= Label(f3, text= "I shoot a look across the room and see a seemingly old looking man in a well dressed suit.")
Line6.pack()
Line7= Label(f3, text= " I leap out of bed and come face to face with the man, who could be dangerous!")
Line7.pack()
Line8= Label(f3, text= "What should I do?")
Line8.pack()

def cont2():
	f3.destroy()
	f4.pack()


def ButtonFight_clicked():
	Answer= Label(f3, text= " I'm a terrible fighter so I give him a flimsy uppercut.")
	Answer.pack()
	Answer2= Label(f3, text=" 'Ouch! My good sir! I implore you to cease this nonsense at once! '")
	Answer2.pack()
	Answer3= Label(f3, text= "'Oh! My apologies! I didn't mean to judge you so quickly!' I say, ashamed of myself suddenly.")
	Answer3.pack()
	Answer4= Label(f3, text= "No problem my good fellow. No one seems to think much of me...How about a stroll? ")
	Answer4.pack()
	Answer5= Label(f3, text= "I must be crazy...trusting this old dude from the 1900s who seems to be a patient. But he seems to trust me even after I punched him.")
	Answer5.pack()
	Continue3= Button(f3, text= "Continue", command= cont2)
	Continue3.pack()


def ButtonAct_clicked():
	Answer6= Label(f3, text= "'Hey, man. How about we both go our own ways out of this nightmarish hellscape? I like your uniform by the way, very... non mental asylum like.'")
	Answer6.pack()
	Answer7= Label(f3, text="'Why, my good sir! While I thank you for you decency, you have the most questionable choices in fashion, I must say. Too much Argyle... blah blah'" )
	Answer7.pack()
	Answer8= Label(f3, text= "While I zone out, ignoring the old geezer's ramble about fashion, I realize he was not crazy. Just a little strange. Maybe likeable, even.")
	Answer8.pack()
	Answer9= Label(f3, text= "'Well you're welcome. I admire your taste in fashion, sir'")
	Answer9.pack()
	Answer10= Label(f3, text= "No problem my good fellow. I admire your politeness and integrity. ")
	Answer10.pack()
	Answer11= Label(f3, text= "I must be crazy...trusting this old dude from the 1900s who seems to be a patient. But he seems to trust me even if I'm a stranger.")
	Answer11.pack()
	Continue3= Button(f3, text= "Continue", command= cont2)
	Continue3.pack()






ButtonFight= Button(f3, text="Fight", command= ButtonFight_clicked)
ButtonFight.pack()

ButtonAct= Button(f3, text= "Act", command= ButtonAct_clicked)
ButtonAct.pack()



#fourth part

def Cont6():
	f4.destroy()
	f5.pack()


def Agree():
	Reply= Label(f4, text= "'Oh my good fellow Max! I knew you were a true intellectual! He says, his eyes shining a bit.")
	Reply.pack()
	Continue4= Button(f4, text= "Continue", command= Cont5)
	Continue4.pack()

def Disagree():
	Reply1= Label(f4, text= "'Sir Max, while you seem like a good fellow! I must implore you to study all manners of a good decorum! This is most disheartening!'")
	Reply1.pack()
	Continue4= Button(f4, text= "Continue", command= Cont5)
	Continue4.pack()

Line9= Label(f4, text= "The prisoner (whose name I learned was Sir Percival) and I walked down the main hall.")
Line9.pack()
Line10= Label(f4, text= "'EUGH!' The wall decorum is simply disgusting! Don't you agree?")
Line10.pack()

ButtonAgree= Button(f4, text= "I agree", command= Agree)
ButtonAgree.pack()

ButtonDisagree= Button(f4, text= " I like the bloodstains on the wall!", command= Disagree)
ButtonDisagree.pack()

def Cont5():

	global REAPER

	REAPER= PhotoImage(file= "reaper.png")
	Nurse= Button(f4, image= REAPER )
	Nurse.pack()


	Fight1= Label(f4, text= "We are suddenly interrupted by someone in a nurse uniform. She cackles loudly.")
	Fight1.pack()
	Button
	Fight2= Label(f4, text= "Sir Percival shrieks in response: 'DEAR GOD, WHAT A TERRIBLE OUTFIT!' He cowers in fear. ")
	Fight2.pack()
	Fight3= Label(f4, text= "What do I do??")
	Fight3.pack()
	Buttonfight= Button(f4, text= "Fight her", command= NurseFight)
	Buttonfight.pack()
	ButtonAct= Button(f4, text= "Act differently", command= NurseAct)
	ButtonAct.pack()

def NurseFight():
	Nurse1= Label(f4, text= "The nurse stabs Sir Percival in the arm with the injection needle she's holding.")
	Nurse1.pack()
	Scream= Label(f4, text= "I shout loudly, 'Sir Percival, No!'")
	Scream.pack()
	Yell= Label(f4, text= "I grab the nurse's arm and pull her away.")
	Yell.pack()
	FancyMove= Label(f4, text= "I try and do the basics of kung fu. It doesn't have the desired effect because she kicks me to the corner of the room. I should try something else.")
	FancyMove.pack()
	Try= Button(f4, text= "Act", command= NurseAct)
	Try.pack()

def NurseAct():
	Nurse2= Label(f4, text= "I use my charisma and charm to impress the nurse, 'Well your outfit is quite dirty. You should wash it.' ")
	Nurse2. pack()
	Nurse3= Label(f4, text= "'Oh my goodness! This is a terrible outfit to give lobotomies in!'")
	Nurse3.pack()
	Nurse4= Label(f4, text= "She runs away mumbling about how much change she needs at the laundromat.")
	Nurse4.pack()
	Continue5= Button(f4, text= "Continue", command= Cont6)
	Continue5.pack()




#finalscene

def cont7():
	f5.destroy()
	f6.pack()

Walk1= Label(f5, text= "As we approach a door at the end of the hall with a faded green neon light spelling: 'EXIT', Sir Percival explains more about the hospital...")
Walk1.pack()


def ButtonContinue1():
	Walk2= Label(f5, text= "'Max, I must tell you: I am a spy for Doctor Origami, the head doctor. I thought you thought I was crazy and would let the Nurse pretend to kill me.'")
	Walk2.pack()
	Walk3= Label(f5, text= "I look at him in surprise. I hated to admit it, but I had gotten attached to Sir Percival")
	Walk3.pack()
	Continue1= Button(f5, text= "Continue Listening", command= ButtonContinue2)
	Continue1.pack()

ButtonContinue= Button(f5, text= "Listen", command= ButtonContinue1)
ButtonContinue.pack()


def ButtonContinue2():
	Walk4= Label(f5, text= "'Why are you telling me this then?'")
	Walk4.pack()
	Continue2= Button(f5, text= "Continue Listening", command= ButtonContinue3)
	Continue2.pack()

def ButtonContinue3():
	Walk6= Label(f5, text= "Sir Percival cleared his throat and whispered quietly into my ear, 'I've been held captive here for 3 years by the Doctor. I've led many patients to their deaths here. But you're...different.'")
	Walk6.pack()
	Walk7= Label(f5, text= "I pull away from him in anger and shout, 'Well then, I guess I should just leave you here! I saved you from the Nurse, and even stay-'")
	Walk7.pack()
	continue10= Button(f5, text= "Continue", command= maxcap)
	continue10.pack()

	
def maxcap():

	global DOCTOR
	DOCTOR= PhotoImage(file= "origami.png")
	Doctor= Button(f5, image= DOCTOR)
	Doctor.pack()
	Walk8= Label(f5, text= "A hand closes over my mouth. My scream is muffled by a glove. I hear the cackle behind me.")
	Walk8.pack()
	Walk9= Label(f5, text= "I hear Sir Percival shout, 'Max!' behind me.")
	Walk9.pack()
	ButtonContinue4=Button(f5, text= "Continue", command= cont7)
	ButtonContinue4.pack()




#doctorfight

def cont8():
	f6.destroy()
	f7.pack()

def battle2a():
	Act1= Label(f6, text= "I decide to stop the Doctor from torturing my friend.")
	Act1.pack()
	ButtonL= Button(f6, text= "Go to the Doctor's Office", command= cont8)
	ButtonL.pack()

def battle2b():
	global DEAD
	DEAD= PhotoImage(file= "dead.png")
	Dead= Button(f6, image= DEAD )
	Dead.pack()

	Act2= Label(f6, text= "I decide to forget Max. Although he was the first victim who I'd grown to like, I decided to let him go")
	Act2.pack()
	Act3= Label(f6, text= "As I hear his screams of pain, I feel my heart sink.")
	Act3.pack()
	Act4= Label(f6, text= "After the Doctor had folded his limbs into a pretzel, I walked over to him, and even though he can't hear, I whisper: ")
	Act4.pack()
	Act5= Label(f6, text= "'I'm Sorry, Max'")
	Act5.pack()
	Act6= Label(f6, text= "BAD ENDING(you might want to pick another option)",font= ("Castellar", 15))
	Act6.pack()

Act= Label(f6, text= "YOU ARE PLAYING AS JOHN(SIR PERCIVAL):")
Act.pack()
battle1= Label(f6, text= "I was shocked as Max was taken away from me. But I realized I had to do something.")
battle1.pack()
battle2= Label(f6, text= "I decided I would not be the Doctor's middleman anymore. But...I'd need Max's help. Did he trust me? Should I help him?")
battle2.pack()

Battle1= Button(f6, text= "Help Max", command= battle2a)
Battle1.pack()

battle2b= Button(f6, text= "Don't Help Max" , command= battle2b)
battle2b.pack()


#battlepercivalvsdoctor

def Maxturn():
	f7.destroy()
	f8.pack()

def finalfight():
	Kool= Label(f7,text= "The Doctor steps forward and smiles, 'So...you think this little wimp over here can break my curse huh?'")
	Kool.pack()
	Kool1= Label(f7, text= " I gulp, but I remember how Max had taken to me kindly, and I even saved him. Just..maybe.")
	Kool1.pack()
	Kool2= Label(f7, text= "'I don't think, doc. I know.'")
	Kool2.pack()
	Kool3= Label(f7, text= "I look at Max, who was been panting and sweating in terror. I try to calm him down by giving him a smile.")
	Kool3.pack()
	Kool4= Label(f7, text= "Ok Max, what are you gonna do?")
	Kool4.pack()
	Continue8= Button(text= "Continue", command= Maxturn)
	Continue8.pack()

def Heckle():
	Heckle1= Label(f7, text= "'Hand me a scalpel, Jeff.'")
	Heckle1.pack()
	Heckle2= Label(f7, text= "'BOOOOO!' I shout")
	Heckle2.pack()
	Heckle3= Label(f7, text= "'Hold him down! Jeez!'")
	Heckle3.pack()
	Heckle4=Label(f7, text= "'BOOO! TERRIBLE!'")
	Heckle4.pack()
	Heckle5= Label(f7, text= " Nurse Jeremy shouts,'Hey! Cut it out, John! We're busy!'")
	Heckle5.pack()
	Heckle6= Label(f7, text= "'John?! What are you doing here? Stay out of this.' Dr Origami shouts")
	Heckle6.pack()
	Heckle7= Label(f7, text= "'Not anymore, doc.' I manage to snap some of Max's bindings.")
	Heckle7.pack()
	Heckle8= Label(f7, text= "Doctor Origami suddenly smirks, and orders calmly, 'Now now everyone, John is here for something else. Not the fashion...correct?' ")
	Heckle8.pack()
	Screech3= Label(f7, text= "Even if I've been under the Doctor's curse for 3 years, he still frightens me.")
	Screech3.pack()
	continue6=Button(f7, text="Continue", command= finalfight)
	continue6.pack()

def Screech():
	Screech= Label(f7, text="Running into the swarm of nurses, and doing my Sir Percival voice I shout: 'Dear god what dirty linen!'")
	Screech.pack()
	Screech1= Label(f7, text= "The nurses angrily jostle around back and forth while I secretly snap this binding. 'John, what's gotten into you?!' One shouts.")
	Screech1.pack()
	Screech2= Label(f7, text= "Doctor Origami orders calmly, 'Now now everyone, John is here for something else. Not the fashion...correct?' ")
	Screech2.pack()
	Screech3= Label(f7, text= "Even if I've been under the Doctor's curse for 3 years, he still frightens me.")
	Screech3.pack()
	continue6=Button(f7, text="Continue", command= finalfight)
	continue6.pack()


GROUP= PhotoImage(file= "nurses.png")
Group= Button(f7, image= GROUP)
Group.pack()

Start= Label(f7,text="I arrive just in time to see Doctor Origami set Max down on his operating table. I quickly disguise myself as Sir Percival again.")
Start.pack()
Start1= Label(f7, text= "The table is surrounded by several evil nurses. I...am an absolute weakling. How do I go about getting past them?")
Start1.pack()

Buttonact= Button(f7,text= "Annoy the Nurses", command= Heckle)
Buttonact.pack()

Buttonscene= Button(f7, text= "Make a scene", command= Screech)
Buttonscene.pack()














#MaxvsDoctor

def cont13():
	f8.destroy()
	f9.pack()


def finalbad():
	global DEAD
	DEAD= PhotoImage(file= "dead.png")
	Dead= Button(f8, image= DEAD )
	Dead.pack()
	Max11= Label(f8, text= "I kneel down and whisper to him, even though I know he won't hear: 'I'm sorry, John.'")
	Max11.pack()
	Max12= Label(f8, text= "BAD ENDING, PICK ANOTHER OPTION",font=  ("Castellar", 15))
	Max12.pack()



def book():
	global APPLE
	APPLE= PhotoImage(file= "apple.png")
	Apple= Button(f8, image= APPLE)
	Apple.pack()

	Max4= Label(f8, text= "The nurses shriek at the sight of the apple as well. ")
	Max4.pack()
	Max5= Label(f8, text= "I look at Sir Percival as I realized that while the ghosts could harm us, they were just phantoms.")
	Max5.pack()
	continue12= Button(f8, text= "Continue", command= cont13)
	continue12.pack()

def fight():
	Max1= Label(f8, text="MAX'S POINT OF VIEW")
	Max1.pack()
	Max2= Label(f8, text= "I decide to lunge at the Doctor, as I successfully manage to fool him into thinking I'd punch him.")
	Max2.pack()
	Max3= Label(f8, text= "I grab a childrens book's picture of an apple and hold it to his face as he screeches.")
	Max3.pack()
	Continue12= Button(f8, text= "Continue" ,  command= book)
	Continue12.pack()

	
def flight():
	Max6= Label(f8, text= "I hate this place. I hate everyone in it. I'm outta here.")
	Max6.pack()
	Max7= Label(f8, text= "I jump out of the bed, free of my restraints and escape the seemingly dozens of hands lunging at me.")
	Max7.pack()
	Max9= Label(f8, text= "I reach the dead end of a hallway as the Doctor's Laugh cackles in the background.")
	Max9.pack()
	Max10= Label(f8, text= "I run back to see the body of the dead Sir Percival lying on the floor.")
	Max10.pack()
	Continue11= Button(f8, text= "Continue", command= finalbad)
	Continue11.pack()


Buttonfight= Button(f8,text= "Fight", command= fight)
Buttonfight.pack()
Buttonflight= Button(f8,text= "Flight" , command= flight)
Buttonflight.pack()


#epilogue

END= PhotoImage(file= "endpic.png")
end= Button(f9, image= END)
end.pack()


def AnswerA():
	AnswerA1= Label(f9,text= "1A. 'There are many secrets in life. Perhaps this should be one too.'")
	AnswerA1.pack()
	AnswerA2= Label(f9,text= "This is definitely not because the creator didn't think of the plot too late.")
	AnswerA2.pack()

def AnswerB():
	AnswerB1= Label(f9, text= "'2A. The Doctor actually took mercy on me. But made me work for him until I found someone I trusted to defeat him. That was Max.'- John")
	AnswerB1.pack()

def AnswerC():
	AnswerC= Label(f9, text= "3A. 'Well you know the saying: An apple a day keeps the Doctor away! Haha'- Max")
	AnswerC.pack()
def AnswerD():
	AnswerD= Label(f9, text= "4A.'The Cow is still inside the hospital. I bet it was the true mastermind all along!'- John and Max")
	AnswerD.pack()
def Thankyou():
	Thanks= Label(f9, text= "Thank you so much for playing! I hope you enjoyed it")
	Thanks.pack()



Exit0= Label(f9, text= "GOOD ENDING")
Exit0.pack()

Exit= Label(f9, text= "John and I walk out of the hospital together and stand outside as we make it out of the exit. We don't say anything to each other.")
Exit.pack()
Exit1= Label(f9,text= "We, however would like to explain any questions you might have had for us. Click a button of your choice.")
Exit1.pack()
Question1= Button(f9,text= "1. How did you both get inside the hospital?", command= AnswerA)
Question1.pack()

Question2= Button(f9,text= "2. What was the curse placed on Sir Percival?", command= AnswerB)
Question2.pack()

Question3= Button(f9,text= "3.How did Max know the weakness of the Doctor?", command= AnswerC)
Question3.pack()

Question4= Button(f9, text= "4. Why was there a cow in the hospital?",command= AnswerD)
Question4.pack()
ButtonFinal= Button(f9,text= "That's all I have for now.", command= Thankyou)
ButtonFinal.pack()


	






wind.mainloop()

