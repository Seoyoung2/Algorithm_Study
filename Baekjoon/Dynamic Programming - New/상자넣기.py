# https://www.acmicpc.net/problem/1965
# 뭔가 오르막길? 이런 문제랑 비슷

from sys import stdin

n = int(stdin.readline())
L = list(map(int, stdin.readline().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if L[i] > L[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(max(dp))
