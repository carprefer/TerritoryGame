import pygame

NEUTRAL = 0
PLAYER = 1
ENEMY = 2

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
BOARD_SIZE = 704
STATUS_SIZE = 384

class Background():
    def __init__(self, posX, posY):
        self.images = [
            pygame.image.load('../resources/images/background_1(3200).png').convert_alpha()
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = (posX, posY))
        
        self.roundFont = pygame.font.SysFont(None, 48)



    def draw(self, window, round):
        window.blit(self.image, self.rect)

        roundText = self.roundFont.render(str(round) + " Round", True, 'white')
        roundRect = roundText.get_rect(center = (self.rect.center[0], self.rect.center[1] - WINDOW_HEIGHT//2 + 50))
        window.blit(roundText, roundRect)

