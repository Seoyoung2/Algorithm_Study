# https://www.acmicpc.net/problem/1699
# dp[n] : n을 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수

from sys import stdin
from math import sqrt

n = int(stdin.readline())
dp = [0] + [99999] * n
for i in range(1, n+1):
    for j in range(1, int(sqrt(i))+1):
        dp[i] = min(dp[i], dp[i-j*j] + 1) 
print(dp[-1])