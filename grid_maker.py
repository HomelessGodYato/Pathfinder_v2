import pygame.draw

import node
from node import BLANK

GRID_LINE = (0, 0, 0)


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows + 1):
        grid.append([])
        for j in range(rows + 1):
            node_ = node.Node(i, j, gap, rows)
            grid[i].append(node_)

    return grid


def draw_grid(window, rows, width):
    gap = width // rows
    for i in range(rows + 1):
        pygame.draw.line(window, GRID_LINE, (0, i * gap), (width, i * gap))
    for j in range(rows + 1):
        pygame.draw.line(window, GRID_LINE, (j * gap, 0), (j * gap, width))


def draw(window, grid, rows, width):
    window.fill(BLANK)
    for row in grid:
        for node_ in row:
            node_.draw(window)
    draw_grid(window, rows, width)
    pygame.display.update()


# Mouse position
def get_pos(position, rows, width):
    gap = width // rows
    y, x = position

    row = y // gap
    col = x // gap

    return row, col
