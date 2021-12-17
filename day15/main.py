from time import time
from get_input import get_input
from dijkgraph import Graph


nodes = get_input('input/test-input.txt')
start = time()
graph = Graph(nodes)
finalnode = graph.dijkstra()
end = time()
print(*finalnode.coords, finalnode.tc)
print("time", end - start)
graph.render(path="out-test.txt")
# 2901
