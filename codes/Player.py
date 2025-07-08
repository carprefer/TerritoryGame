import pygame
from utils import *
from Agent import Agent

class Player1(Agent):
    def __init__(self, board, scale=1):
        images = [
            pygame.image.load('../resources/images/in_game/player_1(32).png').convert_alpha()
        ]
        super().__init__(board, images, scale)
        
        self.team = PLAYER
        self.name = 'Citizen'
        self.feature = 'Standard and normal agent'


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


class Player2(Agent):
    def __init__(self, board, scale=1):
        images = [
            pygame.image.load('../resources/images/in_game/player_1(32).png').convert_alpha()
        ]
        super().__init__(board, images, scale)
        
        self.team = PLAYER
        self.name = 'Land Broker'
        self.feature = 'Soft target, solid ground.'
        self.hp = 2
        self.damage = 2


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


class Player3(Agent):
    def __init__(self, board, scale=1):
        images = [
            pygame.image.load('../resources/images/in_game/player_1(32).png').convert_alpha()
        ]
        super().__init__(board, images, scale)
        
        self.team = PLAYER
        self.name = 'Gambler'
        self.feature = 'High rolls are favored.'
        self.randomPool = [1,2,3,4,5,6,4,5,6]
        self.hp = 2

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


Player = [
    Player1,
    Player2,
    Player3
]



