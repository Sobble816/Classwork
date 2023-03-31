# pygame template

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN

pygame.init()

WIDTH = 600
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


# ---------------------------
# Initialize global variables

sun_x = 300
sun_y = 100

moon_x = 300
moon_y = 10

day_time = 0
night_time = 0


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
            print(f"({mouse_x}, {mouse_y})")



# Day Time
    screen.fill("#c8eefe")
    pygame.draw.circle(screen, "#ffe647", (sun_x, sun_y), 50) #sun
    pygame.draw.rect(screen, "#4db258", (0, 350, WIDTH, 90)) #ground
    
    #moutain
    pygame.draw.polygon(screen, "#646b71", [(-50, 350), (179, 350), (50, 95)])
    pygame.draw.polygon(screen, "#7c848b", [(102, 350), (254, 350), (182, 172)])
   
    #house
    pygame.draw.rect(screen, "#955b0a", (454, 279, 100, 100))
    pygame.draw.polygon(screen, "#e5421a", [(429, 280), (583, 281), (505, 221)]) #roof
    pygame.draw.rect(screen, "#e5421a", (464, 331, 30, 47)) #door
    pygame.draw.circle(screen, "#F0EE7A", (485, 354), 4)
    #window
    pygame.draw.rect(screen, "white", (514, 302, 30, 30))
    pygame.draw.line(screen, "#955b0a", (513, 316), (544, 316), 3)
    pygame.draw.line(screen, "#955b0a", (529, 302), (529, 332), 3)



    day_time += 1
    
    if day_time == 10:
        day_time = 0
        sun_y += 20



#Sun Down
    if sun_y > 240:
        screen.fill("#ff9000")
        pygame.draw.circle(screen, "#ffe647", (sun_x, sun_y), 50) #sun
        pygame.draw.rect(screen, "#4db258", (0, 350, WIDTH, 90)) #ground

       #moutains
        pygame.draw.polygon(screen, "#646b71", [(-50, 350), (179, 350), (50, 95)])
        pygame.draw.polygon(screen, "#7c848b", [(102, 350), (254, 350), (182, 172)])
      
        #house
        pygame.draw.rect(screen, "#955b0a", (454, 279, 100, 100))
        pygame.draw.polygon(screen, "#e5421a", [(429, 280), (583, 281), (505, 221)]) #roof
        pygame.draw.rect(screen, "#e5421a", (464, 331, 30, 47)) #door
        pygame.draw.circle(screen, "#F0EE7A", (485, 354), 4)
        #window
        pygame.draw.rect(screen, "white", (514, 302, 30, 30))
        pygame.draw.line(screen, "#955b0a", (513, 316), (544, 316), 3)
        pygame.draw.line(screen, "#955b0a", (529, 302), (529, 332), 3)
    

#Night
    if sun_y > 385:
        screen.fill("#323132")
        
        #stars
        pygame.draw.circle(screen, "white", (17, 29), 2)
        pygame.draw.circle(screen, "white", (98, 29), 2)
        pygame.draw.circle(screen, "white", (53, 88), 2)
        pygame.draw.circle(screen, "white", (15, 122), 2)
        pygame.draw.circle(screen, "white", (133, 142), 2)
        pygame.draw.circle(screen, "white", (213, 38), 2)
        pygame.draw.circle(screen, "white", (472, 33), 2)
        pygame.draw.circle(screen, "white", (374, 42), 2)
        pygame.draw.circle(screen, "white", (425, 156), 2)
        pygame.draw.circle(screen, "white", (328, 222), 2)
        pygame.draw.circle(screen, "white", (236, 191), 2)
        pygame.draw.circle(screen, "white", (284, 113), 2)
        pygame.draw.circle(screen, "white", (271, 341), 2)
        pygame.draw.circle(screen, "white", (407, 306), 2)
        pygame.draw.circle(screen, "white", (409, 226), 2)
        pygame.draw.circle(screen, "white", (555, 193), 2)
        pygame.draw.circle(screen, "white", (562, 97), 2)
        pygame.draw.circle(screen, "white", (586, 310), 2)
        pygame.draw.circle(screen, "white", (159, 80), 2)
        pygame.draw.circle(screen, "white", (459, 85), 2)
        pygame.draw.circle(screen, "white", (327, 274), 2)
        pygame.draw.circle(screen, "white", (368, 144), 2)
        pygame.draw.circle(screen, "white", (452, 179), 2)


        pygame.draw.circle(screen, "#fbfbfb", (moon_x, moon_y), 40) #moon
        
        

        night_time += 1
        
        if night_time == 10:
            night_time = 0
            moon_y += 20
       


        pygame.draw.rect(screen, "#245329", (0, 350, WIDTH, 90)) #ground
       
        #moutain
        pygame.draw.polygon(screen, "#3c3f47", [(-50, 350), (179, 350), (50, 95)])
        pygame.draw.polygon(screen, "#4d505b", [(102, 350), (254, 350), (182, 172)])
        
        #house
        pygame.draw.rect(screen, "#694007", (454, 279, 100, 100))
        pygame.draw.polygon(screen, "#ad3214", [(429, 280), (583, 281), (505, 221)]) #roof
        pygame.draw.rect(screen, "#ad3214", (464, 331, 30, 47)) #door
        pygame.draw.circle(screen, "#C3C016", (485, 354), 4)
        #window
        pygame.draw.rect(screen, "#b1abb4", (514, 302, 30, 30))
        pygame.draw.line(screen, "#694007", (513, 316), (544, 316), 3)
        pygame.draw.line(screen, "#694007", (529, 302), (529, 332), 3)
        


    if moon_y > HEIGHT:
        sun_y = -50
        moon_y = 0
    


    pygame.display.flip()
    clock.tick(30)



pygame.quit()
