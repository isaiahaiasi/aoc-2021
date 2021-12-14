# Day 12 - Passage Pathing
# undirected graph
# find all permutations of the path between START & END node
# 2 types of nodes: LARGE & small.
# small caves can only be visited once.

class Graph:
    def __init__(self, nodes: dict):
        self.nodes = nodes
        self.path_count = 0

    def get_paths(self):
        for n in self.nodes['start'].adj:
            self.visit_node(n, ["start"])
        print("path count:", self.path_count)
        return self.path_count

    def visit_node(self, node, current_path):
        path = [*current_path, node.name]

        if node.name == 'end':
            self.path_count = self.path_count + 1
            print(path)
            return

        adj = [n for n in node.adj if n.name not in path or n.isbig()]
        if len(adj) == 0:
            return

        for n in adj:
            self.visit_node(n, path)

    def render_nodes(self):
        for name, node in self.nodes.items():
            print(name, ':', node.adj)


class Node:
    def __init__(self, name):
        self.name = name
        self.adj = []

    def add_edge(self, node):
        self.adj.append(node)

    def isbig(self):
        return self.name.isupper()

    def __repr__(self):
        return f"n({self.name})"


def parse_input(input: str):
    nodes = {}
    for line in input.strip().split('\n'):
        l, r = line.split('-')
        for name in [l, r]:
            if name not in nodes:
                nodes[name] = Node(name)

        if l != 'start':
            nodes[r].add_edge(nodes[l])
        if r != 'start':
            nodes[l].add_edge(nodes[r])

    return Graph(nodes)


def get_input(path):
    with open(path) as fp:
        return fp.read()


if __name__ == "__main__":
    input = get_input("input.txt")
    graph = parse_input(input)
    graph.get_paths()
