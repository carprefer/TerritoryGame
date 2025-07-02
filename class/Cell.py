import pygame

NEUTRAL = 0
PLAYER = 1
ENEMY = 2

class Cell():
    def __init__(self, posX, posY):
        self.images = [
            pygame.image.load('../resources/images/cell_1(64).png').convert_alpha(),
            pygame.image.load('../resources/images/cell_2(64).png').convert_alpha(),
            pygame.image.load('../resources/images/cell_3(64).png').convert_alpha(),
        ]
        self.image = self.images[NEUTRAL]
        self.rect = self.image.get_rect(center = (posX, posY))
        self.mask = pygame.mask.from_surface(self.image)
        self.font = pygame.font.SysFont(None, 24)
        
        
        self.value = 0      # 0: neutral / +: player / -: enemy

        self.clickable = False
        self.clickMode = False
        self.selected = False


    def draw(self, window):
        if self.clickMode:
            if self.clickable:
                self.image.set_alpha(255)
            else:
                self.image.set_alpha(128)
        else:
            self.image.set_alpha(255)

        window.blit(self.image, self.rect)
        valueText = self.font.render(str(abs(self.value)), True, 'black')
        window.blit(valueText, self.rect.move(48, 48))

    def change_value(self, diff):
        changed = False
        old = self.value
        new = self.value + diff
        if new > 0 and old <= 0:
            self.image = self.images[PLAYER]
            changed = True
        elif new == 0 and old != 0:
            self.image = self.images[NEUTRAL]
            changed = True
        elif new < 0 and old >= 0:
            self.image = self.images[ENEMY]
            changed = True

        self.value += diff
        return changed 

    def set_clickable(self, clickable):
        self.clickable = clickable

    def is_clicked(self):
        if self.clickable:
            mousePos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mousePos):
                x = mousePos[0] - self.rect.x
                y = mousePos[1] - self.rect.y
                self.selected = True
                return self.mask.get_at((x,y))
            else:
                return False
        else:
            return False

