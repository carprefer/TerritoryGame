import pygame
from utils import *
from Game import Game
from Background import Background
from Setting import *
from UI import *
from Pick import Pick
from Player import Player
from Enemy import Enemy


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
background = Background(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
setting = Setting(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
settingButton = SettingButton(WINDOW_WIDTH - 50, 50)
startButton = StartButton(WINDOW_WIDTH - 130, WINDOW_HEIGHT - 75)

playerPick = Pick(WINDOW_WIDTH//4, WINDOW_HEIGHT//2 - 50, Player)
enemyPick = Pick(WINDOW_WIDTH*3//4, WINDOW_HEIGHT//2 - 50, Enemy)

vsFont = pygame.font.SysFont(None, 64)
vsText = vsFont.render('Player                         VS                         Enemy', True, 'white')
vsRect = vsText.get_rect(center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//16))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.is_clicked():
                game = Game(setting.args, window, playerPick.agentIdx, enemyPick.agentIdx)
                game.run()
            elif settingButton.is_clicked():
                setting.run(window)
        
        elif event.type == pygame.MOUSEMOTION:
            if playerPick.is_hovered():
                playerPick.run(window)
            elif enemyPick.is_hovered():
                enemyPick.run(window)


    background.draw(window)
    settingButton.draw(window)
    startButton.draw(window)
    playerPick.draw(window)    
    enemyPick.draw(window)
    window.blit(vsText, vsRect)

    pygame.display.update()
    clock.tick(setting.args['fps'])