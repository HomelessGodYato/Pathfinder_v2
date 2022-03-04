import pygame, pygame_gui
manager = pygame_gui.UIManager((800, 600))
slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((50, 50), (200, 50)),
                                                start_value=0,
                                                value_range=(0, 100),
                                                manager=manager)

menu = pygame_gui.elements.UIDropDownMenu(options_list=["Astar", "Dijksta", "DFS", "BFS"],
                                          starting_option="Astar",
                                          relative_rect=pygame.Rect((100, 100), (300, 100)),
                                          manager=manager)
