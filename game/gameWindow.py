from game.gameBase import GameBase
from agent.unit import Unit
from layer.agentLayer import AgentLayer
from animation.animation import Animation
from userInterface.userInterface import UserInterface
import pygame
from pygame import Vector2
from const import DIRECTION
from tmxLoader.tmxLoader import Tmx


class Game(GameBase):
    def __init__(self):
        super().__init__()

        self.tmx = Tmx("../asset/test.tmx")

        self.user_interface = UserInterface()

        self.explosion = Animation(asset_path="../asset/units.png", tile_size=(64, 64), frame_row=6, frame_start=0
                                   , frame_end=7, duration=2)
        self.explosion.rotate_frame(30)
        self.agent = Unit((100, 100), self.user_interface)
        self.agentLayer = AgentLayer(asset_path="../asset/units.png", tile_size=(64, 64), agent=self.agent,
                                     tank_sprite_pos=Vector2(1, 0), weapon_sprite_pos=Vector2(0, 6),
                                     explosion=self.explosion)

        self.step_displacement = 1
        #
        # self.bg_layer = ArrayLayer(asset_path="asset/ground.png", tile_size=(64, 64), rect_position=ground)
        # self.wall_layer = ArrayLayer(asset_path="asset/walls.png", tile_size=(64, 64), rect_position=walls)
        # self.bullet_layer = BulletLayer(asset_path="asset/explosions.png", tile_size=(64, 64),
        #                                 current_position=(3, 3), texture_position=(2, 1))

    def processInput(self):
        target = Vector2(pygame.mouse.get_pos())
        user_move = Vector2((0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                self.set_running_flag(False)
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    agent_fire = True
                    self.user_interface.update_on_fire(agent_fire)
                elif event.key == pygame.K_a:
                    user_move.x -= self.step_displacement
                elif event.key == pygame.K_d:
                    user_move.x += self.step_displacement
                elif event.key == pygame.K_s:
                    user_move.y += self.step_displacement
                elif event.key == pygame.K_w:
                    user_move.y -= self.step_displacement
            self.user_interface.update_user_move(user_move)
            self.user_interface.update_user_target(target)

    def update(self):
        self.agent.update()
        pass

    def render(self):
        self.tmx.render(self._screen)
        self.agentLayer.render(self._screen)

        pygame.display.update()
        self._clock.tick(self._fps)

    def run(self):
        while self._running:
            self.processInput()
            self.update()
            self.render()
            print(self.agent.fort.on_fire)

    def close(self):
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
    game.close()
