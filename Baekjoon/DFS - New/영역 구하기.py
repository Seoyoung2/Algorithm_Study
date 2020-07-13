# https://www.acmicpc.net/problem/2583

from sys import stdin

m, n, k = map(int, stdin.readline().split())
graph = [[1] * n for _ in range(m)]

for _ in range(k):
    sy, sx, ey, ex = map(int, stdin.readline().split())
    for x in range(sx, ex):
        for y in range(sy, ey):
            graph[x][y] = 0


def dfs(i, j):
    res = 1
    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= x+dx < m and 0 <= y+dy < n:
                if graph[x+dx][y+dy]:
                    graph[x+dx][y+dy] = 0
                    res += 1
                    stack.append((x+dx, y+dy))
    return res


ans = []
for i in range(m):
    for j in range(n):
        if graph[i][j]:
            graph[i][j] = 0
            ans.append(dfs(i, j))
print(len(ans))
print(*sorted(ans))
