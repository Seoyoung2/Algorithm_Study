# https://www.acmicpc.net/problem/7576

from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
tomato = [list(map(int, stdin.readline().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
day = 0

# BFS
queue = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j))
while queue:
    day += 1
    tmp = queue.copy()
    while tmp:
        x, y = tmp.popleft()
        queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0<=x+dx<n and 0<=y+dy<m and tomato[x+dx][y+dy] == 0:
                tomato[x + dx][y + dy] = 1
                queue.append((x+dx, y+dy))

print(day - 1 if all(0 not in row for row in tomato) else -1)