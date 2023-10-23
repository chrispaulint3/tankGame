from pygame import Vector2
from pygame import Rect
from layer.layerBase import Layer


class Explosion(Layer):
    def __init__(self, asset_path, tile_size, frame_row, frame_start, frame_end):
        """
        :param asset_path: image path to get the surface
        :param frame_position: the frame texture start rect position
        """
        super().__init__(asset_path, tile_size)
        self.frame_start = frame_start
        self.frame_end = frame_end
        self.frame_row = frame_row
        self.frames = self.extract_texture()
        self.current_frame = 0

    def extract_texture(self):
        frame_surface = []
        frame_point = Vector2(self.frame_start, self.frame_row)
        for i in range(self.frame_start, self.frame_end + 1):
            frame_position = frame_point.elementwise() * self.tile_size
            frame_rect = Rect(frame_position, self.tile_size)
            frame_surface.append(self.texture.subsurface(frame_rect))
            frame_point.x += 1
        return frame_surface

    def render(self,surface,sprite_position):
        sprite_position = Vector2(sprite_position).elementwise()*self.tile_size
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        surface.blit(self.frames[self.current_frame], sprite_position)
        self.current_frame += 1




