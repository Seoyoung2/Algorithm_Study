# https://www.acmicpc.net/problem/2156

from sys import stdin

n = int(stdin.readline())
podo = [int(stdin.readline()) for _ in range(n)]
dp = [0, podo[0]]
if n > 1:
    dp.append(podo[0]+podo[1])
for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-2] + podo[i-1], dp[i-3] + podo[i-2] + podo[i-1]))
print(max(dp))
