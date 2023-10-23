from pygame import Vector2
from collections import deque


class UserInterface:
    def __init__(self):
        self._user_target = 0
        self._user_movement = Vector2((0, 0))
        self._agent_fire = deque([])

    def update(self, target_position: Vector2, movement: Vector2, on_fire: bool):
        self._user_target = target_position
        self._user_movement = movement
        self._agent_fire.append(on_fire)

    def get_fire_command(self):
        if not self.agent_fire:
            return False
        else:
            return self.agent_fire.popleft()
