import pygame

Cam = [0,2,0]
Pos = [0,2,0,-1]
nextPos = [0,0,0]
lastPos = [0,0,0]
obj = [
    [0,0,0,1]
] # x, y, z, type

width = 14
height = 14
size = 28
check = [
    [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ],
    [
        [1,1,0],
        [0,1,0],
        [0,1,1]
    ]
]

collisionCheck = [
    # Bottom
    [1,0,0],
    [0,1,0],
    [0,0,1]
]
mult = 4
screenW = 128
screenH = 128

block = pygame.image.load("images/blocks.png")
playerSprt = pygame.image.load("images/playerSprt.png")

pygame.font.init()
txtFont = pygame.font.SysFont('Arial', 10*mult)

def text_to_screen(text, color, x, y, screen):
    img = txtFont.render(text, True, color)
    screen.blit(img, (x,y))