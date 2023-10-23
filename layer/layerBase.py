from abc import ABC, abstractmethod
from pygame.image import load


class Layer(ABC):
    def __init__(self, asset_path: str,tile_size):
        self.texture = load(asset_path)
        self.tile_size = tile_size






