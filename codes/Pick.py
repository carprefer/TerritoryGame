import pygame
from ClickableSprite import ClickableSprite
from UI import *
from utils import *
from Slider import Slider
from Arrow import Arrow

class Pick():
    def __init__(self, posX, posY, agents):
        self.backgroundRect = pygame.Rect(posX - PICK_WIDTH//2, posY - PICK_HEIGHT//2, PICK_WIDTH, PICK_HEIGHT)
        self.leftArrow = Arrow(posX - PICK_WIDTH*2//5, posY - PICK_HEIGHT//4, WEST, 4)
        self.rightArrow = Arrow(posX + PICK_WIDTH*2//5, posY - PICK_HEIGHT//4, EAST, 4)
        self.leftArrow.set_enable(True)
        self.rightArrow.set_enable(True)

        self.nameFont = pygame.font.SysFont(None, 64)
        self.statFont = pygame.font.SysFont(None, 48)

        self.agentIdx = 0

        self.agents = [a(None, 4) for a in agents]

        for a in self.agents:
            a.move_outside_board(posX, posY - PICK_HEIGHT//4)



    def draw(self, window):
        pygame.draw.rect(window, BACKGROUND_COLOR, self.backgroundRect)
        self.leftArrow.draw(window)
        self.rightArrow.draw(window)
        
        agent = self.agents[self.agentIdx]
        agent.draw(window)

        nameText = self.nameFont.render(agent.name, True, 'white')
        nameRect = nameText.get_rect(center = self.backgroundRect.center)
        window.blit(nameText, nameRect)
        
        rect = self.backgroundRect.topleft

        hpText = self.statFont.render("HP: " + str(agent.hp), True, 'white')
        hpRect = hpText.get_rect(topleft = (rect[0] + 20, rect[1]+PICK_HEIGHT//2 + 50))
        window.blit(hpText, hpRect)

        damageText = self.statFont.render("Damage: " + str(agent.damage), True, 'white')
        damageRect = damageText.get_rect(topleft = (rect[0] + 20, rect[1]+PICK_HEIGHT//2 + 100))
        window.blit(damageText, damageRect)

        rect = self.backgroundRect.move(20, PICK_HEIGHT//2 + 170)
        rect.width -= 40

        render_text(window, agent.feature, self.statFont, 'white', rect)




    def is_hovered(self):
        mousePos = pygame.mouse.get_pos() 
        return self.backgroundRect.collidepoint(mousePos)

    def run(self, window):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.leftArrow.is_clicked():
                        self.agentIdx = (self.agentIdx-1)%len(self.agents)
                    elif self.rightArrow.is_clicked():
                        self.agentIdx = (self.agentIdx+1)%len(self.agents)

                elif event.type == pygame.MOUSEMOTION:
                    if not self.is_hovered():
                        running = False

            self.draw(window)
            
            pygame.display.update()


    



    
