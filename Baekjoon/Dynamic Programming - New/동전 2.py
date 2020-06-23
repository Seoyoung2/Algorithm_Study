# https://www.acmicpc.net/problem/2294
# dp[n] : n원을 만드는 데 사용한 동전의 최소 개수 [0,1,2,3,4,1,2,3,4,5,2,3,1

from sys import stdin
from math import inf

n, k = map(int, stdin.readline().split())
dp = [0] + [inf] * k
for _ in range(n):
    x = int(stdin.readline())
    for i in range(x, k+1):
        dp[i] = min(dp[i], dp[i-x] + 1)
print(-1 if dp[k] == inf else dp[k])
