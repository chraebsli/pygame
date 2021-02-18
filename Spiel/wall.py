# Funktion für das setzen der Wände
def wall_blit(screen,walls,wall_coords_xy):
    screen=screen

    wall1=walls[0] #
    wall2=walls[1]
    wall3=walls[2]
    wall4=walls[3]
    wall5=walls[4]
    wall6=walls[5]

    screen.blit(wall1, wall_coords_xy[0]) 
    screen.blit(wall2, wall_coords_xy[1]) 
    screen.blit(wall3, wall_coords_xy[2]) 
    screen.blit(wall4, wall_coords_xy[3]) 
    screen.blit(wall5, wall_coords_xy[4]) 
    screen.blit(wall6, wall_coords_xy[5])
    screen.blit(wall1, wall_coords_xy[6]) 
    screen.blit(wall2, wall_coords_xy[7]) 
    screen.blit(wall3, wall_coords_xy[8]) 
    screen.blit(wall4, wall_coords_xy[9]) 
    screen.blit(wall5, wall_coords_xy[10]) 
    screen.blit(wall6, wall_coords_xy[11]) 
