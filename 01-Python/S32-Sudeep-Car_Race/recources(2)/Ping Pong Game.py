import pygame
from paddle import Paddle
from ball import Ball




pygame.init()

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
size=(700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong Game")


paddleA=Paddle(white,10,100)
paddleA.rect.x=20
paddleA.rect.y=200

paddleB=Paddle(white,10,100)
paddleB.rect.x=670
paddleB.rect.y=200

ball=Ball(white,10,10)
ball.rect.x=345
ball.rect.y=195

all_sprites_list=pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

scoreA=00
scoreB=00

carryon=True
clock=pygame.time.Clock()

font1=pygame.font.Font("freesansbold.ttf",25)

def show_score_A(x,y):
		score__A=font1.render("SCORE_B:"+str(scoreA),True,white)
		screen.blit(score__A,(x,y))

def show_score_B(x,y):
		score__B=font1.render("SCORE_A:"+str(scoreB),True,white)
		screen.blit(score__B,(x,y))

while carryon:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			carryon=False

		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_ESCAPE:
				carryon=False

	keys=pygame.key.get_pressed()
	if keys[pygame.K_w]:
		paddleA.moveUp(5)
	if keys[pygame.K_s]:
		paddleA.moveDown(5)

	if keys[pygame.K_UP]:
		paddleB.moveUp(5)
	if keys[pygame.K_DOWN]:
		paddleB.moveDown(5)

	if ball.rect.x>=690:
		scoreB+=1
		ball.velocity[0]=-ball.velocity[0]
	if ball.rect.x<=0:
		scoreA+=1
		ball.velocity[0]=-ball.velocity[0]
	if ball.rect.y>490:
		ball.velocity[1]=-ball.velocity[1]
	if ball.rect.y<0:
		ball.velocity[1]=-ball.velocity[1]


	if pygame.sprite.collide_mask(ball,paddleA) or pygame.sprite.collide_mask(ball,paddleB):
		ball.bounce()



	

	print(scoreA)
	print(scoreB)


	all_sprites_list.update()
	screen.fill(black)
	show_score_A(520,20)
	show_score_B(20,20)
	pygame.draw.line(screen,green,(349,0),(349,500),5)
	all_sprites_list.draw(screen)
	pygame.display.flip()
	clock.tick(60)


pygame.quit()

