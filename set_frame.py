import pygame
from sys import exit

pygame.init() 

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('begin game')
clock = pygame.time.Clock()


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

			# draw all of elements 
			# update everything 
	pygame.display.update()  
	clock.tick(60)