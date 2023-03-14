import pygame
from sys import exit

pygame.init() 

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('begin game')
clock  = pygame.time.Clock()

sky_surface        = pygame.image.load('image_png/sky.jpg').convert()
sky_size           = 300

player_size        = 133
player_foot        = sky_size - player_size

zombies_size       = 135
zombies_foot       = sky_size - zombies_size

dirt_surface       = pygame.image.load('image_png/dirt.jpg').convert()
dirt_size          = 100

player_surface     = pygame.image.load('image_png/soldier.png').convert_alpha()
player_surface_x   = 100
player_rect        = player_surface.get_rect(midbottom = (player_surface_x,player_foot))


zombies_surface    = pygame.image.load('image_png/zombies.png').convert_alpha()
zombies_surface_x  = 600
zombies_rect       = zombies_surface.get_rect(midleft = (zombies_surface_x,zombies_foot))



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(sky_surface,  (0,0))
	screen.blit(dirt_surface, (0,300))

	zombies_surface_x -= 3
	if zombies_surface_x <= -100: zombies_surface_x = 800
	screen.blit(zombies_surface, (zombies_surface_x,zombies_foot))


	screen.blit(player_surface, (player_surface_x,player_foot))
			# draw all of elements 
			# update everything 
	pygame.display.update()  
	clock.tick(60)