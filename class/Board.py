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

        self.cells = [[Cell(*self.idx_to_pos(xIdx, yIdx)) for xIdx in range(xNum)] for yIdx in range(yNum)]

        self.canons = [[None for _ in range(self.xNum)] for _ in range(self.yNum)]


    def draw(self, window):
        window.blit(self.image, self.rect)
        for yIdx in range(self.yNum):
            for xIdx in range(self.xNum):
                self.cells[yIdx][xIdx].draw(window)
        
        for yIdx in range(self.yNum):
            for xIdx in range(self.xNum):
                canon = self.canons[yIdx][xIdx]
                if canon != None:
                    canon.draw(window)


    def idx_to_pos(self, xIdx, yIdx):
        x = self.posX + (BOARD_SIZE - CELL_SIZE * self.xNum - CELL_GAP * (self.xNum-1))//2 + (CELL_SIZE+CELL_GAP) * xIdx + CELL_SIZE//2
        y = self.posY + (BOARD_SIZE - CELL_SIZE * self.yNum - CELL_GAP * (self.yNum-1))//2 + (CELL_SIZE+CELL_GAP) * yIdx + CELL_SIZE//2

        return x, y
    
    def is_in_board(self, xIdx, yIdx):
        return xIdx < self.xNum and yIdx < self.yNum
    
    def change_cell_value(self, xIdx, yIdx, diff):
        if self.is_in_board(xIdx, yIdx):
            if self.cells[yIdx][xIdx].change_value(diff):
                self.delete_canon(xIdx, yIdx)
    
    def add_canon(self, xIdx, yIdx, team, dir, range):
        canon = Canon(self, xIdx, yIdx, team, dir, range)
        self.canons[yIdx][xIdx] = canon
        canon.enable_arrow()

    def delete_canon(self, xIdx, yIdx):
        canon = self.canons[yIdx][xIdx]
        del canon
        self.canons[yIdx][xIdx] = None

    def fire_all_canon(self):
        for yIdx in range(self.yNum):
            for xIdx in range(self.xNum):
                canon = self.canons[yIdx][xIdx]
                if canon != None:
                    canon.fire()

    def get_clicked_cell_idx(self):
        for yIdx in range(self.yNum):
            for xIdx in range(self.xNum):
                if self.cells[yIdx][xIdx].is_clicked():
                    return (xIdx, yIdx)
        return None
                
    def set_clickable_cross(self, xIdx, yIdx):
        for y in range(self.yNum):
            for x in range(self.xNum):
                if (abs(xIdx - x) == 1 and yIdx == y) or (xIdx == x and abs(yIdx - y) == 1):
                    self.cells[y][x].set_clickable(True)
                else:
                    self.cells[y][x].set_clickable(False)

    def set_clickable_connected(self, xIdx, yIdx):
        visited = [[False for _ in range(self.xNum)] for _ in range(self.yNum)]
        def dfs(xIdx, yIdx):
            visited[yIdx][xIdx] = True
            curV = self.cells[yIdx][xIdx].value
            if not visited[yIdx+1][xIdx] and self.cells[yIdx+1][xIdx].value * curV > 0:
                dfs(xIdx, yIdx+1)
            if not visited[yIdx-1][xIdx] and self.cells[yIdx-1][xIdx].value * curV > 0:
                dfs(xIdx, yIdx-1)
            if not visited[yIdx][xIdx+1] and self.cells[yIdx][xIdx+1].value * curV > 0:
                dfs(xIdx+1, yIdx)
            if not visited[yIdx][xIdx-1] and self.cells[yIdx][xIdx-1].value * curV > 0:
                dfs(xIdx-1, yIdx)

        dfs(xIdx, yIdx)

        for y in range(self.yNum):
            for x in range(self.xNum):
                if visited[y][x]:
                    self.cells[y][x].set_clickable(True)
                else:
                    self.cells[y][x].set_clickable(False)
        
        


    

