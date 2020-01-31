import pygame
from datetime import datetime
from datetime import timedelta

import common
from gameBoard import GameBoard
from snakeCollisionException import SnakeCollisionException

pygame.display.set_caption("snake game")
game_board = GameBoard()
last_turn_time = datetime.now()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in common.DIRECTION_ON_KEY:
                game_board.snake.turn(common.DIRECTION_ON_KEY[event.key])

    if common.TURN_INTERVAL < datetime.now() - last_turn_time:
        try:
            game_board.process_turn()
        except SnakeCollisionException:
            exit()
        last_turn_time = datetime.now()

    common.draw_background(common.screen)
    game_board.draw(common.screen)
    pygame.display.update()
