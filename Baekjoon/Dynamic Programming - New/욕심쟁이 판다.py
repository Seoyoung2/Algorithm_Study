# https://www.acmicpc.net/problem/1937
# DFS + DP

from sys import stdin

n = int(stdin.readline())
M = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]


def dfs(x, y):
    m = 0
    if dp[x][y] == 0:
        dp[x][y] = 1
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= x+dx < n and 0 <= y+dy < n:
                if M[x][y] < M[x+dx][y+dy]:
                    m = max(m, dfs(x+dx, y+dy))
        dp[x][y] += m
    return dp[x][y]


for i in range(n):
    for j in range(n):
        if not dp[i][j]:
            dfs(i, j)
print(max([max(num) for num in dp]))
