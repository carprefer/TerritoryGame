import pygame
from utils import *
from Cell import Cell
from Canon import Canon


class Board():
    def __init__(self, xNum, yNum, posX, posY):
        self.xNum = xNum
        self.yNum = yNum
        self.posX = posX
        self.posY = posY

        self.images = [
            pygame.image.load('../resources/images/in_game/board_1(704).png').convert_alpha()
        ]

        self.image = self.images[0]

        self.rect = self.image.get_rect(topleft = (posX, posY))

        self.cells = [[Cell(*self.idx_to_pos(xIdx, yIdx)) for xIdx in range(xNum)] for yIdx in range(yNum)]

        self.canons = [[None for _ in range(self.xNum)] for _ in range(self.yNum)]


    def draw(self, window):
        window.blit(self.image, self.rect)
        [self.cells[y][x].draw(window) for y in range(self.yNum) for x in range(self.xNum)]
        [self.canons[y][x].draw(window) for y in range(self.yNum) for x in range(self.xNum) if self.canons[y][x] != None]

    def count_cells(self):
        playerCount = 0
        enemyCount = 0
        for yIdx in range(self.yNum):
            for xIdx in range(self.xNum):
                v = self.cells[yIdx][xIdx].value
                if v > 0:
                    playerCount += 1
                elif v < 0:
                    enemyCount += 1

        return playerCount, enemyCount

    def idx_to_pos(self, xIdx, yIdx):
        x = self.posX + (BOARD_SIZE - CELL_SIZE * self.xNum - CELL_GAP * (self.xNum-1))//2 + (CELL_SIZE+CELL_GAP) * xIdx + CELL_SIZE//2
        y = self.posY + (BOARD_SIZE - CELL_SIZE * self.yNum - CELL_GAP * (self.yNum-1))//2 + (CELL_SIZE+CELL_GAP) * yIdx + CELL_SIZE//2

        return x, y
    
    def is_in_board(self, xIdx, yIdx):
        return 0 <= xIdx and xIdx < self.xNum and 0 <= yIdx and yIdx < self.yNum
    
    def change_cell_value(self, xIdx, yIdx, diff):
        if self.is_in_board(xIdx, yIdx):
            self.cells[yIdx][xIdx].change_value(diff)
            if self.cells[yIdx][xIdx].value == 0:
                self.delete_canon(xIdx, yIdx)
    
    def add_canon(self, xIdx, yIdx, team, dir, range):
        if self.canons[yIdx][xIdx] != None:
            print('canon error')
        canon = Canon(self, xIdx, yIdx, team, dir, range)
        self.canons[yIdx][xIdx] = canon
        canon.enable_arrow(True)

    def delete_canon(self, xIdx, yIdx):
        canon = self.canons[yIdx][xIdx]
        del canon
        self.canons[yIdx][xIdx] = None

    def fire_all_canon(self, player, enemy):
        [self.canons[y][x].fire(player,enemy) for y in range(self.yNum) for x in range(self.xNum) if self.canons[y][x] != None]

    def get_clicked_cell_idx(self):
        for yIdx in range(self.yNum):
            for xIdx in range(self.xNum):
                if self.cells[yIdx][xIdx].is_clicked():
                    return (xIdx, yIdx)
        return None
                
    def set_clickable_cross(self, xIdx, yIdx, team):
        for y in range(self.yNum):
            for x in range(self.xNum):
                if ((abs(xIdx - x) == 1 and yIdx == y) or (xIdx == x and abs(yIdx - y) == 1)) and team * self.cells[y][x].value >= 0:
                    self.cells[y][x].set_clickable(True)
                else:
                    self.cells[y][x].set_clickable(False)

    def set_clickable_connected(self, xIdx, yIdx):
        visited = [[False for _ in range(self.xNum)] for _ in range(self.yNum)]
        def dfs(xIdx, yIdx):
            visited[yIdx][xIdx] = True
            curV = self.cells[yIdx][xIdx].value
            if self.is_in_board(xIdx, yIdx+1) and not visited[yIdx+1][xIdx] and self.cells[yIdx+1][xIdx].value * curV > 0:
                dfs(xIdx, yIdx+1)
            if self.is_in_board(xIdx, yIdx-1) and not visited[yIdx-1][xIdx] and self.cells[yIdx-1][xIdx].value * curV > 0:
                dfs(xIdx, yIdx-1)
            if self.is_in_board(xIdx+1, yIdx) and not visited[yIdx][xIdx+1] and self.cells[yIdx][xIdx+1].value * curV > 0:
                dfs(xIdx+1, yIdx)
            if self.is_in_board(xIdx-1, yIdx) and not visited[yIdx][xIdx-1] and self.cells[yIdx][xIdx-1].value * curV > 0:
                dfs(xIdx-1, yIdx)

        dfs(xIdx, yIdx)

        [self.cells[y][x].set_clickable(visited[y][x]) for y in range(self.yNum) for x in range(self.xNum)]

    def set_clickable_all(self, clickable):
        [self.cells[y][x].set_clickable(clickable) for y in range(self.yNum) for x in range(self.xNum)]

    def get_clickable_cells(self):
        return [(x,y) for y in range(self.yNum) for x in range(self.xNum) if self.cells[y][x].clickable]
    
    def set_clickMode_all(self, clickMode):
        for y in range(self.yNum):
            for x in range(self.xNum):
                self.cells[y][x].clickMode = clickMode
    
    

        
        


    

