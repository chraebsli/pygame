import pygame, sys, time, figures, wall,collision_detct, functions,itertools

from pygame.locals import *
counter_felder=0
gamescreen_delete=True
player_coords,player_coords_c=[],[]
moves = []



def titlescreen(data, data_1):
    send_data=False
    screen = data['screen']
    background_titlescreen = data_1['background_titlescreen']
    background_xy = data['background_xy']
    play_button=data_1['play_button']
    skin_button=data_1['skin_button']
    quit_button=data_1['quit_button']
    buttons_titlescreen_xy = data_1['buttons_titlescreen_xy']
    play_button_rect=data_1['play_button_rect']
    skin_button_rect=data_1['skin_button_rect']
    quit_button_rect=data_1['quit_button_rect']
    screenmode=data['screenmode']
    screen.blit(background_titlescreen, (background_xy[0],background_xy[1])) 
    screen.blit(play_button, (buttons_titlescreen_xy[0],buttons_titlescreen_xy[1]))
    screen.blit(skin_button, (buttons_titlescreen_xy[0],buttons_titlescreen_xy[1]))
    screen.blit(quit_button, (buttons_titlescreen_xy[0],buttons_titlescreen_xy[1]))

    for event in pygame.event.get():
        if event.type==pygame.QUIT: # stoppt Script
            print('Quit game ...')
            pygame.quit() 
            exit(0) 
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            if x > play_button_rect[0] and y > play_button_rect[1] and x < play_button_rect[2] and y < play_button_rect[3]:
                screenmode='gamescreen'
                send_data=True           
            elif x > skin_button_rect[0] and y > skin_button_rect[1] and x < skin_button_rect[2] and y < skin_button_rect[3]:
                screenmode='skinscreen'
                send_data=True           
            elif x > quit_button_rect[0] and y > quit_button_rect[1] and x < quit_button_rect[2] and y < quit_button_rect[3]:
                screenmode='quitscreen'
                send_data=True           
    if send_data==True:
        return screenmode


def skinscreen(data, data_3,data_2):
    global player
    send_data=False
    screen = data['screen']
    background_xy = data['background_xy']
    background_skinscreen=data_3['background_skinscreen']
    screenmode=data['screenmode']
    skins_skinscreen=data_3['skins_skinscreen']
    message_skin_one=data_3['message_skin_one']
    skins = data['skins']
    screen.blit(background_skinscreen, (background_xy[0],background_xy[1]))
    c=0
    one = None
    z,w=270,375
    for skin in skins_skinscreen:
        if c==0:
            z=112
        if c==1:
            z=485
        if c==2:
            z=870
        if c==3:
            z=1230
        screen.blit(skins_skinscreen[c], (z,w))
        c+=1
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT: # stoppt Script
            print('Quit game ...')
            pygame.quit() 
            exit(0) 

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:            
                print('escape')
                player = data_2['player']
                screenmode='titlescreen'
                send_data=True
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            if x > 112 and y > 375 and x < 392 and y < 655:
                print('Skin picked')
                player = skins[0]
                screenmode='titlescreen'
                send_data=True
            if x > 485 and y > 375 and x < 765 and y < 655:
                print('Skin 2 picked')
                player = skins[1]
                screenmode='titlescreen'
                send_data=True           
            if x > 870 and y > 375 and x < 1150 and y < 655:
                print('Skin 3 picked')
                player = skins[2]
                screenmode='titlescreen'
                send_data=True
            if x > 1230 and y > 375 and x < 1510 and y < 655:
                print('Skin 4 picked')
                player = skins[3]
                screenmode='titlescreen'
                send_data=True 
              
        
    if send_data==True:
        return screenmode

    
    time.sleep(0.02)


def gamescreen(data, data_2):
    send_data=False
    global counter_felder,block_coords,gamescreen_delete,player_coords, player
    screenmode=data['screenmode']
    keys = data['keys']
    path = data['path']
    screen = data['screen']
    start=data_2['start']
    start_xy=data_2['start_xy']
    end_xy=data_2['end_xy']
    player_xy=data_2['player_xy']
    display_xy=data_2['display_xy']
    end2=data_2['end2']
    wall_coords_xy=data_2['wall_coords_xy']
    walls=data_2['walls']
    block = data_2['block']
    block_coords = data_2['block_coords']
    walls_rect=data_2['walls_rect'] #[wallnr][wallcoord(x,y,-x-y)]
    skins = data['skins']
    main_path=data['main_path']

    
    if gamescreen_delete==True:
        screen.fill(0)
        gamescreen_delete=False
    # Sprites hinzufügen
    #screen.blit(background_game, (background_xy[0],background_xy[1])) 
    end = figures.rand_endskin(path1 = path, end1 = end2)
    screen.blit(start, (start_xy[0],start_xy[1])) 
    screen.blit(end, (end_xy[0],end_xy[1]))
    wall.wall_blit(screen,walls,wall_coords_xy)
    try:
        screen.blit(player, (player_xy[-2],player_xy[-1])) 
    except NameError:
        player = pygame.image.load(path+"images/gamescreen/player.png")
    # überprüft ob eine Taste gedrückt ist
    for event in pygame.event.get(): 
        # überprüft ob das Fenster geschlossen wurde
        if event.type==pygame.QUIT: 
            # stoppt Script
            print('Quit game ...')
            pygame.quit() 
            exit(0) 
        elif event.type == pygame.KEYDOWN:

            if event.key==K_w or event.key==K_UP:
                keys[0]=True
            elif event.key==K_a or event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_s or event.key==K_DOWN:
                keys[2]=True 
            elif event.key==K_d or event.key==K_RIGHT:
                keys[3]=True
            
            elif event.key == K_ESCAPE:            
                print('escape')
                screenmode='titlescreen'
                send_data=True

        elif event.type == pygame.KEYUP:
            if event.key==pygame.K_w or event.key==K_UP:
                keys[0]=False
            elif event.key==pygame.K_a or event.key==K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_s or event.key==K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_d  or event.key==K_RIGHT:
                keys[3]=False

    if keys[0] or keys[1] or keys[2] or keys[3]:
        # Bewegt Player um 1 Feld
        if keys[0]:
            player_xy[1]-=49
        elif keys[2]:
            player_xy[1]+=49
        elif keys[1]:
            player_xy[0]-=49
        elif keys[3]:
            player_xy[0]+=49

# detect für begangene Felder und Wände (funktioniert nicht)
    '''
        # erkennen ob ein Feld bereits begangen ist
        player_coords.append(tuple(player_xy))
        player_coords_c = tuple(player_xy)   
    for e in player_coords:
        try:
#            print('current pos:',player_coords_c)
            if player_coords_c ==e and e != player_coords[-1] :
                print('Duplicate found:',e)
        except UnboundLocalError:
            pass
    # collisiondetect für Wände
    c=0
    for e in walls_rect:
        try:
            if walls_rect[c][0]==player_coords_c[0]:
                if walls_rect[c][1]==player_coords_c[1]:
                    print('Wall detected')
        except UnboundLocalError:
            pass
        c+=1
#    print(player_coords)
    #'''

    # Player wird an anderen Bildschirmrand gesetzt wenn überschritten
    if player_xy[0] > display_xy[0]-5:
        player_xy[0] = 6
    if player_xy[0] < 5:
        player_xy[0] = display_xy[0]-(5+44)
    if player_xy[1] > display_xy[1]-5:
        player_xy[1] = 6
    if player_xy[1] < 5:
        player_xy[1] = display_xy[1]-(5+44)

    # collisiondetect für Wände
    occupied = []
    collision_detct.wall_collision(walls = walls,wall_coords_xy=wall_coords_xy,occupied=occupied,player_coords=player_xy)
    
    # winscreen bzw Nachricht
    if player_xy == end_xy:
        print('You ended this round')
        screenmode='titlescreen.1'.split('.')
        send_data=True
        with open(main_path+'/output.txt', 'w') as out:
            print(screenmode, file=out)    
        if send_data==True:
            return screenmode
    
    time.sleep(0.02)