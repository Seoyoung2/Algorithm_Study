# https://www.acmicpc.net/problem/1463
# dp[i] : i에서 1을 만드는데 필요한 횟수의 최솟값

from sys import stdin

n = int(stdin.readline())
dp = [0 for _ in range(n+1)]
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
print(dp[n])
