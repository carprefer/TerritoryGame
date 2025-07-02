import pygame
from random import choice
from Agent import Agent

PLAYER = 1
ENEMY = -1

class Enemy(Agent):
    def __init__(self, board, xIdx, yIdx):
        super().__init__(board)
        self.images = [
            pygame.image.load('../resources/images/enemy_1(32).png').convert_alpha()
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        
        self.team = ENEMY

     
        self.move_in_board(xIdx, yIdx)

    def generate_input(self, dices):
        if sum(dices) > 0:
            priority = [5, 1, 4]
            pool = []
            for i, d in enumerate(dices):
                if d != 0:
                    pool += [(i,d)] * d * priority[i]

            i, d = choice(pool)
            self.prepare_input(i, d)
            while not self.is_input_end():
                self.receive_input()

    def prepare_move_input(self, dice):
        self.remainDice = dice
        self.path = []
        self.board.set_clickable_cross(self.xIdx, self.yIdx, self.team)

    def prepare_strengthen_input(self, dice):
        self.remainDice = dice
        self.path = []
        self.board.set_clickable_connected(self.xIdx, self.yIdx)

    def prepare_canon_input(self, dice):
        self.board.add_canon(self.xIdx, self.yIdx, self.team, 0, dice)
        self.remainDice = dice

    def receive_move_input(self):
        priority = [5, 1]
        pool = []
        for (x,y) in self.board.get_clickable_cells():
            pool += [(x,y)] * priority[abs(self.board.cells[y][x].value) > 0]
        cellIdx = choice(pool)
        if cellIdx != None and self.remainDice > 0:
            self.path.append((cellIdx[0], cellIdx[1]))
            self.board.set_clickable_cross(cellIdx[0], cellIdx[1], self.team)
            self.remainDice -= 1

    def receive_strengthen_input(self):
        cellIdx = choice(self.board.get_clickable_cells())
        if cellIdx != None and self.remainDice > 0:
            self.path.append((cellIdx[0], cellIdx[1]))
            self.remainDice -= 1

    def receive_canon_input(self):
        canon = self.board.canons[self.yIdx][self.xIdx]
        arrowDir = choice([0,1,2,3])
        if arrowDir != None:
            canon.set_direction(arrowDir)
            self.remainDice = 0
            canon.unable_arrow()
                






