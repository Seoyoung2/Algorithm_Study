# https://www.acmicpc.net/problem/14502

from sys import stdin
from itertools import combinations


n, m = map(int, stdin.readline().split())
M = [list(map(int, stdin.readline().split())) for _ in range(n)]
candi, virus = [], []
for i in range(n):
    for j in range(m):
        if M[i][j] == 0:
            candi.append((i, j))


def dfs(graph, x, y):
    graph[x][y] = 1
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        if 0 <= x+dx < n and 0 <= y+dy < m:
            if graph[x+dx][y+dy] != 1:
                dfs(graph, x+dx, y+dy)


ans = 0
for wall in combinations(candi, 3):
    tmpM = [M[i][:] for i in range(n)]
    for wx, wy in wall:
        tmpM[wx][wy] = 1
    for i in range(n):
        for j in range(m):
            if tmpM[i][j] == 2:
                dfs(tmpM, i, j)
    cnt = 0
    for row in tmpM:
        cnt += row.count(0)
    if ans < cnt:   ans = cnt

print(ans)