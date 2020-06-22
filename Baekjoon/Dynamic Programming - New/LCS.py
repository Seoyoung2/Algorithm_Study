# https://www.acmicpc.net/problem/9251
# dp[n] : n글자까지의 LCS -> [0,1,2,2,3,4]

from sys import stdin

# dp를 1차원 배열로 해보려했지만 실패!!!

# [A, B] = [" "+stdin.readline().rstrip() for _ in range(2)]
# dp = [0] * max(len(A), len(B))
# for i in range(1, len(A)):
#     for j in range(1, len(B)):
#         if A[i] == B[j]:
#             dp[j] = dp[j-1] + 1
#         dp[j] = max(dp[j-1], dp[j])
# print(dp)

# 2차원 배열로 해결 !!!!
[A, B] = [" "+stdin.readline().rstrip() for _ in range(2)]
dp = [[0] * len(B) for _ in range(len(A))]
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[-1][-1])
