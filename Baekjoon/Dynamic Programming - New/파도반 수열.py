# https://www.acmicpc.net/problem/9461

from sys import stdin

dp = [1, 1, 1]
for i in range(3, 101):
    dp.append(dp[i-2] + dp[i-3])
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    print(dp[n-1])