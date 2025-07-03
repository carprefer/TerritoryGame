import pygame

class Status():
    def __init__(self, posX, posY, agent, name):
        self.images = [
            pygame.image.load('../resources/images/status_1(384).png').convert_alpha(),
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))
        self.mask = pygame.mask.from_surface(self.image)

        self.nameFont = pygame.font.SysFont(None, 64)
        self.statFont = pygame.font.SysFont(None, 48)

        self.name = name
        self.agent = agent


    def draw(self, window):
        window.blit(self.image, self.rect)
        nameText = self.nameFont.render(str(self.name), True, 'white')
        nameRect = nameText.get_rect(topleft = (self.rect.topleft[0] + 20, self.rect.topleft[1]+60))
        window.blit(nameText, nameRect)

        hpText = self.statFont.render("HP: " + str(self.agent.hp), True, 'white')
        hpRect = hpText.get_rect(topleft = (self.rect.topleft[0] + 20, self.rect.topleft[1]+160))
        window.blit(hpText, hpRect)

        diceText = self.statFont.render("Territory: " + str(self.agent.territory), True, 'white')
        diceRect = diceText.get_rect(topleft = (self.rect.topleft[0] + 20, self.rect.topleft[1]+220))
        window.blit(diceText, diceRect)

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

            


