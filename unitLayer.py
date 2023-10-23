import pygame
from pygame.math import Vector2
from layer.layerBase import Layer


class UnitLayer(Layer):
    def __init__(self, asset_path, base_position, tower_position, tile_size):
        super().__init__(asset_path, tile_size)
        self.base_position = base_position
        self.tower_position = tower_position

    def render(self, surface, sprite_position, angle):
        self.__render_tank_body(surface, sprite_position)
        self.__render_weapon(surface, sprite_position, angle)

    def __render_weapon(self, surface, sprite_position, angle):
        # 绘制坦克炮
        texture_point = Vector2(self.tower_position).elementwise() * self.tile_size
        rect = pygame.rect.Rect(texture_point, self.tile_size)

        fort_surface = self.texture.subsurface(rect)
        rotated_fort_surface = pygame.transform.rotate(fort_surface, angle)
        x_shift = rotated_fort_surface.get_width() // 2 - fort_surface.get_width() // 2
        y_shift = rotated_fort_surface.get_height() // 2 - fort_surface.get_height() // 2

        sprite_position = Vector2((sprite_position)).elementwise() * self.tile_size
        sprite_position = sprite_position - Vector2((x_shift, y_shift))
        surface.blit(rotated_fort_surface, sprite_position)

    def __render_tank_body(self, surface, sprite_position):
        # 绘制坦克基座
        texture_point = Vector2(self.base_position).elementwise() * self.tile_size
        rect = pygame.rect.Rect(texture_point, self.tile_size)
        sprite_position = Vector2(sprite_position).elementwise() * self.tile_size
        surface.blit(self.texture, sprite_position, rect)
