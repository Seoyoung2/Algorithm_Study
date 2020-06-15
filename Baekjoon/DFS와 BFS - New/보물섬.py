# https://www.acmicpc.net/problem/2589

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [list(stdin.readline().rstrip()) for _ in range(n)]

mm = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visit = [[-1] * m for _ in range(n)]
            queue = deque([(i, j)])
            visit[i][j] = 0
            while queue:
                x, y = queue.popleft()
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    if 0 <= x+dx < n and 0 <= y+dy < m:
                        if graph[x+dx][y+dy] == 'L' and visit[x+dx][y+dy] == -1:
                            queue.append((x+dx, y+dy))
                            visit[x+dx][y+dy] = visit[x][y] + 1
            mm = max(mm, max(map(max, visit)))
print(mm)
