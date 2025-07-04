import pygame
from ClickableSprite import ClickableSprite
from UI import *
from utils import *
from Slider import Slider

class SettingButton(ClickableSprite):
    def __init__(self, posX, posY):
        images = [
            pygame.image.load('../resources/images/setting_1(64).png').convert_alpha()
        ]
        super().__init__(posX, posY, images)



class Setting():
    def __init__(self, posX, posY):
        self.backgroundImage = pygame.image.load('../resources/images/setting_background_1(3200).png').convert_alpha()
        self.backgroundRect = self.backgroundImage.get_rect(center = (posX, posY))
        self.backgroundImage.set_alpha(128)

        self.fpsSlider = Slider(100, 100, 'FPS', 60, 24, 144)
        self.bxSlider = Slider(100, 200, 'Rows', 10, 3, 10)
        self.bySlider = Slider(100, 300, 'Columns', 10, 3, 10)
        self.maxRoundSlider = Slider(100, 400, 'Round', 30, 5, 100)

        self.exitButton = ExitButton(posX + WINDOW_WIDTH//2 - 50, posY - WINDOW_HEIGHT//2 + 50)

        self.args = {}
        self.update_value()

    def draw(self, window):
        window.blit(self.backgroundImage, self.backgroundRect)
        self.exitButton.draw(window)
        self.fpsSlider.draw(window)
        self.bxSlider.draw(window)
        self.bySlider.draw(window)
        self.maxRoundSlider.draw(window)

    def update_value(self):
        self.args['fps'] = self.fpsSlider.value
        self.args['b_xNum'] = self.bxSlider.value
        self.args['b_yNum'] = self.bySlider.value
        self.args['max_round'] = self.maxRoundSlider.value

    def run(self, window):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.exitButton.is_clicked():
                        running = False
                elif event.type == pygame.MOUSEMOTION:
                    if self.fpsSlider.is_hovered():
                        self.fpsSlider.run(window)
                    elif self.bxSlider.is_hovered():
                        self.bxSlider.run(window)
                    elif self.bySlider.is_hovered():
                        self.bySlider.run(window)
                    elif self.maxRoundSlider.is_hovered():
                        self.maxRoundSlider.run(window)

            self.draw(window)

            pygame.display.update()
        
        self.update_value()


    



    
