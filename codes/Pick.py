import pygame
from ClickableSprite import ClickableSprite
from UI import *
from utils import *
from Slider import Slider
from Arrow import Arrow

class Pick():
    def __init__(self, posX, posY):
        self.leftArrow = Arrow(posX, posY, WEST, 4)
        self.rightArrow = Arrow(posX  + 300, posY, EAST, 4)

        self.leftArrow.set_enable(True)
        self.rightArrow.set_enable(True)

    def draw(self, window):
        self.leftArrow.draw(window)
        self.rightArrow.draw(window)


    



    
