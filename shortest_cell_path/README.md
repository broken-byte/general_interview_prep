# The Shortest Cell Path

In a given grid of 0s and 1s, we have some starting row and column sr, sc and a target row and column tr, tc. 
Return the length of the shortest path from sr, sc to tr, tc that walks along 1 values only.

Each location in the path, including the start and the end, must be a 1. Each subsequent location in the path must be 
4-directionally adjacent to the previous location.

It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the starting and target positions are different.

If the task is impossi~~~~ble, return -1.