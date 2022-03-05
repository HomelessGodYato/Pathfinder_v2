from queue import PriorityQueue
import pygame


def h(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(previous, current, start, draw):
    while current in previous:
        current = previous[current]
        current.set_path()
        if current == start:
            start.set_start()
        draw()


def astar(draw, grid, start, end):
    count = 0
    open_list = PriorityQueue()
    open_list.put((0, count, start))
    previous_node = {}

    g_score = {node_: float("inf") for row in grid for node_ in row}
    g_score[start] = 0

    f_score = {node_: float("inf") for row in grid for node_ in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_list_hash = {start}

    while not open_list.empty():
        current_node = open_list.get()[2]
        open_list_hash.remove(current_node)

        if current_node == end:
            end.set_end()
            start.set_start()
            reconstruct_path(previous_node, current_node, start, draw)
            return True

        for neighbor in current_node.neighbors:
            tmp_g_score = g_score[current_node] + 1

            if tmp_g_score < g_score[neighbor]:
                previous_node[neighbor] = current_node
                g_score[neighbor] = tmp_g_score
                f_score[neighbor] = tmp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_list_hash:
                    count += 1
                    open_list.put((f_score[neighbor], count, neighbor))
                    open_list_hash.add(neighbor)
                    neighbor.set_open()
        draw()

        if current_node != start:
            current_node.set_visited()


    return False

def reset(grid_):
    for row in grid_:
        for node_ in row:
            if node_.is_open() or node_.is_visited():
                node_.reset_color()


def reset_obstacles(grid_):
    for row in grid_:
        for node_ in row:
            if node_.is_obstacle():
                node_.reset_color()