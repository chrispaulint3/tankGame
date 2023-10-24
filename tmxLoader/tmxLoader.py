import pytmx
from pytmx import load_pygame
from pygame import Surface
from pygame.display import flip


class Tmx:
    def __init__(self, tmx_path):
        self.map = load_pygame(tmx_path)
        self.tile_cache = []
        self.object_cache = []
        self.get_tile()

    def render(self, surface: Surface):
        # for layer in self.map.visible_layers:
        #     if isinstance(layer,pytmx.TiledTileLayer):
        #         for x, y, gid in layer:
        #             if gid:
        #                 tile = self.map.get_tile_image_by_gid(gid)
        #                 surface.blit(tile, (x * self.map.tilewidth, y * self.map.tilewidth))
        #     elif isinstance(layer,pytmx.TiledObjectGroup):
        #         print(f"Object Layer: {layer.name}")
        #         for obj in layer:
        #             # obj 是一个 TiledObject，你可以获取其属性如 obj.x, obj.y, obj.name 等
        #             print(obj)
        #             pass

    def get_tile(self):
        for layer in self.map.visible_layers:
            if isinstance(layer,pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    if gid:
                        tile = self.map.get_tile_image_by_gid(gid)
                        self.tile_cache.append(tile)
            elif isinstance(layer,pytmx.TiledObjectGroup):
                for obj in layer:
                    # obj 是一个 TiledObject，你可以获取其属性如 obj.x, obj.y, obj.name 等
                    self.object_cache.append(obj)
                    pass

