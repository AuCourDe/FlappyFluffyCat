import pygame as pg
from settings import *


class Score:
    def __init__(self, game):
        self.game = game
        self.font = pg.font.Font('assets/font/Doom.ttf', 150)
        self.font_pos = (WIDTH // 2, HEIGHT // 8)

    def draw(self):
        score = self.game.pipe_handler.passed_pipes
        self.text = self.font.render(f'{score}', True, 'pink')
        self.game.screen.blit(self.text, self.font_pos)


class Sound:
    def __init__(self):
        self.hit_sound = pg.mixer.Sound('assets/sound/hit.mp3')
        self.point_sound = pg.mixer.Sound('assets/sound/point.mp3')
        self.wing_sound = pg.mixer.Sound('assets/sound/wing.mp3')
        self.wing_sound.set_volume(0.5)
        self.music = pg.mixer.music.load('assets/sound/theme.mp3')
        pg.mixer.music.set_volume(0.7)
        pg.mixer.music.play(-1)


class Background:
    def __init__(self, game):
        self.game = game
        self.x = 0
        self.y = 0
        self.speed = SCROLL_SPEED - 2
        self.image = self.game.background_image

    def update(self):
        self.x = (self.x - self.speed) % -WIDTH

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))
        self.game.screen.blit(self.image, (WIDTH + self.x, self.y))


class Ground(Background):
    def __init__(self, game):
        super().__init__(game)
        self.y = GROUND_Y
        self.speed = SCROLL_SPEED
        self.image = self.game.ground_image