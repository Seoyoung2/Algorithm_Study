# https://www.acmicpc.net/problem/11403

from sys import stdin

n = int(stdin.readline())
G = [list(map(int, stdin.readline().split())) for _ in range(n)]
R = [[0] * n for _ in range(n)]


def dfs(x, y):
    R[x][y] = 1
    for k in range(n):
        if G[y][k] and not R[x][k]:
            dfs(x, k)


for i in range(n):
    for j in range(n):
        if G[i][j] and not R[i][j]:
            dfs(i, j)

for row in R:
    print(*row)
