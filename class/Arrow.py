import pygame


NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Arrow():
    def __init__(self, posX, posY, dir):
        self.images = [
            pygame.image.load('../resources/images/arrow_north_1(32).png').convert_alpha(),
            pygame.image.load('../resources/images/arrow_east_1(32).png').convert_alpha(),
            pygame.image.load('../resources/images/arrow_south_1(32).png').convert_alpha(),
            pygame.image.load('../resources/images/arrow_west_1(32).png').convert_alpha(),
        ]
        self.image = self.images[dir]
        self.rect = self.image.get_rect(center = (posX, posY))
        self.mask = pygame.mask.from_surface(self.image)

        self.clickable = False


    def draw(self, window):
        if self.clickable:
            window.blit(self.image, self.rect)

    def set_clickable(self, clickable):
        self.clickable = clickable

    def is_clicked(self):
        if self.clickable:
            mousePos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mousePos):
                x = mousePos[0] - self.rect.x
                y = mousePos[1] - self.rect.y
                return self.mask.get_at((x,y))
            else:
                return False
        else:
            return False

