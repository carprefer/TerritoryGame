import pygame
from utils import *
from Game import Game
from Background import Background
from Setting import *
from UI import *
from Pick import Pick


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
background = Background(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
setting = Setting(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
settingButton = SettingButton(WINDOW_WIDTH - 50, 50)
startButton = StartButton(WINDOW_WIDTH - 130, WINDOW_HEIGHT - 75)

playerPick = Pick(50, 300)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.is_clicked():
                game = Game(setting.args, window)
                game.run()
            elif settingButton.is_clicked():
                setting.run(window)


    background.draw(window)
    settingButton.draw(window)
    startButton.draw(window)
    playerPick.draw(window)    

    pygame.display.update()
    clock.tick(setting.args['fps'])