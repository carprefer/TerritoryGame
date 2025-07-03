import pygame
from utils import *
from random import choice
from Agent import Agent

class Enemy(Agent):
    def __init__(self, board, xIdx, yIdx):
        images = [
            pygame.image.load('../resources/images/enemy_1(32).png').convert_alpha()
        ]
        super().__init__(board, images, xIdx, yIdx)
        
        self.team = ENEMY

    def generate_input(self, dices):
        if sum(dices) > 0:
            movePathCandidates = self.exhaustive_search(self.xIdx, self.yIdx, [], dices[0])
            movePathScores = [self.calculate_path_score(c) for c in movePathCandidates]
            canonScores = self.calculate_canon_score(dices[2])
            if max(movePathScores) > max(canonScores):
                maxIdxs = [i for i, s in enumerate(movePathScores) if s == max(movePathScores)]
                choosenIdx = choice(maxIdxs)
                self.path = movePathCandidates[choosenIdx]
                self.remainDice = 0
                self.option = 0
            else:
                maxIdxs = [i for i, s in enumerate(canonScores) if s == max(canonScores)]
                self.board.add_canon(self.xIdx, self.yIdx, self.team, 0, dices[2])
                canon = self.board.canons[self.yIdx][self.xIdx]
                canon.visible = False
                arrowDir = choice(maxIdxs)
                if arrowDir != None:
                    canon.set_direction(arrowDir)
                    self.remainDice = 0
                    canon.enable_arrow(False)
                self.option = 2


    def exhaustive_search(self, xIdx, yIdx, selected, dice):
        if len(selected) == dice:
            return [selected]
        result = []
        self.board.set_clickable_cross(xIdx, yIdx, self.team)
        clickableCells = self.board.get_clickable_cells()
        for (x,y) in clickableCells:
            result += self.exhaustive_search(x, y, selected + [(x,y)], dice)
        return result

    def calculate_path_score(self, path):
        score = 0
        for (x,y) in path:
            if self.board.cells[y][x].value == 0:
                score += 2
            else:
                score += 1
        return score
    
    def calculate_canon_score(self, dice):
        pool = [0,0,0,0]
        for r in range(1, dice + 1):
            targetX = self.xIdx
            targetY = self.yIdx - r
            if self.board.is_in_board(targetX, targetY):
                if self.board.cells[targetY][targetX].value * self.team < 0:
                    pool[0] += 3
                    if self.board.canons[targetY][targetX] != None:
                        pool[0] += 3
                else:
                    pool[0] += 1
            targetX = self.xIdx + r
            targetY = self.yIdx
            if self.board.is_in_board(targetX, targetY):
                if self.board.cells[targetY][targetX].value * self.team < 0:
                    pool[1] += 3
                    if self.board.canons[targetY][targetX] != None:
                        pool[1] += 3
                else:
                    pool[1] += 1
            targetX = self.xIdx
            targetY = self.yIdx + r
            if self.board.is_in_board(targetX, targetY):
                if self.board.cells[targetY][targetX].value * self.team < 0:
                    pool[2] += 3
                    if self.board.canons[targetY][targetX] != None:
                        pool[2] += 3
                else:
                    pool[2] += 1
            targetX = self.xIdx - r
            targetY = self.yIdx
            if self.board.is_in_board(targetX, targetY):
                if self.board.cells[targetY][targetX].value * self.team < 0:
                    pool[3] += 3
                    if self.board.canons[targetY][targetX] != None:
                        pool[3] += 3
                else:
                    pool[3] += 1

        return pool



                






