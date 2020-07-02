# https://www.acmicpc.net/problem/5557

from sys import stdin

# 2차원 리스트로 dp memoization --> 메모리초과
# n = int(stdin.readline())
# num = list(map(int, stdin.readline().split()))
# dp = [[] for _ in range(n-1)]
# dp[0] = [num[0]]
# for i in range(1, n-1):
#     for j in range(len(dp[i-1])):
#         if dp[i-1][j] + num[i] <= 20:
#             dp[i].append(dp[i-1][j] + num[i])
#         if dp[i-1][j] - num[i] >= 0:
#             dp[i].append(dp[i-1][j] - num[i])
# print(dp[-1].count(num[-1]))

# dictionary로 dp memoization --> 성공!
n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
dp = [{} for _ in range(n-1)]
dp[0][num[0]] = 1
for i in range(1, n-1):
    for k in dp[i-1].keys():
        if k + num[i] <= 20:
            if k + num[i] not in dp[i]:
                dp[i][k + num[i]] = 0
            dp[i][k + num[i]] += dp[i-1][k]
        if k - num[i] >= 0:
            if k - num[i] not in dp[i]:
                dp[i][k - num[i]] = 0
            dp[i][k - num[i]] += dp[i-1][k]
print(dp[-1][num[-1]])
