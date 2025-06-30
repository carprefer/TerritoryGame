import pygame
from Cell import Cell
from Canon import Canon

CELL_GAP = 4
BOARD_SIZE = 704
CELL_SIZE = 64

class Board():
    def __init__(self, xNum, yNum, posX, posY):
        self.xNum = xNum
        self.yNum = yNum
        self.posX = posX
        self.posY = posY

        self.images = [
            pygame.image.load('../resources/images/board_1(704).png').convert_alpha()
        ]

        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))

        self.cellGroup = pygame.sprite.Group()
        for yIdx in range(yNum):
            for xIdx in range(xNum):
                cell = Cell(*self.idx_to_pos(xIdx, yIdx))
                self.cellGroup.add(cell)

        self.canons = [[None for _ in range(self.xNum)] for _ in range(self.yNum)]
        self.canonGroup = pygame.sprite.Group()


    def draw(self, window):
        window.blit(self.image, self.rect)
        self.cellGroup.draw(window)
        self.canonGroup.draw(window)

    def idx_to_pos(self, xIdx, yIdx):
        x = self.posX + (BOARD_SIZE - CELL_SIZE * self.xNum - CELL_GAP * (self.xNum-1))//2 + (CELL_SIZE+CELL_GAP) * xIdx + CELL_SIZE//2
        y = self.posY + (BOARD_SIZE - CELL_SIZE * self.yNum - CELL_GAP * (self.yNum-1))//2 + (CELL_SIZE+CELL_GAP) * yIdx + CELL_SIZE//2

        return x, y
    
    def add_canon(self, xIdx, yIdx, team, dir, range):
        canon = Canon(self, xIdx, yIdx, team, dir, range)
        self.canonGroup.add(canon)
        self.canons[yIdx][xIdx] = canon

    def delete_canon(self, xIdx, yIdx):
        canon = self.canons[yIdx][xIdx]
        canon.kill()
        del canon
        self.canons[yIdx][xIdx] = None
        


    

