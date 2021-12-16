# Day 15: Chiton

Seems pretty straightforward, just implement a lowest-cost pathfinding algorithm for a grid of nodes. *Unfortunately*, I've never done pathfinding before :[

## Dijkstra

nodes: [{ visited: false, tc: inf }]
    (tc of node 0 is 0)
    tc (tentative cost) = cost of current shortest path between n and start
for each node:
    consider all unvisited neighbors and calc tc thru cur node
    mark as visited/remove from unvisited set. should never be checked again
    if destination node has been marked visited
        stop
    else
        select unvisited node that is marked with the smallest tentative distance
