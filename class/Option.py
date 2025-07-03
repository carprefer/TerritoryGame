import pygame
from ClickableSprite import ClickableSprite

class Option(ClickableSprite):
    def __init__(self, posX, posY, description):
        images = [
            pygame.image.load('../resources/images/option_1(160).png').convert_alpha(),
        ]
        super().__init__(posX, posY, images)

        self.diceFont = pygame.font.SysFont(None, 48)
        self.descriptionFont = pygame.font.SysFont(None, 24)

        self.description = description
        self.dice = 0

    def draw(self, window):
        super().draw(window)
        if self.visible:
            diceText = self.diceFont.render(str(self.dice), True, 'white')
            diceRect = diceText.get_rect(center = (self.rect.center[0], self.rect.center[1]-30))
            window.blit(diceText, diceRect)

            descriptionText = self.descriptionFont.render(self.description, True, 'white')
            descriptionRect = descriptionText.get_rect(center = (self.rect.center[0], self.rect.center[1]+20))
            window.blit(descriptionText, descriptionRect)

    def set_dice(self, dice):
        self.dice = dice


            


