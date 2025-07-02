import pygame
from sys import exit
from random import choice
from Background import Background
from Board import Board
from Player import Player
from Enemy import Enemy
from Option import Option
from Status import Status

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
BOARD_SIZE = 704
STATUS_SIZE = 384

OPTION_Y = 400

STATUS_X_GAP = ((WINDOW_WIDTH - BOARD_SIZE)//2 - STATUS_SIZE)//2

MAX_ROUND = 20

# state
START_STATE = 0
OPTION_STATE = 1
INPUT_STATE = 2
OUTPUT_STATE = 3
FIRE_STATE = 4

class Game:
    def __init__(self, args):
        self.args = args
        self.clock = pygame.time.Clock()

        self.state = START_STATE
        self.round = 0

        self.background = Background(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
        self.board = Board(self.args['b_xNum'], self.args['b_yNum'], (WINDOW_WIDTH - BOARD_SIZE)//2, (WINDOW_HEIGHT - BOARD_SIZE)//2)

        self.player = Player(self.board, 1, 8)
        self.enemy = Enemy(self.board, 8, 1)
        
        self.player.occupy_here()
        self.enemy.occupy_here()

        self.playerOptions = [
            Option(0, OPTION_Y, 'Move'),
            Option((WINDOW_WIDTH - BOARD_SIZE)//6, OPTION_Y, 'Strengthen'),
            Option((WINDOW_WIDTH - BOARD_SIZE)//3, OPTION_Y, 'Canon')
        ]

        self.enemyOptions = [
            Option((WINDOW_WIDTH + BOARD_SIZE)//2, OPTION_Y, 'Move'),
            Option((WINDOW_WIDTH + BOARD_SIZE)//2 + (WINDOW_WIDTH - BOARD_SIZE)//6, OPTION_Y, 'Strengthen'),
            Option((WINDOW_WIDTH + BOARD_SIZE)//2 + (WINDOW_WIDTH - BOARD_SIZE)//3, OPTION_Y, 'Canon')
        ]

        self.playerStatus = Status(STATUS_X_GAP, 0, self.player, 'player')
        self.enemyStatus = Status((WINDOW_WIDTH + BOARD_SIZE)//2 + STATUS_X_GAP, 0, self.enemy, 'enemy')

    def is_game_end(self):
        if self.player.hp <= 0 or self.enemy.hp <= 0:
            return True
        if self.round >= MAX_ROUND:
            return True
        return False
    
    def show_ending(self):
        playerCellCount, enemyCellCount = self.board.count_cells()
        if self.player.hp <= 0 and self.enemy.hp > 0:
            print('enemy win!')
        elif self.player.hp > 0 and self.enemy.hp <= 0:
            print('player win!')
        else:
            if playerCellCount > enemyCellCount:
                print('player win!')
            elif playerCellCount < enemyCellCount:
                print('enemy win!')
            else:
                print('draw')

        pygame.quit()
        exit()
        

    def run(self):
        while True:
            if self.is_game_end():
                self.show_ending()
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == OPTION_STATE:
                        for i, o in enumerate(self.playerOptions):
                            if o.is_clicked():
                                self.state = INPUT_STATE
                                self.player.prepare_input(i, o.dice)

                    elif self.state == INPUT_STATE:
                        self.player.receive_input()
                        if self.player.is_input_end():
                            self.state = OUTPUT_STATE

                if event.type == pygame.KEYDOWN:
                    {}

            if self.state == START_STATE:
                self.round += 1
                playerDices = [0,0,0]
                for i, o in enumerate(self.playerOptions):
                    if self.player.is_possible_option(i):
                        o.set_dice(self.player.roll_the_dice())
                        o.set_visible(True)
                        playerDices[i] = o.dice
                    else:
                        o.set_visible(False)
                enemyDices = [0,0,0]
                for i, o in enumerate(self.enemyOptions):
                    if self.enemy.is_possible_option(i):
                        o.set_dice(self.enemy.roll_the_dice())
                        o.set_visible(True)
                        enemyDices[i] = o.dice
                    else:
                        o.set_visible(False)
                
                # enemy logic
                self.enemy.generate_input(enemyDices)
                
                if sum(playerDices) > 0:
                    self.state = OPTION_STATE
                else:
                    self.state = OUTPUT_STATE

            elif self.state == OUTPUT_STATE:
                if bool(set(self.player.path) & set(self.enemy.path)):
                    print('intersect')
                    playerCellCount, enemyCellCount = self.board.count_cells()
                    if playerCellCount > enemyCellCount:
                        self.player.path = []
                        self.player.curDice = 0
                    elif playerCellCount < enemyCellCount:
                        self.enemy.path = []
                        self.enemy.curDice = 0
                    else:
                        self.player.path = []
                        self.enemy.path = []
                        self.player.curDice = 0
                        self.enemy.curDice = 0
                self.player.action()
                self.enemy.action()
                self.state = FIRE_STATE
            
            elif self.state == FIRE_STATE:
                self.board.fire_all_canon(self.player, self.enemy)
                self.state = START_STATE

            self.background.draw(window, self.round)
            self.board.draw(window)
            self.player.draw(window)
            self.enemy.draw(window)
            [o.draw(window) for o in self.playerOptions]
            [o.draw(window) for o in self.enemyOptions]
            self.playerStatus.draw(window)
            self.enemyStatus.draw(window)
        
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

