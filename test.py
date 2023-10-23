import math

from pytmx import load_pygame, TiledMap
import pygame


pygame.init()
screen = pygame.display.set_mode((1024,640))
running = True

map = load_pygame("asset/test.tmx")


while running:
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    angle = math.atan2(y,x)
    print(angle)
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False




    # render here
    for layer in map.visible_layers:
        for x, y, gid in layer:
            if gid:
                tile = map.get_tile_image_by_gid(gid)
                screen.blit(tile, (x * map.tilewidth, y * map.tilewidth))

    pygame.display.update()


pygame.quit()

