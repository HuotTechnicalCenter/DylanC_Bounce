import pygame,sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()

window=pygame.display.set_mode((500,400))
while True:
    pygame.draw.circle(window,(255,255,0),(250,200),30)

    pygame.draw.lines(window,
                (255,0,255),
                True,
                  ((50,50),
                   (75,75),
                   (25,75)),
                 1)
    pygame.draw.rect(window,(255,0,0),[400,325,50,50],)
    
    pygame.display.update()

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
