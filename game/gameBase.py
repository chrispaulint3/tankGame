from abc import abstractmethod
from pygame import init
from pygame.display import set_mode
from pygame.display import set_caption
from pygame.time import Clock
from config.gameConfig import *


class GameBase:
    def __init__(self):
        init()
        set_caption(GAME_CAPTION)
        self._screen = set_mode(RESOLUTION)
        self._running = True
        self._clock = Clock()
        self._fps = FPS

    def set_running_flag(self,flag:bool):
        self._running = flag

    @abstractmethod
    def processInput(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def run(self):
        pass
