# https://www.acmicpc.net/problem/2579
# dp[n] = max(dp[n-3]+stair[n-1]+stair[n], dp[n-2]+stair[n])

from sys import stdin

n = int(stdin.readline())
stair = [int(stdin.readline()) for _ in range(n)]
dp = stair[:]
if len(dp) > 1:   dp[1] += stair[0]
if len(dp) > 2:   dp[2] += max(stair[0], stair[1])
for i in range(3, n):
    dp[i] += max(dp[i-3] + stair[i-1], dp[i-2])

print(dp[-1])
