#Brett 2:00 pm - 4:00 pm 5/2/2022
import pygame
pygame.init()
background = pygame.display.set_mode((630, 630))
base_color = (160, 170, 120)
pygame.draw.rect(background, base_color, pygame.Rect((10, 10), (300, 300)))
pygame.draw.rect(background, base_color, pygame.Rect((320, 10), (300, 300)))
pygame.draw.rect(background, base_color, pygame.Rect((10, 320), (300, 300)))
pygame.draw.rect(background, base_color, pygame.Rect((320, 320), (300, 300)))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if running == False:
            pygame.quit()