# pygame template
import math
import pygame
import random

from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN

pygame.init()
pygame.font.init()

# screen size
WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


# -------------------
# Initialize global variables

#start button
start_x = 300
start_y = 300
start_radius = 100


game = 0
score = 0

font = pygame.font.SysFont("Comic Sans MS", 30)


circle_radius = 50

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            
            mouse_x, mouse_y = event.pos

        #start button
            a = start_x - mouse_x
            b = start_y - mouse_y
            distance = math.sqrt(a**2 + b**2)
            if distance < start_radius:
                game = 1
                score = 0
                timer = 500

    else:
    #start screen
        screen.fill("white")
        
        score_text = font.render(f"Score: {score}", False, (0, 0, 0))
        screen.blit(score_text, (0,0))

        pygame.draw.circle(screen, "green", (start_x, start_y), start_radius)
        button_text = font.render("START", False, (0, 0, 0))
        screen.blit(button_text, (245, 278))


    pygame.display.flip()
    clock.tick(30)



pygame.quit()
