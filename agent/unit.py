from agent.fort import Fort
from agent.tank import Tank
from pygame import Vector2
from const import DIRECTION


class Unit:
    def __init__(self, unit_position: Vector2):
        self.tank = Tank(unit_position)
        self.fort = Fort(unit_position)

    def update(self, user_target: Vector2, user_movement: Vector2, direction: DIRECTION,on_fire):
        self.tank.update(user_movement, direction)
        self.fort.update(user_target, user_movement,on_fire)
