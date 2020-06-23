# https://www.acmicpc.net/problem/11048

from sys import stdin

n, m = map(int, stdin.readline().split())
L = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + L[i-1][j-1]
print(dp[-1][-1])
