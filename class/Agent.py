import pygame
from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self, board):
        self.images = None
        self.image = None
        self.rect = None

        self.board = board

        self.xIdx = 0
        self.yIdx = 0
        
        self.diceSum = 0
        self.hp = 10
        self.randomPool = [1,2,3,4,5,6]

    def draw(self, window):
        window.blit(self.image, self.rect)

    def move_in_board(self, xIdx, yIdx):
        self.xIdx = xIdx
        self.yIdx = yIdx
        posX, posY = self.board.idx_to_pos(xIdx, yIdx)

        self.rect.center = (posX, posY)
    





