import pygame 
from pygame.locals import *

if __name__=="__main__":
	pygame.init()

	surface = pygame.display.set_mode((1000,500))
	surface.fill((204, 91, 53))
	block = pygame.image.load("resources/block.jpg").convert()
	surface.blit(block,(100,100))

	pygame.display.flip()

	running = True

	while running:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
			elif event.type == QUIT:
				running = False