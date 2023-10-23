from pygame import Vector2
from math import atan2
from math import pi


class UserInterface:
    def __init__(self):
        self.user_target = 0
        self.user_movement = Vector2((0, 0))
        self.agent_fire = []

    def update_agle(self, target_position: Vector2):
        # diff = target_position-agent_position
        # self.user_angle = atan2(-diff.x, -diff.y) * 180 / diff.pi
        self.user_target = target_position

    def update_move(self, movement: Vector2):
        self.user_movement = movement
        pass

    def update_fire_command(self,command:bool):
        self.agent_fire.append(command)

    def get_fire_command(self):
        if not self.agent_fire:
            return False



