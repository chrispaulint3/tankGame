from pytmx import load_pygame
from pygame import Surface
from pygame.display import flip


class Tmx:
    def __init__(self, tmx_path):
        self.map = load_pygame(tmx_path)

    def render(self, surface: Surface):
        for layer in self.map.visible_layers:
            for x, y, gid in layer:
                if gid:
                    tile = self.map.get_tile_image_by_gid(gid)
                    surface.blit(tile, (x * self.map.tilewidth, y * self.map.tilewidth))
