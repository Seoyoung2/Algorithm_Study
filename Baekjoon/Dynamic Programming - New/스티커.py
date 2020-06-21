# https://www.acmicpc.net/problem/9465

from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    score = [list(map(int, stdin.readline().split())) for _ in range(2)]
    if n >= 2:
        score[0][1] += score[1][0]
        score[1][1] += score[0][0]
    for i in range(2, n):
        score[0][i] += max(score[1][i - 1], score[1][i - 2])
        score[1][i] += max(score[0][i - 1], score[0][i - 2])
    print(max(score[0][-1], score[1][-1]))


    # 이런 방법도 있음
    
    # dp = [[score[0][0]], [score[1][0]]]
    # if n >= 2:
    #     dp[0].append(score[1][0]+score[0][1])
    #     dp[1].append(score[0][0]+score[1][1])
    # for i in range(2, n):
    #     dp[0].append(max(dp[1][i-1], dp[1][i-2]) + score[0][i])
    #     dp[1].append(max(dp[0][i-1], dp[0][i-2]) + score[1][i])
    # print(max(dp[0][-1], dp[1][-1]))

    # dp = [score[0][:], score[1][:]]
    # if n >= 2:
    #     dp[0][1] += score[1][0]
    #     dp[1][1] += score[0][0]
    # for i in range(2, n):
    #     dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
    #     dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
    # print(max(dp[0][-1], dp[1][-1]))