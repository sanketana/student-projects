import pygame,sys
pygame.init()
from pygame.locals import *
import time
import random
screen=pygame.display.set_mode((800,600))

pygame.mixer.init()
pygame.display.set_caption("Max Cars!!!")
logo=pygame.image.load("logo.jpeg")
pygame.display.set_icon(logo)
font1=pygame.font.Font("freesansbold.ttf",38)


introfont=pygame.font.Font("freesansbold.ttf",38)

def introming(x,y):
    intro=pygame.image.load("intro.png")
    screen.blit(intro,(x,y))

def instruming(x,y):
    intro=pygame.image.load("instructun.png")
    run=True
    while run:
        screen.blit(intro,(x,y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

def aboutimg(x,y):
    aboutimg=pygame.image.load("About.png")
    run=True
    while run:
        screen.blit(aboutimg,(x,y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

def play(x,y):
    playtext=introfont.render("PLAY",True,(255,0,0))
    screen.blit(playtext,(x,y))

def about(x,y):
    abouttext=introfont.render("ABOUT",True,(255,0,0))
    screen.blit(abouttext,(x,y))

def instruction(x,y):
    instructiontext=introfont.render("INSTRUCTION",True,(255,0,0))
    screen.blit(instructiontext,(x,y))

def introscreen():
    run=True
    pygame.mixer.music.load("startingMusic.mp3")
    pygame.mixer.music.play()
    while run:
        screen.fill((0,0,0))
        introming(0,0)
        play(100,450)
        instruction(280,440)
        about(600,450)
        x,y=pygame.mouse.get_pos()

        button1=pygame.Rect(60,440,175,50)
        button2=pygame.Rect(265,440,300,50)
        button3=pygame.Rect(590,440,165,50)

        pygame.draw.rect(screen,(255,255,255),button1,6)
        pygame.draw.rect(screen,(255,255,255),button2,6)
        pygame.draw.rect(screen,(255,255,255),button3,6)

        if button1.collidepoint(x,y):
            pygame.draw.rect(screen,(0,255,255),button1,6)
            if click:
                countdown()
        if button2.collidepoint(x,y):
            pygame.draw.rect(screen,(0,255,255),button2,6)
            if click:
                instructionimg()
        if button3.collidepoint(x,y):
            pygame.draw.rect(screen,(0,255,255),button3,6)
            if click:
                aboutimg(0,0)

        click=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
            pygame.display.update()

def  countdown():
    font2=pygame.font.Font("freesansbold.ttf",38)
    countdownbackground=pygame.image.load("bg.png")
    three=font2.render("3",True,(187,30,0))
    two=font2.render("2",True,(187,130,0))
    one=font2.render("1",True,(187,230,0))
    go=font2.render("GO!!!",True,(187,30,0))

    screen.blit(countdownbackground,(0,0))
    pygame.display.update()
    screen.blit(three,(350,250))
    pygame.display.update()
    time.sleep(1)
    screen.blit(countdownbackground,(0,0))
    pygame.display.update()
    screen.blit(two,(350,250))
    pygame.display.update()
    time.sleep(1)
    screen.blit(countdownbackground,(0,0))
    pygame.display.update()
    screen.blit(one,(350,250))
    pygame.display.update()
    time.sleep(1)
    screen.blit(countdownbackground,(0,0))
    pygame.display.update()
    screen.blit(go,(350,250))
    pygame.display.update()
    time.sleep(1)
    gameloop()
    pygame.display.update()
def gameloop():
    pygame.mixer.music.load("BackgroundMusic.mp3")
    pygame.mixer.music.play()
    crash_sound=pygame.mixer.Sound("crashSound.mp3")
    score_value=0

    font2=pygame.font.Font("freesansbold.ttf",25)

    def show_score(x,y):
        score=font2.render("SCORE:"+str(score_value),True,(255,0,0))
        screen.blit(score,(x,y))
    with open("highscore.txt","r") as f:
        highscore=f.read()
    def show_highscore(x,y):
        highscore_text=font1.render("HIGHSCORE:"+str(highscore),True,(255,0,0))
        screen.blit(highscore_text,(x,y))
        pygame.display.update()
    def gameover():
        gameoverimg=pygame.image.load("gameover.png")
        run=True
        while run:
            screen.blit(gameoverimg,(0,0))
            time.sleep(1)
            show_score(330,400)
            time.sleep(1)
            show_highscore(330,450)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                        if event.key==K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                            run=False
                        if event.key==pygame.K_SPACE:
                            countdown()
    bg=pygame.image.load("bg.png")
    
    maincar=pygame.image.load("car.png")
    maincarx=350
    maincary=495
    maincarxchange=0
    maincarychange=0

    car1=pygame.image.load("car1.jpeg")
    car1x=random.randint(178,490)
    car1y=100
    car1ychange=5
 
    car2=pygame.image.load("car2.png")
    car2x=random.randint(178,490)
    car2y=100
    car2ychange=5

    car3=pygame.image.load("car3.png")
    car3x=random.randint(178,490)
    car3y=100
    car3ychange=5

    run=True
    while run:
        for event in pygame.event.get():
           if event.type==pygame.QUIT:
                run=False
                pygame.quit()
                sys.exit()
           if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_RIGHT:
                   maincarxchange-=5
               if event.key==pygame.K_LEFT:
                   maincarxchange+=5
               if event.key==pygame.K_UP:
                   maincarychange-=5
               if event.key==pygame.K_DOWN:
                   maincarychange+=5

           if event.type==pygame.KEYUP:
               if event.key==pygame.K_RIGHT:
                   maincarxchange-=0
               if event.key==pygame.K_LEFT:
                   maincarxchange+=0
               if event.key==pygame.K_UP:
                   maincarychange-=0
               if event.key==pygame.K_DOWN:
                   maincarychange+=0
        if maincarx<178:
            maincarx=178
        if maincarx>490:
            maincarx=490

        if maincary<0:
            maincary=0
        if maincary>495:
            maincary=495

        screen.fill((0,0,0))
        screen.blit(bg,(0,0))
        screen.blit(maincar,(maincarx,maincary))
        screen.blit(car1,(car1x,car1y))
        screen.blit(car2,(car2x,car2y))
        screen.blit(car3,(car3x,car3y))
        show_score(570,280)
        show_highscore(0,0)
        maincarx+=maincarxchange
        maincary+=maincarychange
        car1y+=car1ychange
        car2y+=car2ychange
        car3y+=car3ychange
        if car1y>670:
            car1y=-50
            car1x=random.randint(178,490)
            score_value+=1

        if car2y>670:
            car2y=-10
            car2x=random.randint(178,490)
            score_value+=1

        if car3y>670:
            car3y=-10
            car3x=random.randint(178,490)
            score_value+=1

        if score_value> int(highscore):
            highscore=score_value

        def iscollision(carx,cary,maincary,maincarx):
            distance=abs(carx-maincarx)+abs(cary-maincary)
            if distance<50:
                return True
            else:
                return False
        coll1=iscollision(car1x,car1y,maincarx,maincary)
        coll2=iscollision(car2x,car2y,maincarx,maincary)
        coll3=iscollision(car3x,car3y,maincarx,maincary)

        if coll1 or coll2 or coll3:
            car1ychange=0
            car2ychange=0
            car3ychange=0
            car1y=0
            car2y=0
            car3y=0
            maincarxchange=0
            maincarychange=0
            pygame.mixer.music.stop()
            crash_sound.play()
            time.sleep(1)
            gameover()
        if car1ychange==0 and car2ychange and car3ychange==0:
            pass
        with open("highscore.txt","w") as f:
            f.write(str(highscore))
        pygame.display.update()

introscreen()

