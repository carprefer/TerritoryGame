import pygame
from Agent import Agent

class Player(Agent):
    def __init__(self, board, xIdx, yIdx):
        super().__init__(board)
        self.images = [
            pygame.image.load('../resources/images/player_1(32).png').convert_alpha()
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()

     
        self.move_in_board(xIdx, yIdx)






