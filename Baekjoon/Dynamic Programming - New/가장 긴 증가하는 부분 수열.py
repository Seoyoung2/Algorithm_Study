# https://www.acmicpc.net/problem/11053

from sys import stdin

n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
dp = [1] * n  # 1, 2, 1, 3, 2, 4

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
