import random
from datetime import timedelta

import color
import common
import snake
import apple
from snakeCollisionException import SnakeCollisionException
import pygame


class GameBoard:
    width = 40
    height = 40
    score = 0
    time_interval = 0.3

    def __init__(self):
        self.snake = snake.Snake()
        self.apple = apple.Apple()

    def draw(self, screen):
        self.apple.draw(screen)
        self.snake.draw(screen)
        self.show_score(screen)

    def process_turn(self):
        self.snake.crawl()
        y, x = self.snake.positions[0]

        if self.snake.positions[0] in self.snake.positions[1:]:
            raise SnakeCollisionException()

        if x < 0 or (x == self.width) or y < 0 or (y == self.height):
            raise SnakeCollisionException()

        if self.snake.positions[0] == self.apple.position:
            self.score += 1
            self.snake.grow()
            self.put_new_apple()

            # 사과를 먹을 때 마다, 이동속도 증가
            self.time_interval -= 0.025
            common.TURN_INTERVAL = timedelta(seconds=self.time_interval)

    def put_new_apple(self):
        self.apple = apple.Apple((random.randint(0, 19), random.randint(0, 19)))
        for position in self.snake.positions:
            if self.apple.position == position:
                self.put_new_apple()
                break

    def show_score(self, screen):
        smallFont = pygame.font.SysFont("comicsansms", 12)
        text = smallFont.render("Score: " + str(self.score), True, color.WHITE)
        screen.blit(text, [0, 0])