# https://www.acmicpc.net/problem/16194
# 2장 이상의 카드팩 사는거 가능
# dp[i] : i개의 카드를 사는데 드는 최소 비용

from sys import stdin

N = int(stdin.readline())
P = list(map(int, stdin.readline().split()))

dp = P[:]
for i in range(1, N):
    for j in range(i):
        dp[i] = min(dp[i], dp[i-j-1] + P[j])
print(dp[-1])
