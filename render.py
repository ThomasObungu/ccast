import pygame
import math
import time

from map import *
from main import SCREEN_RESOLUTION

RAYS_CASTED = 480
RAY_DEPTH = 480
FOV = math.pi/3
MAP_SCALE = SCREEN_RESOLUTION[0] / RAYS_CASTED

class Circle(Map):
    def __init__(self, radius : float, centre : tuple, angle : float) -> None:
        super().__init__(tile_size_x=2,tile_size_y=2,map_resolution=SCREEN_RESOLUTION)  
        self.radius = radius 
        self.centre = centre
        self.angle = angle
        self.raypoint_x = self.centre[0]
        self.raypoint_y = self.centre[1]
   
      
    def define_circle(self,array : list, function_type):
        angle = self.angle
        for ray in range(RAYS_CASTED):
            ray_x = self.centre[0] + math.cos(angle) * self.radius**2
            ray_y = self.centre[1] + math.sin(angle) * self.radius**2
            
            row = int(ray_y / self.tile_size_y)
            column = int(ray_x / self.tile_size_x)

            array[row][column] = 1 

            angle+= 1
    
    def define_function(self,array : list, function_type):
            for ray in range(RAYS_CASTED):
                ray_x = ray
                ray_y = 0
                if function_type == "sine": ray_y = math.sin(math.radians(ray_x)*4)*180
                elif function_type == "cosine": ray_y = math.cos(math.radians(ray_x)*4)*180

                row = 90+int(ray_y / self.tile_size_y)
                column = int(ray_x)

                array[row][column] = 1 
    
    def draw_types(self, render_type : str):
        types = {
            "circle" : [(100,255,50), self.define_circle],
            "sine" : [(255,0,0),self.define_function],
            "cosine" : [(0,255,0),self.define_function],
        }
        return types[render_type]
        #types[render_type][1](array,render_type)


    def draw(self,surface,array : list, render_type : str):
        type = self.draw_types(render_type)
        type[1](array,render_type) 
        for row in range(len(array)):
            for column in range(len(array[row])):
                if array[row][column] == 1:
                    pygame.draw.rect(surface, type[0],
                                    (column * self.tile_size_x, row * self.tile_size_y, 
                                    self.tile_size_x, self.tile_size_y ))
        
                 
        
    def draw_raypoint(self, surface):
        pygame.draw.circle(surface, (0,150,250), (self.raypoint_x,self.raypoint_y), 8)
                    
    def user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: self.angle += 0.05
        if keys[pygame.K_LEFT]: self.angle -= 0.05
        # if keys[pygame.K_UP]: 
        #     self.raypoint_x += math.cos(self.angle)
        #     self.raypoint_y += math.sin(self.angle)
        # if keys[pygame.K_DOWN]:
        #     self.raypoint_x -= math.cos(self.angle)
        #     self.raypoint_y -= math.sin(self.angle)
        
   
    def cast_rays(self,surface,array,render_type):
        
        colour = self.draw_types(render_type)

        start_angle = (self.angle + FOV)

        for ray in range(RAYS_CASTED):
            for step in range(RAY_DEPTH):
                ray_x = self.raypoint_x + math.cos(start_angle) * step
                ray_y = self.raypoint_y + math.sin(start_angle) * step

                row = int(ray_y / self.tile_size_y)
                column = int(ray_x / self.tile_size_x)

                if array[row][column] == 1:
                    break
            
            pygame.draw.line(surface, (255,0,255), (self.centre[0], self.centre[1]), 
                                    (ray_x, ray_y))
        
            step *= math.cos(self.angle - start_angle)

            wall_height = 21000 / (step + 0.0001)

            # pygame.draw.rect(surface, colour[0], (0 + ray * MAP_SCALE, 
            #                     (SCREEN_RESOLUTION[1] / 2) - wall_height / 2, 
            #                     MAP_SCALE, wall_height ))
            
            start_angle += FOV / RAYS_CASTED
        

        
         



                




    
    
    

