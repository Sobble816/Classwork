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

#game option buttons
timed_x = 100
timed_y = 300
timed_radius = 40

stage_x = 400
stage_y = 300
stage_radius = 40

#back button
back_x = 33
back_y = 71
back_radius = 30


game = 0

frame_count = 0
score = 0
timer = 500

circle_count = 0

font = pygame.font.SysFont("Comic Sans MS", 30)


circle_radius = 50


#targets
target_x = random.randrange(0, 600)
target_y = random.randrange(0, 600)

# ----------------------------------------------------------------------------------------------------------------------------------
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

        #back button
            back_a = back_x - mouse_x
            back_b = back_y - mouse_y
            back_distance = math.sqrt(back_a**2 + back_b**2)
            if back_distance < back_radius:
                game = 1
                frame_count = 0
                
        #if Timed option was chosen
            timed_a = timed_x - mouse_x
            timed_b = timed_y - mouse_y
            timed_distance = math.sqrt(timed_a**2 + timed_b**2)
            if timed_distance < timed_radius:
                game = 2
                score = 0
                timer = 500    
            
        #if Stage option was chosen
            stage_a = stage_x - mouse_x
            stage_b = stage_y - mouse_y
            stage_distance = math.sqrt(stage_a**2 + stage_b**2)
            if stage_distance < stage_radius:
                game = 3
                score = 0
                frame_count = 0
            
        #target
            target_A = target_x - mouse_x
            target_B = target_y - mouse_y
            target_distance = math.sqrt(target_A**2 + target_B**2)
            if target_distance < circle_radius:
                score += 1
                frame_count = 0
                target_x = random.randrange(0, 600)
                target_y = random.randrange(0, 600)
  

#-------------------------------------------------------------------------------------------------------------------------------
   #so the buttons don't interfer with the game
    if not game == 0: 
        start_radius = 0
    else:
        start_radius = 100


    if not game == 1:
        timed_radius = 0
        stage_radius = 0
    else:
        timed_radius = 40
        stage_radius = 40

# ---Target Boundery-------------------------------------------------------------------------------------------------------------
    if target_x <= 150:
        target_x = 150
    elif  target_x <= 300:
        target_x = 300
    else:
        target_x = 450
    
    if target_y <= 150:
        target_y = 150
    elif target_y <= 300:
        target_y = 300
    else:
        target_y = 450 

#---Starting Screen----------------------------------------------------------------------------------------------------------------
    if game == 0:
        screen.fill("white")
        
        score_text = font.render(f"Score: {score}", False, (0, 0, 0))
        screen.blit(score_text, (0,0))

        pygame.draw.circle(screen, "green", (start_x, start_y), start_radius)
        button_text = font.render("START", False, (0, 0, 0))
        screen.blit(button_text, (245, 278))

#---Chose Game Option Screen------------------------------------------------------------------------------------------------------------------
    elif game == 1:
        screen.fill("white")
        
        #timed option
        pygame.draw.circle(screen, "black", (timed_x, timed_y), timed_radius)
        button_text = font.render("Timed", False, (0, 0, 0))
        screen.blit(button_text, (57, 196))
        
        #stages option
        pygame.draw.circle(screen, "black", (stage_x, stage_y), stage_radius)
        button_text = font.render("Stage", False, (0, 0, 0))
        screen.blit(button_text, (363, 196))

#---Timed Option--------------------------------------------------------------------------------------------------------------------
    elif game == 2:

        frame_count += 1
        timer -= 1
        
    #drawing board
        screen.fill("white")
        #collum 1
        pygame.draw.circle(screen, "grey", (WIDTH/2, HEIGHT/2), circle_radius)
        pygame.draw.circle(screen, "grey", (WIDTH/2, HEIGHT/4), circle_radius)
        pygame.draw.circle(screen, "grey", (WIDTH/2, HEIGHT/1.33), circle_radius)

        #collum 2
        pygame.draw.circle(screen, "grey", (WIDTH/4, HEIGHT/2), circle_radius)
        pygame.draw.circle(screen, "grey", (WIDTH/4, HEIGHT/4), circle_radius)
        pygame.draw.circle(screen, "grey", (WIDTH/4, HEIGHT/1.33), circle_radius)

        #collum 3
        pygame.draw.circle(screen, "grey", (WIDTH/1.33, HEIGHT/2), circle_radius)
        pygame.draw.circle(screen, "grey", (WIDTH/1.33, HEIGHT/4), circle_radius)
        pygame.draw.circle(screen, "grey", (WIDTH/1.33, HEIGHT/1.33), circle_radius)

        #back button
        pygame.draw.circle(screen, "white", (back_x, back_y), back_radius)
        back_font = pygame.font.SysFont("Comic Sans MS", 25)
        back_text = back_font.render("Back", False, (0, 0, 0))
        screen.blit(back_text, (5, 50))


    #drawing targets
        if frame_count < 15:
            pygame.draw.circle(screen, "blue", (target_x, target_y), circle_radius)

        score_text = font.render(f"Score: {score}", False, (0, 0, 0))
        screen.blit(score_text, (0,0))
        
        timer_text = font.render(f"Time: {timer}", False, (0, 0, 0))
        screen.blit(timer_text, (450,0))

        if timer == 0:
            game = 0

#---Stage Option---------------------------------------------------------------------------------------------------------------------
    elif game == 3:
        frame_count += 1
        
        screen.fill("black") # background colour
        # collum 1
        pygame.draw.circle(screen, "white", (WIDTH/2, HEIGHT/2), circle_radius)
        pygame.draw.circle(screen, "white", (WIDTH/2, HEIGHT/4), circle_radius)
        pygame.draw.circle(screen, "white", (WIDTH/2, HEIGHT/1.33), circle_radius)

        # collum 2
        pygame.draw.circle(screen, "white", (WIDTH/4, HEIGHT/2), circle_radius)
        pygame.draw.circle(screen, "white", (WIDTH/4, HEIGHT/4), circle_radius)
        pygame.draw.circle(screen, "white", (WIDTH/4, HEIGHT/1.33), circle_radius)

        # collum 3
        pygame.draw.circle(screen, "white", (WIDTH/1.33, HEIGHT/2), circle_radius)
        pygame.draw.circle(screen, "white", (WIDTH/1.33, HEIGHT/4), circle_radius)
        pygame.draw.circle(screen, "white", (WIDTH/1.33, HEIGHT/1.33), circle_radius)
        
        #back button
        pygame.draw.circle(screen, "black", (back_x, back_y), back_radius)
        back_font = pygame.font.SysFont("Comic Sans MS", 25)
        back_text = back_font.render("Back", False, (0, 0, 0), "white")
        screen.blit(back_text, (5, 50))

    # LEVEL 1 -----------------
        # drawing targets
        if frame_count < 15:
            pygame.draw.circle(screen, "#7AD3FF", (target_x, target_y), circle_radius)

        score_text = font.render(f"Score: {score}", False, (0, 0, 0), "white")
        screen.blit(score_text, (0,0))

    # LEVEL 2 ------------------
        if score == 20:
            circle_radius = 40

#------------------------------------------------------------------------------------------------------------------------------------
  
    pygame.display.flip()
    clock.tick(30)



pygame.quit()
