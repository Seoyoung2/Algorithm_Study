# https://www.acmicpc.net/problem/7569

from sys import stdin
from collections import deque

m, n, h = map(int, stdin.readline().split())
graph = [[list(map(int, stdin.readline().split())) for _ in range(n)] for _ in range(h)]
dxdydz = (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)

# h->n->m
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))

day = 0
while queue:
    day += 1
    tmp = queue.copy()
    while tmp:
        z, x, y = tmp.pop()
        queue.popleft()
        for dz, dx, dy in dxdydz:
            if 0 <= z+dz < h and 0 <= x+dx < n and 0 <= y+dy < m:
                if graph[z+dz][x+dx][y+dy] == 0:
                    queue.append((z+dz, x+dx, y+dy))
                    graph[z + dz][x + dx][y + dy] = 1
print(day-1 if all(0 not in row for face in graph for row in face) else -1)
