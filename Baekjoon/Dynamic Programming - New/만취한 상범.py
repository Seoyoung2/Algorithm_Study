# https://www.acmicpc.net/problem/6359

from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    dp = [1] * (n+1)
    for i in range(2, n+1):
        for j in range(i, n+1):
            if j % i == 0:
                dp[j] = 1 - dp[j]
    print(dp.count(1) - 1)
