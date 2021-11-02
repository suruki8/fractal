import pygame
from pygame.constants import QUIT

pygame.init()
w, h  = 1000, 1000

def compute_color(c, thrash = 4., max_iter = 50):
    z = 0 + 0j
    #z = c
    i = 0
    while (abs(z) < thrash) and (i < max_iter):
        z = z * z + c
        #z = z * z - 1
        i += 1
    if i < 50:
        return ( 255 - 5 * i, 255 - 5 * i,0)
    return (0, 0, 0)

def convert(x, y):
    return complex(
        ((x - w // 2) / w) * 3,
        ((y - h // 2) / h) * 3
    )


ui = pygame.display.set_mode((w, h))
running = True
pxarray = pygame.PixelArray(ui)
for i in range(w):
    for j in range(h):
        c = convert(i, j)
        pxarray[i, j] = compute_color(c)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False 
    pygame.display.flip()