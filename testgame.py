import time

import pygame

pygame.init()

WINDOW_W = 600
WINDOW_H = 800
FRAME_DURATION = 1. / 60.

window = pygame.display.set_mode((WINDOW_W, WINDOW_H))

clock = pygame.time.Clock()

player_rect = pygame.Rect (200, 500, 50, 50)

player_rect2 = pygame.Rect (200, 0, 50, 50)

gameOn = True 

speed_a = 8
speed_b = -7



# laisse le temps a pygame.init de se lancer avant de lancer le jeu 
time.sleep(1)

while gameOn:

	# time nombre de temps qui s'est ecouler depuis 1970 on fait la difference depuis 1970 jusqu'a maintenant 
    render_start = time.time()

    for event in pygame.event.get():
         
        # Check for KEYDOWN event
        if event.type == pygame.KEYDOWN:
             
            # If the Backspace key has been pressed set
            # running to false to exit the main loop
            if event.key == pygame.K_BACKSPACE:
                gameOn = False
                 
        # Check for QUIT event
        elif event.type == pygame.QUIT:
            gameOn = False

    player_rect  .bottom += speed_a
    player_rect2 .top    += speed_b

    collide = pygame.Rect.colliderect (player_rect, player_rect2)

    if collide:
        speed_a *= -1
        speed_b *= -1

    if player_rect  .top < 0 or player_rect  .bottom > WINDOW_H :  speed_a *= -1
    if player_rect2 .top < 0 or player_rect2 .bottom > WINDOW_H :  speed_b *= -1

    pygame.draw.rect (window, (0, 255, 0), player_rect)
    pygame.draw.rect (window, (0, 0, 255), player_rect2)

    pygame.display.update()
    window.fill ((155, 155, 155))

    # render_end soustraction avec render_start pour avoir le temps ecouler entre le debut et la fin 
    # render rendu visuel, calcul visuel 
    # sleep switch a la frame suivante
    render_end  = time.time()
    render_time = render_end - render_start
    sleep_time  = FRAME_DURATION - render_time
    if render_time < FRAME_DURATION:
        time.sleep(sleep_time)
    pygame.display.flip()