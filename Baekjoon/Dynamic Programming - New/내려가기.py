# https://www.acmicpc.net/problem/2096

from sys import stdin

n = int(stdin.readline())
L = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [L[0][:], [0, 0, 0]]
for i in range(1, n):
    k = i % 2
    dp[k][0] = L[i][0] + max(dp[1-k][0], dp[1-k][1])
    dp[k][1] = L[i][1] + max(dp[1-k])
    dp[k][2] = L[i][2] + max(dp[1-k][1], dp[1-k][2])
big = max([num for num in max(dp)])
dp = [L[0][:], [0, 0, 0]]
for i in range(1, n):
    k = i % 2
    dp[k][0] = L[i][0] + min(dp[1-k][0], dp[1-k][1])
    dp[k][1] = L[i][1] + min(dp[1-k])
    dp[k][2] = L[i][2] + min(dp[1-k][1], dp[1-k][2])
small = min(dp[0]) if n % 2 else min(dp[1])

print(big, small)