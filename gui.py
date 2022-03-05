import pygame, pygame_gui
import grid_maker
import node

HEIGHT = 1920
WIDTH = 1080

window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Pathfinder")
'''
manager = pygame_gui.UIManager((800, 600))
slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((50, 50), (200, 50)),
                                                start_value=0,
                                                value_range=(0, 100),
                                                manager=manager)

menu = pygame_gui.elements.UIDropDownMenu(options_list=["Astar", "Dijksta", "DFS", "BFS"],
                                          starting_option="Astar",
                                          relative_rect=pygame.Rect((100, 100), (300, 100)),
                                          manager=manager)

'''

def main(window, width):
    rows = 50
    grid = grid_maker.make_grid(rows, width)

    start = None
    end = None

    run = True
    while run:
        grid_maker.draw(window,grid,rows,width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if pygame.mouse.get_pressed()[0]:  # LMB
            position = pygame.mouse.get_pos()
            row, col = grid_maker.get_pos(position, rows, width)
            node_ = grid[row][col]

            if not start and node_!=end:
                start = node_
                start.set_start()

            elif not end and node_!=start:
                end = node_
                end.set_end()

            elif node_ !=end and node_!=start:
                node_.set_obstacle()

        if pygame.mouse.get_pressed()[2]:  # RMB
            position = pygame.mouse.get_pos()
            row,col = grid_maker.get_pos(position,rows,width)
            node_= grid[row][col]
            node_.reset_node()
            if node_ == start:
                start = None
            if node_ == end:
                end = None
    pygame.quit()

main(window,1000)