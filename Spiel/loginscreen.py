import pygame, sys, time,collision_detct,itertools,gamescreens

from pygame.locals import *

def loginscreen(data):
    playername = ''
    send_data=False
    screen = data['screen']
    base_font = pygame.font.SysFont(None, 160)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(725, 400,50, 130)
    color_inactive = pygame.Color('white')
    color_active = pygame.Color('grey')
    color = color_inactive
    active = False
    play_button=data['start1']
    rand_unten=data['rand_unten']
    rand_oben=data['rand_oben']
    rand_links=data['rand_links']
    rand_rechts=data['rand_rechts']
    corners=data['corners']
    logo = data['logo']
    screenmode=data['screenmode']
    done = False
    #playername = data['playername']


    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: # stoppt Script
                print('Quit game ...')
                pygame.quit() 
                exit(0) 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

                if x > 600 and y > 600 and x < 1005 and y < 735 and len(playername) > 0:
                    screenmode = 'titlescreen'
                    send_data = True
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
        
        width = max(475, text_surface.get_width()-400)
        input_box.w = width
        screen.blit(text_surface, (input_box.x-350, input_box.y+5),)
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(play_button, (600,600))
        screen.blit(rand_links,(0,0))
        screen.blit(rand_rechts,(1613,0))
        screen.blit(rand_unten,(0,985))  
        screen.blit(rand_oben,(0,0))
        screen.blit(corners,(1602,0))
        screen.blit(corners,(0,0))
        screen.blit(corners,(0,970))
        screen.blit(corners,(1602,970))
        screen.blit(logo,(435,150))
        pygame.display.flip()
        clock.tick(30)
        if send_data==True:
            return screenmode
            global player_name
            player_name = playername
