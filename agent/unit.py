from agent.fort import Fort
from agent.tank import Tank
from userInterface.userInterface import UserInterface
from pygame import Vector2
from const import DIRECTION


class Unit:
    def __init__(self, unit_position: Vector2,user_interface:UserInterface):
        self.tank = Tank(unit_position)
        self.fort = Fort(unit_position)
        self.user_interface = user_interface

    def update(self):
        self.tank.update(self.user_interface.user_move,self.user_interface.user_direction)
        self.fort.update(self.user_interface.user_target,self.user_interface.user_move,self.user_interface.on_fire)
