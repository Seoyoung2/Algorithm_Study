# https://www.acmicpc.net/problem/11066
# 동적계획법을 위한 배열 dp말고도 dp배열을 채워나가기 위해 또 하나의 배열이 필요,,

from sys import stdin, maxsize

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    L = list(map(int, stdin.readline().split()))
    S = [0, L[0]]
    for num in L[1:]:
        S.append(S[-1] + num)

    dp = [[0] * n for _ in range(n)]
    for diag in range(1, n):
        for i in range(n-diag):
            j = i + diag
            dp[i][j] = maxsize
            for k in range(i, j):
                tmp = dp[i][k] + dp[k+1][j] + S[j+1] - S[i]
                if dp[i][j] > tmp:
                    dp[i][j] = tmp
                    
    print(dp[0][-1])

