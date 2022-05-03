import pygame
pygame.init()
background = pygame.display.set_mode((630, 630))
base_color = (160, 170, 120)
alt_color = (160, 180, 120)
pygame.draw.rect(background, base_color, pygame.Rect((10, 10), (300, 300)))
pygame.draw.rect(background, base_color, pygame.Rect((320, 10), (300, 300)))
pygame.draw.rect(background, base_color, pygame.Rect((320, 320), (300, 300)))
button = pygame.Surface((300, 300))
pygame.Surface.fill(button, alt_color)
b = background.blit(button, (10, 320))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if running == False:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if b.collidepoint(pos):
                pygame.quit()