import pygame
from ClickableSprite import ClickableSprite

class StartButton(ClickableSprite):
    def __init__(self, posX, posY):
        images = [
            pygame.image.load('../resources/images/start_1(192).png').convert_alpha()
        ]
        super().__init__(posX, posY, images)

        font = pygame.font.SysFont(None, 48)
        self.text = font.render('Start', True, 'white')
        self.textRect = self.text.get_rect(center= self.rect.center)

    def draw(self, window):
        super().draw(window)
        window.blit(self.text, self.textRect)


class ExitButton(ClickableSprite):
    def __init__(self, posX, posY):
        images = [
            pygame.image.load('../resources/images/exit_1(32).png').convert_alpha()
        ]
        super().__init__(posX, posY, images)

