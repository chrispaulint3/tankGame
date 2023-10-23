from pygame import Vector2
from enum import Enum









class Bullet:
    def __init__(self,start_position,current_position,bullet_range=100,angle=0,v=0.1):
        self.start_position=start_position
        self.current_position = current_position
        self.bullet_range = bullet_range
        self.angle = angle
        self.v = v

    def update(self,current_position):
        self.current_position = current_position



