# https://www.acmicpc.net/problem/15990
# 합을 나타낼 때는 수를 1개 이상 사용, 같은 수를 두 번 이상 연속해서 사용하면 안 된다
# dp[i][j] : 합이 i인 수를 만드는데 끝이 j+1(1,2,3)로 끝나는 경우의 수

from sys import stdin

dp = [[0] * 3 for _ in range(100001)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]
for i in range(4, 100001):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009

T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    print(sum(dp[n]) % 1000000009)
