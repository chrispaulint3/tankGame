import math

import agent
from layer.layerBase import GameBase
from unitLayer import UnitLayer
from arrayLayer import ArrayLayer
import pygame
from const import ground
from const import walls
from pygame import Vector2
from agent.tank import Tank
from bulletLayer import BulletLayer
from



class Game(GameBase):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("tankGame")
        self.screen = pygame.display.set_mode((1024, 640))
        self.__running = True

        self.tank = Tank((3,3))
        self.unit_layer = UnitLayer(asset_path="asset/units.png",base_position=(1,0),tower_position=(0,6),
                                    tile_size=(64,64))

        self.bg_layer = ArrayLayer(asset_path="asset/ground.png",tile_size=(64,64),rect_position=ground)
        self.wall_layer = ArrayLayer(asset_path="asset/walls.png",tile_size=(64,64),rect_position=walls)
        self.bullet_layer = BulletLayer(asset_path="asset/explosions.png",tile_size=(64,64),
                                        current_position=(3,3),texture_position=(2,1))

        self.explosion = Explosion(asset_path="asset/explosions.png",tile_size=(64,64),frame_row=4,frame_start=0
                                   ,frame_end=27)

        self.user_angle = 0
        self.user_move = Vector2((0,0))
        self.step_displacement = 0.1

        self.clock = pygame.time.Clock()

    def processInput(self):
        mouse_position = pygame.mouse.get_pos()
        target_position = pygame.Vector2(mouse_position)
        res = target_position-self.tank.get_screen_position()
        self.angle = math.atan2(-res.x,-res.y)*180/math.pi
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                self.__running = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.user_move.x -= self.step_displacement
                elif event.key == pygame.K_d:
                    self.user_move.x += self.step_displacement
                    pass
                elif event.key == pygame.K_s:
                    self.user_move.y += self.step_displacement
                elif event.key == pygame.K_w:
                    self.user_move.y -= self.step_displacement


    def update(self):
        self.tank.update(self.user_move, self.angle,agent.DIRECTION.DOWN)
        self.user_move = Vector2((0,0))
        pass

    def render(self):
        self.bg_layer.render_array(self.screen)
        # self.wall_layer.render_array(self.screen)
        self.unit_layer.render(self.screen,self.tank.position,self.tank.angle)
        self.bullet_layer.render(self.screen,(3,3))
        self.explosion.render(self.screen,(1,1))

        pygame.display.update()
        self.clock.tick(60)
        pass

    def run(self):
        while self.__running:
            self.processInput()
            self.update()
            self.render()

    def close(self):
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
    game.close()

