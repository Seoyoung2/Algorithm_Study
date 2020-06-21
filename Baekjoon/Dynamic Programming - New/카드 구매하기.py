# https://www.acmicpc.net/problem/11052
# dp[n] : n개의 카드를 사는데 드는 최대 가격
# dp[n] = max(dp[n-1]+P[n],

from sys import stdin

n = int(stdin.readline())
P = list(map(int, stdin.readline().split()))
dp = [P[0]]
for i in range(1, n):
    dp.append(P[i])
    for j in range(i):
        dp[i] = max(dp[i], dp[i-j-1] + P[j])
print(dp[-1])

