from pygame import Vector2
from pygame import Rect
from pygame import Surface
from pygame.display import flip
from layer.layerBase import Layer
from pygame.transform import rotate
from collections import deque


class Animation(Layer):
    def __init__(self, asset_path: str, tile_size: tuple,
                 frame_row: int, frame_start: int, frame_end: int, duration):
        """
        :param asset_path: image path to get the surface
        :param frame_position: the frame texture start rect position
        """
        super().__init__(asset_path, tile_size)
        self.frame_start = frame_start
        self.frame_end = frame_end
        self.frame_row = frame_row
        self.duration = duration
        self.frame_elapse = 0
        self.frames = self.extract_surface()
        self.rotated_frames = []
        self.current_frame = 0
        self.animation_complete = False
        self.angle = 0
        self.task_queue = None

    def extract_surface(self):
        frame_surface = []
        frame_point = Vector2(self.frame_start, self.frame_row)
        for i in range(self.frame_start, self.frame_end + 1):
            frame_position = frame_point.elementwise() * self.tile_size
            frame_rect = Rect(frame_position, self.tile_size)
            frame_surface.append(self.texture.subsurface(frame_rect))
            frame_point.x += 1
        return frame_surface

    def render(self, surface: Surface, sprite_position: Vector2, angle: float,task_queue:deque):
        if not task_queue:
            return
        elif self.frame_elapse < self.duration:
            self.frame_elapse += 1
            return

        elif self.current_frame >= len(self.frames):
            task_queue.popleft()
            self.current_frame = 0
            return

        frames = self.rotate_frame(angle)

        surface.blit(frames[self.current_frame], sprite_position)
        print("播放了")
        self.current_frame += 1
        self.frame_elapse = 0

    def rotate_frame(self, angle: float):
        if self.angle == angle and self.rotated_frames:
            return self.rotated_frames

        self.rotated_frames.clear()
        for frame in self.frames:
            self.angle = angle
            self.rotated_frames.append(rotate(frame, angle))
        return self.rotated_frames

    def reset(self):
        # self.animation_complete = True
        pass
