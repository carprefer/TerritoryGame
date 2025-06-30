import pygame
from sys import exit
from Board import Board
from Player import Player

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
BOARD_SIZE = 704

class Game:
    def __init__(self, args):
        self.args = args
        self.clock = pygame.time.Clock()

        self.board = Board(self.args['b_xNum'], self.args['b_yNum'], (WINDOW_WIDTH - BOARD_SIZE)//2, (WINDOW_HEIGHT - BOARD_SIZE)//2)

        self.player = Player(self.board, 0, 0)
        self.board.add_canon(0,5,0,1,1)
        self.board.delete_canon(0,5)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.board.draw(window)
            self.player.draw(window)
        
            pygame.display.update()
            self.clock.tick(self.args['fps'])



if __name__ == "__main__":
    args = {
        'fps': 60, 
        'b_xNum': 10,
        'b_yNum': 10,
    }
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    game = Game(args)
    game.run()

