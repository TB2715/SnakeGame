import color
import common


class Snake:
    color = color.WHITE

    def __init__(self):
        self.positions = [(9, 6), (9, 7), (9, 8), (9, 9)]
        self.direction = 'north'

    def draw(self, screen):
        for position in self.positions:
            common.draw_block(screen, self.color, position)

    def crawl(self):
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'north':
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'south':
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'west':
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'east':
            self.positions = [(y, x + 1)] + self.positions[:-1]

    def turn(self, direction):
        self.direction = direction

    def grow(self):
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'north':
            self.positions.append((y-1, x))
        elif self.direction == 'south':
            self.positions.append((y+1, x))
        elif self.direction == 'west':
            self.positions.append((y, x-1))
        elif self.direction == 'east':
            self.positions.append((y, x+1))