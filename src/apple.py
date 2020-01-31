import color
import common


class Apple:
    color = color.RED

    def __init__(self, position=(5, 5)):
        self.position = position

    def draw(self, screen):
        common.draw_block(screen, self.color, self.position)
