# import moduleswww
import os, pygame, random, sys, time, gamescreens,gamefunctions,collision_detct
from gamescreens import *
from pygame.locals import *

remo_list = []
print('please select the game window, the game started')
main_path = os.path.dirname(__file__) # Where your .py file is located
path = str(os.path.join(main_path, 'resources'))+'/' # The resource folder path

# random Wände generieren (Koordinaten)
wall_coords_x,wall_coords_y,wall_coords_xy=[],[],[]
coin_coords_x,coin_coords_y,coin_coords_xy=[],[],[]
for x in range(12): 
    x = random.randrange(1,34)*49+6
    wall_coords_x.append(x)
for y in range(12):
    y = random.randrange(2,15)*49+6
    wall_coords_y.append(y)
#random Coins generieren(Koordinaten)
for x1 in range(10):
    x1 = random.randrange(1,34)*49+7
    coin_coords_x.append(x1)
for y1 in range(10):
    y1 = random.randrange(1,21)*49+7
    coin_coords_y.append(y1)
len_coins=len(coin_coords_x)
coin_coords_xy = [list(w) for w in zip(coin_coords_x, coin_coords_y)]
len_walls=len(wall_coords_x)

# zusammenführen der Koordinaten
wall_coords_xy = [list(k) for k in zip(wall_coords_x, wall_coords_y)]
wall1=pygame.image.load(path + "images/gamescreen/waende/Wand1x4.png")
wall2=pygame.image.load(path + "images/gamescreen/waende/Wand1x5.png")
wall3=pygame.image.load(path + "images/gamescreen/waende/Wand1x6.png")
wall4=pygame.image.load(path + "images/gamescreen/waende/Wand4x1.png")
wall5=pygame.image.load(path + "images/gamescreen/waende/Wand5x1.png")
wall6=pygame.image.load(path + "images/gamescreen/waende/Wand6x1.png")
walls=[wall1,wall2,wall3,wall4,wall5,wall6]

# load variables
newgame=False
playername=''
screenmode,sm ='loginscreen','loginscreen'
keys = [False, False, False, False,True,False]
display_xy = [1671, 1034] # bildschirmgrösse
startx_rand = random.randrange(1,34)*49+5
endx_rand = random.randrange(1,34)*49+5
background_xy = [1,1]
start_xy = [startx_rand,986]
end_xy = [endx_rand, 6]
player_xy = [start_xy[0],start_xy[1]]
buttons_titlescreen_xy = [1,1]
play_button_rect = [564,203,1114,477] # x, y, -x, -y
skin_button_rect = [320,553,770,777] # x, y, -x, -y
quit_button_rect = [900,551,1350,775] # x, y, -x, -y
block_xy = [1,1]
end2 = 0
coin2 = 0
status=0
block_coords=[]

# var für pygame.Rect
wall1_rect=[wall_coords_x[0],wall_coords_y[0],48,192] # x, y, -x, -y
wall2_rect=[wall_coords_x[1],wall_coords_y[1],48,242]
wall3_rect=[wall_coords_x[2],wall_coords_y[2],48,291]
wall4_rect=[wall_coords_x[3],wall_coords_y[3],193,48]
wall5_rect=[wall_coords_x[4],wall_coords_y[4],241,48]
wall6_rect=[wall_coords_x[5],wall_coords_y[5],291,48]
wall7_rect=[wall_coords_x[6],wall_coords_y[6],48,192] 
wall8_rect=[wall_coords_x[7],wall_coords_y[7],48,242]
wall9_rect=[wall_coords_x[8],wall_coords_y[8],48,291]
wall10_rect=[wall_coords_x[9],wall_coords_y[9],193,48]
wall11_rect=[wall_coords_x[10],wall_coords_y[10],242,48]
wall12_rect=[wall_coords_x[11],wall_coords_y[11],291,48]
walls_rect=[wall1_rect,wall2_rect,wall3_rect,wall4_rect,wall5_rect,wall6_rect,wall7_rect,wall8_rect,wall9_rect,wall10_rect,wall11_rect,wall12_rect]

coin1_rect=pygame.Rect(coin_coords_x[0],coin_coords_y[0],44,44) # x, y, -x, -y
coin2_rect=pygame.Rect(coin_coords_x[1],coin_coords_y[1],44,44)
coin3_rect=pygame.Rect(coin_coords_x[2],coin_coords_y[2],44,44)
coin4_rect=pygame.Rect(coin_coords_x[3],coin_coords_y[3],44,44)
coin5_rect=pygame.Rect(coin_coords_x[4],coin_coords_y[4],44,44)
coin6_rect=pygame.Rect(coin_coords_x[5],wall_coords_y[5],44,44)
coin7_rect=pygame.Rect(coin_coords_x[6],coin_coords_y[6],44,44)
coin8_rect=pygame.Rect(coin_coords_x[7],coin_coords_y[7],44,44)
coin9_rect=pygame.Rect(coin_coords_x[8],coin_coords_y[8],44,44)
coin10_rect=pygame.Rect(coin_coords_x[9],coin_coords_y[9],44,44)
coins_rect =[coin1_rect,coin2_rect,coin3_rect,coin4_rect,coin5_rect,coin6_rect,coin7_rect,coin8_rect,coin9_rect,coin10_rect]
# load images
background_titlescreen = pygame.image.load(path+"images/titlescreen/background_titlescreen.png")
background_game = pygame.image.load(path+"images/gamescreen/background.png")
background_skinscreen=pygame.image.load(path+"images/skinsscreen/background.png")
start = pygame.image.load(path+"images/gamescreen/start.png")
player = pygame.image.load(path+"images/gamescreen/player.png")
play_button = pygame.image.load(path+"images/titlescreen/button_play.png")
skin_button= pygame.image.load(path+"images/titlescreen/button_skins.png")
quit_button= pygame.image.load(path+"images/titlescreen/button_quit.png")
block = pygame.image.load(path + "images/gamescreen/block.png")
skin1_skinscreen = pygame.image.load(path + "images/skinsscreen/skin1.png")
skin2_skinscreen = pygame.image.load(path + "images/skinsscreen/skin2.png")
skin3_skinscreen = pygame.image.load(path + "images/skinsscreen/skin3.png")
skin4_skinscreen = pygame.image.load(path + "images/skinsscreen/skin4.png")
skins_skinscreen = [skin1_skinscreen,skin2_skinscreen,skin3_skinscreen,skin4_skinscreen]
message_skin_one = pygame.image.load(path + "images/skinsscreen/Message_One.png")
skin_one = pygame.image.load(path + "images/gamescreen/skins/skin1.png")
skin_two = pygame.image.load(path + "images/gamescreen/skins/skin2.png")
skin_three = pygame.image.load(path + "images/gamescreen/skins/skin3.png")
skin_four = pygame.image.load(path + "images/gamescreen/skins/skin4.png")
skins = [skin_one,skin_two,skin_three,skin_four]
start1 = pygame.image.load(path + "images/loginscreen/start.png")
rand_unten = pygame.image.load(path + "images/loginscreen/rand_unten.png")
rand_oben = pygame.image.load(path + "images/loginscreen/rand_oben.png")
rand_links = pygame.image.load(path + "images/loginscreen/rand_links.png")
rand_rechts = pygame.image.load(path + "images/loginscreen/rand_rechts.png")
corners = pygame.image.load(path + "images/loginscreen/corners.png")
logo = pygame.image.load(path + "images/loginscreen/logo.png")

pygame.init()
screen=pygame.display.set_mode((display_xy))

# Datenpakete für Parameter
# data: universell, data_1: titlescreen, data_2: gamescreen,data_3: skinscreen
data = {'path':path,'display_xy':display_xy,'background_xy':background_xy,'keys':keys,'main_path':main_path,'newgame':newgame,
'screen':screen, 'gamescreens':gamescreens,'screenmode':screenmode, 'skins':skins,'start1':start1,'rand_unten':rand_unten,
'rand_oben':rand_oben,'rand_links':rand_links,'rand_rechts':rand_rechts,'corners':corners,'logo':logo,'playername':playername}
data_1 = {'background_titlescreen':background_titlescreen,
'play_button':play_button,'buttons_titlescreen_xy':buttons_titlescreen_xy,
'play_button_rect':play_button_rect,'quit_button':quit_button,'skin_button':skin_button,
'skin_button_rect':skin_button_rect,'quit_button_rect':quit_button_rect}
data_2 = {'background_game':background_game,'start':start,
'player': player,'start_xy':start_xy,'end_xy': end_xy,'player_xy': player_xy,
'display_xy':display_xy,'end2': 0,'walls':walls,'block_xy': block_xy,'block':block,'coin2':0,
'block_coords':block_coords,'wall_coords_xy':wall_coords_xy,'walls_rect':walls_rect,'coin_coords':coin_coords_xy,'coins_rect':coins_rect}
data_3={'background_skinscreen':background_skinscreen,'skins_skinscreen':skins_skinscreen,
'message_skin_one':message_skin_one}

screen.fill(0) 
# Spielablauf
running = True
while running == True:
    
    # wenn das spiel beendet wird setzt es das spiel zurück
    if newgame==True:
        screen.fill(0) 
        pygame.display.flip()
        player_xy.clear()
        player_xy=start_xy.copy()
        keys = [False, False, False, False]
        newgame=False
        data.update({'newgame':newgame})
        data.update({'keys':keys})
        data_2.update({'player_xy':player_xy}) 
        remo_list.clear()

    # loginscreen
    if screenmode == 'loginscreen' or sm== 'loginscreen':
        screenmode,sm == 'loginscreen', 'loginscreen'
        sm=gamescreens.loginscreen(data)

    # titlescreen
    if screenmode =='titlescreen'or sm=='titlescreen':
        screenmode,sm='titlescreen','titlescreen'
        sm=gamescreens.titlescreen(data,data_1)

    # gamescreen    
    if screenmode =='gamescreen' or sm=='gamescreen':
        screenmode,sm='gamescreen','gamescreen'
        sm=gamescreens.gamescreen(data=data,data_2=data_2,remo_list=remo_list)
        try:
            sm = str(sm).split('.')
            newgame,sm=bool(sm[1]),sm[0]
        except IndexError:
            pass

    # skinscreen
    if screenmode =='skinscreen'or sm=='skinscreen':
        screenmode,sm='skinscreen','skinscreen'
        sm=gamescreens.skinscreen(data=data,data_3=data_3,data_2=data_2)
    
    # quit
    if screenmode =='quitscreen'or sm=='quitscreen':
        print('Quit...')
        pygame.quit() 
        exit(0) 
    
    # grundlegende Funktionen
    pygame.display.flip() 
    time.sleep(0.05)
