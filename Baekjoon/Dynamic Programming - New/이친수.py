# https://www.acmicpc.net/problem/2193

# dynamic programming 을 쓰지 않고 풀었더니 시간초과 뜸

# from sys import stdin
# from itertools import combinations
#
# n = int(stdin.readline())
# num = ['1'] + ['0' for _ in range(n-1)]
# answer = 0
# for j in range(n//2+1):
#     for i in combinations([x for x in range(2, n)], j):
#         tmp = num[:]
#         for idx in i:
#             tmp[idx] = '1'
#         if '11' not in str("".join(tmp)):
#             answer += 1
# print(answer)

# dynamic programming
# dp[n][0] = dp[n-1][0]+dp[n-1][1] / dp[n][1] = dp[n-1][0]

from sys import stdin

n = int(stdin.readline())
dp = [[0, 1] for _ in range(n)]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
print(dp[-1][0] + dp[-1][1])