import pygame
from Agent import Agent

PLAYER = 1
ENEMY = -1

class Player(Agent):
    def __init__(self, board, xIdx, yIdx):
        super().__init__(board)
        self.images = [
            pygame.image.load('../resources/images/player_1(32).png').convert_alpha()
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        
        self.team = PLAYER

     
        self.move_in_board(xIdx, yIdx)

    def prepare_move_input(self, dice):
        self.remainDice = dice
        self.path = []
        self.board.set_clickable_cross(self.xIdx, self.yIdx)

    def prepare_strengthen_input(self, dice):
        self.remainDice = dice
        self.path = []
        self.board.set_clickable_connected(self.xIdx, self.yIdx)

    def prepare_canon_input(self, dice):
        self.board.add_canon(self.xIdx, self.yIdx, self.team, 0, dice)
        self.remainDice = dice

    def receive_move_input(self):
        cellIdx = self.board.get_clicked_cell_idx()
        if cellIdx != None and self.remainDice > 0:
            self.path.append((cellIdx[0], cellIdx[1]))
            self.board.set_clickable_cross(cellIdx[0], cellIdx[1])
            self.remainDice -= 1

    def receive_strengthen_input(self):
        cellIdx = self.board.get_clicked_cell_idx()
        if cellIdx != None and self.remainDice > 0:
            self.path.append((cellIdx[0], cellIdx[1]))
            self.remainDice -= 1

    def receive_canon_input(self):
        canon = self.board.canons[self.yIdx][self.xIdx]
        arrowDir = canon.get_clicked_arrow_dir()
        if arrowDir != None:
            canon.set_direction(arrowDir)
            self.remainDice = 0
            canon.unable_arrow()
                






