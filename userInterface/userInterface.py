from pygame import Vector2
from collections import deque
from const import DIRECTION


class UserInterface:
    def __init__(self):
        self.__user_target = 0
        self.__user_move = Vector2((0, 0))
        self.__direction = DIRECTION.DOWN
        self.__on_fire = deque()

    def update_user_target(self, target_position: Vector2):
        self.__user_target = target_position

    def update_user_move(self, move: Vector2):
        self.__user_move = move

    def update_on_fire(self, on_fire: bool):
        self.__on_fire.append(on_fire)

    @property
    def user_target(self):
        return self.__user_target

    @property
    def user_move(self):
        return self.__user_move

    @property
    def user_direction(self):
        return self.__direction

    @property
    def on_fire(self):
        return self.__on_fire

    # def get_fire_command(self):
    #     if not self.agent_fire:
    #         return False
    #     else:
    #         return self.agent_fire.popleft()
