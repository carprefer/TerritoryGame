import pygame
from utils import *
from sys import exit
from Background import Background
from Board import Board
from Player import Player
from Enemy import Enemy
from Option import Option
from Status import Status



class Game:
    def __init__(self, args, window, playerIdx, enemyIdx):
        self.args = args
        self.window = window
        self.clock = pygame.time.Clock()

        self.state = START_STATE
        self.round = 0

        self.background = Background(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
        self.board = Board(self.args['b_xNum'], self.args['b_yNum'], (WINDOW_WIDTH - BOARD_SIZE)//2, (WINDOW_HEIGHT - BOARD_SIZE)//2)

        self.player = Player[playerIdx](self.board)
        self.enemy = Enemy[enemyIdx](self.board)

        self.player.move_in_board(1, args['b_yNum'] - 2)
        self.enemy.move_in_board(args['b_xNum'] - 2, 1)
        
        self.player.occupy_here()
        self.enemy.occupy_here()

        self.playerOptions = [
            Option(80, OPTION_Y, 'Move'),
            Option((WINDOW_WIDTH - BOARD_SIZE)//6 + 80, OPTION_Y, 'Strengthen'),
            Option((WINDOW_WIDTH - BOARD_SIZE)//3 + 80, OPTION_Y, 'Canon')
        ]

        self.enemyOptions = [
            Option((WINDOW_WIDTH + BOARD_SIZE)//2 + 80, OPTION_Y, 'Move'),
            Option((WINDOW_WIDTH + BOARD_SIZE)//2 + (WINDOW_WIDTH - BOARD_SIZE)//6 + 80, OPTION_Y, 'Strengthen'),
            Option((WINDOW_WIDTH + BOARD_SIZE)//2 + (WINDOW_WIDTH - BOARD_SIZE)//3 + 80, OPTION_Y, 'Canon')
        ]

        self.playerStatus = Status(STATUS_X_GAP, 0, self.player, 'player')
        self.enemyStatus = Status((WINDOW_WIDTH + BOARD_SIZE)//2 + STATUS_X_GAP, 0, self.enemy, 'enemy')

        self.roundFont = pygame.font.SysFont(None, 48)


    def is_game_end(self):
        return self.player.hp <= 0 or self.enemy.hp <= 0 or self.round >= self.args['max_round']
    
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
                    if self.player.territory >= self.enemy.territory:
                        self.player.path = []
                    if self.player.territory <= self.enemy.territory:
                        self.enemy.path = []
                self.player.action()
                self.enemy.action()
                self.player.territory, self.enemy.territory = self.board.count_cells()
                self.state = FIRE_STATE
            
            elif self.state == FIRE_STATE:
                self.board.fire_all_canon(self.player, self.enemy)
                self.player.territory, self.enemy.territory = self.board.count_cells()
                self.state = START_STATE

            self.draw_all()
        
            pygame.display.update()
            self.clock.tick(self.args['fps'])

    def draw_all(self):
        self.background.draw(self.window)
        self.board.draw(self.window)
        self.player.draw(self.window)
        self.enemy.draw(self.window)
        [o.draw(self.window) for o in self.playerOptions]
        [o.draw(self.window) for o in self.enemyOptions]
        self.playerStatus.draw(self.window)
        self.enemyStatus.draw(self.window)

        roundText = self.roundFont.render(str(self.round) + " Round", True, 'white')
        roundRect = roundText.get_rect(center = (WINDOW_WIDTH//2, 50))
        self.window.blit(roundText, roundRect)




if __name__ == "__main__":
    args = {
        'fps': 60, 
        'b_xNum': 10,
        'b_yNum': 10,
    }
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    game = Game(args, window)
    game.run()

