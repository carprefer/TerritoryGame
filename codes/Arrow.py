import pygame
from ClickableSprite import ClickableSprite

class Arrow(ClickableSprite):
    def __init__(self, posX, posY, dir, scale=1):
        images = [
            pygame.image.load('../resources/images/in_game/arrow_north_1(32).png').convert_alpha()
        ]
        images = [pygame.transform.scale(i, (i.get_width()*scale, i.get_height()*scale)) for i in images]
        images = [pygame.transform.rotate(i, -90*dir) for i in images]
        super().__init__(posX, posY, images)

        self.clickable = False
        self.visible = False

