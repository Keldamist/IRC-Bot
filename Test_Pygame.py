import pygame
from pygame.locals import *
from Test_Bot import main

pygame.init()


screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont('Monster hunter', 30)

bg = (127, 127, 127)


run = True
while run:
    
	main()
	screen.fill(bg)
	screen.blit(message,10, 10)
	screen.blit(img, 100, 100)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False	


	pygame.display.update()


pygame.quit()
