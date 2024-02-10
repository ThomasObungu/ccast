import pygame

class Map:
    def __init__(self, tile_size_x : int, tile_size_y : int, map_resolution : tuple) -> None:
        self.tile_size_x = tile_size_x
        self.tile_size_y = tile_size_y
        self.map_resolution = map_resolution

    def initalize_array(self) -> list:
        array = [ [] for i in range(self.map_resolution[0])]
        for i in range(len(array)):
           array[i] = [ 0 for i in range(self.map_resolution[1])]
        return array
    
