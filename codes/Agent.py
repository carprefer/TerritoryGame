from utils import *
from random import choice


class Agent():
    def __init__(self, board, images, xIdx, yIdx):
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.team = None

        self.board = board

        self.xIdx = 0
        self.yIdx = 0
        
        self.territory = 0
        self.hp = 10
        self.damage = 1
        self.randomPool = [1,2,3,4,5,6]
        self.option = 0
        self.path = []
        self.remainDice = 0

        self.move_in_board(xIdx, yIdx)


    def draw(self, window):
        window.blit(self.image, self.rect)

    def move_in_board(self, xIdx, yIdx):
        self.xIdx = xIdx
        self.yIdx = yIdx
        posX, posY = self.board.idx_to_pos(xIdx, yIdx)

        self.rect.center = (posX, posY)
    
    def roll_the_dice(self):
        return choice(self.randomPool)
    
    def occupy_here(self):
        self.board.change_cell_value(self.xIdx, self.yIdx, self.damage * self.team)

    def is_possible_option(self, option):
        if option == MOVE:
            self.board.set_clickable_cross(self.xIdx, self.yIdx, self.team)
            return len(self.board.get_clickable_cells()) > 0
        elif option == STRENGTHEN:
            return self.board.cells[self.yIdx][self.xIdx].value * self.team > 0
        elif option == CANON:
            return self.board.canons[self.yIdx][self.xIdx] == None

    def is_input_end(self):
        return self.remainDice == 0


    def action(self):
        if self.option == MOVE:
            for (x,y) in self.path:
                self.board.change_cell_value(x, y, self.damage * self.team)
                self.move_in_board(x,y)
        elif self.option == STRENGTHEN:
            for (x,y) in self.path:
                self.board.change_cell_value(x, y, self.damage * self.team)
        elif self.option == CANON:
            self.board.canons[self.yIdx][self.xIdx].set_visible(True) 

        playerCellCount, enemyCellCount = self.board.count_cells()
        if self.team == PLAYER:
            self.territory = playerCellCount
        else:
            self.territory = enemyCellCount




