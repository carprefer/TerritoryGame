import pygame
from utils import *
from ClickableSprite import ClickableSprite


class Cell(ClickableSprite):
    def __init__(self, posX, posY):
        images = [
            pygame.image.load('../resources/images/in_game/cell_1(64).png').convert_alpha(),
            pygame.image.load('../resources/images/in_game/cell_2(64).png').convert_alpha(),
            pygame.image.load('../resources/images/in_game/cell_3(64).png').convert_alpha(),
        ]
        super().__init__(posX, posY, images)

        self.font = pygame.font.SysFont(None, 24)
        
        
        self.value = 0      # 0: neutral / +: player / -: enemy

        self.clickable = False
        self.clickMode = False


    def draw(self, window):
        if self.clickMode:
            if self.clickable:
                self.images[self.imageIdx].set_alpha(255)
            else:
                self.images[self.imageIdx].set_alpha(128)
        else:
            self.images[self.imageIdx].set_alpha(255)

        super().draw(window)
        valueText = self.font.render(str(abs(self.value)), True, 'black')
        window.blit(valueText, self.rect.move(48, 48))


    def change_value(self, diff):
        old = self.value
        new = self.value + diff
        if new > 0 and old <= 0:
            self.imageIdx = PLAYER
        elif new == 0 and old != 0:
            self.imageIdx = NEUTRAL
        elif new < 0 and old >= 0:
            self.imageIdx = ENEMY

        self.value = new



