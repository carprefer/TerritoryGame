import pygame
from Arrow import Arrow

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

PLAYER = 1
ENEMY = -1

class Canon():
    def __init__(self, board, xIdx, yIdx, team, dir, range):
        (posX, posY) = board.idx_to_pos(xIdx, yIdx)
        self.images = [
            pygame.image.load('../resources/images/canon_north_1(64).png').convert_alpha(),
            pygame.image.load('../resources/images/canon_east_1(64).png').convert_alpha(),
            pygame.image.load('../resources/images/canon_south_1(64).png').convert_alpha(),
            pygame.image.load('../resources/images/canon_west_1(64).png').convert_alpha(),
        ]
        self.image = self.images[dir]
        self.rect = self.image.get_rect(center = (posX, posY))

        
        self.board = board
        self.xIdx = xIdx
        self.yIdx = yIdx
        self.team = team
        self.dir = dir
        self.range = range
        self.damage = 1

        
        self.arrows = [
            Arrow(posX, posY - 28, 0),
            Arrow(posX + 28, posY, 1),
            Arrow(posX, posY + 28, 2),
            Arrow(posX - 28, posY, 3),
        ]

    def draw(self, window):
        window.blit(self.image, self.rect)
        [a.draw(window) for a in self.arrows]
    
    def set_direction(self, dir):
        self.dir = dir
        self.image = self.images[dir]

    def get_front_index(self, distance):
        if self.dir == NORTH:
            return self.xIdx, self.yIdx - distance
        elif self.dir == EAST:
            return self.xIdx + distance, self.yIdx
        elif self.dir == SOUTH:
            return self.xIdx, self.yIdx + distance
        elif self.dir == WEST:
            return self.xIdx - distance, self.yIdx
        
    def damage_to_value(self):
        if self.team == PLAYER:
            return self.damage
        elif self.team == ENEMY:
            return - self.damage

    def fire(self):
        for r in range(1, self.range + 1):
            targetX, targetY = self.get_front_index(r)
            if self.board.is_in_board(targetX, targetY) and self.board.cells[targetY][targetX].value * self.team < 0:
                self.board.change_cell_value(targetX, targetY, self.damage_to_value())
            
    def enable_arrow(self):
        for a in self.arrows:
            a.set_clickable(True)

    def unable_arrow(self):
        for a in self.arrows:
            a.set_clickable(False)

    def get_clicked_arrow_dir(self):
        for i, a in enumerate(self.arrows):
            if a.is_clicked():
                return i
        return None


