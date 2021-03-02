import pygame, sys, time,collision_detct,gamefunctions,itertools,random
from os import read, write
from pygame.locals import *
felder = []

counter_felder=0
player_coords,player_coords_c=[],[]
moves = []
black = pygame.Color('black')
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
    button_highscore=data_1['button_highscore']
    screenmode=data['screenmode']
    main_path=data['main_path']
    upperplayername = playername.upper()
    base_font = pygame.font.SysFont(None, 110)
    text_surface = base_font.render(upperplayername,False,(255,255,255))
    screen.blit(background_titlescreen, (background_xy[0],background_xy[1])) 
    screen.blit(play_button, (buttons_titlescreen_xy[0],buttons_titlescreen_xy[1]))
    screen.blit(skin_button, (buttons_titlescreen_xy[0],buttons_titlescreen_xy[1]))
    screen.blit(quit_button, (buttons_titlescreen_xy[0],buttons_titlescreen_xy[1]))
    screen.blit(button_highscore,(1200,5))
    screen.blit(text_surface,(50,5))

    for event in pygame.event.get():
        if event.type==pygame.QUIT: # stoppt Script
            print('Quit game ...')
            pygame.quit() 
            exit(0) 

        # erkennen von Mausposition 
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
            elif x > 1200 and y > 5 and x < 1652 and y < 94:
                screenmode='highscore'
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
    skins = data['skins']
    screen.blit(background_skinscreen, (background_xy[0],background_xy[1]))
    c=0
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
        
        # laden der skins
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            if x > 112 and y > 375 and x < 392 and y < 655:
                print('Skin 1 picked')
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


def gamescreen(data, data_2,remo_list):
    send_data=False
    #Punkte die man In-Game mit Münzen erzielt
    points = 0
    global counter_felder,block_coords,player_coords, player
    screenmode=data['screenmode']
    keys = data['keys']
    path = data['path']
    screen = data['screen']
    start1=data_2['start']
    start_xy=data_2['start_xy']
    end_xy=data_2['end_xy']
    player_xy=data_2['player_xy']
    display_xy=data_2['display_xy']
    end2=data_2['end2']
    block_coords = data_2['block_coords']
    walls_rect=data_2['walls_rect'] #[wallnr][wallcoord(x,y,-x-y)]
    newgame=data['newgame']
    coin2=data_2['coin2']
    coin_coords_xy = data_2['coin_coords']
    coins_rect = data_2['coins_rect']
    wall_complete = []
    coin_complete = []
    coin_coords_x = []
    coin_coords_y = []
    stop = False
    

    # Sprites hinzufügen
    counter = 0
    if counter == 0:
        list_coords = collision_detct.move(screen,player_xy,False)
        counter += 1
    if counter != 0:
        collision_detct.move(screen,player_xy,True)
    
    collision_detct.drawing(screen,walls_rect)
    coinskin = gamefunctions.random_coinskin(path1 = path,coin1 = coin2)
    endskin = gamefunctions.random_endskin(path1 = path, end1 = end2)
    
    
    screen.blit(endskin, (end_xy[0],end_xy[1]))
    screen.blit(start1, (start_xy[0],start_xy[1])) 
    gamefunctions.background(screen, path)
    collision_detct.playerpath(remo_list,screen,player_xy)
    
    # bei Feheler vom laden von Playersprite
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
            elif event.key==K_q:
                if keys[5] == False:
                    keys[5] = True
                elif keys[5] == True:
                    keys[5]=False
            elif event.key == K_ESCAPE:
                screenmode=='titlescreen'

        elif event.type == pygame.KEYUP:
            if event.key==pygame.K_w or event.key==K_UP:
                keys[0]=False
            elif event.key==pygame.K_a or event.key==K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_s or event.key==K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_d  or event.key==K_RIGHT:
                keys[3]=False
            elif event.key==pygame.K_q:
                keys[5] = False

    if keys[0] or keys[1] or keys[2] or keys[3]:
        counter_felder=1
        for e in remo_list:
            counter_felder+=1
        counter_felder += 1
        print('counter:',counter_felder)
        # Colissiondetect für Wände, begangene Felder
        collision_detct.run(screen,player_xy)
        collision_detct.check_counter(screen,remo_list,coinskin,coins_rect)
        remo_list = collision_detct.collideplayer(player_xy,list_coords,remo_list,False)
    if keys[5]:
        gamefunctions.show_points(points,remo_list,screen,coins_rect)
    if keys[4]:
        collision_detct.check_counter(screen,remo_list,coinskin,coins_rect)  
        # Bewegt Player um 1 Feld
        if keys[0]:
            player_xy[1]-=49
        elif keys[2]:
            player_xy[1]+=49
        elif keys[1]:
            player_xy[0]-=49
        elif keys[3]:
            player_xy[0]+=49
        points += 1
        collide=collision_detct.wall_collision(walls_rect,player_xy)
        remo_list = collision_detct.collideplayer(player_xy,list_coords,remo_list,True)
        points = gamefunctions.calculate_points(points,remo_list,coins_rect)
        print(points)
        try:
            remo_list = str(remo_list).split('.')
            newgame,remo_list=bool(remo_list[1]),remo_list[0]
        except IndexError:
            pass
        if collide=='titlescreen.True':
            newgame=True
    
    # Player wird an anderen Bildschirmrand gesetzt wenn überschritten
    if player_xy[0] > 1624:
        player_xy[0] = 6
    if player_xy[0] < 5:
        player_xy[0] = 1623
    if player_xy[1] > 987:
        player_xy[1] = 6
    if player_xy[1] < 5:
        player_xy[1] = 986
        player_xy[1] = display_xy[1]-(5+44)

    # winscreen bzw Nachricht
    if player_xy == end_xy:
        global playername
        print('You ended this round')
        print(playername)
        print(points)
        send_data=True
    if screenmode=='titlescreen' or newgame==True:
        send_data=True
    if send_data==True:
        #gamefunctions.scores(counter_felder,playername,path)
        screenmode='titlescreen.True'
        return screenmode


def loginscreen(data):
    global playername
    playername = ""
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
        pygame.draw.rect(screen, color, input_box, 2)
        blit_list=[text_surface,play_button,rand_links,rand_rechts,rand_unten,rand_oben,corners,corners,corners,corners,logo]
        list2=[(input_box.x-350, input_box.y+5),(600,600),(0,0),(1613,0),(0,985),(0,0),(1602,0),(0,0),(0,970),(1602,970),(435,150)]
        c=0
        for img in blit_list:
            screen.blit(img,list2[c])
            c+=1
        pygame.display.flip()
        clock.tick(30)
        if send_data==True:
            return screenmode

def highscorescreen(data):
    screen = data['screen']
    banner = data['banner']
    return_banner = data['return_banner']
    black = pygame.Color('black')
    screen.fill(black)
    screen.blit(banner,(410,15))
    screen.blit(return_banner,(1225,900))
    for event in pygame.event.get():
            if event.type==pygame.QUIT: # stoppt Script
                print('Quit game ...')
                pygame.quit() 
                exit(0) 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if x > 1225 and y > 900 and x < 1630 and y < 1035:
                    screenmode='titlescreen'
                    send_data=True
                    return screenmode