from datetime import timedelta

import pygame
import color

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 10

TURN_INTERVAL = timedelta(seconds=0.3)
time_interval = 0.3

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 36)

DIRECTION_ON_KEY = {
    pygame.K_UP: 'north',
    pygame.K_DOWN: 'south',
    pygame.K_LEFT: 'west',
    pygame.K_RIGHT: 'east',
}

def draw_background(screen):
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, color.BLACK, background)


def draw_block(screen, color, position):
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)


def show_game_over(screen):
    # pygame.draw.rect(screen, color.GREEN, [SCREEN_WIDTH, SCREEN_HEIGHT, 50, 50])
    text = font.render("Game Over", True, color.WHITE)
    screen.blit(text, (0, 0))


