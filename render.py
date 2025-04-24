import pygame
import random
import library as lib

def convert3D_2D(objs):
    x, y, z = (objs[0] - lib.Cam[0]), (objs[1] - lib.Cam[1]), (objs[2] - lib.Cam[2])

    screen_x = (x - z) * lib.width
    screen_y = (x + z) * lib.width / 2 - (y * lib.height)

    return screen_x, screen_y

def checkPos(objs, amt):
    x, y, z, point = objs
    if point == 0:
        return False
    
    checked = [[0, 0, 0], [0, 0, 0]]
    
    for i in range(3):
        check_pos1 = (x + lib.check[0][i][0], y + lib.check[0][i][1], z + lib.check[0][i][2])
        check_pos2 = (x + lib.check[1][i][0], y + lib.check[1][i][1], z + lib.check[1][i][2])

        if any(obj[:3] == check_pos1 for obj in lib.obj):
            checked[0][i] = 1
        if any(obj[:3] == check_pos2 for obj in lib.obj):
            checked[1][i] = 1

    if checked[0] == [1, 1, 1] or checked[1] == [1, 1, 1]:
        return False
    return True

def createWorld():
    lib.obj = []

    for y in range(10):
        for x in range(10):
            for z in range(10):
                if y < 2:
                    rand = random.randint(0,20)
                if 2 < y < 4:
                    rand = random.randint(0,14)
                if y > 4:
                    rand = random.randint(0,11)
                
                if rand > 10:
                    lib.obj.append([x,y,z, random.randint(0,2)])
                

def blockType(idx):
    if idx == 1:
        return 0, 0
    if idx == 2:
        return 28, 0