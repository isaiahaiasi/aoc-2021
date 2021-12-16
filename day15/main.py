from math import inf


def get_input(path):
    fp = open(path)
    lines = fp.read().split('\n')
    fp.close()

    nodes = []
    for y in range(len(lines)):
        noderow = []
        for x in range(len(lines[0])):
            noderow.append(Node(x, y, int(lines[y][x])))
        nodes.append(noderow)
    return nodes


class Node:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost
        self.visited = False
        self.tc = inf


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.h = len(nodes)
        self.w = len(nodes[0])

    def dijkstra(self):
        node = self.get_node(0, 0)
        node.tc = 0
        adj = self.get_adj(node.x, node.y)

        destnode = self.get_node(self.w - 1, self.h - 1)

        while (not destnode.visited and len(adj) > 0):
            for an in adj:
                tc = node.tc + an.cost
                if (an.tc > tc):
                    an.tc = tc
            node.visited = True

            print(self.render(), self.render("tc"))
            print(node.tc)

            node = min(adj, key=lambda x: x.tc)
            adj = self.get_adj(node.x, node.y)
        return node

    def get_node(self, x, y):
        return self.nodes[y][x]

    def get_min(self):

        # get node with minimum tc
        # this is why I would want a minheap
        # but unfortunately heapq doesn't let me lower priority :(
        pass

    # this could be an optimization target ("unvisited set")
    def get_adj(self, x, y):
        adj_nodes = []
        loc_adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for locx, locy in loc_adj:
            cx, cy = x + locx, y + locy

            if self.in_range(cx, cy) and not self.get_node(cx, cy).visited:
                adj_nodes.append(self.get_node(cx, cy))

        return adj_nodes

    def in_range(self, x, y):
        return y < self.h and x < self.w and y >= 0 and x >= 0

    def render(self, attr="cost"):
        out = ''
        for line in self.nodes:
            for n in line:
                if n.visited:
                    out += '*' + str(getattr(n, attr))
                else:
                    out += ' ' + str(getattr(n, attr))
            out += '\n'
        return out


nodes = get_input('input/test-input.txt')
graph = Graph(nodes)
finalnode = graph.dijkstra()
print(finalnode.x, finalnode.y, finalnode.cost)
