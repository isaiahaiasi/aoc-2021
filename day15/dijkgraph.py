from math import inf
from heap import Heap

MAXVAL = 1000000


class Node:
    def __init__(self, x, y, cost):
        self.coords = x, y
        self.cost = cost
        self.tc = MAXVAL
        self.visited = False
        self.heappos = -1


class Graph:
    def __init__(self, nodes: dict[tuple[int, int], Node]):
        self.nodes = nodes
        self.h = max(nodes, key=lambda n: n[1])[1] + 1
        self.w = max(nodes, key=lambda n: n[0])[0] + 1
        self.exitnode = nodes[(self.w - 1, self.h - 1)]
        self.exitnode.tc = inf

        nodelist = [n for _, n in nodes.items()]
        def sortfn(a, b): return 1 if a.tc < b.tc else -1
        self.unvisited = Heap(nodelist, sortfn)

    def dijkstra(self):
        node = self.get_min()
        node.tc = 0
        adj = self.get_adj(*node.coords)

        # ! tmp
        vc = 0

        while (not self.exitnode.visited):
            for an in adj:
                tc = node.tc + an.cost
                if (an.tc > tc):
                    an.tc = tc
                    self.unvisited.updatepos(an.heappos)

            node.visited = True
            vc += 1

            if (node == self.exitnode):
                print(str(vc))
                return node

            node = self.get_min()
            adj = self.get_adj(*node.coords)

    def get_min(self):
        minnode = self.unvisited.pop()
        while (minnode.visited):
            minnode = self.unvisited.pop()
        return minnode

    def get_adj(self, x, y, include_visited=False):
        adj_nodes = []
        loc_adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for locx, locy in loc_adj:
            coords = x + locx, y + locy

            if coords in self.nodes:
                if include_visited or not self.nodes[coords].visited:
                    adj_nodes.append(self.nodes[coords])

        return adj_nodes

    def render(self, path=False):
        out = ''
        for y in range(self.h):
            for x in range(self.w):
                n = self.nodes[(x, y)]
                out += f"{n.tc}({n.cost})\t"
            out += '\n'

        if path:
            with open(path, "w") as fp:
                fp.write(out)

        return out
