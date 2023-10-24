from agent.unit import Unit
from layer.layerBase import Layer
from pygame import Vector2
from pygame.rect import Rect
from pygame import transform
from pygame import Surface
from pygame.display import flip
from math import atan2
from math import pi
from animation.animation import Animation


class AgentLayer(Layer):
    def __init__(self, asset_path, tile_size, agent: Unit, weapon_sprite_pos, tank_sprite_pos, explosion: Animation):
        super(AgentLayer, self).__init__(asset_path, tile_size)
        self.agent = agent
        self.weapon_sprite_pos = weapon_sprite_pos
        self.tank_sprite_pos = tank_sprite_pos
        self.explosion = explosion
        pass

    def render(self, surface: Surface):
        self.__render_tank_body(surface, self.agent.tank.agent_position)
        self.__render_rotation(surface, self.agent.fort.agent_position)

    def __render_rotation(self, surface: Surface, sprite_position: Vector2):
        # 绘制坦克炮
        texture_point = self.weapon_sprite_pos.elementwise() * self.tile_size
        rect = Rect(texture_point, self.tile_size)

        # 计算旋转角度
        angle = self.get_rotation()
        fort_surface = self.texture.subsurface(rect)
        rotated_fort_surface = transform.rotate(fort_surface, angle)
        x_shift = rotated_fort_surface.get_width() // 2 - fort_surface.get_width() // 2
        y_shift = rotated_fort_surface.get_height() // 2 - fort_surface.get_height() // 2

        sprite_position = sprite_position - Vector2((x_shift, y_shift))
        surface.blit(rotated_fort_surface, sprite_position)

        self.explosion.render(surface, sprite_position, angle,self.agent.fort.on_fire)

    def __render_tank_body(self, surface, sprite_position):
        # 绘制坦克基座
        texture_point = self.tank_sprite_pos.elementwise() * self.tile_size
        rect = Rect(texture_point, self.tile_size)
        sprite_position = sprite_position
        surface.blit(self.texture, sprite_position, rect)

    def get_rotation(self):
        diff = self.agent.fort.target_position - self.agent.fort.agent_position
        return atan2(-diff.x, -diff.y) * 180 / pi
