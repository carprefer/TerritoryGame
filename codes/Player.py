import pygame
from utils import *
from Agent import Agent

class Player(Agent):
    def __init__(self, board, xIdx, yIdx):
        images = [
            pygame.image.load('../resources/images/in_game/player_1(32).png').convert_alpha()
        ]
        super().__init__(board, images, xIdx, yIdx)
        
        self.team = PLAYER


    def prepare_input(self, option, dice):
        self.board.set_clickMode_all(True)
        self.board.set_clickable_all(False)
        self.option = option
        self.remainDice = dice
        self.path = []
        if self.option == MOVE:
            self.board.set_clickable_cross(self.xIdx, self.yIdx, self.team)
        elif self.option == STRENGTHEN:
            self.board.set_clickable_connected(self.xIdx, self.yIdx)
        elif self.option == CANON:
            self.board.add_canon(self.xIdx, self.yIdx, self.team, 0, dice)

    def receive_input(self):
        if self.option == MOVE:
            cellIdx = self.board.get_clicked_cell_idx()
            if cellIdx != None and self.remainDice > 0:
                self.path.append((cellIdx[0], cellIdx[1]))
                self.board.set_clickable_cross(cellIdx[0], cellIdx[1], self.team)
                self.remainDice -= 1
        elif self.option == STRENGTHEN:
            cellIdx = self.board.get_clicked_cell_idx()
            if cellIdx != None and self.remainDice > 0:
                self.path.append((cellIdx[0], cellIdx[1]))
                self.remainDice -= 1
        elif self.option == CANON:
            canon = self.board.canons[self.yIdx][self.xIdx]
            arrowDir = canon.get_clicked_arrow_dir()
            if arrowDir != None:
                canon.set_direction(arrowDir)
                self.remainDice = 0
                canon.enable_arrow(False)

        if self.is_input_end():
            self.board.set_clickMode_all(False)
            self.board.set_clickable_all(False)







