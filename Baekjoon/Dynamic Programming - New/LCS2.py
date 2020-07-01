# https://www.acmicpc.net/problem/9252

from sys import stdin

A = " "+stdin.readline().rstrip()
B = " "+stdin.readline().rstrip()
dp = [[0] * len(B) for _ in range(len(A))]
ans = []
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if dp[i][j] != dp[i][j-1] and dp[i][j] != dp[i-1][j]:
            print(A[i], B[j])