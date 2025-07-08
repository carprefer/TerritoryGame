import pygame

# direction
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# cell type
NEUTRAL = 0
PLAYER = 1
ENEMY = 2

# board frame
CELL_GAP = 4
BOARD_SIZE = 704
CELL_SIZE = 64

# team
PLAYER = 1
ENEMY = -1

# option
MOVE = 0
STRENGTHEN = 1
CANON = 2

# window frame
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
BOARD_SIZE = 704
STATUS_SIZE = 384
OPTION_Y = 450

STATUS_X_GAP = ((WINDOW_WIDTH - BOARD_SIZE)//2 - STATUS_SIZE)//2


# in game state
START_STATE = 0
OPTION_STATE = 1
INPUT_STATE = 2
OUTPUT_STATE = 3
FIRE_STATE = 4


# UI info
BACKGROUND_COLOR = '#202400'
SLIDER_WIDTH = 300
SLIDER_HEIGHT = 10
HANDLE_SIZE = 10
PICK_WIDTH = 600
PICK_HEIGHT = 600
UI_GAP = 50


def render_text(window, text, font, color, rect, lineGap=5):
    words = text.split(' ')
    lines = []
    curLine = ''
    
    for word in words:
        tmpLine = curLine + word + ' '
        if font.size(tmpLine)[0] <= rect.width:
            curLine = tmpLine
        else:
            lines.append(curLine.strip())
            curLine = word + ' '
    lines.append(curLine.strip())
    
    y = rect.top
    for line in lines:
        text = font.render(line, True, color)
        window.blit(text, (rect.left, y))
        y += text.get_height() + lineGap
