import pygame

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

PLAYER = 1
ENEMY = 2

class Canon(pygame.sprite.Sprite):
    def __init__(self, board, xIdx, yIdx, team, dir, range):
        super().__init__()
        self.images = [
            pygame.image.load('../resources/images/canon_north_1(64).png').convert_alpha(),
            pygame.image.load('../resources/images/canon_east_1(64).png').convert_alpha(),
            pygame.image.load('../resources/images/canon_south_1(64).png').convert_alpha(),
            pygame.image.load('../resources/images/canon_west_1(64).png').convert_alpha(),
        ]
        self.image = self.images[dir]
        self.rect = self.image.get_rect(center = board.idx_to_pos(xIdx, yIdx))

        
        self.board = board
        self.xIdx = xIdx
        self.yIdx = yIdx
        self.team = team
        self.dir = dir
        self.range = range




