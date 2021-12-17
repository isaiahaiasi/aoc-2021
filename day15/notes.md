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

## Min Heap

This is where my haziness on complex tree data structures becomes an issue...

It is possible to implement dijkstra's algo using a linear search to find the unvisited element with the minimum tentative cost, but it's wildly inefficient. Calculating the final answer takes ~45 minutes. The alternative: a priority queue, implemented using a min heap

Unfortunately, Python's heapq doesn't implement a "decrease priority" method, which is required. On the plus side, this seems like a reasonable justification to implement my own.

Min Heap properties:

- A *complete* binary tree. This means all children should have two nodes, except for the leftovers, which fill the bottom left-to-right.
  - you can fill out a binary tree from a list using the pattern:
    - `left: (2i + 1)`
    - `right: (2i + 2)`
    - `parent: (i - 1)/2`
- Each node's children have a lower value than the node
- 

to heapify:
- create a complete binary tree from list
- "percolate" each node to a valid heap position based on sortfn
- "leaf" nodes don't need to be percolated. We can get the parent of the last node (see above pattern), and that will be the last non-leaf.
  - `parent = (i - 1)/2 => ((len - 1) - 1) / 2 => ((len - 2) /2) => (len/2)-1`
