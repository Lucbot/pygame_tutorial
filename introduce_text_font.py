test_font = pygame.font.Font(font-type or none, font-size)

# or import font from file
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# AA is antialiasing 'amticrenage' utilisée pour lisser les bords dentelés 
text_surface = test_font.render(text, AA "False or True", 'color') 


screen.blit(text_surface,(width, heigth))