import pygame

# Colors
PATH = (204, 0, 0)
OBSTACLE = (0, 0, 0)
VISITED = (255, 255, 0)
OPEN = (102, 204, 0)
START = (0, 153, 0)
END = (56, 17, 253)
BLANK = (255, 255, 255)


class Node():
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.neighbors = []
        self.color = BLANK
        self.width = width
        self.total_rows = total_rows

    def get_position(self):
        return self.x, self.y

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

    def is_path(self):
        return self.color == PATH

    def reset_node(self):
        self.color = BLANK

    def set_open(self):
        self.color = OPEN

    def set_start(self):
        self.color = START

    def set_end(self):
        self.color = END

    def set_obstacle(self):
        self.color = OBSTACLE

    def set_visited(self):
        self.color = VISITED

    def set_path(self):
        self.color = PATH

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_obstacle():  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_obstacle():  # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_obstacle():  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_obstacle():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self):
        return False

