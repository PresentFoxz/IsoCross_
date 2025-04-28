import pygame
import pygame.freetype
import keyboard
import math
import library as lib
import render as rend
import player as plr

pygame.init()
screen = pygame.display.set_mode((lib.screenW * lib.mult, lib.screenH * lib.mult))
pygame.display.set_caption("IsoCross")
clock = pygame.time.Clock()

debug = True

def movement():
    move_delta = 0.2

    if keyboard.is_pressed('left'):
        lib.Cam[0] -= move_delta
        lib.Cam[2] += move_delta
    if keyboard.is_pressed('right'):
        lib.Cam[0] += move_delta
        lib.Cam[2] -= move_delta
    if keyboard.is_pressed('up'):
        lib.Cam[0] -= move_delta
        lib.Cam[2] -= move_delta
    if keyboard.is_pressed('down'):
        lib.Cam[0] += move_delta
        lib.Cam[2] += move_delta
    
    if keyboard.is_pressed('e'):
        lib.Cam[1] -= move_delta
    if keyboard.is_pressed('q'):
        lib.Cam[1] += move_delta

#rend.createWorld()

running = True
while running:
    print("Start")
    screen.fill((255, 0, 0))
    lib.obj = [o for o in lib.obj if o[3] >= 0]
    lib.obj.append(lib.Pos)
    movement()
    plr.playerMove(keyboard)
    lib.obj.sort(key=lambda o: o[0] + o[1] + o[2], reverse=False)
    i = 0
    rendering = 0
    for objs in lib.obj:
        if objs[3] != -1:
            if lib.Cam[1] - 4 < objs[1] < lib.Cam[1] + 4:
                x, y = rend.convert3D_2D(objs)
                x *= lib.mult
                y *= lib.mult
                
                if (((-lib.size * lib.mult) < x < ((lib.screenW * lib.mult) + lib.size)) and ((-lib.size * lib.mult) < y < ((lib.screenH * lib.mult) + lib.size))):
                    if rend.checkPos(objs):
                        xPixel, yPixel = rend.blockType(objs[3])
                        tile_rect = pygame.Rect(xPixel, yPixel, lib.size, lib.size)
                        tile_sprite = lib.block.subsurface(tile_rect)
                        scaled_tile = pygame.transform.scale(tile_sprite, (lib.size * lib.mult, lib.size * lib.mult))
                        screen.blit(scaled_tile, (x, y))

                        #rendering += 1
        else:
            for i in range(3):
                plr.collision(i, screen, pygame)
            plr.playerRend(screen, pygame)
        #i += 1
    
    #print("Amt Rendered: ", rendering)

    if debug:
        ySize = 20
        if lib.mult != 1:
            ySize = 12
        CamText = f"Cam Pos: ( X: {int(lib.Cam[0])}, Y: {int(lib.Cam[1])}, Z: {int(lib.Cam[2])} )"
        posText = f"Plr Pos: ( X: {int(lib.Pos[0])}, Y: {int(lib.Pos[1])}, Z: {int(lib.Pos[2])} )"
        lib.text_to_screen(CamText, (255,255,255), 5, 5, screen)
        lib.text_to_screen(posText, (255,255,255), 5, ySize * lib.mult, screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(30)

    print("Finish")

pygame.quit()
