# https://www.acmicpc.net/problem/1389

from sys import stdin

n, m = map(int, stdin.readline().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(x, y):
    # 최단경로를 구해야할 거 같은데 dfs 가능한가?


bacon = 99999
ans = -1
for i in range(n):
    graph[i][i] = 1
    for j in range(n):
        if graph[i][j] == 0:
            dfs(i, j)
    if sum(graph[i]) < bacon:
        ans = i + 1