import pygame


class ClickableSprite():
    def __init__(self, posX, posY, images):
        self.images = images
        self.imageIdx = 0
        self.rect = self.images[self.imageIdx].get_rect(center = (posX, posY))

        self.clickable = True
        self.visible = True

    def draw(self, window):
        if self.visible:
            window.blit(self.images[self.imageIdx], self.rect)

    def is_clicked(self):
        if self.clickable and self.visible:
            mousePos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mousePos):
                x = mousePos[0] - self.rect.x
                y = mousePos[1] - self.rect.y
                mask = pygame.mask.from_surface(self.images[self.imageIdx])
                return mask.get_at((x,y))
            else:
                return False
        else:
            return False

    def set_clickable(self, clickable):
        self.clickable = clickable

    def set_visible(self, visible):
        self.visible = visible

    def set_enable(self, enable):
        self.clickable = enable
        self.visible = enable

            


