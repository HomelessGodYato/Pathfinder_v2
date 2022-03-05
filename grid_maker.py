import node


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node_ = node.Node(i, j, gap, rows)
            grid[i].append(node_)
