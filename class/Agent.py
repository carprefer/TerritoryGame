import pygame
from random import choice
from abc import ABC, abstractmethod

PLAYER = 1
ENEMY = -1

class Agent(ABC):
    def __init__(self, board):
        self.images = None
        self.image = None
        self.rect = None

        self.team = None

        self.board = board

        self.xIdx = 0
        self.yIdx = 0
        
        self.diceSum = 0
        self.hp = 10 
        self.damage = 1
        self.randomPool = [1,2,3,4,5,6]
        self.optionNum = 0
        self.path = []
        self.remainDice = 0

    def draw(self, window):
        window.blit(self.image, self.rect)

    def move_in_board(self, xIdx, yIdx):
        self.xIdx = xIdx
        self.yIdx = yIdx
        posX, posY = self.board.idx_to_pos(xIdx, yIdx)

        self.rect.center = (posX, posY)
    
    def roll_the_dice(self):
        return choice(self.randomPool)
    
    def prepare_input(self, n, dice):
        self.optionNum = n
        if self.optionNum == 0:
            self.prepare_move_input(dice)
        elif self.optionNum == 1:
            self.prepare_strengthen_input(dice)
        elif self.optionNum == 2:
            self.prepare_canon_input(dice)

    @abstractmethod
    def prepare_move_input(self, dice):
        pass

    @abstractmethod
    def prepare_strengthen_input(self, dice):
        pass

    @abstractmethod
    def prepare_canon_input(self, dice):
        pass

    def receive_input(self):
        if self.optionNum == 0:
            self.receive_move_input()
        elif self.optionNum == 1:
            self.receive_strengthen_input()
        elif self.optionNum == 2:
            self.receive_canon_input()

    @abstractmethod
    def receive_move_input(self):
        pass

    @abstractmethod
    def receive_strengthen_input(self):
        pass

    @abstractmethod
    def receive_canon_input(self):
        pass

    def is_input_end(self):
        if self.optionNum == 0:
            return self.remainDice == 0
        elif self.optionNum == 1:
            return self.remainDice == 0
        elif self.optionNum == 2:
            return self.remainDice == 0

    def damage_to_value(self):
        if self.team == PLAYER:
            return self.damage
        elif self.team == ENEMY:
            return - self.damage

    def action(self):
        if self.optionNum == 0:
            for (x,y) in self.path:
                self.board.change_cell_value(x, y, self.damage_to_value())
            self.move_in_board(x,y)
        elif self.optionNum == 1:
            for (x,y) in self.path:
                self.board.change_cell_value(x, y, self.damage_to_value())
        elif self.optionNum == 2:
            {}




