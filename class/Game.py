import pygame
from sys import exit
from Board import Board
from Player import Player
from Option import Option

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
BOARD_SIZE = 704

OPTION_Y = 100

# state
START_STATE = 0
OPTION_STATE = 1
PLAYER_INPUT_STATE = 2
ENEMY_INPUT_STATE = 3
OUTPUT_STATE = 4
FIRE_STATE = 5

class Game:
    def __init__(self, args):
        self.args = args
        self.clock = pygame.time.Clock()

        self.state = START_STATE

        self.board = Board(self.args['b_xNum'], self.args['b_yNum'], (WINDOW_WIDTH - BOARD_SIZE)//2, (WINDOW_HEIGHT - BOARD_SIZE)//2)

        self.player = Player(self.board, 0, 0)
        self.board.add_canon(0,5,1,1,10)

        self.playerOptions = [
            Option(0, OPTION_Y, 'Move'),
            Option((WINDOW_WIDTH - BOARD_SIZE)//6, OPTION_Y, 'Strengthen'),
            Option((WINDOW_WIDTH - BOARD_SIZE)//3, OPTION_Y, 'Canon')
        ]
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == OPTION_STATE:
                        for i, o in enumerate(self.playerOptions):
                            if o.is_clicked():
                                self.state = PLAYER_INPUT_STATE
                                self.player.prepare_input(i, o.dice)

                    elif self.state == PLAYER_INPUT_STATE:
                        self.player.receive_input()
                        if self.player.is_input_end():
                            self.state = OUTPUT_STATE

                if event.type == pygame.KEYDOWN:
                    if self.state == START_STATE:
                        for o in self.playerOptions:
                            o.set_dice(self.player.roll_the_dice())
                            o.set_visible(True)
                        self.state = OPTION_STATE
                    elif self.state == OUTPUT_STATE:
                        self.player.action()
                        self.state = FIRE_STATE
                    elif self.state == FIRE_STATE:
                        self.board.fire_all_canon()
                        self.state = START_STATE

            self.board.draw(window)
            self.player.draw(window)
            [o.draw(window) for o in self.playerOptions]
        
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

