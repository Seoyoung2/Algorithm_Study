# https://www.acmicpc.net/problem/2293

from sys import stdin

n, k = map(int, stdin.readline().split())
coin = [0] * n
for i in range(n):
    coin[i] = int(stdin.readline())
dp = [1] + [0] * k
for i in range(n):
    for j in range(coin[i], k+1):
        dp[j] += dp[j-coin[i]]
print(dp[k])