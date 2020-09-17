# https://www.acmicpc.net/problem/9095
# dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

from sys import stdin

dp = [1, 2, 4]
for i in range(3, 11):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    print(dp[n-1])