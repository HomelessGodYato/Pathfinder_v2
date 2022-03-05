import time

import pygame

import algorithm as alg
import grid_maker
import node

HEIGHT = 600
WIDTH = 600

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinder")


def main(window, width):
    rows = 25
    grid = grid_maker.make_grid(rows, width)

    start = None
    end = None

    run = True
    while run:
        grid_maker.draw(window, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:  # LMB
                position = pygame.mouse.get_pos()
                row, col = node.get_clicked_pos(position, rows, width)
                node_ = grid[row][col]

                if not start and node_ != end:
                    start = node_
                    start.set_start()

                elif not end and node_ != start:
                    end = node_
                    end.set_end()

                elif node_ != end and node_ != start:
                    node_.set_obstacle()

            if pygame.mouse.get_pressed()[2]:  # RMB
                position = pygame.mouse.get_pos()
                row, col = node.get_clicked_pos(position, rows, width)
                node_ = grid[row][col]
                node_.reset_color()
                if node_ == start:
                    start = None
                if node_ == end:
                    end = None

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and rows > 5:
                    start = None
                    end = None
                    alg.reset(grid)
                    rows -= 5
                    grid = grid_maker.make_grid(rows, width)
                    time.sleep(0.1)

                if event.key == pygame.K_RIGHT and rows < 50:
                    start = None
                    end = None
                    alg.reset(grid)
                    rows += 5
                    grid = grid_maker.make_grid(rows, width)
                    time.sleep(0.1)

                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node_ in row:
                            node_.update_neighbors(grid)
                    alg.astar(lambda: grid_maker.draw(window, grid, rows, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    alg.reset(grid)
                    grid = grid_maker.make_grid(rows,width)
    pygame.quit()


main(window, WIDTH)
