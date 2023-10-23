from layer.layerBase import Layer
from pygame.rect import Rect
from pygame.math import Vector2


class ArrayLayer(Layer):
    def __init__(self, asset_path, tile_size, rect_position: list[Vector2]):
        super().__init__(asset_path, tile_size)
        self.rect_position = rect_position
        self.height = len(self.rect_position)
        self.width = len(self.rect_position[0])

    def render_array(self, surface):
        for i in range(self.height):
            for j in range(self.width):
                if not self.rect_position[i][j] is None:
                    texture_point = self.rect_position[i][j].elementwise() * self.tile_size
                    rect = Rect(texture_point, self.tile_size)
                    sprite_point = Vector2((j, i)).elementwise() * self.tile_size
                    surface.blit(self.texture, sprite_point, rect)
