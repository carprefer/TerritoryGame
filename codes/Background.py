import pygame

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
BOARD_SIZE = 704
STATUS_SIZE = 384

class Background():
    def __init__(self, posX, posY):
        self.images = [
            pygame.image.load('../resources/images/in_game/background_1(3200).png').convert_alpha()
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = (posX, posY))
        


    def draw(self, window):
        window.blit(self.image, self.rect)


