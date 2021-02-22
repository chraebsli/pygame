import pygame, sys, time, figures, wall,collision_detct, functions,itertools

from pygame.locals import *

def loginscreen(data):
    send_data=False
    screen = data['screen']
    base_font = pygame.font.SysFont(None, 160)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 130,250, 100)
    color_inactive = pygame.Color('white')
    color_active = pygame.Color('black')
    color = color_inactive
    active = False
    play_button=data['start']
    playername = ''
    screenmode=data['screenmode']
    done = False


    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: # stoppt Script
                print('Quit game ...')
                pygame.quit() 
                exit(0) 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                            print(playername)
                            playername = ''
                    elif event.key == pygame.K_BACKSPACE:
                            playername = playername[:-1]
                    else:
                        playername = playername + event.unicode
        
        text_surface = base_font.render(f'Name: {playername}',True,(255,255,255))
        width = max(200, text_surface.get_width()+10)
        input_box.w = width
        screen.blit(text_surface, (input_box.x+5, input_box.y+5),)
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(play_button, (100,400))  
        pygame.display.flip()
        clock.tick(30)
        if send_data==True:
            return screenmode


