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
    screen.fill("#76D3FF")
    pygame.draw.circle(screen, "#ffe647", (sun_x, sun_y), 50) #sun
    pygame.draw.rect(screen, "#4db258", (0, 350, WIDTH, HEIGHT/4)) #ground
    
    #moutain
    pygame.draw.polygon(screen, "#575e63", [(120, 53), (220, 350), (20, 350)])
    pygame.draw.polygon(screen, "#646b71", [(-50, 350), (179, 350), (50, 95)])
    pygame.draw.polygon(screen, "#7c848b", [(88, 350), (137, 218), (153, 233), (182, 172), (254, 350)])
   
    #house
    pygame.draw.rect(screen, "#955b0a", (454, 279, 100, 100))
    pygame.draw.polygon(screen, "#e5421a", [(429, 280), (583, 281), (505, 221)]) #roof
    pygame.draw.rect(screen, "#e5421a", (464, 331, 30, 47)) #door
    pygame.draw.circle(screen, "#F0EE7A", (485, 354), 4)
    #window
    pygame.draw.rect(screen, "white", (514, 302, 30, 30))
    pygame.draw.line(screen, "#955b0a", (513, 316), (544, 316), 3)
    pygame.draw.line(screen, "#955b0a", (529, 302), (529, 332), 3)


    day_time = 0
    day_time += 1
    
    if day_time == 1:
        sun_y += 1



#Sun Down
    if sun_y > 260:
        screen.fill("#ff9000")
        pygame.draw.circle(screen, "#ffe647", (sun_x, sun_y), 50) #sun
        pygame.draw.rect(screen, "#4db258", (0, 350, WIDTH, HEIGHT/4)) #ground

       #moutains
        pygame.draw.polygon(screen, "#575e63", [(120, 53), (220, 350), (20, 350)])
        pygame.draw.polygon(screen, "#646b71", [(-50, 350), (179, 350), (50, 95)])
        pygame.draw.polygon(screen, "#7c848b", [(88, 350), (137, 218), (153, 233), (182, 172), (254, 350)])
      
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
        screen.fill("#0f1012")
        
        #stars
        pygame.draw.circle(screen, "#F6F7F7", (17, 29), 1)
        pygame.draw.circle(screen, "#F6F7F7", (98, 29), 1)
        pygame.draw.circle(screen, "#F6F7F7", (53, 88), 1)
        pygame.draw.circle(screen, "#F6F7F7", (15, 122), 1)
        pygame.draw.circle(screen, "#F6F7F7", (286, 166), 1)
        pygame.draw.circle(screen, "#F6F7F7", (213, 38), 1)
        pygame.draw.circle(screen, "#F6F7F7", (472, 33), 1)
        pygame.draw.circle(screen, "#F6F7F7", (374, 42), 1)
        pygame.draw.circle(screen, "#F6F7F7", (425, 156), 1)
        pygame.draw.circle(screen, "#F6F7F7", (328, 222), 1)
        pygame.draw.circle(screen, "#F6F7F7", (236, 191), 1)
        pygame.draw.circle(screen, "#F6F7F7", (284, 113), 1)
        pygame.draw.circle(screen, "#F6F7F7", (289, 318), 1)
        pygame.draw.circle(screen, "#F6F7F7", (407, 306), 1)
        pygame.draw.circle(screen, "#F6F7F7", (409, 226), 1)
        pygame.draw.circle(screen, "#F6F7F7", (555, 193), 1)
        pygame.draw.circle(screen, "#F6F7F7", (562, 97), 1)
        pygame.draw.circle(screen, "#F6F7F7", (586, 310), 1)
        pygame.draw.circle(screen, "#F6F7F7", (159, 80), 1)
        pygame.draw.circle(screen, "#F6F7F7", (459, 85), 1)
        pygame.draw.circle(screen, "#F6F7F7", (327, 274), 1)
        pygame.draw.circle(screen, "#F6F7F7", (368, 144), 1)
        pygame.draw.circle(screen, "#F6F7F7", (487, 188), 1)
        pygame.draw.circle(screen, "#F6F7F7", (295, 30), 1)
        pygame.draw.circle(screen, "#F6F7F7", (540, 24), 1)
        pygame.draw.circle(screen, "#F6F7F7", (510, 134), 1)
        pygame.draw.circle(screen, "#F6F7F7", (478, 0), 1)
        pygame.draw.circle(screen, "#F6F7F7", (249, 263), 1)
        pygame.draw.circle(screen, "#F6F7F7", (208, 107), 1)
        pygame.draw.circle(screen, "#F6F7F7", (338, 81), 1)
        pygame.draw.circle(screen, "#F6F7F7", (406, 89), 1)
        pygame.draw.circle(screen, "#F6F7F7", (514, 72), 1)
        pygame.draw.circle(screen, "#F6F7F7", (279, 219), 1)


        pygame.draw.circle(screen, "#FDFDFD", (moon_x, moon_y), 40) #moon
        

        night_time = 0
        night_time += 1

        if night_time == 1:    
            moon_y += 1
       


        pygame.draw.rect(screen, "#245329", (0, 350, WIDTH, HEIGHT/4)) #ground
       
        #moutain
        pygame.draw.polygon(screen, "#32353b", [(120, 53), (220, 350), (20, 350)])
        pygame.draw.polygon(screen, "#3c3f47", [(-50, 350), (179, 350), (50, 95)])
        pygame.draw.polygon(screen, "#4d505b", [(88, 350), (137, 218), (153, 233), (182, 172), (254, 350)])
        
        
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
