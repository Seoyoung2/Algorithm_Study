# https://www.acmicpc.net/problem/10844

# 1 / 10,12 / 101,121,123
# 2 / 21,23 / 210,212,232,234 / 2101,2121,2123,2321,2323,2343,2345
# 8 / 87,89 / 876,878,898
# 9 / 98 / 987,989

from sys import stdin

n = int(stdin.readline())
dp = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1] for _ in range(n)]
for i in range(1, n):
    for j in range(10):
        # dp[i][j] : j로 시작하는 i+1 자리 숫자의 개수
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
            continue
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
            continue
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[-1]) % 1000000000)
