# https://www.acmicpc.net/problem/10942
#

from sys import stdin

n = int(stdin.readline())
L = list(map(int, stdin.readline().split()))
dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1                            # 한글자일때
    if i+1 < n and L[i] == L[i+1]:
        dp[i][i+1] = 1                      # 두글자일때
for i in range(n-1, -1, -1):                # 세글자 이상일때
    for j in range(i+2, n):
        if L[i] == L[j] and dp[i+1][j-1]:
            dp[i][j] = 1

m = int(stdin.readline())
for _ in range(m):
    s, e = map(int, stdin.readline().split())
    print(dp[s-1][e-1])
