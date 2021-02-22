# import modules
import os, pygame, random, sys, time, gamescreens,background
from gamescreens import *
from pygame.locals import *

print('please select the game window, the game started')
main_path = os.path.dirname(__file__) # Where your .py file is located
path = str(os.path.join(main_path, 'resources'))+'/' # The resource folder path
# random Wände generieren (Koordinaten)
wall_coords_x,wall_coords_y,wall_coords_xy=[],[],[]
for x in range(12): 
    x = random.randrange(1,34)*49
    wall_coords_x.append(x)
for y in range(12):
    y = random.randrange(1,21)*49
    wall_coords_y.append(y)
len_walls=len(wall_coords_x)
wall_coords_xy = [list(k) for k in zip(wall_coords_x, wall_coords_y)]

wall1=pygame.image.load(path + "images/gamescreen/waende/Wand1x4.png")
wall2=pygame.image.load(path + "images/gamescreen/waende/Wand1x5.png")
wall3=pygame.image.load(path + "images/gamescreen/waende/Wand1x6.png")
wall4=pygame.image.load(path + "images/gamescreen/waende/Wand4x1.png")
wall5=pygame.image.load(path + "images/gamescreen/waende/Wand5x1.png")
wall6=pygame.image.load(path + "images/gamescreen/waende/Wand6x1.png")
walls=[wall1,wall2,wall3,wall4,wall5,wall6]

# load variables
screenmode,sm ='titlescreen',''
keys = [False, False, False, False]
display_xy = [1671, 1034] # bildschirmgrösse
startx_rand = random.randrange(1,34)*49+6
endx_rand = random.randrange(1,39)*49+6
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
status=0
block_coords=[]
wall1_rect=[wall_coords_x[0],wall_coords_y[0],wall_coords_x[0]+55,wall_coords_y[0]+201]
wall2_rect=[wall_coords_x[1],wall_coords_y[1],wall_coords_x[1]+55,wall_coords_y[1]+250]
wall3_rect=[wall_coords_x[2],wall_coords_y[2],wall_coords_x[2]+55,wall_coords_y[2]+299]
wall4_rect=[wall_coords_x[3],wall_coords_y[3],wall_coords_x[3]+201,wall_coords_y[3]+55]
wall5_rect=[wall_coords_x[4],wall_coords_y[4],wall_coords_x[4]+250,wall_coords_y[4]+55]
wall6_rect=[wall_coords_x[5],wall_coords_y[5],wall_coords_x[5]+299,wall_coords_y[5]+55]
walls_rect=[wall1_rect,wall2_rect,wall3_rect,wall4_rect,wall5_rect,wall6_rect]

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
start = pygame.image.load(path + "images/loginscreen/start.png")

pygame.init()
screen=pygame.display.set_mode((display_xy))

# Datenpakete für Parameter
# data: universell, data_1: titlescreen, data_2: gamescreen,data_3: skinscreen
data = {'path':path,'display_xy':display_xy,'background_xy':background_xy,'keys':keys,
'screen':screen, 'gamescreens':gamescreens,'screenmode':screenmode,'main_path':main_path,'skins':skins}
data_1 = {'background_titlescreen':background_titlescreen,
'play_button':play_button,'buttons_titlescreen_xy':buttons_titlescreen_xy,
'play_button_rect':play_button_rect,'quit_button':quit_button,'skin_button':skin_button,
'skin_button_rect':skin_button_rect,'quit_button_rect':quit_button_rect}
data_2 = {'background_game':background_game,'start':start,
'player': player,'start_xy':start_xy,'end_xy': end_xy,'player_xy': player_xy,
'display_xy':display_xy,'end2': 0,'walls':walls,'block_xy': block_xy,'block':block,
'block_coords':block_coords,'wall_coords_xy':wall_coords_xy,'walls_rect':walls_rect}
data_3={'background_skinscreen':background_skinscreen,'skins_skinscreen':skins_skinscreen,
'message_skin_one':message_skin_one}

screen.fill(0) 
# Spielablauf
running = True
while running == True:

    # wenn das spiel erfolgreich beendet wird löscht es den screen
    if status==1:
        screen.fill(0) 
    
    # titlescreen
    if screenmode =='titlescreen'or sm=='titlescreen':
        screenmode,sm='titlescreen','titlescreen'
        sm=gamescreens.titlescreen(data,data_1)

    # gamescreen    
    if screenmode =='gamescreen' or sm=='gamescreen':
        #screen.fill(0) # wenn funktion == True: keine Playerdots
        screenmode,sm='gamescreen','gamescreen'
        sm=gamescreens.gamescreen(data=data,data_2=data_2)
        background.back(screen = screen, path =path)
        a=open(main_path+'/output.txt', 'r')
        t=a.read()
        if t=="['titlescreen', '1']":
            t=list(t)
            status=t[1]
            sm=t[0]
            print(status,sm)


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
