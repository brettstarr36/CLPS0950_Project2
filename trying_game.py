import pygame
import random
pygame.init()
score = 0
N = 50
print("Welcome to the Color Visual Acuity Game!")  # welcoming message
intro_1 = input("enter 1 to continue") # engagement to trigger directions
if intro_1 == "1": # confirm engagement
    print("Directions: You will be shown an image with a grid where")
    print("all the colors are of the same hue except one square") # displays instructions to participant
    print("you will click on the square of the different hue")
    intro_2 = input ("enter 1 to begin"); #  engagement to confirm understanding of part 1 of directions
else:
    disp('End game') #ends game if they do not want to enter 1 to play
    pygame.quit() # end script if they do not enter '1' to continue
if intro_2 == "1":# confirmation of part 1 of directions triggers part two of directions
    background = pygame.display.set_mode((670, 670))
    R_value = random.randint(0, 255)
    G_value = random.randint(0, 255)
    B_value = random.randint(0, 255)
    base_color = (R_value, G_value, B_value)
    if R_value > 205:
        R_val_alt = R_value - 50
    else:
        R_val_alt = R_value + 50
    if G_value > 205:
        G_val_alt = G_value - 50
    else:
        G_val_alt = G_value + 50
    if B_value > 205:
        B_val_alt = B_value - 50
    else:
        B_val_alt = B_value + 50
    alt_color = (R_val_alt, G_val_alt, B_val_alt)
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
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if running == False:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if b.collidepoint(pos):#If they click the right button
                    N -=10
                    score += 1
                    R_value = random.randint(0, 255)
                    G_value = random.randint(0, 255)
                    B_value = random.randint(0, 255)
                    base_color = (R_value, G_value, B_value)
                    if R_value > 205:
                        R_val_alt = R_value - N
                    else:
                        R_val_alt = R_value + N
                    if G_value > 205:
                        G_val_alt = G_value - N
                    else:
                        G_val_alt = G_value + N
                    if B_value > 205:
                        B_val_alt = B_value - N
                    else:
                        B_val_alt = B_value + N
                    alt_color = (R_val_alt, G_val_alt, B_val_alt)

                    for n in range(0, 6):
                        for j in range(0, 6):
                            pygame.draw.rect(background, base_color,
                                             pygame.Rect((((100 * j) + 10 * (j + 1)), ((100 * n) + 10 * (n + 1))),
                                                         (100, 100)))

                    n_cord = random.randint(0, 5)
                    j_cord = random.randint(0, 5)
                    button = pygame.Surface((100, 100))
                    pygame.Surface.fill(button, alt_color)
                    b = background.blit(button,
                                        (((100 * j_cord) + 10 * (j_cord + 1)), ((100 * n_cord) + 10 * (n_cord + 1))))
                    pygame.display.flip()

                else: #if they click the wrong button
                    pygame.quit()
                    print('Your score was', score)