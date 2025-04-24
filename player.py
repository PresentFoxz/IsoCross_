import library as lib
import render as rend

move_delta = 0.2
lastPos = lib.Pos
def playerMove(keyboard):
    if keyboard.is_pressed('a'):
        lib.Pos[0] -= move_delta
        lib.Pos[2] += move_delta
    if keyboard.is_pressed('d'):
        lib.Pos[0] += move_delta
        lib.Pos[2] -= move_delta
    if keyboard.is_pressed('w'):
        lib.Pos[0] -= move_delta
        lib.Pos[2] -= move_delta
    if keyboard.is_pressed('s'):
        lib.Pos[0] += move_delta
        lib.Pos[2] += move_delta
    
    if keyboard.is_pressed('c'):
        lib.Pos[1] -= move_delta
    if keyboard.is_pressed('z'):
        lib.Pos[1] += move_delta
    
    collision(keyboard)
    
    lastPos[0] = lib.Pos[0]
    lastPos[1] = lib.Pos[1]
    lastPos[2] = lib.Pos[2]

def collision(keyboard):
    for checks in lib.collisionCheck:
        check_pos = [lib.Pos[0] + checks[0], lib.Pos[1] + checks[1], lib.Pos[2] + checks[2]]
        for i in range(len(check_pos)):
            check_pos[i] = int(check_pos[i])
        #print(check_pos)
        if any(obj[:3] == check_pos for obj in lib.obj):
            print("hit")
            if keyboard.is_pressed('d'):
                lib.Pos[0] -= move_delta
                lib.Pos[2] += move_delta
            if keyboard.is_pressed('a'):
                lib.Pos[0] += move_delta
                lib.Pos[2] -= move_delta
            if keyboard.is_pressed('s'):
                lib.Pos[0] -= move_delta
                lib.Pos[2] -= move_delta
            if keyboard.is_pressed('w'):
                lib.Pos[0] += move_delta
                lib.Pos[2] += move_delta
            
            if keyboard.is_pressed('z'):
                lib.Pos[1] -= move_delta
            if keyboard.is_pressed('c'):
                lib.Pos[1] += move_delta
            

def playerRend(screen, pygame):
    xPos, yPos = rend.convert3D_2D(lib.Pos)

    xPos *= lib.mult
    yPos *= lib.mult

    xPos = int(xPos)
    yPos = int(yPos)

    scaled_tile = pygame.transform.scale(lib.playerSprt, (28 * lib.mult, 56 * lib.mult))
    screen.blit(scaled_tile, (xPos - (14 * lib.mult), yPos - (56 * lib.mult)))
    pygame.draw.rect(screen, (0, 255, 0), (xPos, yPos, 2, 2))
