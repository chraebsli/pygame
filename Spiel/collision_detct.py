z = 0
a = 0
def check_moves(player_coords,savedlist):
    x = [5,54,103,152,201,299,348,446,544,642,691,740,789,838,887,936,985,1034,1132,1181,1230,1279,1328,1426,1475,1524,1573,1622]
    y = [6,55,104,153,202,300,349,447,545,643,692,741,790,839,888,937,986]
    
def wall_collision(walls,wall_coords_xy,occupied,player_coords):
    occupied = [wall_coords_xy[0],[wall_coords_xy[0][0],wall_coords_xy[0][1]-49],[wall_coords_xy[0][0],wall_coords_xy[0][1]-98],[wall_coords_xy[0][0],wall_coords_xy[0][1]-147],
    wall_coords_xy[6],[wall_coords_xy[6][0],wall_coords_xy[6][1]-49],[wall_coords_xy[6][0],wall_coords_xy[6][1]-98],[wall_coords_xy[6][0],wall_coords_xy[6][1]-147]]
    if player_coords in occupied:
        print('lost')



def check_reset(player_coords,coords):
    
    SavedList = [player_coords[-2],player_coords[-1]]
    
    coords.append(SavedList)
    coords.reverse()
