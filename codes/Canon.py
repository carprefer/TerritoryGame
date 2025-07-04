import pygame
from utils import *
from Arrow import Arrow


class Canon():
    def __init__(self, board, xIdx, yIdx, team, dir, range):
        (posX, posY) = board.idx_to_pos(xIdx, yIdx)
        self.images = [
            pygame.image.load('../resources/images/in_game/canon_1(64).png').convert_alpha(),
            pygame.image.load('../resources/images/in_game/canon_2(64).png').convert_alpha()
        ]
        self.imageIdx = 0
        self.images = [pygame.transform.rotate(i, -90*dir) for i in self.images]
        self.rect = self.images[self.imageIdx].get_rect(center = (posX, posY))
        self.font = pygame.font.SysFont(None, 24)

        self.animationMode = False
        self.visible = True

        
        self.board = board
        self.xIdx = xIdx
        self.yIdx = yIdx
        self.team = team
        self.dir = dir
        self.range = range
        self.damage = 1

        
        self.arrows = [
            Arrow(posX, posY - 28, NORTH),
            Arrow(posX + 28, posY, EAST),
            Arrow(posX, posY + 28, SOUTH),
            Arrow(posX - 28, posY, WEST),
        ]

    def draw(self, window):
        if self.visible:
            if self.animationMode:
                self.imageIdx += 0.1
                if self.imageIdx >= self.range*2:
                    self.animationMode = False
            else:
                self.imageIdx = 0
            window.blit(self.images[int(self.imageIdx) % len(self.images)], self.rect)

            rangeText = self.font.render(str(self.range), True, 'yellow')
            rangeRect = rangeText.get_rect(center = (self.rect.center[0]-15, self.rect.center[1]-15))
            window.blit(rangeText, rangeRect)

            [a.draw(window) for a in self.arrows]

    def set_visible(self, visible):
        self.visible = visible
    
    def set_direction(self, dir):
        self.dir = dir
        self.images = [pygame.transform.rotate(i, -90*dir) for i in self.images]

    def get_front_index(self, distance):
        if self.dir == NORTH:
            return self.xIdx, self.yIdx - distance
        elif self.dir == EAST:
            return self.xIdx + distance, self.yIdx
        elif self.dir == SOUTH:
            return self.xIdx, self.yIdx + distance
        elif self.dir == WEST:
            return self.xIdx - distance, self.yIdx
        
    def fire(self, player, enemy):
        self.animationMode = True
        for r in range(1, self.range + 1):
            targetX, targetY = self.get_front_index(r)
            #if self.board.is_in_board(targetX, targetY) and self.board.cells[targetY][targetX].value * self.team < 0:
            if self.board.is_in_board(targetX, targetY):
                if targetX == player.xIdx and targetY == player.yIdx:
                    player.hp -= 1
                elif targetX == enemy.xIdx and targetY == enemy.yIdx:
                    enemy.hp -= 1
                else:
                    v = self.board.cells[targetY][targetX].value
                    if v > 0:
                        f = -1
                    elif v < 0:
                        f = 1
                    else:
                        f = 0
                    self.board.change_cell_value(targetX, targetY, self.damage * f)


    def enable_arrow(self, enable):
        [a.set_clickable(enable) for a in self.arrows]
        [a.set_visible(enable) for a in self.arrows]

    def get_clicked_arrow_dir(self):
        for i, a in enumerate(self.arrows):
            if a.is_clicked():
                return i
        return None


