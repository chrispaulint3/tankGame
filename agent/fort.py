from agent.agentBase import Agent
from pygame import Vector2
from math import atan2
from math import pi


class Fort(Agent):
    def __init__(self, agent_position):
        super().__init__(agent_position)
        self.target_position = 0
        self.on_fire = False

    def update(self, user_target: Vector2, user_movement: Vector2,on_fire:bool):
        self.target_position = user_target
        self.agent_position += user_movement
        self.on_fire = on_fire

    def _get_rotate_angle(self, user_target):
        diff = user_target - self.agent_position.elementwise()*(64,64)
        self.angle = atan2(-diff.x, -diff.y) * 180 / pi
