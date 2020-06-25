# https://www.acmicpc.net/problem/11722
# dp[n] : n까지의 답 --> [1,1,2,2,2,3](포함X)/ [1,1,1,2,2,3](포함)
# 30 20 10 40 30 20 10 --> [1,2,3,3,3,3,4](포함X) / [1,2,3,1,2,3,4](포함)

from sys import stdin

n = int(stdin.readline())
L = list(map(int, stdin.readline().split()))
dp = [1]*n
for i in range(n):
    for j in range(i):
        if L[i] < L[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))