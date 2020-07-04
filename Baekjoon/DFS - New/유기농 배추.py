# https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(10000)

def dfs(graph, x, y):
    graph[x][y] = 0
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        if 0 <= x + dx < n and 0 <= y + dy < m:
            if graph[x + dx][y + dy]:
                dfs(graph, x+dx, y+dy)


t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    farm = [[0] * m for _ in range(n)]
    for _ in range(k):
        b, a = map(int, sys.stdin.readline().split())
        farm[a][b] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if farm[i][j]:
                cnt += 1
                dfs(farm, i, j)
    print(cnt)
