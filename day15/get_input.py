from dijkgraph import Node


def get_input(path, outpath=False):
    fp = open(path)
    lines = fp.read().split('\n')
    fp.close()

    height = len(lines)
    width = len(lines[0])

    strout = ""
    nodes = {}
    board_dupe_factor = 1
    for y in range(height * board_dupe_factor):
        for x in range(width * board_dupe_factor):
            incr = x // width + y // height
            bigcost = int(lines[y % height][x % width]) + incr
            cost = bigcost if bigcost < 10 else (bigcost % 10) + 1
            nodes[(x, y)] = Node(x, y, cost)
            strout += str(cost)
        strout += "\n"

    if outpath:
        with open(outpath, "w") as fp:
            fp.write(strout)

    return nodes
