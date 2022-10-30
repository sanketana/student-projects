import pygame
from pygame.locals import *
import random

pygame.init()
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)

screenwidth=900
screenheight=600
gamewindow=pygame.display.set_mode((screenwidth,screenheight))

pygame.display.set_caption("Sudeep's snake game")
pygame.display.update()
clock=pygame.time.Clock()
print(clock)
font=pygame.font.SysFont(None,55)

def textscreen(text,color,x,y):
     screentext=font.render(text,False,color)
     gamewindow.blit(screentext,[x,y])

def plotsnake(gamewindow,red,snklist,snakesize):
     for x,y in snklist:
          pygame.draw.rect(gamewindow,red,[x,y,snakesize,snakesize])
def play(x,y):
     playtext=introfont.render("PLAY",True,(255,0,0))
     screen.blit(playtext,(x,y))



def gameloop():
     exitgame=False
     gameover=False
     pygame.mixer.music.load("TimeOfYourLife.mp3")
     pygame.mixer.music.play()
     snakex=45
     snakey=55
     velocityx=0
     velocityy=0
     snklist=[]
     snklength=1
     foodx=random.randint(20,screenwidth-20)
     
     foody=random.randint(120,screenheight-20)
     score=0
     initvelocity=4
     snakesize=30
     fps=60
     while not exitgame:
          if gameover:
               pygame.mixer.music.stop()
               gamewindow.fill(red)
               textscreen("Game Over!Press Enter to continue",green,100,300)
               for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                         exitgame=True
                    if event.type==pygame.KEYDOWN:
                         if event.key==K_ESCAPE:
                              exitgame=True
                         if event.key==pygame.K_RETURN:
                              gameloop()

          else:
               for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                         exitgame=True
                    if event.type==pygame.KEYDOWN:
                         if event.key==pygame.K_ESCAPE:
                              exitgame=True
                         if event.key==pygame.K_RIGHT:
                              velocityx=initvelocity
                              velocityy=0
                         if event.key==pygame.K_LEFT:
                              velocityx=-initvelocity
                              velocityy=0
                         if event.key==pygame.K_UP:
                              velocityx=0
                              velocityy=-initvelocity
                         if event.key==pygame.K_DOWN:
                              velocityx=0
                              velocityy=initvelocity
               snakex=snakex+velocityx
               snakey=snakey+velocityy
               if score>10:
                    fps=90
               if score>20:
                    fps=180

               if abs(snakex-foodx)<10 and abs(snakey-foody)<10:
                    score+=1
                    foodx=random.randint(50,screenwidth-50)
     
                    foody=random.randint(120,screenheight-20)
                    sound=pygame.mixer.Sound("collect.mp3")
                    pygame.mixer.Sound.play(sound)
                    snklength+=5

               gamewindow.fill(white)
               textscreen("Score:"+str(score),red,5,5)
               pygame.draw.line(gamewindow,red,(0,40),(900,40),5)
               pygame.draw.rect(gamewindow,red,[foodx,foody,snakesize,snakesize])
               head=[]
               head.append(snakex) 
               head.append(snakey) 
               snklist.append(head) 

               if len(snklist)>snklength:
                    del snklist[0]
#               if head in snklist[:-1]:
#                    gameover=True

               if snakex<0 or snakex>screenwidth or snakey<50 or snakey>screenheight-20:
                    gameover=True

               plotsnake(gamewindow,black,snklist,snakesize)
          pygame.display.update()
          clock.tick(fps)

     
gameloop()
                    
                    
                    
                    

               
                         
                              
                         

                    
                         
                         
                    
               
               
     
     
     
     


     
   

