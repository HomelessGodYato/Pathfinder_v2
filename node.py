import pygame

import grid_maker

# It's just a way to assign a color to a variable.
BLANK = (255, 255, 255)
END = (56, 17, 253)
START = (0,153,0)
OBSTACLE = (0, 0, 0)
PATH = (204, 0, 0)
OPEN = (0,255,255)
VISITED = (255, 255, 0)


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.neighbors = []
        self.color = BLANK
        self.x_pos = row * width
        self.y_pos = col * width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_visited(self):
        return self.color == VISITED

    def is_open(self):
        return self.color == OPEN

    def is_obstacle(self):
        return self.color == OBSTACLE

    def is_start(self):
        return self.color == START

    def is_end(self):
        return self.color == END

    def reset_color(self):
        self.color = BLANK

    def set_visited(self):
        self.color = VISITED

    def set_open(self):
        self.color = OPEN

    def set_start(self):
        self.color = START

    def set_end(self):
        self.color = END

    def set_obstacle(self):
        self.color = OBSTACLE

    def set_path(self):
        self.color = PATH

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x_pos, self.y_pos, self.width, self.width))

    def update_neighbors(self, grid_):
        self.neighbors = []

        if self.row < self.total_rows - 1 and not grid_[self.row + 1][self.col].is_obstacle():  # DOWN
            self.neighbors.append(grid_[self.row + 1][self.col])

        if self.row > 0 and not grid_[self.row - 1][self.col].is_obstacle():  # UP
            self.neighbors.append(grid_[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid_[self.row][self.col + 1].is_obstacle():  # RIGHT
            self.neighbors.append(grid_[self.row][self.col + 1])

        if self.col > 0 and not grid_[self.row][self.col - 1].is_obstacle():  # LEFT
            self.neighbors.append(grid_[self.row][self.col - 1])

    def __lt__(self, other):
        return False


# Mouse position
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col


def draw(window, grid_, rows, width):
    window.fill(BLANK)

    for row in grid_:
        for node_ in row:
            node_.draw(window)

    grid_maker.draw_grid(window, rows, width)
    pygame.display.update()
