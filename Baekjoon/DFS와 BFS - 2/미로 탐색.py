# https://www.acmicpc.net/problem/2178

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
visited = [[0] * m for _ in range(n)]
graph = []
for i in range(n):
    graph.append([])
    tmp = stdin.readline()
    for j in range(m):
        graph[i].append(int(tmp[j]))

# BFS
queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= x+dx < n and 0 <= y+dy < m and graph[x+dx][y+dy] and visited[x+dx][y+dy] == 0:
            visited[x+dx][y+dy] = visited[x][y] + 1
            queue.append((x+dx, y+dy))

print(visited[-1][-1] + 1)

