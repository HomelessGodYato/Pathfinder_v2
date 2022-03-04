import node
import pygame

LINE = (0, 0, 0)


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            new_node = node.Node(i, j, gap, rows)
            grid[i].append(new_node)
    return grid


def draw_grid(window, rows, width):
    gap = width // rows
    for i in range(rows+1):
        pygame.draw.line(window, LINE, (0, i * gap), (width, i * gap))
        for j in range(rows+1):
            pygame.draw.line(window, LINE, (j * gap, 0), (j * gap, width))
