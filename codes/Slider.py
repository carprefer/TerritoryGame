import pygame
from utils import *

class Slider():
    def __init__(self, posX, posY, name, value, minimum, maximum):
        self.backgroundRect = pygame.Rect(posX, posY, SLIDER_WIDTH * 2, SLIDER_HEIGHT * 5)
        self.sliderRect = pygame.Rect(posX + SLIDER_WIDTH//2, posY + SLIDER_HEIGHT*2, SLIDER_WIDTH, SLIDER_HEIGHT)
        self.handlePos = 0

        self.font = pygame.font.SysFont(None, 24)

        self.dragging = False

        self.name = name
        self.value = value
        self.minimum = minimum
        self.maximum = maximum

        self.calculate_handle_pos()

    def draw(self, window):
        pygame.draw.rect(window, 'black', self.backgroundRect)
        pygame.draw.rect(window, 'gray', self.sliderRect)
        pygame.draw.circle(window, 'dark green', (self.handlePos, self.sliderRect.y + SLIDER_HEIGHT//2), HANDLE_SIZE)

        self.value = round(self.minimum + (self.maximum - self.minimum) * (self.handlePos - self.sliderRect.x) / self.sliderRect.width)
        valueText = self.font.render(str(self.value), True, (255, 255, 255))
        window.blit(valueText, (self.sliderRect.center[0] + 250, self.sliderRect.center[1] - SLIDER_HEIGHT//2))

        nameText = self.font.render(self.name, True, 'white')
        window.blit(nameText, (self.sliderRect.center[0] - 250, self.sliderRect.center[1] - SLIDER_HEIGHT//2))

    def is_hovered(self):
        mousePos = pygame.mouse.get_pos() 
        return self.backgroundRect.collidepoint(mousePos)
    
    def calculate_handle_pos(self):
        self.handlePos = self.sliderRect.x + SLIDER_WIDTH * (self.value - self.minimum) / (self.maximum - self.minimum)


    def run(self, window):
        running = True
        while running:
            mouseX, mouseY = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if abs(mouseX - self.handlePos) <= HANDLE_SIZE and abs(mouseY - self.sliderRect.y - SLIDER_HEIGHT//2) <= HANDLE_SIZE:
                        self.dragging = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.dragging = False

                elif event.type == pygame.MOUSEMOTION:
                    if not self.is_hovered():
                        self.dragging = False
                        running = False

            if self.dragging:
                self.handlePos = max(self.sliderRect.x, min(mouseX, self.sliderRect.x + self.sliderRect.width))

                self.draw(window)

            
            pygame.display.update()

            


