import pygame
from ClickableSprite import ClickableSprite

class Arrow(ClickableSprite):
    def __init__(self, posX, posY, dir):
        images = [
            pygame.image.load('../resources/images/arrow_north_1(32).png').convert_alpha()
        ]
        images = [pygame.transform.rotate(i, -90*dir) for i in images]
        super().__init__(posX, posY, images)

        self.clickable = False
        self.visible = False

