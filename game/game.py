from gameBase import GameBase
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

        self.explosion = Animation(asset_path="../asset/units.png", tile_size=(64, 64), frame_row=6, frame_start=0
                                   , frame_end=7, duration=0)
        self.explosion.rotate_frame(30)
        self.agent = Unit((3, 3))
        self.agentLayer = AgentLayer(asset_path="../asset/units.png", tile_size=(64, 64), agent=self.agent,
                                     tank_sprite_pos=Vector2(1, 0), weapon_sprite_pos=Vector2(0, 6),
                                     explosion=self.explosion)
        #
        # self.bg_layer = ArrayLayer(asset_path="asset/ground.png", tile_size=(64, 64), rect_position=ground)
        # self.wall_layer = ArrayLayer(asset_path="asset/walls.png", tile_size=(64, 64), rect_position=walls)
        # self.bullet_layer = BulletLayer(asset_path="asset/explosions.png", tile_size=(64, 64),
        #                                 current_position=(3, 3), texture_position=(2, 1))

        self.user_interface = UserInterface()

    def processInput(self):
        target_position = Vector2(pygame.mouse.get_pos())
        self.user_interface.update_agle(target_position)
        # res = target_position - self.tank.get_screen_position()
        # self.angle = math.atan2(-res.x, -res.y) * 180 / math.pi
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                self.__running = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("按了")
                    self.user_interface.agent_fire = True
            #     if event.key == pygame.K_a:
            #         self.user_move.x -= self.step_displacement
            #     elif event.key == pygame.K_d:
            #         self.user_move.x += self.step_displacement
            #         pass
            #     elif event.key == pygame.K_s:
            #         self.user_move.y += self.step_displacement
            #     elif event.key == pygame.K_w:
            #         self.user_move.y -= self.step_displacement

    def update(self):
        # self.tank.update(self.user_move, self.angle, agent.DIRECTION.DOWN)
        # self.user_move = Vector2((0, 0))
        self.agent.update(self.user_interface.user_target, self.user_interface.user_movement,
                          DIRECTION.DOWN,self.user_interface.agent_fire)
        pass

    def render(self):
        # self.bg_layer.render_array(self.screen)
        # self.wall_layer.render_array(self.screen)
        # self.unit_layer.render(self.screen, self.tank.position, self.tank.angle)
        # self.bullet_layer.render(self.screen, (3, 3))
        self.tmx.render(self._screen)
        self.agentLayer.render(self._screen,self.user_interface.agent_fire)
        # self.explosion.reset()

        pygame.display.update()
        self._clock.tick(self._fps)

    def run(self):
        while self._running:
            self.processInput()
            self.update()
            self.render()

    def close(self):
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
    game.close()
