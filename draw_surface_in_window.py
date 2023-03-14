# draw start at bottom left of the screen 
test_surface = pygame.Surface((widht, height))

# color surfaces 
test_surface.fill('RED')

# import image from even file of pygame 
test_surface = pygame.image.load('image_png/dirt.png')


screen.blit(test_surface, (width,height))