from layer.layerBase import Layer
from pygame import Vector2
from pygame import Rect


class BulletLayer(Layer):
    def __init__(self, asset_path, tile_size, current_position, texture_position):
        super().__init__(asset_path, tile_size)
        self.sprite_position = Vector2(current_position)
        self.texture_position = Vector2(texture_position)

    def extract_texture(self):
        texture_position = self.texture_position.elementwise() * self.tile_size
        rect = Rect(texture_position, self.tile_size)
        return self.texture.subsurface(rect)

    def render(self,surface,sprite_position):
        bullet_surface = self.extract_texture()
        surface.blit(bullet_surface,sprite_position)

