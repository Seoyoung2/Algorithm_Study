# "행렬 곱셈 순서"문제와 비슷하다.
# dp[i][j] : i+1번째 챕터부터 j+1번째 챕터까지 합치는데 필요한 최소비용
# dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+sum(data[tt][i:j+1]))


import sys

for tt in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    sum = [0]
    for i in range(n):
        sum.append(sum[i] + data[i])

    dp = [[0 for _ in range(n)] for _ in range(n)]
    for diag in range(1, n):
        for i in range(n-diag):
            j = diag + i
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+sum[j+1]-sum[i])
    print(dp[0][-1])


# dp에 값을 넣을 때, sum()함수를 썼더니 계속 시간초과 문제가 발생했다.
# sum()함수 대신 리스트를 만들어 저장해서 불러썼더니 통과했당
