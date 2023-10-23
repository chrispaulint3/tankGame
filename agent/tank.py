from agent.agentBase import Agent
from pygame import Vector2
from const import DIRECTION


class Tank(Agent):
    def __init__(self, agent_position: Vector2):
        super().__init__(agent_position)
        self.direction = DIRECTION.DOWN

    def update(self, user_movement: Vector2, direction: DIRECTION):
        self.agent_position += user_movement
        self.direction = direction
