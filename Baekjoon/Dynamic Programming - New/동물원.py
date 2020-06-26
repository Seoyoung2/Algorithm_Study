# https://www.acmicpc.net/problem/1309

from sys import stdin

n = int(stdin.readline())
dp = [1, 3]
for i in range(2, n+1):
    dp.append((dp[i-1] * 2 + dp[i-2]) % 9901)
print(dp[-1])