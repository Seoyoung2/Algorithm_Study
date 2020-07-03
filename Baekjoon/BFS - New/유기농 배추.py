# https://www.acmicpc.net/problem/1012

from sys import stdin
from collections import deque


def bfs(q, v, num):
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0<=x+dx<n and 0<=y+dy<m:
                if farm[x+dx][y+dy] and v[x+dx][y+dy] == 0:
                    q.append((x+dx, y+dy))
                    v[x+dx][y+dy] = num


t = int(stdin.readline())
for _ in range(t):
    m, n, k = map(int, stdin.readline().split())
    farm = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, stdin.readline().split())
        farm[y][x] = 1

    # BFS
    queue = deque()
    visit = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if farm[i][j] and visit[i][j] == 0:
                cnt += 1
                queue.append((i, j))
                visit[i][j] = cnt
                bfs(queue, visit, cnt)
    print(cnt)
