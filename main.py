import pygame
import sys
import math

SCREEN_RESOLUTION = (720,480)
CIRLCE_RADIUS = 8
MAP_TILE_SIZE_X = 2
MAP_TILE_SIZE_Y = 2

from map import * 
from render import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_RESOLUTION[0],SCREEN_RESOLUTION[1]))

    angle = math.pi
    
    map = Map(MAP_TILE_SIZE_X,MAP_TILE_SIZE_Y,SCREEN_RESOLUTION)
    circle = Circle(CIRLCE_RADIUS,(SCREEN_RESOLUTION[0]/2,SCREEN_RESOLUTION[1]/2),angle)

    render_type="cosine"
    
    map_array = map.initalize_array()
    
    while True:
        pygame.draw.rect(screen,(0,0,0),(0,0,SCREEN_RESOLUTION[0],SCREEN_RESOLUTION[1]))
        circle.draw(screen,map_array,render_type)
        circle.draw_raypoint(screen)
        circle.user_input()
        circle.cast_rays(screen,map_array,render_type)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit(0)

        pygame.display.update() 
        clock.tick(60)

        pygame.display.set_caption(str(clock)[7:15])
        
if __name__ == "__main__":
    main()