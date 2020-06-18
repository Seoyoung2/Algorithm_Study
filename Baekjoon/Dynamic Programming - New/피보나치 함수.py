# https://www.acmicpc.net/problem/1003
# dp[n] = dp[n-1] + dp[n-1]

from sys import stdin

dp = [(1, 0), (0, 1)]
for _ in range(40):
    dp.append((dp[-1][0] + dp[-2][0], dp[-1][1] + dp[-2][1]))

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    print(dp[n][0], dp[n][1])

