# dp[i][j] : i+1번째 행렬부터 j+1번째 행렬까지 곱하는데 필요한 곱셈 연산의 최솟값
# dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+d[i]*d[k+1]*d[j+1])
# ( i <= k < j , d[i]는 행렬들의 크기의 리스트 )


import sys

t = int(sys.stdin.readline())
d = []
for i in range(t):
    tmp = list(map(int, sys.stdin.readline().split()))
    if i == 0:
        d.append(tmp[0])
    d.append(tmp[1])

dp = [[0 for _ in range(t)] for _ in range(t)]
for diag in range(1, t):
    for i in range(t-diag):
        j = diag + i
        dp[i][j] = sys.maxsize
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+d[i]*d[k+1]*d[j+1])
print(dp[0][-1])


# 풀이는 맞는 것 같은데 백준에서 시간초과 때문에 통과가 안된다...
