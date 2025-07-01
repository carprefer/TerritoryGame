import pygame

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
BOARD_SIZE = 704

class Option():
    def __init__(self, posX, posY, description):
        self.images = [
            pygame.image.load('../resources/images/option_1(160).png').convert_alpha(),
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))
        self.mask = pygame.mask.from_surface(self.image)

        self.diceFont = pygame.font.SysFont(None, 48)
        self.descriptionFont = pygame.font.SysFont(None, 24)

        self.description = description
        self.dice = 5

        self.visible = False

    def draw(self, window):
        if self.visible:
            window.blit(self.image, self.rect)
            diceText = self.diceFont.render(str(self.dice), True, 'white')
            diceRect = diceText.get_rect(center = (self.rect.center[0], self.rect.center[1]-30))
            window.blit(diceText, diceRect)

            descriptionText = self.descriptionFont.render(self.description, True, 'white')
            descriptionRect = descriptionText.get_rect(center = (self.rect.center[0], self.rect.center[1]+20))
            window.blit(descriptionText, descriptionRect)

    def is_clicked(self):
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos):
            x = mousePos[0] - self.rect.x
            y = mousePos[1] - self.rect.y
            return self.mask.get_at((x,y))
        else:
            return False

    def set_dice(self, dice):
        self.dice = dice

    def set_visible(self, visible):
        self.visible = visible

            


