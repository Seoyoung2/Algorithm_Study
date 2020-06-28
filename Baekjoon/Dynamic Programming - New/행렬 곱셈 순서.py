# https://www.acmicpc.net/problem/11049
# 배열의 대각선까지 생각해야해서 어렵다..

from sys import stdin, maxsize

n = int(stdin.readline())
matrix = []
for _ in range(n):
    r, c = map(int, stdin.readline().split())
    matrix.append(r)
matrix.append(c)

dp = [[0] * n for _ in range(n)]
for diag in range(1, n):
    for i in range(n-diag):
        j = i + diag
        dp[i][j] = maxsize
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i]*matrix[k+1]*matrix[j+1])
print(dp[0][n-1])
