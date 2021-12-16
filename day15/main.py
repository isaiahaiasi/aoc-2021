from math import inf
from time import time


def get_input(path):
    fp = open(path)
    lines = fp.read().split('\n')
    fp.close()

    nodes = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            nodes[(x, y)] = Node(x, y, int(lines[y][x]))
    return nodes


class Node:
    def __init__(self, x, y, cost):
        self.coords = x, y
        self.cost = cost
        self.tc = inf


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.h = max(nodes, key=lambda n: n[1])[1] + 1
        self.w = max(nodes, key=lambda n: n[0])[0] + 1
        self.unvisited = nodes.copy()  # todo: reimplement using minheap

    def dijkstra(self):
        node = self.get_unvisited_node(0, 0)
        node.tc = 0
        adj = self.get_adj(*node.coords)

        while ((self.w - 1, self.h - 1) in self.unvisited):
            del self.unvisited[node.coords]
            for an in adj:
                tc = node.tc + an.cost
                if (an.tc > tc):
                    an.tc = tc
            node.visited = True

            if (node == self.get_last()):
                return node

            node = self.get_min()
            adj = self.get_adj(*node.coords)

    def get_unvisited_node(self, x, y):
        return self.unvisited[(x, y)]

    # todo: reimplement using minheap
    def get_min(self):
        return min(self.unvisited.items(), key=lambda n: n[1].tc)[1]

    def get_adj(self, x, y):
        adj_nodes = []
        loc_adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for locx, locy in loc_adj:
            cx, cy = x + locx, y + locy

            if self.in_range(cx, cy) and (cx, cy) in self.unvisited:
                adj_nodes.append(self.get_unvisited_node(cx, cy))

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

    def get_last(self):
        return self.nodes[(self.w - 1, self.h - 1)]


nodes = get_input('input/test-input.txt')
start = time()
graph = Graph(nodes)
finalnode = graph.dijkstra()
end = time()
print(*finalnode.coords, finalnode.tc)
print("time", end - start)
