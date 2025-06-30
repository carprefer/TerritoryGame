import pygame

NEUTRAL = 0
PLAYER = 1
ENEMY = 2

class Cell(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.images = [
            pygame.image.load('../resources/images/cell_1(64).png').convert_alpha(),
            pygame.image.load('../resources/images/cell_2(64).png').convert_alpha(),
            pygame.image.load('../resources/images/cell_3(64).png').convert_alpha(),
        ]
        self.image = self.images[NEUTRAL]
        self.rect = self.image.get_rect(center = (posX, posY))


        self.value = 0      # 0: neutral / +: player / -: enemy


    def change_value(self, diff):
        old = self.value
        new = self.value + diff
        if new > 0 and old <= 0:
            self.image = self.images[PLAYER]
        elif new == 0 and old != 0:
            self.image = self.images[NEUTRAL]
        elif new < 0 and old >= 0:
            self.image = self.images[ENEMY]

        self.value += diff



