import pygame
import random
pygame.init()
background = pygame.display.set_mode((670, 670))
R_value = random.randint(0,255)
G_value = random.randint(0,255)
B_value = random.randint(0,255)
base_color = (R_value, G_value, B_value)
alt_color = ((R_value + 50), (G_value + 10), (B_value + 10))

for n in range(0,6):
    for j in range(0,6):
        pygame.draw.rect(background, base_color, pygame.Rect((((100*j) + 10*(j+1)),((100*n) + 10*(n+1))), (100,100)))

n_cord = random.randint(0,5)
j_cord = random.randint(0,5)
button = pygame.Surface((100, 100))
pygame.Surface.fill(button, alt_color)
b = background.blit(button, (((100*j_cord) + 10*(j_cord+1)), ((100*n_cord) + 10*(n_cord+1))))
pygame.display.flip()
running = True
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if running == False:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
        else:
            pos = pygame.mouse.get_pos()
            if not b.collidepoint(pos):#If they click the wrong button
                pygame.quit()
            elif b.collidepoint(pos): #if they click the right button
                score += 1