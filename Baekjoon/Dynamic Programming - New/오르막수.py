# https://www.acmicpc.net/problem/11057
# dp[i][j] : j로 시작하는 i+1 자리 숫자의 개수
# [[1,1,...,1], [10,9,8,...,1], [55,45,36,...1], ...]

from sys import stdin

n = int(stdin.readline())
dp = [[1] * 10]
for i in range(1, n):
    dp.append([0]*10)
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])
print(sum(dp[-1]) % 10007)
