import library as lib
import render as rend

move_delta = 0.2
def playerMove(keyboard):

    lib.lastPos[0] = lib.Pos[0]
    lib.lastPos[1] = lib.Pos[1]
    lib.lastPos[2] = lib.Pos[2]
    
    lib.nextPos[0] = lib.Pos[0]
    lib.nextPos[1] = lib.Pos[1]
    lib.nextPos[2] = lib.Pos[2]

    if keyboard.is_pressed('a'):
        lib.nextPos[0] -= move_delta
        lib.nextPos[2] += move_delta
    if keyboard.is_pressed('d'):
        lib.nextPos[0] += move_delta
        lib.nextPos[2] -= move_delta
    if keyboard.is_pressed('w'):
        lib.nextPos[0] -= move_delta
        lib.nextPos[2] -= move_delta
    if keyboard.is_pressed('s'):
        lib.nextPos[0] += move_delta
        lib.nextPos[2] += move_delta

    if keyboard.is_pressed('c'):
        lib.nextPos[1] -= move_delta
    if keyboard.is_pressed('z'):
        lib.nextPos[1] += move_delta

def aabb_corner_collision(pos1, pos2, size=28, plrsize=24):
    min1 = [pos1[0], pos1[1], pos1[2]]
    max1 = [pos1[0] + plrsize, pos1[1] + plrsize, pos1[2] + plrsize]
    
    min2 = [pos2[0], pos2[1], pos2[2]]
    max2 = [pos2[0] + size, pos2[1] + size, pos2[2] + size]
    
    print(f"Min1: {min1} Max1: {max1} | Min2: {min2} Max2: {max2}")
    print(f"Player Pos: {lib.Pos}, Object Pos: {lib.obj[0]}")
    
    for i in range(3):
        if max1[i] <= min2[i] or min1[i] >= max2[i]:
            return False 
    return True

def collision(z, screen, pygame):
    for checks in lib.collisionCheck:
        check_pos = [lib.Pos[0] + checks[0], lib.Pos[1] + checks[1], lib.Pos[2] + checks[2]]
        for i in range(len(check_pos)):
            check_pos[i] = int(check_pos[i])
        if any(obj[:3] == check_pos for obj in lib.obj):
            if aabb_corner_collision(lib.Pos, check_pos, size=28):
                lib.Pos[z] = lib.lastPos[z]
                rend.outline(check_pos, screen, pygame)
                break
        else:
            lib.Pos[z] = lib.nextPos[z]

def playerRend(screen, pygame):
    xPos, yPos = rend.convert3D_2D(lib.Pos)

    xPos *= lib.mult
    yPos *= lib.mult

    xPos = int(xPos)
    yPos = int(yPos)

    #scaled_tile = pygame.transform.scale(lib.playerSprt, (28 * lib.mult, 56 * lib.mult))
    #screen.blit(scaled_tile, (xPos - (14 * lib.mult), yPos - (50 * lib.mult)))
    pygame.draw.rect(screen, (0, 255, 0), (xPos, yPos, 10, 10))
