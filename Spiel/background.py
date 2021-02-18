import pygame
def back(screen,path):
    x,y = 1,1
    counter_v,counter_h=0,0
    senkrechte = pygame.image.load(path + "images/gamescreen/senkrechte.png")
    gerade = pygame.image.load(path + "images/gamescreen/gerade.png")

    run_v=True
    while run_v==True:
        counter_v+=1
        screen.blit(senkrechte, (x,1))
        x+=49
        if counter_v==36:
            run_v=False
    
    run_h=True
    while run_h==True:
        counter_h+=1
        screen.blit(gerade, (1,y))
        y+=49
        if counter_h==36:
            run_h=False