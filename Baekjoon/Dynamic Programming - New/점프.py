# https://www.acmicpc.net/problem/1890
# dp[i][j] : M[i][j]로 갈 수 있는 경로의 개수

from sys import stdin

n = int(stdin.readline())
M = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for x in range(n):
    for y in range(n):
        if dp[x][y] == 0 or (x == n-1 and y == n-1):
            continue
        for dx, dy in (1, 0), (0, 1):
            nx, ny = x + M[x][y] * dx, y + M[x][y] * dy
            if nx < n and ny < n:
                dp[nx][ny] += dp[x][y]
print(dp[-1][-1])